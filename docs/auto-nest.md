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

**Keep like parts together**, beside the engine list, is on by default. It nests each
part type as one group, so parts are easier to sort and package off the table. It can
leave a slightly shorter offcut than mixing the types. Turn it off for the shortest
layout. Auto Nest remembers the choice. It changes how Irregular nests, so it also
affects Default when Irregular's layout is the one kept.

## Sheet sizes and stock {#stock-options}

With **Stock Options** off, Auto Nest uses sheets the size of the plate you're looking
at, with that plate's spacing. Turn it on to let Auto Nest choose from several sizes.

![Plates tab with Stock Options turned on](images/auto-nest-stock.png)

1. **Nest Engine.** See the table above.
2. **Stock Options.** Tick to offer a list of sheet sizes.
3. The sheet sizes on offer. Type each **Size** as width x length, for example
   `60 x 120`. Type in the blank last row to add a size. To remove one, click the grey
   box at the left of its row and press ++delete++.
    - **Use:** untick a row to leave it out of this run without deleting it.
    - **Qty:** how many of that sheet you have. Leave it blank for no limit.
    - **Cost** is the price of one sheet. Either leave every cost at 0, which makes Auto
      Nest use the least material, or give every row a cost to have it spend the least
      money. Don't mix the two.
    - **Source** says where a row loaded [from MaterialLedger](#materialledger) came
      from. It's blank on rows you type.
4. **Salvage Rate.** How much of a usable offcut's value counts as saved. At 50%,
   leftover material that can go back on the rack counts half its cost (or area).
   Set it to 0 to count only what you buy.
5. **Min Salvage Size.** Offcuts smaller than this, in the nest's units, count as
   scrap.
6. Click **Accept** to start nesting.

The sizes, costs and salvage rate are saved with the nest, so they're filled in the
next time you run Auto Nest on it.

### Stock from MaterialLedger {#materialledger}

If your shop tracks sheets and drops in MaterialLedger, Auto Nest can offer the stock
that's free right now. Set it up once on each PC: in **Tools > Options**, under
**MaterialLedger**, enter the ledger's **URL** and **API key**, click **Test**, then
**Save Ledger**. The nest needs a material and a thickness (**Nest > Edit**).

1. Turn on **Stock Options** and click **Load from ledger**.
2. The ledger's free full sheets and drops of the nest's material are added as rows,
   each with how many are free. Rows you typed yourself stay. Point at a row to see its
   item codes and rack locations.
3. Lower a ledger row's **Qty**, or untick **Use**, to keep stock out of the run. You
   can't change a ledger row's size or cost.

The line under the list sums up what was loaded, or why nothing was (for example, no
mapping for the material, or the ledger can't be reached).

- **Substitutes.** Stock the ledger accepts in place of the nest's grade reads, for
  example, **A1011 P&O for HR** in amber. It's ticked like the rest; untick **Use** if
  you don't want it.
- **Drops** of the same size share one row. An irregular drop shows **(irr.)** and is
  offered as the largest rectangle that's safe to use.
- **Costs.** While any ledger row is ticked, Auto Nest uses the least material and
  ignores the costs on rows you typed. The summary line says so.
- **Nothing is reserved.** The stock is what was free when you loaded it; someone else
  can take the same drop first. Hold the sheets in MaterialLedger.

When you keep the result, each sheet cut from ledger stock remembers its item code. The
**Plates** tab shows it when you point at the plate. Ledger rows aren't saved with the
nest. In Database mode the status bar shows the nest's [ledger holds](nest-server.md#ledger-holds).

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
