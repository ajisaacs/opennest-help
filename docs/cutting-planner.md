# Plan the cutting

Plan Cutting decides how each plate is cut:

- the order of the parts, and of the holes in each part
- where each contour starts, and its lead-in and lead-out
- the rapid moves between cuts, so the head never crosses a part that's already cut

It shows the plan beside the plate first. Nothing on the plate changes until you click
**Apply**.

| To plan | Use |
| --- | --- |
| The plate you're looking at | **Plan Cutting** on the toolbar, or **Plate > Plan Cutting** |
| Every plate with parts | **Nest > Plan Cutting (All Plates)** |

## The Cutting Inspection panel {#panel}

![Cutting Inspection panel showing a plan ready to apply](images/cutting-plan-panel.png)

1. **Plan Cutting** on the toolbar opens the panel and starts planning at once.
2. The outcome:
    - Green **Ready to apply** means every plate passed every check.
    - Yellow **Unverified plan** means the plan can be used only after you review it;
      see [When a plate isn't ready](#not-ready).
    - Red **Can't apply** means a plate is blocked. The issues below say why.
3. The panel's mode. **Plan Cutting** shows the new plan. **Validate Nest (live
   programs)** checks what's on the plates now; see [Check a nest](validate.md).
4. **Cutting Settings** sets lead-ins, lead-outs, tabs and pierces (see below). The
   line beside it sums them up.
5. **Keep current part order.** Tick it to keep the parts in their current order and
   plan only where and how each one is cut. Leave it off to let the planner reorder
   the parts as well.
6. **Add scrap cut-offs** adds cut-off lines that chop the skeleton into strips, and
   plans them with the parts. **Cut-off Settings** sets the strip size; see
   [Scrap cut-offs](#scrap-cut-offs).
7. **Replan** plans again. **Apply** puts the plan on the plates. **Close** (or
   ++esc++) closes the panel and leaves the plates as they were.
8. A line for the plate: its part count, whether the part order changed, and the
   total length of rapid moves.
9. **Issues** lists every problem by plate and part; **Parts** lists every part and
   whether it passed. Click an issue to show it on the plate.

Changing a setting, or ticking or clearing a box, plans again straight away. While the
plan is shown, the plate view shows the proposed cutting order as part numbers.

When the panel covers several plates, **Previous** and **Next** move between them.
**Apply** applies every plate at once, or none.

## Cutting settings {#cutting-settings}

**Cutting Settings** opens the **Cutting Parameters** dialog. The settings start from
the nest's [machine](machines.md#machine-lead-ins) for the material and thickness,
or from the settings you applied last.

![Cutting Parameters dialog](images/cutting-settings.png)

1. One tab for each kind of contour: **External** (outside edges), **Internal**
   (holes) and **Arc / Circle** (round holes).
2. **Lead-In.** The **Type** is **None**, **Line**, **Arc**, **Line + Arc**, **Clean
   Hole** or **Line + Line**. Set its **Length** and **Approach Angle** (or the sizes
   the type needs).
3. **Lead-Out.** **None**, **Line** or **Arc**.
4. **Tabs** leave small uncut gaps that hold parts in the sheet. Tick **Enable
   Tabs**, set the **Tab Size**, then choose **Tab all parts** or **Tab parts the
   support grid cannot hold level**. The second uses the nest's
   [support grid](machines.md#support-grid).
5. **Pierce.** **Pierce Clearance** is how far each pierce stays from its own contour.
   **Pierce Diameter** is the size of the hole a pierce blows through this plate; when
   it's above 0, every pierce keeps half of it clear of all parts. **Round Lead-In
   Angles** rounds approach angles to the **Increment**.
6. Click **OK**. The plan starts again with the new settings.

With lead-in type **None**, the cut pierces right on the contour. The plan allows it,
but the check before posting still reports **Missing lead-ins**.

When you apply a plan, each plate keeps its settings, and they become the starting
settings for the next plan.

## When a plate already has lead-ins {#existing-lead-ins}

If a plate already has lead-ins or cut-offs, a red banner above the settings says how
many. The plan keeps lead-ins that are locked (for example, ones placed with **Place
Lead-in**) and the cut-offs exactly as they are, and plans everything else.

To start from scratch, click **Clear Lead-ins & Cut-offs** and confirm. It removes
every lead-in (locked ones too), every cut-off and the plates' cutting settings, then
plans again. Parts keep their places. There's no undo.

## Scrap cut-offs {#scrap-cut-offs}

Tick **Add scrap cut-offs** to cut the leftover skeleton into strips that fit your
scrap bin. The strip size is shown on the box, for example **35 in strips**. Click
**Cut-off Settings** to change the spacing, the smallest strip and the tail to keep;
**Use These Settings** returns to the plan.

The cut-offs are planned like parts: a cut-off that crosses parts comes before them,
and one that separates the sheet comes last. Clearing the box, or closing the panel
without applying, takes them off again.

## When a plate isn't ready {#not-ready}

**Overlapping parts** block the plan for that plate. Fix the layout first; see
[Check a nest](validate.md#overlap-check).

**Hard plates.** If the planner runs out of tries before finding a plan that passes
every check, it tries again with the current part order. If that fails too, it offers
the safest route it found, with every rule it breaks listed under **Issues**. To let
it search longer, raise **Cut planning effort** in **Tools > Options** (1 is normal;
up to 10). A longer search takes more time and may still find no plan.

**Unverified plans.** When a plan couldn't be fully checked (for example, a drawing
with touching or uncertain outlines) or only the safest route was found, the outcome
reads **Unverified plan** and the plate's line says **UNVERIFIED**. Read every issue and
look at the plan on the plate, especially its lead-ins and cut order. To use it anyway,
tick **Accept the unverified plan**, then click **Apply**.

**Stale plan.** If the plate changed after planning, **Apply** does nothing and asks
you to replan.

!!! note "Applying a plan isn't approval to post"
    OpenNest checks the nest again when you post, whatever the plan said. See
    [Check a nest](validate.md#before-posting).
