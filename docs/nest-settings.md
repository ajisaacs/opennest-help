# Nest settings

This page covers the settings that belong to a nest, the defaults new nests start
from, OpenNest's own options, and how to get a nest out as files and reports.

## Typing sizes {#typing-sizes}

Size and spacing boxes show their unit beside the number. You can type a value in other
units and OpenNest converts it to the nest's: `10 mm`, `2.5 cm`, `1 m`, `0.5 in`,
`1 ft`, or a fraction such as `3/8"` or `1-1/4`.

**Thickness** boxes (in **Nest > Edit** and when you save to the Drawing Library) list
steel gauges (26 to 3 ga) and plate fractions (1/16" to 2") with their decimals. Pick
one, or type a gauge (`16ga`, `#16`), a fraction (`3/32`) or a decimal. Text OpenNest
can't read stops **Done** or **Save** instead of being read as zero.

## The nest's details {#nest-info}

**Nest > Edit**, or a click on the material in the status bar, opens **Edit Nest**.

**Info** tab:

- **Name.** In Database mode you can rename the nest here. In File mode the name is the
  file name; change it with **File > Save As**.
- **Customer**, **Made By** and the dates it was made and last changed.
- **Status:** **Draft**, **Quote**, **To Be Cut** or **Has Been Cut**; see
  [Nest status](nest-server.md#nest-status).
- **Material**, **Grade** and **Thickness.** The material list includes every material
  in **Tools > Machine Configuration**, and the grade list shows the grades on file for
  the chosen material. Together with the [machine](machines.md), they decide the
  starting lead-ins, kerf and cut-off settings.
- **Units:** **Inches** or **Millimeters**.

**Defaults** tab: the **Size**, **Part Spacing**, **Edge Spacing** and **Quadrant** that
new plates in this nest get. **Notes** tab: free text saved with the nest.

To change one plate instead, use **Plate > Edit**; see
[Edit a plate by hand](edit-plates.md#plates).

## Defaults for new nests {#nest-defaults}

**Tools > Nest Defaults** sets what **File > New** and BOM import start from: **Units**,
**Plate width** and **Plate length**, **Quadrant**, **Part spacing**, the four **Edge**
spacings and the [**Machine**](machines.md#default-machine). Click **Save**.

**Tools > Save Current Plate as Defaults** copies the current plate's size and spacing
into those defaults in one step.

In Database mode the server keeps one shared copy of the nest defaults; see
[Shared settings](nest-server.md#shared-settings).

## Options {#options}

**Tools > Options** holds settings for OpenNest on this PC:

| Setting | What it does |
| --- | --- |
| **Create a new nest on startup** | Opens an empty nest when OpenNest starts. |
| **Auto-size plate factor** | The step **Plate > Resize to Fit** rounds plate sizes up to. |
| **Cut planning effort** | How long [Plan Cutting](cutting-planner.md#not-ready) searches on hard plates: 1 is normal, up to 10. |
| **Color scheme** | The colors of the plate view. |
| **Fill Strategies** | Which fill methods the engines try, and in what order. Leave them as they are unless you're asked to change them. |
| **Nest server URL** | The [nest server's](nest-server.md#change-server-address) address. **Set / Change Server** saves it at once. |
| **Auto-update feed URL** | Where OpenNest checks for updates. Leave it blank to turn update checks off. **Save Feed URL** saves it at once. |
| **MaterialLedger** | The ledger **URL** and **API key**, for [stock from MaterialLedger](auto-nest.md#materialledger). **Test** checks the connection; **Save Ledger** saves them at once. |

Click **Save** for the rest.

## Machines and posts {#machine-configuration}

**Tools > Machine Configuration** lists your machines. For each one you set its
materials, grades and thicknesses, with the lead-ins, lead-outs, kerf and cut-off
settings for each thickness, its plate sizes, its [support bed](machines.md#support-grid)
and its acceleration limits for [cut time](sequencing.md#cut-time). See
[Machines](machines.md) for how a nest uses them.

Each post processor has its own settings, shown when you [post](first-nest.md#post).
OpenNest saves them for next time. In Database mode, machines and post settings are
[shared by every PC](nest-server.md#shared-settings).

## Save and export {#export}

- **File > Save** (++ctrl+s++) and **Save As** save the nest: to a `.nest` file in File
  mode, or to the [nest server](nest-server.md) in Database mode.
- **File > Export .nest...** writes a `.nest` file in either mode, to share or back up.
  It doesn't change where **Save** goes.
- **File > Export** saves the current plate as a **DXF file**, an **SVG file**, an
  **image** as it's shown on screen (`.jpg`), or a text file of each part's **locations
  and rotations**.
  **Export All** does the same for every plate in turn.
- **File > Export Nest Report...** writes a PDF report of the whole nest: each sheet
  layout, the parts and quantities, utilization and any shortfall. It doesn't post or
  check the nest.

## Other ways to add drawings {#add-drawings}

Most drawings come in through the [CAD Converter](cad-converter.md) or the
[Drawing Library](drawing-library.md). Two more ways:

- **Nest > Shape Library** makes simple parts without a DXF: rectangles, rounded
  rectangles, circles, rings, triangles, trapezoids, polygons, L and T shapes and pipe
  flanges. Pick a shape, enter its sizes, a **Name** and a **Quantity**, and click
  **Add to Nest**.
- **File > Import BOM...** in File mode reads a BOM spreadsheet (`.xlsx`). Choose the
  **BOM File**, the **DXF Folder** that holds its drawings, a **Job Name** and the
  **Plate Size**, then click **Analyze**. The **Parts** list shows each row and whether
  its drawing was found; **Groups** has one row per material and thickness. **Create
  Nests** makes one nest per group. In Database mode the same command makes a
  [drawing set](drawing-sets.md#import-bom) instead.
