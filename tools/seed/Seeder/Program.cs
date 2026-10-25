using System.Net.Http.Json;
using System.Text.Json;
using OpenNest;
using OpenNest.Data;
using OpenNest.IO;

// Usage: Seeder <server url> <catalog.json>
// Uploads the catalog's drawings to the library, then its sets and materials, the way the
// desktop does (DrawingPackage + RemoteDrawingLibrary). Refuses a server that already has
// library drawings, so it can't touch a real server's data.
if (args.Length != 2)
{
    Console.Error.WriteLine("Usage: Seeder <server url> <catalog.json>");
    return 2;
}

var url = args[0];
var catalog = JsonDocument.Parse(File.ReadAllText(args[1])).RootElement;
var savedBy = catalog.GetProperty("savedBy").GetString();
var library = new RemoteDrawingLibrary(url);
var sets = new RemoteDrawingSetStore(url);

var existing = await library.QueryAsync(new DrawingLibraryQuery { Limit = 1 });
if (existing.Total > 0)
{
    Console.Error.WriteLine($"{url} already has {existing.Total} library drawings; seed only an empty throwaway server.");
    return 1;
}

var ids = new Dictionary<string, Guid>();
foreach (var d in catalog.GetProperty("drawings").EnumerateArray())
{
    var name = d.GetProperty("name").GetString();
    var drawing = CadImporter.ImportDrawing(d.GetProperty("file").GetString());
    var record = new DrawingLibraryRecord
    {
        Id = Guid.NewGuid(),
        Name = name,
        Customer = d.GetProperty("customer").GetString(),
        MaterialName = d.GetProperty("material").GetString(),
        MaterialGrade = d.GetProperty("grade").GetString(),
        Thickness = d.GetProperty("thickness").GetDouble(),
        Units = Units.Inches,
        CutType = CutType.Laser,
        Notes = d.GetProperty("notes").GetString(),
        // No stored color, so each nest assigns its own.
        Settings = DrawingNestingSettings.FromDrawing(drawing) with
        {
            CutFirst = d.GetProperty("cutFirst").GetBoolean(),
            ColorArgb = 0,
        },
        SavedBy = savedBy,
    };
    var saved = await library.UploadAsync(record, DrawingPackage.Write(drawing, Units.Inches));
    ids[name] = saved.Id;
}
Console.WriteLine($"{ids.Count} library drawings");

var setCount = 0;
foreach (var s in catalog.GetProperty("sets").EnumerateArray())
{
    await sets.CreateAsync(new DrawingSetRecord
    {
        Id = Guid.NewGuid(),
        Name = s.GetProperty("name").GetString(),
        Customer = s.GetProperty("customer").GetString(),
        Notes = s.GetProperty("notes").GetString(),
        SavedBy = savedBy,
        Members = s.GetProperty("members").EnumerateArray()
            .Select(m => new DrawingSetMember
            {
                DrawingId = ids[m.GetProperty("drawing").GetString()],
                Quantity = m.GetProperty("quantity").GetInt32(),
            })
            .ToList(),
    });
    setCount++;
}
Console.WriteLine($"{setCount} drawing sets");

using var http = new HttpClient { BaseAddress = new Uri(url.TrimEnd('/') + "/") };
var materials = catalog.GetProperty("drawings").EnumerateArray()
    .Select(d => (Name: d.GetProperty("material").GetString(), Grade: d.GetProperty("grade").GetString()))
    .Distinct()
    .ToList();
foreach (var (name, grade) in materials)
    (await http.PostAsJsonAsync("api/materials", new { name, grade })).EnsureSuccessStatusCode();
Console.WriteLine($"{materials.Count} material grades");
return 0;
