# Machines

Every nest is cut on one machine. The machine you pick for a nest decides:

- the **support grid** its sheets rest on, used to judge whether cut parts can tip
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

- Every sheet moves to the new machine's support grid, or has none if that machine
  gives nests no grid.
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

## Support grid {#support-grid}

The support grid is the pattern of slats or points the sheet rests on. OpenNest uses it
to warn when a cut part can tip, and Plan Cutting can tab those parts in place. Open it
with **Nest > Support Grid**.

![Support Grid dialog](images/support-grid.png)

1. **This nest's sheets rest on a support grid.** Turn the grid on or off for this
   nest only.
2. The grid's spacing, where its first point is from the plate origin, and the
   tolerances for checking whether a part can tip.
3. **Give nests on this machine this grid.** When ticked, every new nest on this machine,
   and every nest you switch to it, gets this grid. The box's title names the machine.
4. **Save as Machine Defaults** saves the values above as this machine's grid straight
   away; **Cancel** doesn't undo it. **Load Machine Defaults** puts the machine's saved
   grid back into the boxes.
5. Click **OK** to apply the grid to this nest.

The machine-defaults buttons are greyed out when the nest has no machine. Pick one
with **Nest > Machine** first.

## Lead-ins from the machine {#machine-lead-ins}

When you plan the cutting (or place lead-ins by hand) on a plate that has no cutting
settings yet, OpenNest starts from the machine's **Lead In** and **Lead Out** settings
for the nest's material and thickness. It also uses the kerf for that thickness. The
material and thickness come from **Nest > Edit**.

- The machine's lead-in goes on outside edges and holes, round holes included. You can still
  change them in **Cutting Settings** before you apply the plan.
- A **Clean Hole** lead-in is used on holes only; outside edges keep their lead-in.
- A **Line + Line** lead-in isn't copied. Set it in **Cutting Settings**.
- If the machine has nothing on file for that material and thickness, the settings you
  used last are used instead.
