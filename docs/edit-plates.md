# Edit a plate by hand

Auto Nest lays out a whole job, but you can place, move and fill parts yourself, and
change the plates they sit on. Everything here works on the plate in the plate view.
Use the arrows above it, or **Nest > Next Plate** (++ctrl+right++) and **Previous
Plate** (++ctrl+left++), to move between plates.

After editing a plate by hand, check it with [Overlap Check](validate.md#overlap-check)
before you plan the cutting.

## Plates {#plates}

The **Plates** tab lists every sheet in the nest with its size and utilization.

- **Plate > Add** adds an empty plate. **Plate > Remove**, or **Remove Selected
  Plate** on the **Plates** tab, removes the current one. **Nest > Remove Empty Plates**
  removes every plate with no parts.
- **Plate > Edit** changes the plate's **Size**, its **Quantity** (how many sheets are
  cut with this layout), its **Part Spacing** and **Edge Spacing**, and the
  **Quadrant** its origin is in.
- **Plate > Set as Default** makes this plate's size and spacing the nest's default for
  new plates. **Tools > Save Current Plate as Defaults** saves them for new nests too;
  see [Nest settings](nest-settings.md#nest-defaults).
- **Plate > Rotate** turns the whole plate and its parts 90° either way, or 180°.
- **Plate > Resize to Fit** (++ctrl+p++) shrinks the plate to the nearest standard size
  that holds its parts. **Auto-size plate factor** in **Tools > Options** sets the step
  it rounds up to.
- **Nest > Clear Nest...** removes every part from every plate.

Point at a plate in the **Plates** list to see the stock it's cut from, when it was
loaded from [MaterialLedger](auto-nest.md#materialledger).

## Place parts {#place-parts}

1. On the **Drawings** tab, click a drawing, then move the pointer onto the plate. A
   copy of the part follows the pointer.
2. Click to place it. Keep clicking to place more. ++enter++ places one too.
3. Press ++esc++ to stop.

While a part follows the pointer, press ++ctrl+f++ to fill the largest empty area
around the pointer with that part. On an empty plate it fills the whole sheet.

You can also drag a drawing from the list onto the plate.

The **Drawings** tab counts each placed part: **12 of 30 nested** goes up as you place
parts and down when you delete them. **Hide fully nested drawings** hides the
drawings that are done.

### Fill with a pair {#best-fit}

**Tools > Best-Fit Viewer** shows the best ways to pair two copies of a part, for
example one turned 180° to tuck into the other. Use **Prev** and **Next** to page
through them, then double-click one to place that pair on the plate like a single part.

### Pattern tile {#pattern-tile}

**Plate > Arrange > Pattern Tile** fills a plate with a repeated pattern of one or two
drawings. Pick **Drawing A** (and optionally **Drawing B**) and the **Spacing**, then
compare the **Horizontal** and **Vertical** layouts. With two drawings, **Auto Arrange**
pushes them together as tightly as they fit. Click **Apply** to put the layout on the
plate.

### Fill remnants {#remnants}

**Remnants** on the toolbar opens a list of the empty areas on the current plate. Click
one to show it on the plate. **Filter by part size** hides areas too small for any
part in the nest. Place or fill parts into a remnant as above.

## Select and move parts {#move-parts}

- Click a part to select it. Drag a window to select several, or hold ++ctrl++ to add
  to the selection. **Edit > Select All** (++ctrl+a++) selects every part.
- Drag selected parts to move them.
- The arrow keys move the selection by the offset increment. Set it with **Tools > Set
  Offset Increment** (++f5++).
- ++x++ or ++shift+left++ pushes the selection left until it meets another part or the
  plate edge; ++shift+x++ or ++shift+right++ pushes it right. ++y++ or
  ++shift+down++ pushes down; ++shift+y++ or ++shift+up++ pushes up.
- Click the middle mouse button to turn the selection 90°. ++shift++ + scroll turns it
  by the rotation increment (**Tools > Set Rotation Increment**, ++f6++); add ++ctrl++
  for a tenth of that.
- ++delete++ removes the selected parts.
- **Edit > Copy** (++ctrl+c++) puts copies of the selection on the pointer to place
  like a new part, on this plate or another. **Edit > Cut** (++ctrl+x++) does the same
  but takes the originals off the plate first.

## Arrange parts {#arrange}

**Plate > Arrange** lines up the selected parts. The part you selected first stays put
and the others move to it.

| Command | What it does |
| --- | --- |
| **Left**, **Right**, **Top**, **Bottom** | Line up those edges. |
| **Horizontally**, **Vertically** | Line up the centers across or up and down. |
| **Evenly Space Horizontally**, **Evenly Space Vertically** | Spread the parts out evenly between the outermost two. |
| **Center Parts** | Moves every part on the plate together to the middle of the sheet. |
| **Expand Spacing** | Pushes the selected parts apart as far as the plate and the other parts allow. It can take a while; **Cancel** leaves the parts where they were. |

## Clamps {#clamps}

Clamps hold the sheet on the table. Parts must stay clear of them, and Auto Nest and
the checks treat them as off-limits.

- **Nest > Clamps...** sets where the clamps are for every plate in the nest. Click
  **Add** and enter the **Center** of each clamp, measured from the plate origin.
  **Save as Machine Defaults** saves them for the machine; tick **Give new nests these
  clamps** to use them in new nests.
- **Plate > Edit Clamps** (or right-click a clamp and choose **Edit Clamps**) edits them
  on the plate itself: drag a clamp along its edge or onto another edge, click near an
  edge to add one, or click a clamp's dimension to type its position. ++delete++
  removes the selected clamp. The change applies to every plate in the nest, as in the
  dialog.

## Sheet cut-offs {#sheet-cut-off}

A cut-off is a straight cut across the sheet that trims away the unused part, or chops
the skeleton for the scrap bin.

1. Click **Sheet Cut-Off** on the toolbar (or **Plate > Sheet Cut-Off**).
2. A preview line follows the pointer. Press ++space++ to switch between a vertical
   and a horizontal cut.
3. Click to add the cut-off. It stops short of parts by the machine's cut-off
   clearance, and at the first cut-off that crosses it. Press ++tab++ for lines that
   run the full sheet instead.
4. Press ++esc++ to stop.

Drag a cut-off to move it; the lines that stop on it move with it. To shorten, lengthen
or gap a line where others cross it, see [Trim and extend cut-offs](trim-extend-cutoff.md). For cut-offs that chop the whole skeleton into strips, see
[Scrap cut-offs](cutting-planner.md#scrap-cut-offs).

## Lead-ins by hand {#place-lead-in}

[Plan Cutting](cutting-planner.md) places lead-ins for you. To put one exactly where
you want it, use **Plate > Place Lead-in**:

1. Click the part.
2. Click the contour (the outside edge or a hole) to lock onto it.
3. Click where the cut should start. The point snaps to corners and midpoints.

Right-click to step back: first unlock the contour, then let go of the part. Lead-ins
placed this way are locked, so Plan Cutting keeps them. **Plate > Remove Lead-ins**
removes the current plate's lead-ins; **Nest > Remove Lead-ins (All Plates)** removes
them all.

## Other tools {#other-tools}

- **Tools > Measure Area**: point at an empty spot on the plate to see the size of the
  open area around it. ++space++ switches between the area's two possible shapes
  (wider or taller).
- **View** turns on extra drawing: **Draw Rapids**, **Draw Pierce Points**, **Draw
  Bounds** (each part's box), **Draw Offset** (the part spacing around each part),
  **Draw Cut Direction** and **Draw Support** (the [support bed](machines.md#support-grid)).
- **View > Zoom To** zooms to an **Area** you drag, the **Plate**, the **Selected** parts
  or everything (**Fit**, or ++f++).
- **Plate > View in CAD** opens the current plate as a DXF in your CAD program.
