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
Right-click the material in the status bar for **Edit Nest...** and **Show in Machine
Configuration...**, which opens the nest machine's settings for this material; see
[Machines](machines.md).

**Info** tab:

- **Name.** In Database mode you can rename the nest here. In File mode the name is the
  file name; change it with **File > Save As**.
- **Customer**, **Made By** and the dates it was made and last changed. A blank **Made
  By** starts with your name: the one you last typed there, or your Windows user name.
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

**Tools > Nest Defaults** sets what **File > New** and BOM import start from: the
[**Machine**](machines.md#default-machine) and **Units**, the **Plate Size** (**Width**
and **Length**), the **Quadrant** (click one to select it), the **Spacing**
**Between parts** and from each of the **Plate edges**, and under **Auto Nest** the
[**Common lines**](auto-nest.md#common-lines) choice new nests start with. Click
**Save**.

**Tools > Save Current Plate as Defaults** copies the current plate's size and spacing
into those defaults in one step.

In Database mode the server keeps one shared copy of the nest defaults; see
[Shared settings](nest-server.md#shared-settings).

## Options {#options}

**Tools > Options** holds settings for OpenNest on this PC. Pick a page in the list on
the left. **Save** keeps the changes on every page except where a button below says it
saves at once; **Cancel** drops the rest.

**General**

| Setting | What it does |
| --- | --- |
| **Create a new nest on startup** | Opens an empty nest with your nest defaults each time OpenNest starts. |
| **Color scheme:** | The colors of plates, parts and cut paths. |
| **Clone push placement:** | Where ++shift++ + click and ++ctrl++ + click [push a placed part](edit-plates.md#place-parts). Every push goes toward the plate's origin corner. **Closest to origin** tries a sideways push first and an up-or-down push first, and keeps whichever ends nearer that corner; **Push horizontally first** and **Push vertically first** always push in that order. |

**Nesting & Cutting**

| Setting | What it does |
| --- | --- |
| **Auto-size plate factor:** | The step **Plate > Resize to Fit** rounds plate sizes up to. |
| **Cut planning effort:** | How long [Plan Cutting](cutting-planner.md#not-ready) searches on hard plates: 1 is normal, up to 10. |

**Fill Strategies**: the fill methods the engines try, in order. Clear a strategy's box
to skip it. Leave them as they are unless you're asked to change them.

**Nest Server**: the [nest servers](nest-server.md#change-server-address) this PC uses.

- **Saved servers** lists each server's **Name** and **URL**. Type in the blank last
  row to add one. To remove one, select its row and click **Remove Server**.
- **Active server:** is the one Database mode uses; it's marked **Active** in the list.
  You can't remove the active server until you choose another.
- Changes here are kept when you click **Save**.

**MaterialLedger**: the ledger **URL:** and **API key:**, for
[stock from MaterialLedger](auto-nest.md#materialledger). **Test Connection** checks
them; **Save Ledger** saves them at once. Leave **URL:** blank to turn the ledger off.

**Updates**

| Setting | What it does |
| --- | --- |
| **Install:** | Which versions this PC installs. **Stable releases only** (the default) takes full releases. The development-build choices also take the newest test build, made from every change as it's finished: **Development builds, at most once a day**, **Development builds, at most once a week**, or **Every development build**. Keep PCs that cut production work on stable releases. Takes effect after a restart. |
| **Feed URL:** | Where OpenNest checks for [updates](#updates). Leave it blank to get them from the nest server in Database mode (or GitHub if the server has none), and from OpenNest's GitHub releases otherwise. **Save Feed URL** saves it at once. Takes effect after a restart. |

## Updates {#updates}

The status bar shows which version of OpenNest is running. A copy installed with the
OpenNest installer checks for a new version a minute after it starts and downloads it in
the background. When it's ready, the status bar says **Update … ready - click to
restart**; click it and save your work first, because an unsaved nest is lost.

- **Help > Check for Updates...** checks now, even when **Install:** is set to once a day or
  once a week. If you're up to date, it says so.
- **Help > About OpenNest** shows the version and the releases page.
- A copy that wasn't installed with the installer, such as one unzipped to a folder,
  can't update itself. **Check for Updates...** offers to open the releases page so you
  can download the new version.

## Machines and posts {#machine-configuration}

**Tools > Machine Configuration** lists your machines. For each one you set its
materials, grades and thicknesses, with the lead-ins, lead-outs, kerf, tabs, pierce and
cut-off settings for each thickness, its plate sizes, its clamps and their clearance, its
[support bed](machines.md#support-grid) and its acceleration limits for
[cut time](sequencing.md#cut-time). See [Machines](machines.md) for how a nest uses them.

Each post processor has its own settings, shown when you [post](first-nest.md#post).
OpenNest saves them for next time. In Database mode, machines and post settings are
[shared by every PC](nest-server.md#shared-settings).

## Save and export {#export}

- **File > Save** (++ctrl+s++) and **Save As** save the nest: to a `.nest` file in File
  mode, or to the [nest server](nest-server.md) in Database mode.
- **File > Save Copy as .nest File...** writes a `.nest` file in either mode, to share
  or back up. It doesn't change where **Save** goes.
- **File > Export Plate...** saves the current plate as a **DXF file**, an **SVG file**,
  an **image** as it's shown on screen (`.jpg`), or a text file of each part's
  **locations and rotations**. **SVG for laser software, e.g. LightBurn (*.svg)** saves
  only what gets cut or marked, without the plate outline, rapids or uncut tabs, with
  each kind of line in its own color so it lands on its own layer.
  **Export All Plates...** does the same for every plate in turn.
- **File > Nest Report...** opens a PDF report of the whole nest in a window, with
  **Save As...** to keep it as a file and **Print...**: each sheet layout, every part
  with its size, weight, and how many are needed and nested, utilization and any
  shortfall (marked **SHORT**). The report doesn't post or check the nest.
  On each sheet layout, every part carries its ID from the parts table. A part too thin
  to hold its ID gets it just outside, on a thin leader line. Parts are also filled in
  their drawing's color, and that color sits beside the ID in the parts table, so you
  can match parts that have no room for an ID. A part held by tabs has a **\*** after
  its ID.
- **File > Part Printouts...** opens a one-page printout for every part in the
  nest, with **Save As...** and **Print...**: the part drawn to fit the page with its
  overall dimensions, its size,
  material, thickness, cut length, pierce count, area, weight and quantity needed. To
  print one part, right-click it in the drawing list and choose **View Part
  Printout...**.
- Part weights use the nest's thickness and the material's density from **Tools >
  Machine Configuration**. When either is missing, the report shows **-** and says
  what's missing.

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
