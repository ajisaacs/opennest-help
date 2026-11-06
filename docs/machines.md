# Machines

Every nest is cut on one machine. The machine you pick for a nest decides:

- the **support bed** its sheets rest on, used to judge whether cut parts can tip
- the **lead-ins, lead-outs, kerf, tabs and pierce** for the nest's material and
  thickness
- the **cut-off** clearance, overtravel and direction

Machines and their settings for each material and thickness are set up in
**Tools > Machine Configuration**. A new install starts with one machine, **Generic
Laser**: mild steel (CR, HR, HR P&O), stainless (304, 316) and aluminum (5052, 6061) in
gauge and plate thicknesses, with fiber-laser kerfs, line lead-ins and the usual plate
sizes up to 72 × 144. Change its values, or add your own machines, before you cut.
Each thickness can have a **Name / Gauge**, such as `16 ga`, shown beside its value in
the list. In Database mode every PC shares one set of machines
from the nest server; see [Shared settings](nest-server.md#shared-settings).

## Choose the nest's machine {#nest-machine}

A new nest gets the machine chosen in **Tools > Nest Defaults** (see below). To change it:

![Nest menu with the Machine list open](images/nest-machine-menu.png)

1. Open the **Nest** menu.
2. Point to **Machine**.
3. Click the machine. The checked one is this nest's machine.

The status bar at the bottom of the window shows **Machine:** and the nest's machine.
Click or right-click it for the same list.

The nest file remembers its machine. When you change it:

- Every sheet moves to the new machine's support bed, or has none if that machine
  gives nests no bed.
- The new machine's cut-off settings apply the next time cut-offs are made or moved.
- Plates you've already planned keep their lead-ins. To use the new machine's, remove the
  lead-ins (**Nest > Remove Lead-ins (All Plates)**) and plan the cutting again.

!!! note "Machine not on file"
    A nest made on another PC may name a machine this PC doesn't have. It's shown greyed
    out with **(not on file)**. Pick one of your machines to use its settings.

## Machine for new nests {#default-machine}

![Nest Defaults dialog with the Machine list](images/nest-defaults.png)

1. In **Tools > Nest Defaults**, pick the **Machine** that new nests use. **File > New**
   and BOM import both use it.
2. Click **Save**.

If you never pick one, new nests use the first machine in alphabetical order.

## Support bed {#support-grid}

The support bed is what the sheet rests on while it's cut: a grid of points, as on a laser
table, or straight slats, as on a plasma table. OpenNest uses it to warn when a cut part
can tip, and Plan Cutting can tab those parts in place. Open it with
**Nest > Support Bed**. The machine's own bed is also set on the **Support Bed** tab in
**Tools > Machine Configuration**.

![Support Bed dialog](images/support-grid.png)

1. **This nest's sheets rest on a support bed.** Turn the bed on or off for this nest
   only.
2. Pick **Grid of points** or **Slats**. Only that kind's settings can be changed.
3. For a grid: the distance between points along X and Y (**Pitch**), and how far the
   first point is from the plate origin.
4. For slats: whether they run along X (the full length) or Y (the full width), the
   distance between slats, how wide each slat is (**Slat thickness**), and how far the
   first slat's center is from the origin.
5. **Registration tolerance** allows for a sheet loaded a little off its place.
   **Stability margin** is how far inside its supports a part's center of gravity must
   be for it to stay level. A part balanced on one slat can't meet it.
6. **Give nests on this machine this bed.** When ticked, every new nest on this machine,
   and every nest you switch to it, gets this bed. The box's title names the machine.
7. **Save as Machine Defaults** saves the values above as this machine's bed straight
   away; **Cancel** doesn't undo it. **Load Machine Defaults** puts the machine's saved
   bed back into the boxes.
8. Click **OK** to apply the bed to this nest.

The machine-defaults buttons are greyed out when the nest has no machine. Pick one
with **Nest > Machine** first. **How the support bed works** opens this page.

To see the bed, turn on **View > Draw Support**. It draws the points or slats, the
points each part rests on and each part's balance point: green when the part is held
level, red when it can tip. A red part also shows an orange diamond where one tab would
steady it best.

## Cutting settings from the machine {#machine-lead-ins}

Each thickness of a machine's material keeps its own cutting settings. When you plan
the cutting (or place lead-ins by hand), OpenNest uses the settings of the nest's
machine for the nest's material and thickness, which come from **Nest > Edit**. Change
them in **Cutting Settings** in the Plan Cutting panel, or in **Tools > Machine
Configuration**; either way they're saved on the machine.

- The **General** tab holds the thickness's kerf. The **Outside Cuts** tab sets the
  lead-in and lead-out for outside edges. The **Inside Cuts** tab sets them for holes,
  round holes included. While **Same as outside cuts** is ticked, holes use the outside
  settings; clear it to give holes their own.
- The **Tabs & Pierce** tab sets lead-in angle rounding,
  [tabs](cutting-planner.md#cutting-settings) and pierce for the thickness. Tick **Use
  for this thickness** to give it its own; unticked, nests of that thickness use the
  tab and pierce settings last used on each PC.
- To give several thicknesses the same tabs and pierce, right-click the thickness in
  the list and choose **Copy Tabs & Pierce To...**. Tick the thicknesses to copy to
  (**Thinner**, **Thicker**, **All** and **None** tick them for you), then click
  **Copy**. For example, set tabs on 1/4" and copy them to every thinner thickness. A
  thickness with no tabs and pierce of its own copies that too, so the others go back
  to each PC's settings.
- **Clean Hole** is offered on the **Inside Cuts** tab only. An **Arc** lead-in is a
  half circle, and a machine thickness can't hold a **Line + Line** lead-in.
- If the machine has nothing on file for that material and thickness, the settings you
  used last on this PC are used as they are, and **Cutting Settings** can use every
  lead type.
- Plates you've already planned keep their lead-ins until you apply a new plan.
