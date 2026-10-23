# CAD Converter

The CAD Converter turns DXF and DWG files into drawings OpenNest can nest. It opens
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
4. **Bend Lines**, **Breakoffs** and **Tabbed Cutouts.** Expand a section to see or
   add them. Bend lines are found in the file when it's imported.
5. **Preview.** Scroll to zoom, drag with the middle button to pan, and double-click
   the middle button to fit the drawing. Right-click a line to change how it's used
   (see [below](#entities)).
6. **Qty** is how many of this drawing you need. **Customer** is saved with the
   drawing.
7. **Split** cuts a part too big for your sheets into pieces. **Simplify** replaces
   runs of short lines with true arcs; when it finds some, the button shows how many,
   for example **Simplify (3)**. **Export DXF** saves the drawing, as it is now, to a
   new DXF file.
8. **Original** shows the geometry as imported, faded, behind the current drawing,
   so you can compare after simplifying. **Labels** numbers each entity. **Bends**
   chooses how bend lines are found in files you add from now on; **Auto** suits most
   files.
9. **Accept** adds every drawing in the list to the nest. **Cancel** adds none.

Press ++f1++ in the converter to open this page.

## Choose what's cut {#entities}

Right-click any line, arc or circle in the preview to set what it's for. To set
several at once, click them with ++ctrl++ or ++shift++ held, then right-click one.

![Right-click menu on a hole in the preview](images/converter-entity-menu.png)

1. The menu for the selected hole:
    - **Cut** (the default): cut through.
    - **Etch**: marked on the surface, not cut through.
    - **Display Only**: shown here but not cut or marked.
    - **Exclude** (++delete++): left out of the drawing. Right-click it again and
      choose **Include** to bring it back.

Text in the file isn't cut. To engrave it, right-click the text and choose
**Convert "…" to Geometry**; OpenNest asks for an engraving font (`.CHR`) the first
time.

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
