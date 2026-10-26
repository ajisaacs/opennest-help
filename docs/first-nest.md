# Your first nest

This guide walks through a whole job: four parts, 72 pieces in total, nested on one
60 × 120 sheet and posted for the laser. The numbered markers on each picture match the
numbered steps under it.

## The main window {#main-window}

![OpenNest main window with its areas numbered](images/main-window.png)

1. **Menu bar.** Every command lives here. **Help** opens this guide.
2. **Toolbar.** Shortcuts for common jobs:
    - New, open and save
    - The nesting **Engine** and **Auto Nest**
    - Cut-off, **Plan Cutting** and cutting simulation
    - **Post**
3. **Drawings and Plates tabs.** **Drawings** lists the parts in this nest and how many
   are nested. **Plates** lists the sheets.
4. **Plate view.** The current sheet, drawn to scale. Scroll to zoom. Use the arrows
   above it to move between plates.
5. **Status bar.** The cursor position, the plate's material and its utilization (how
   much of the sheet is used by parts).

OpenNest opens a new, empty nest when it starts. Its name is in the
title bar. To start another, use **File > New** (++ctrl+n++).

## Undo a change {#undo}

**Edit > Undo** (++ctrl+z++) takes back the last change to the nest, and **Edit > Redo**
(++ctrl+y++ or ++ctrl+shift+z++) puts it back. The menu names the step, for example
**Undo Rotate** or **Redo Auto Nest**. Each nest keeps its own last 50 steps while it is
open; saving doesn't clear them.

Almost anything you do to the nest can be undone: moving, rotating, adding or deleting
parts, fills and Auto Nest, **Clear Nest**, plates and their settings, clamps and the
support grid, cut-offs, the cut order and lead-ins, applying a cutting plan, and adding,
editing or deleting drawings.

Some things can't be undone:

