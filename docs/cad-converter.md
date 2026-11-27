# CAD Converter

The CAD Converter turns DXF, DWG and SVG files into drawings OpenNest can nest. It opens
when you click **Import Drawings** on the **Drawings** tab (or use **Nest > Import
Drawing**) and pick one or more files. Check each drawing here before it goes into the
nest: what you see in the preview is what will be cut.

## The converter window {#window}

![CAD Converter with its areas numbered](images/cad-converter.png)

1. **Drawing list.** Every file you picked, with its size and number of entities
   (lines, arcs and circles). The number on the right is the quantity. Click a drawing
   to check it. To add more files, drag them from File Explorer onto the window.
2. **CAD View** shows the drawing as it came from the file. **Program** shows the
   contours OpenNest will cut, in order (see [below](#program)).
3. **Layers**, **Colors** and **Line Types** in the file. Untick one to leave
   everything on it out of the drawing: dimensions, title blocks, notes or a border.
   **All** and **None** tick or untick every layer.
4. **Bend Lines**, **Breakoffs**, **Tabbed Cutouts** and **Dimensions.** Expand a section
   to see or add them. Bend lines are found in the file when it's imported.
5. **Preview.** Scroll to zoom, drag with the middle button to pan, and double-click
   the middle button to fit the drawing. Rulers along the left and bottom edges measure
   in the drawing's units and mark where the pointer is; the grid lines follow the
   ruler marks as you zoom. Right-click a line to change how it's used
   (see [below](#entities)).
6. **Qty** is how many of this drawing you need. **Customer** is saved with the
   drawing.
7. **Split** cuts a part too big for your sheets into pieces. **Simplify** replaces
   runs of short lines with true arcs; when it finds some, the button shows how many,
   for example **Simplify (3)**. **Separate (2)** shows when the file draws more than
   one part; see [Files with several parts](#separate). **Export...** saves the drawing,
   as it is now, to a new file. Pick the file type in the save window: DXF (R14 through 2018), DWG (2004
   through 2018) or SVG. The file keeps its layers and includes the bend lines with
   notes for their direction, angle and radius, so if you import it again the bends
   come back with it. **Holes...** opens the [hole table](#hole-table). **Label Box...**
   sets where the part number is etched; see [Part number label](#label-box).
8. **Original** shows the file's geometry as it was read, before any cleanup, faded
   behind the current drawing, so you can compare it with what will be cut. **Labels** numbers each entity. **Bends**
   chooses how bend lines are found in files you add from now on; **Auto** suits most
   files.
9. **Accept** adds every drawing in the list to the nest. **Cancel** adds none.

## Choose what's cut {#entities}

Right-click any line, arc or circle in the preview to set what it's for. To set
several at once, click them with ++ctrl++ or ++shift++ held, then right-click one. To
take a whole outline at once, right-click one of its lines and choose **Select Chain**:
it selects every line and arc joined end to end with it. Right-click again to set what
they're for.

![Right-click menu on a hole in the preview](images/converter-entity-menu.png)

1. The menu for the selected hole:
    - **Cut** (the default): cut through.
    - **Etch**: marked on the surface, not cut through.
    - **Display Only**: shown here but not cut or marked.
    - **Exclude** (++delete++): left out of the drawing. Right-click it again and
      choose **Include** to bring it back.
    - **Add Radius Dimension** and **Add Diameter Dimension** (circles and arcs only):
      see [Dimensions](#dimensions).

Text in the file isn't cut. To engrave it, right-click the text and choose
**Convert "…" to Geometry**; OpenNest asks for an engraving font (`.CHR`) the first
time.

## Dimensions {#dimensions}

Dimensions show a part's sizes on the drawing while you check it. They're measured from
the geometry that will be cut, so they follow along as you untick layers, exclude lines
or simplify. They never change the part's program, and they don't appear on plates,
reports or exported files (DXF, DWG or SVG).

![Mounting Plate with overall, diameter and radius dimensions](images/converter-dimensions.png)

1. **Overall size:** in the **Dimensions** section, click **Add Overall Dimensions**. It
   adds the width and the height, below and to the right of the part.
2. **Holes and radii:** select one or more circles or arcs, right-click and choose **Add
   Radius Dimension** or **Add Diameter Dimension**. Only a curve that's cut or etched
   can have one; right-click it and choose **Cut** or **Etch** first.
3. The **Dimensions** section lists each one with its value. Selecting one highlights it
   in the preview.
4. **Remove** deletes the selected dimension.

Drag a dimension by its line or its value to move it, across the part to its other side
if you like. Drag a radius or diameter dimension to swing it around the curve or move it
in or out.

Dimensions are saved with the drawing in the nest.

## Hole table {#hole-table}

![Hole Table beside the preview of a plate with two hole sizes](images/converter-hole-table.png)

1. **Holes...** opens the **Hole Table** beside the preview.
2. One row for each hole size, by diameter and smallest first, with how many there are.
   The line under the rows counts the holes and sizes.
3. Every hole in the preview takes the color of its row. Closing the table puts the
   normal colors back.

You can drag the table aside if it covers part of the drawing.

- A round hole is a cut circle, or a ring of arcs on one center, inside the part. The
  outline of a round part isn't a hole.
- A keyed hole, a round hole with a keyway or a flat, gets its own row marked **keyed**,
  after round holes of the same diameter.
- Slots and other shapes aren't listed, nor are etched, display-only or excluded circles.

The table follows the drawing you're checking and updates as you change what's cut. It
only shows; it doesn't change the drawing.

## Part number label {#label-box}

Plan Cutting can etch each part's number on it, so the parts can be told apart after
cutting. The label box sets where the number goes on each drawing. Nothing is etched
until **Etch part label** is turned on in
[Leads & Tabs…](cutting-planner.md#part-labels).

- Click **Label Box...**. OpenNest puts the box on flat material clear of the edges,
  holes and bend lines, where it has the most room, level when it can. It uses half-inch
  text when the part has room for it, else 3/8 in, else 1/4 in (12, 9 or 6 mm).
- The box is drawn dashed, with the number inside as it will be etched. Drag the box to
  move it, a corner to resize it (the text is as tall as the box), or the round handle
  above it to turn it, in 5° steps or freely with ++shift++ held.
- Once the drawing has a box, **Label Box...** opens a menu: **Find Best Location**,
  **Rotate 90°**, **Make Horizontal** and **Remove**. However you turn it, the text never
  reads upside down.
- The text reads along the box's width and shrinks to fit a short box. If it would end
  up under half the box's height, the box turns red and shows **Too small to etch**:
  nothing is etched there. To run the text up the part, click **Rotate 90°** first, then
  resize the box.
- When not even 1/4 in text fits clear of everything, OpenNest says so and places a box
  for you to move and resize. Until you do, it may cover an edge or a bend line.

The number is the drawing's name in capitals. The etching font has digits, capital
letters and `- _ . /`; spaces and other characters are left out. The box is saved with
the drawing. It doesn't change the part's program and isn't exported to DXF, DWG or SVG.

## Bend lines and bend groups {#bend-groups}

With **View > Show Bend Lines** on, each bend line on the plates is colored by how it runs
against the sheet's grain:

| Line | Bend |
| --- | --- |
| Green, dashed | Across the grain (within 5°): the best direction |
| Yellow, dotted | At any other angle |
| Red, dash-dot | With the grain (within 5°): the most likely to crack |

When **Etch part label** is set to **Part number and bend groups**, Plan Cutting also
etches a letter in a circle beside each bend line: its bend group. **A** is across the
grain and **B** with it, each within 5°; **C** to **L** are the 15° steps between,
counterclockwise from the grain. The grain changes springback, so bends with the same
letter take the same angle correction at the press brake and can be formed together.
The letter doesn't say which way the part bends. It depends on how the part is turned on
the sheet, so it's worked out when the cutting is planned.

- The letter sits just off the bend line, clear of the band the bend forms, of edges,
  holes, other marks and the label box. It's the largest of the label sizes that fits; a
  bend with no room for one gets none.
- Parallel bends within 12 in (300 mm) of each other share one letter.
- Bend letters don't need a label box. A drawing without one still gets its bend
  letters, just no number.
- The CAD Converter previews the letters beside the bend lines, as they'd be for the
  part cut unturned on a sheet whose grain runs along X.

## Files with several parts {#separate}

A file can draw several separate parts, such as a sheet of brackets. It comes in as one
drawing, which would cut every part as one. When OpenNest finds two or more parts in it,
**Separate** shows in the bar under the preview with how many, for example **Separate
(4)**.

- Click **Separate (4)** to make each part its own drawing in the list.
- To take out only some, select a line of each, right-click and choose **Separate This
  Part**. **Separate All 4 Parts** on the same menu separates them all.

Each part keeps what you set on its lines (cut, etch, excluded, breakoffs, tabbed
cutouts and dimensions), and the **Qty** and **Customer**. An SVG's titles name the parts
when the file has them; otherwise each is the file's name and a number, counted in rows
from the top, left to right. A part sitting in another part's hole counts as a part of
its own.

OpenNest won't separate parts that a breakoff or tabbed cutout joins; remove it first.
Changes made on the **Program** tab are lost, so OpenNest asks before it separates.

## SVG files {#svg}

An SVG doesn't always say how big it really is. When a file states its width or height in
real units, such as inches or millimeters, OpenNest uses that. When it doesn't, the **SVG Scale** dialog asks
what one of the file's units is: **1/96 inch (web and Inkscape pixels)**, **1/72 inch
(Illustrator points)**, **1 millimeter** or **1 inch**. The **Imported size** line shows
how big the part comes out for each choice; pick the one that matches the part. **Skip
File** leaves that file out.

## Check the program {#program}

The **Program** tab shows each contour OpenNest will cut, in order, with the code it
makes.

![Program tab with the contour list and G-code](images/converter-program.png)

1. The contours, holes first and the perimeter last. Each shows its direction
   (**CW** or **CCW**) and shape.
2. **Reverse Direction** reverses the selected contour. You can also right-click a
   contour for it.
3. The preview. Holes are drawn in blue and the perimeter in green.
4. **G-Code** for the drawing. This is the part's own program; lead-ins, the
   cutting order on the sheet and the machine's code come later, when you
   [plan the cutting](cutting-planner.md) and post.

## Problems on import {#problems}

- **A drawing looks wrong or has extra lines.** Untick the layers or colors that
  aren't part of the shape, or right-click the stray lines and **Exclude** them.
- **A file won't import.** OpenNest names the file and the error. Open the file in
  your CAD program, save it again as DXF, and import that.
- **The outline has gaps.** OpenNest doesn't close gaps for you. Fix the drawing in
  CAD, or Plan Cutting will report the open contour by number and gap size.
