# Machines

Every nest is cut on one machine. The machine you pick for a nest decides:

- the **support bed** its sheets rest on, used to judge whether cut parts can tip
- the starting **lead-ins, lead-outs and kerf** for the nest's material and thickness
- the **cut-off** clearance, overtravel and direction

Machines and their settings for each material and thickness are set up in
**Tools > Machine Configuration**.

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
with **Nest > Machine** first. **How the support bed works**, or ++f1++, opens this page.

**View > Draw Support** shows the points or slats on the plate.

## Lead-ins from the machine {#machine-lead-ins}

When you plan the cutting (or place lead-ins by hand) on a plate that has no cutting
settings yet, OpenNest starts from the machine's lead-in and lead-out settings for the
nest's material and thickness. It also uses the kerf for that thickness. The material and
thickness come from **Nest > Edit**.

- The **Outside Cuts** tab sets the lead-in and lead-out for outside edges. The
  **Inside Cuts** tab sets them for holes, round holes included. While **Same as outside
  cuts** is ticked, holes use the outside settings; clear it to give holes their own. You can
  still change them in **Cutting Settings** before you apply the plan.
- **Clean Hole** is offered on the **Inside Cuts** tab only.
- An **Arc** lead-in is a half circle (**Sweep Angle** 180). Change the sweep in **Cutting Settings**.
- A **Line + Line** lead-in isn't copied. Set it in **Cutting Settings**.
- If the machine has nothing on file for that material and thickness, the settings you
  used last are used instead.
