<#
.SYNOPSIS
Starts a throwaway OpenNest nest server on this PC and fills it with made-up data for
screenshots of the Database-mode screens.

.DESCRIPTION
Never capture those screens against a real or shared test server: they show customer
names, job numbers and notes in nearly every column. This script builds OpenNest.Server
from an OpenNest source checkout, runs it on 127.0.0.1 with its own empty database in
.seed\ (ignored by git), then adds the library drawings, drawing sets and material list
from tools\seed\catalog.py. Start the app against it with
tools\launch-app.ps1 -ServerUrl http://127.0.0.1:<Port>, make the releases in README.md,
then run tools\seed\copy_nests.py for the example saved nests.

Needs the .NET 8 SDK and Python with ezdxf (pip install ezdxf).

.EXAMPLE
./tools/seed-server.ps1 -OpenNest C:\src\OpenNest
.EXAMPLE
./tools/seed-server.ps1 -Stop
#>
param(
    [string] $OpenNest,
    [int] $Port = 8095,
    # Deletes .seed\ first, so the server starts empty again.
    [switch] $Reset,
    [switch] $Stop
)

$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$data = Join-Path $root '.seed'
$pidFile = Join-Path $data 'server.pid'

function Stop-SeedServer {
    if (Test-Path $pidFile) {
        $id = [int](Get-Content $pidFile)
        # The PID is the cmd.exe wrapper; /T takes the server with it.
        taskkill /T /F /PID $id 2>&1 | Out-Null
        Remove-Item $pidFile
        "Stopped the seed server (PID $id)."
    }
}

if ($Stop) { Stop-SeedServer; return }
if (-not $OpenNest) { throw 'Pass -OpenNest <path to the OpenNest source checkout>.' }
$OpenNest = (Resolve-Path $OpenNest).Path

Stop-SeedServer
if ($Reset -and (Test-Path $data)) { Remove-Item $data -Recurse -Force }
if (Test-Path (Join-Path $data 'nests.db')) {
    throw "$data already has a database. Use -Reset to start over, or -Stop to stop it."
}
New-Item -ItemType Directory -Force $data | Out-Null

$serverProject = Join-Path $OpenNest 'OpenNest.Server\OpenNest.Server.csproj'
dotnet build $serverProject -c Release -v q -nologo -o (Join-Path $data 'server')
if ($LASTEXITCODE) { throw 'OpenNest.Server did not build.' }

$url = "http://127.0.0.1:$Port"
# Started through WMI so the server inherits none of this script's handles: with
# Start-Process it would hold the caller's output pipe open until it stopped.
$command = "cmd.exe /s /c `"dotnet `"$data\server\OpenNest.Server.dll`" --database `"$data\nests.db`" " +
    "--urls $url > `"$data\server.log`" 2> `"$data\server.err.log`"`""
$started = Invoke-CimMethod Win32_Process -MethodName Create -Arguments @{ CommandLine = $command; CurrentDirectory = $data }
if ($started.ReturnValue -ne 0) { throw "Could not start the server (WMI error $($started.ReturnValue))." }
$serverId = $started.ProcessId
$serverId | Set-Content $pidFile

$deadline = (Get-Date).AddSeconds(30)
while ($true) {
    try { if ((Invoke-RestMethod "$url/healthz").status -eq 'ok') { break } } catch { }
    if (-not (Get-Process -Id $serverId -ErrorAction SilentlyContinue)) { throw "The server exited; see $data\server.err.log." }
    if ((Get-Date) -gt $deadline) { throw "The server did not answer at $url within 30 seconds." }
    Start-Sleep -Milliseconds 500
}

python (Join-Path $PSScriptRoot 'seed\catalog.py') $data
if ($LASTEXITCODE) { throw 'catalog.py failed (is ezdxf installed?).' }
dotnet run --project (Join-Path $PSScriptRoot 'seed\Seeder\Seeder.csproj') -v q "-p:OpenNestDir=$OpenNest" -- $url (Join-Path $data 'catalog.json')
if ($LASTEXITCODE) { throw 'Seeding the server failed.' }

"Seed server running at $url. Next:"
"  ./tools/launch-app.ps1 -Exe <OpenNest.exe> -ServerUrl $url"
"  make the releases in README.md, then: python tools/seed/copy_nests.py $url $data\catalog.json"
"  ./tools/seed-server.ps1 -Stop when done"
