# OpenNest Help

OpenNest arranges flat parts on sheets of material and writes the CNC programs that
cut them. You bring in part drawings (DXF, DWG or SVG) and say how many of each you need.
OpenNest nests them on sheets, plans the cutting order and posts a program for your
machine.

## Start here

**[Your first nest](first-nest.md):** a complete job from start to finish. You import
drawings, set quantities, run Auto Nest, plan the cutting and post the program. It takes
about 10 minutes.

**[Machines](machines.md):** pick the machine a nest is cut on. It sets the support bed,
the starting lead-ins and the cut-off settings.

**[Shared nest server](nest-server.md):** keep nests on a server every shop PC shares,
and connect each PC to it with **File > Storage Mode**.

## Guides

- **[CAD Converter](cad-converter.md):** check drawings as you import them, choose what
  is cut, etched or left out, add dimensions, and read each part's program.
- **[Auto Nest](auto-nest.md):** quantities, priorities and rotations, choosing an
  engine, and letting Auto Nest pick sheet sizes by cost or from MaterialLedger stock.
- **[Plan the cutting](cutting-planner.md):** cut order, lead-ins, tabs, pierces and
  scrap cut-offs, and what to do when a plate isn't ready.
- **[Trim and extend cut-offs](trim-extend-cutoff.md):** shorten or lengthen cut-off
  lines where they cross, and swap which line runs through a junction.
- **[Check a nest](validate.md):** Overlap Check, Validate Nest and the check that runs
  before every post.
- **[Edit a plate by hand](edit-plates.md):** add and change plates, place, fill, move
  and line up parts, clamps, sheet cut-offs and lead-ins placed by hand.
- **[Cut order and simulation](sequencing.md):** set the cut order yourself, watch the
  cut play out and estimate the cut time.
- **[Nest settings](nest-settings.md):** the nest's material and status, defaults for
  new nests, Options, exports and reports, and the Shape Library.

### With the shared nest server

- **[Drawing Library](drawing-library.md):** keep every part on the server, add parts
  to a nest from it and save nest drawings to it.
- **[Drawing sets](drawing-sets.md):** lists of library drawings for an assembly or a
  repeat order, made by hand or from a BOM.
- **[Releases](releases.md):** turn sets and drawings into nests, one per material,
  merging into waiting Draft nests, and undo a release.

## Getting help in the app

- Press ++f1++ in OpenNest to open this help. Inside a dialog, ++f1++ opens the page
  for that dialog.
- Use **Help** on the menu bar to jump to a guide.
- Use the search box at the top of this window to find any topic.
- **Help > Check for Updates...** and **Help > About OpenNest** show which version you
  have; see [Updates](nest-settings.md#updates).

## Follow along with sample parts

The tutorials use four simple parts: a gusset, an L bracket, a mounting plate and a
round flange. The DXF files are in the `samples` folder of the
[opennest-help repository](https://github.com/ajisaacs/opennest-help/tree/main/samples).
Download them if you want your screens to match the pictures.
