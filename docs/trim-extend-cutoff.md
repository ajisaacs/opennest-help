# Trim and extend cut-offs

**Trim/Extend Cut-Off** shortens or lengthens a cut-off line where it meets the
cut-offs that cross it, so you don't have to delete a line and draw it again. Use it to
choose which line runs through a junction: for example, to let a vertical cut-off split
the whole sheet and keep the remnant beyond it in one piece.

To add or remove cut-off lines, see [Add a cut-off by hand](cutting-planner.md#sheet-cutoff).

## Trim or extend a line {#trim-extend}

Open **Plate > Trim/Extend Cut-Off**, or click the **Trim/Extend Cut-Off** toolbar
button, just after **Sheet Cut-Off**. The tool starts in Trim mode.

- **Trim:** click the piece of a cut-off you want to remove. The piece runs from where
  you click back to the nearest cut-off that crosses the line (or to the line's end),
  and the line now stops on that crossing cut-off.
- **Extend:** click near the end of a cut-off you want to grow. The end runs to the next
  cut-off that crosses its path, or to the sheet edge if none does. Click again to go
  one crossing further.
- Press ++tab++ to switch between Trim and Extend. The status bar shows which mode is on.
- Press ++esc++ when you're done.

While the tool is on, ++f1++ opens this page.

As you move the pointer, a dashed preview shows what a click will do:

- dashed **red** marks the piece a trim removes
- dashed **green** marks the piece an extend adds

You can only trim a piece at an end of a line. The middle piece between two crossing
cut-offs can't be trimmed, because a cut-off has one start and one end.

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
| Trimming the middle piece would split the line in two; trim an end piece instead. | Click a piece at one end of the line. |
| Trimming here would leave a line shorter than the minimum segment length. | Trim at a different crossing, or delete the line. |
| This end already runs to the sheet edge. | There's nothing further to extend to. |
| These cut-offs do not meet with one running through and the other stopping at it. | Swap only works where one line stops at the other. |

**Head-locked cut-offs.** A cut-off made with **Lock head height and overcut the far
edge** overcuts the far sheet edge. Trimming its far end turns the overcut off, and
extending it back to that edge turns the overcut on again. The status bar tells you
each time.
