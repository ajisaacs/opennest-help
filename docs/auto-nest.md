# Auto Nest

Auto Nest lays out every part you still need on as many sheets as it takes. It never
touches a plate that already has parts: the sheets it makes go onto empty plates, and
nothing is added to the nest until you keep the result.

Open it with **Auto Nest** on the toolbar or **Nest > Auto Nest**. For a short
walk-through, see [Your first nest](first-nest.md#run-auto-nest).

## Choose the parts {#parts}

![Auto Nest dialog, Parts tab](images/auto-nest-parts.png)

1. **Qty** is how many of each drawing to nest. It starts at the number still to be
   nested (the full quantity, less any already on plates). Set it to 0 to leave a
   drawing out of this run.
2. **Priority** decides which parts get space first. Lower numbers go first, and when
   not everything fits, the lowest numbers are the ones placed. Leave every row at 0
   to treat all parts alike.
3. **Rot Start**, **Rot End** and **Step** limit how a part may be turned, in
   degrees. Leave **Step** at 0 to let OpenNest choose the rotations. Most jobs
   should.
4. The total number of parts and drawings this run will nest.

!!! note "Keep a part to its grain"
    To allow only 0° and 90° for a part with a grain direction, enter **Rot Start**
    0, **Rot End** 90 and **Step** 90.

## Choose the engine {#engines}

The **Plates** tab picks the nesting engine. The engine chosen on the toolbar is
selected when the dialog opens.

![Nest Engine list on the Plates tab](images/auto-nest-engines.png)

| Engine | Use it for |
| --- | --- |
| **Default** | Most jobs. It tries Irregular, Rectangles and Circles and keeps the best layout. |
| **Rectangles** | Rectangular and nearly rectangular parts. Each part is packed as its bounding box, so it never tucks a part into another's notch. It is the fastest. |
| **Irregular** | Odd shapes that should interlock. |
| **Circles** | Jobs where every part is round: blanks, washers, flanges. If any part isn't round it places nothing. |
| **FlatBar** | Cutting parts from flat bar, one row along the bar. Shaped ends are nested into each other. |
| **Fill**, **Strip**, **Vertical Remnant**, **Horizontal Remnant** | Fixed fill patterns, the same ones used to fill a single plate by hand. |

Whatever the engine, Auto Nest first puts small parts inside the holes of larger parts
where they fit.

## Sheet sizes and stock {#stock-options}

With **Stock Options** off, Auto Nest uses sheets the size of the plate you're looking
at, with that plate's spacing. Turn it on to let Auto Nest choose from several sizes.

![Plates tab with Stock Options turned on](images/auto-nest-stock.png)

1. **Nest Engine.** See the table above.
2. **Stock Options.** Tick to offer a list of sheet sizes.
3. The sheet sizes on offer. Type each **Size** as width x length, for example
   `60 x 120`. Type in the blank last row to add a size. To remove one, click the grey
   box at the left of its row and press ++delete++.
   **Cost** is the price of one sheet. Either leave every cost at 0, which makes Auto
   Nest use the least material, or give every row a cost to have it spend the least
   money. Don't mix the two.
4. **Salvage Rate.** How much of a usable offcut's value counts as saved. At 50%,
   leftover material that can go back on the rack counts half its cost (or area).
   Set it to 0 to count only what you buy.
5. **Min Salvage Size.** Offcuts smaller than this, in the nest's units, count as
   scrap.
6. Click **Accept** to start nesting.

The sizes, costs and salvage rate are saved with the nest, so they're filled in the
next time you run Auto Nest on it.

## Watch it run {#progress}

The **Nesting Progress** window shows the stages and the **Best plan so far** while
the engine works. **Stop** throws the run away and leaves your nest as it was. See
[Your first nest](first-nest.md#run-auto-nest) for a picture.

## Keep or discard the result {#review}

![Review Auto Nest window](images/auto-nest-review.png)

1. Every sheet in the result, with its size, part count and utilization. A layout cut
   more than once is shown once, titled with its sheet numbers and count, for example
   **Sheets 2–4 (×3)**.
2. Totals for the run. When the sheets have costs, the gross cost and salvage credit
   are listed too. Any part that couldn't be placed is named here with the reason.
3. **Keep** (++enter++) puts the sheets on empty plates in the nest. **Discard**
   (++esc++) drops the whole result.

### When the result fails its check {#validation-problems}

Auto Nest checks every layout before you see it. If a layout breaks a rule (parts
overlapping or closer than the part spacing, off the sheet, on a clamp, or turned
outside their rotation limits), the **Auto Nest — validation problems** window lists
each problem first.

- **Discard** leaves your plates unchanged. Try another engine, or check the drawings
  for bad geometry.
- **Keep anyway** goes on to the review. If you keep the layout, **View > Overlap
  Check** is turned on so the overlaps are shaded on the plates. Fix them before you
  plan the cutting; see [Check a nest](validate.md#overlap-check).

### Clamps removed {#removed-clamps}

When a part only fits by moving a clamp out of the way, Auto Nest may remove the
clamp as a last resort. After you keep the result, a message names each removed clamp
by sheet and the time it adds. Move those clamps before cutting.
