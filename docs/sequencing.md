# Cut order, simulation and cut time

The cut order is the order the parts on a plate are cut in. [Plan
Cutting](cutting-planner.md) chooses it for you, with the lead-ins and rapids, and is
the usual way to set it. This page covers changing the order yourself, watching the cut
play out, and estimating how long it takes.

When you change the order after planning, plan the cutting again (with **Keep current
part order** ticked to keep your order), or run [Validate Nest](validate.md#validate-nest)
to check the rapids.

## Sequence parts {#sequence-parts}

**Plate > Sequence Parts** has three ways to set the order:

| Command | What it does |
| --- | --- |
| **Auto Sequence** | Orders the current plate's parts for a short route. **Nest > Auto Sequence All Plates** does every plate. |
| **Manual Sequence** | You click the parts one at a time. |
| **Sequence by Path** | You draw lines over the plate, and parts are cut in the order the lines pass them. |

Turn on **View > Draw Rapids** to see the route between parts.

### Manual sequence {#manual-sequence}

1. Choose **Plate > Sequence Parts > Manual Sequence**.
2. Set **Sequence** to the position to start from (1 for the first part).
3. Click the parts in the order they should be cut. Each click puts that part at the
   current number, and the number goes up by one.
4. Click **Done**, right-click or press ++esc++ to finish.

### Sequence by path {#sequence-by-path}

Sequence by Path is quickest for rows and columns of parts. Open it with **Sequence by
Path** on the toolbar or **Plate > Sequence Parts > Sequence by Path**.

1. Drag a line over the plate through the parts you want cut first. Their numbers update
   as you drag. Each part goes to the line that passes closest to its middle.
2. Let go, then drag the next line. The jump between lines is a rapid and doesn't pick
   up parts. To add a single part, click it.
3. Parts no line has reached yet are drawn faded. They're cut last, in the order of the
   line they're nearest to.
4. Click **Done** or press ++esc++ when you're finished.

**Undo Line** (++backspace++ or ++ctrl+z++) removes the last line. **Clear** (or a
right-click) removes them all and puts the order back as it was when you started.

### What stays fixed {#fixed-order}

- **Cut first** drawings, such as a test square, are always cut before everything else.
  Tick **Cut first** in the drawing's properties (double-click it on the **Drawings**
  tab).
- A cut-off that crosses parts is moved ahead of them, and one that splits the whole
  sheet is cut last, whichever way you order the parts.

## Simulate cutting {#simulate-cutting}

**Simulate Cutting** on the toolbar (or **Plate > Simulate Cutting**) plays the cut on
the plate view: the head moves along each lead-in, cut and rapid in order, and parts
not reached yet are drawn faded.

- **Play / pause** (++space++), **Restart** (++home++) and **Jump to end**.
- **◀◀ Part** and **Part ▶▶** (++page-up++, ++page-down++) go to the previous and next
  part; **◀ Cutout** and **Cutout ▶** (++ctrl+left++, ++ctrl+right++) go to the previous
  and next cutout or perimeter. ++left++ and ++right++ step one move.
- Drag the slider to scrub through the cut. **Speed** sets how fast it plays.
- The window shows the time so far and the total, which part is being cut, and its
  drawing.

You can still zoom and pan the plate while it plays. Click **Done** or press ++esc++
to close it.

The time uses the same settings as Calculate Cut Time (below): the outside and hole
feeds, the machine whose acceleration times the moves, and **Skip etch-only contours**.

## Calculate cut time {#cut-time}

**Plate > Calculate Cut Time** estimates the current plate; **Nest > Calculate Cut Time**
estimates every plate.

1. Enter the **Feedrate** (outside contours and cut-offs), **Hole feed**, **Rapid
   Feedrate** and **Pierce Time**, and pick the machine for **Acceleration**. The
   choices are remembered.
2. Click **Accept**. The result lists the cut and rapid distances, the number of pierces
   and the estimated **Cut Time**.

Feeds are per minute in an inch nest and per second in a millimeter nest.

!!! note "An estimate, not a quote"
    The acceleration comes from the machine in **Tools > Machine Configuration**. A
    machine shown as **(placeholder)** has no measured limits yet, so its times are
    rough. **None (full speed)** ignores acceleration and reads low.
