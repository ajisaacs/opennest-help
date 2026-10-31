# Trim and extend cut-offs

**Trim/Extend Cut-Off** shortens or lengthens a cut-off line where it meets the
cut-offs that cross it, or leaves a gap in it, so you don't have to delete a line and
draw it again. Use it to
choose which line runs through a junction: for example, to let a vertical cut-off split
the whole sheet and keep the remnant beyond it in one piece.

To add or remove cut-off lines, see [Add a cut-off by hand](cutting-planner.md#sheet-cutoff).

## Trim or extend a line {#trim-extend}

Open **Plate > Trim/Extend Cut-Off**, or click the **Trim/Extend Cut-Off** toolbar
button, just after **Sheet Cut-Off**. The tool starts in Trim mode.

- **Trim:** click the piece of a cut-off you want to remove. The piece runs between the
  cut-offs that cross the line on either side of your click (or to the line's end), and
  the line now stops on that crossing cut-off.
- **Trim a middle piece** to leave a gap: click the piece between two crossing cut-offs.
  That stretch is left uncut, and the line is cut as two pieces, one on each side of the
  gap, each with its own place in the cutting order.
- **Extend:** click near the end of a cut-off you want to grow. The end runs to the next
  cut-off that crosses its path, or to the sheet edge if none does. Click again to go
  one crossing further. Click beside a gap to close it again in one click.
- Press ++tab++ to switch between Trim and Extend. The status bar shows which mode is on.
- Press ++esc++ when you're done.

While the tool is on, ++f1++ opens this page.

As you move the pointer, a dashed preview shows what a click will do:

- dashed **red** marks the piece a trim removes
- dashed **green** marks the piece an extend adds

A gap is never cut, so nothing waits for it: the parts inside it can be cut in any order
around the pieces of the line.

## Move a line with the lines that meet it {#drag}

Drag a cut-off to move it. The lines that stop on it, or whose gap ends on it, come with
it: they grow or shorten to keep meeting it, and the drag undoes as one step. A line can't
be dragged past the next line that crosses it; it stops a **Minimum segment length**
short. A line that already stopped short of it before the drag isn't joined; bring it to
the line with Extend or Trim first.

## Swap which line runs through {#swap-through-cut}

Where two cut-offs meet, one usually runs through and the other stops at it. To swap
them, right-click the junction with the normal select pointer (not while another tool
is on) and choose **Swap Through-Cut**.

- The line that stopped now runs through the junction, to the next crossing cut-off
  or the sheet edge.
- The line that ran through now stops at the other one. It keeps the side nearer the
  plate's origin and loses its far side, because only the origin-side sheet edge is a
  known position.
- If a line now splits the sheet in two, it moves to the end of the cutting order, so
  the head never travels back across the separated piece.
- **Swap Through-Cut** isn't offered where a gap touches the junction. Close the gap
  with Extend first.

### Example {#swap-example}

On a 48 × 96 sheet, a horizontal cut-off at Y 31.51 runs the full width. A vertical
cut-off at X 70.22 stops at it.

Right-click where they meet and choose **Swap Through-Cut**. The vertical at X 70.22
now runs the full height of the sheet, and the horizontal stops at X 70.22. The area
beyond X 70.22 stays whole, and the vertical, which now splits the sheet, is cut last.

## Undo and messages {#messages}

Each trim, extend or swap undoes as one step with **Edit > Undo**
([Undo a change](first-nest.md#undo)).

When an edit can't be made, nothing changes and the status bar says why:

| Status bar | What to do |
| --- | --- |
| No cut-off crosses this line to trim it to; delete it instead. | Select the line and press ++delete++. |
| That stretch of the line is already uncut. | You clicked inside a gap. Use Extend to close it. |
| Trimming here would leave a line shorter than the minimum segment length. | Trim at a different crossing, or delete the line. |
| This end already runs to the sheet edge. | There's nothing further to extend to. |
| These cut-offs do not meet with one running through and the other stopping at it. | Swap only works where one line stops at the other. |
| A gap in one of these lines meets the junction; extend to close it before swapping. | Switch to Extend and click beside the gap, then swap. |

**Head-locked cut-offs.** A cut-off made with **Lock head height and overcut the far
edge** overcuts the far sheet edge. Trimming its far end turns the overcut off, and
extending it back to that edge turns the overcut on again. The status bar tells you
each time.
