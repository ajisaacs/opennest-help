<#
.SYNOPSIS
Starts OpenNest for screenshot captures in File storage mode, sized for docs.

.DESCRIPTION
In Database mode every new nest (including the one created at startup) takes a
number from the shared nest server, so captures would leave gaps in real job
numbers. OpenNest reads %APPDATA%\OpenNest\storage.json once at startup, so this
script switches it to File mode only while the app starts, then restores it.
Other running OpenNest instances are unaffected.

.EXAMPLE
./tools/launch-app.ps1 -Exe C:\src\OpenNest\OpenNest\bin\Debug\net8.0-windows\OpenNest.exe
#>
param(
    [Parameter(Mandatory)] [string] $Exe,
    [int] $Width = 1280,
    [int] $Height = 820
)

$ErrorActionPreference = 'Stop'
$storage = Join-Path $env:APPDATA 'OpenNest\storage.json'
$original = if (Test-Path $storage) { Get-Content $storage -Raw } else { $null }

$env:OPENNEST_HELP_DIR = Join-Path (Split-Path $PSScriptRoot -Parent) 'site'
try {
    '{ "mode": 0 }' | Set-Content $storage -Encoding utf8
    $process = Start-Process $Exe -PassThru
    if (-not $process.WaitForInputIdle(30000)) { throw 'OpenNest did not start within 30 seconds.' }
    Start-Sleep -Seconds 2
}
finally {
    if ($null -eq $original) { Remove-Item $storage -ErrorAction SilentlyContinue }
    else { [IO.File]::WriteAllText($storage, $original) }
}

Add-Type -Namespace Win32 -Name Window -MemberDefinition @'
[DllImport("user32.dll")] public static extern bool MoveWindow(IntPtr hWnd, int x, int y, int w, int h, bool repaint);
'@
$process.Refresh()
[Win32.Window]::MoveWindow($process.MainWindowHandle, 40, 40, $Width, $Height, $true) | Out-Null
"OpenNest PID $($process.Id): $($process.MainWindowTitle)"