- Saving, posting and exporting, and anything saved on the nest server: releases (use
  [Undo Release](releases.md#releases-tab)) and the Drawing Library.
- **Machine Configuration**, **Save as Machine Defaults** and nest defaults. (Picking
  the nest's machine can be undone.)
- Zoom, pan, the view options and what is selected.
- The nest's name, status and who made it.

Undo and Redo are greyed out while Auto Nest, a fill or the **Plan Cutting** panel is
open. Wait for the job to finish or close the panel first. In a text or number box,
++ctrl+z++ undoes your typing in that box.

## Import the drawings {#import-drawings}

![Drawings tab with the Import Drawings button and the imported parts](images/first-nest-import.png)

1. On the **Drawings** tab, click **Import Drawings**.
2. After you import them, the drawings appear in this list.

![Windows Open dialog with four DXF files selected](images/first-nest-open-dialog.png)

1. Select the DXF or DWG files for the job. Hold ++ctrl++ to pick several, or press
   ++ctrl+a++ to pick the whole folder.
2. Click **Open**. The files open in the CAD Converter.

### Check each part and set its quantity

![CAD Converter showing the mounting plate, with the quantity field](images/first-nest-converter.png)

1. **Drawing list.** Click a drawing to check it. The number on the right (for
   example ×10) is how many you need.
2. **Qty.** Type how many of the selected drawing to make. Do this for each drawing.
3. **Preview.** Shows the geometry OpenNest will cut. Check that holes and outlines look
   right. Use the panel to the left of the preview to hide layers or colors you don't
   want cut, such as dimensions or title blocks.
4. Click **Accept** to add the drawings to the nest.

The [CAD Converter](cad-converter.md) page covers the rest of this window.

![Drawings tab listing the four parts, none nested yet](images/first-nest-drawings.png)

1. Each drawing shows **0 of 30 nested** (or its own quantity) until it is placed on
   a sheet.
2. Click **Auto Nest** on the toolbar to nest them.

## Run Auto Nest {#run-auto-nest}

![Auto Nest dialog, Parts tab](images/first-nest-autonest.png)

1. **Qty** comes from the CAD Converter. Change it here if you need to. The other
   columns set each part's nesting priority and the range of rotations it may use. The
   defaults suit most jobs.
2. The **Plates** tab picks the nesting engine and the sheet stock.
3. Click **Accept** to start nesting.

![Auto Nest dialog, Plates tab](images/first-nest-autonest-plates.png)

1. **Nest Engine.** Different engines suit different jobs. The engine chosen on the
   toolbar is selected here.
2. **Stock Options.** Turn this on to offer several sheet sizes, with their costs.
   Leave it off to nest on the nest's default sheet.

![Nesting Progress window](images/first-nest-progress.png)

1. The stages Auto Nest works through.
2. **Best plan so far** fills in as soon as the engine has a complete plan.
3. **Stop** cancels the run. Nothing in your nest changes.

### Keep or discard the result

![Review window with one sheet holding all 72 parts](images/first-nest-review.png)

1. Every sheet the engine proposes, with its size, part count and utilization.
2. Totals for the whole run. If any parts didn't fit, they're listed here with the
   reason.
3. Click **Keep** (++enter++) to add the sheets to the nest, or **Discard**
   (++esc++) to throw the result away.

For priorities, rotation limits, engines and sheet costs, see [Auto Nest](auto-nest.md).

![Main window with the nested sheet](images/first-nest-result.png)

1. **Plate 1 of 1 | 60 x 120:** the sheet you're looking at, and its size.
2. Each drawing now shows **30 of 30 nested** (or its own quantity).
3. Arrows to move between sheets when a job needs more than one.
4. **Util:** how much of this sheet the parts use.

## Plan the cutting {#plan-cutting}

Plan Cutting chooses the order parts and holes are cut in, where each cut starts, and
the rapid moves between them. The head never travels across parts that are already
cut.

![Cutting Inspection panel with a plan ready to apply](images/first-nest-plan-cutting.png)

1. Click **Plan Cutting** on the toolbar (or **Plate > Plan Cutting**).
2. The panel on the right reports whether the plan is ready.
3. **Cutting Settings** sets the lead-ins and lead-outs for outside edges and holes
   (round holes included). They start from the nest's
   [machine](machines.md#machine-lead-ins) when it has settings for the material and
   thickness. Check them before you apply the plan.
4. Click **Apply** to put the plan on the plate. After you change settings, click
   **Replan** to plan again.
5. **Issues** lists anything the plan couldn't solve, such as a part with no safe
   place to start a cut.

!!! note "Lead-ins come from Cutting Settings"
    If the nest's machine has no settings for its material and thickness (set them in
    **Nest > Edit**), outside edges start with no lead-ins. If you post without setting
    them, the check before posting reports **Missing lead-ins** for every contour.

[Plan the cutting](cutting-planner.md) covers the panel and its settings in full.

## Post the program {#post}

![Post button and its list of machines](images/first-nest-post-menu.png)

1. Click the arrow beside **Post** on the toolbar (or use **Nest > Post**).
2. Pick the machine's post processor.

![Post processor settings](images/first-nest-post-settings.png)

1. The post's settings: output units, line numbers, subprograms, assist gas, kerf
   compensation and more. OpenNest saves them for next time.
2. Click **OK** to continue.

### Check the nest before it is written

OpenNest checks the nest before it writes any CNC code.

![Verify Nest Before Posting window](images/first-nest-verify.png)

1. A summary of the checks. A green check means that check found nothing.
2. Each finding, by plate and part. Click one to read it in full.
3. If you've reviewed every finding and still want to post, tick this box. It accepts
   the risks for this one post only.
4. **Post Anyway** writes the program once the box is ticked. **Cancel** goes back so
   you can fix the problems.

[Check a nest](validate.md#before-posting) explains every check.

When the checks pass, OpenNest asks where to save the program, then writes it.
Remember to save the nest itself with **File > Save** (++ctrl+s++).
