# Check a nest

OpenNest has three ways to find problems before anything is cut:

| Check | What it finds | When to use it |
| --- | --- | --- |
| [Overlap Check](#overlap-check) | Parts whose material overlaps, parts closer than the part spacing, and parts off the plate or outside its work area | Runs by itself on the plate you're looking at; check it after moving parts by hand, or keeping an Auto Nest result that failed its check |
| [Validate Nest](#validate-nest) | Every check before posting, on every plate: overlaps, missing lead-ins, rapids that cross cut parts, spacing, the plate edge and more | After planning the cutting, or any time you want a full check |
| [Check before posting](#before-posting) | Everything Validate Nest finds, and whether the post changes the cutting order | Runs by itself every time you post |

None of them changes the nest. They point at problems; you decide how to fix them.

## Overlap Check {#overlap-check}

The plate view can shade overlapping material in magenta. Use the **View > Overlap
Check** menu:

- **Check Active Plate** checks the plate you're looking at. **Cancel Check** stops a
  long check.
- **Display** chooses how overlaps are shown: **Areas** shades the shared material,
  **Markers** puts a marker on each overlap, **Both** does both, and **Off** hides
  them.

OpenNest checks the plate you're looking at by itself, half a second after you stop
changing it. **Check Active Plate** runs the check at once.

The check also finds parts that don't overlap but sit closer than the plate's part
spacing. Each pair gets an orange ring at its narrowest gap, labeled with the gap, for
example **1/3 gap 0.1**. Point at a ring or an overlap marker to see the parts and the
gap. These are the same pairs the [check before posting](#before-posting) warns about.

It also checks each part against the sheet. A red crosshair marks where a part leaves
the plate, and an orange ring marks a part that's **outside the work area**: inside the
plate's edge spacing, or too close to the edge of an [odd-shaped
sheet](edit-plates.md#sheet-outline) or an area to keep empty. Point at a marker to
read it. Leads aren't checked here; Validate Nest and the check before posting check
them too.

When something is wrong, the top-left corner of the plate view says so, for example
**Overlaps: 1 pairs; part spacing: 3 pairs too close; 1 parts off the plate**. A clear
plate leaves the corner empty. A check that failed, was canceled or couldn't check every
part always says so.

The **Layout** section of the status bar, beside utilization, follows the check:
**Layout: checking…**, **Layout: OK**, or the findings in red, such as **Layout: 1
overlap, 3 too close, 1 off plate, 2 outside work area**. Point at it for the full
wording.

A part inside another part's hole doesn't count as an overlap when it fits in the
hole.

## Validate Nest {#validate-nest}

**Nest > Validate Nest** checks every plate as it is now: the parts' places, their
lead-ins and the cutting order. It opens the **Cutting Inspection** panel in
**Validate Nest (live programs)** mode.

![Validate Nest panel with a rapid crossing selected](images/validate-nest.png)

1. The result: the number of warnings of each kind, or that every plate is clear. This
   plate hasn't been planned yet, so every contour is missing its lead-in and many
   rapids cross parts.
2. The panel's mode. Switch to **Plan Cutting** to [plan the cutting](cutting-planner.md)
   from here.
3. **Recheck all plates** runs the check again after you change something. **Close**
   (or ++esc++) closes the panel.
4. Every warning, by **Plate**, **Part** (its number in the cutting order) and, for a
   problem between two parts, the part it's **With**. Click a warning to show it.
5. The plate view moves to that plate and zooms to the problem. The parts involved keep
   their colors and the rest turn grey. The line above the list says what the marks
   mean: here, orange dashes show the rapid, and crosshairs mark where it crosses a cut
   contour.

What each warning means:

- **Overlap:** two parts share material, or a part sits on an active clamp. The shared
  area is shaded in magenta.
- **Missing lead-in:** a contour starts with no lead-in. Plan the cutting, or place a
  lead-in by hand. A ring marks where the contour starts.
- **Rapid crossing:** a rapid move passes over a part or hole that's already cut, or
  over a clamp. The cut piece could tip up and hit the head. Plan the cutting again, or
  change the order by hand.
- **Off the plate** and **Outside work area:** a part, or a lead, past the edge of the
  sheet, or a part inside the edge spacing. Move the part back onto the plate.

It also lists everything else the [check before posting](#before-posting) finds, such
as **Part spacing**, **Part support** and **Common line**, under the same names.

Validate Nest doesn't check the post processor's output. While the panel is open you
can still zoom and pan the plate view, but you can't edit the nest or post. Close the
panel first.

## Check before posting {#before-posting}

When you post, OpenNest checks every plate after you accept the post settings and
before it asks where to save the program.

![Verify Nest Before Posting window](images/first-nest-verify.png)

1. A summary of the checks. **Overlapping parts and clamps**, **Missing lead-ins** and
   **Rapid crossings** are always listed; a green check means that check found nothing.
   Other checks are listed only when they find something (see below).
2. Each finding, by plate and part. Click one to read it in full. This nest has none.
3. **Continue Posting** writes the program. **Cancel** (the default, and ++esc++) goes
   back without writing anything.

When there are findings, the button reads **Post Anyway** and stays greyed out until you
tick the box saying you understand the risks. The box applies to this one post only; the
next post starts unticked.

The extra checks, listed only when they find something:

- **Off the plate:** a part, or a lead-in, lead-out or etch, past the edge of the sheet,
  or on an area of an odd-shaped sheet that must stay empty.
- **Outside work area:** a part inside the plate's edge spacing, or that close to an
  odd-shaped sheet's outline or an area to keep empty. Leads may run there.
- **Fixed leads:** a locked lead-in or lead-out that runs into a part or a clamp.
- **Part support:** a part the [support bed](machines.md#support-grid) can't hold
  level, with no tab to keep it in place. With **Tab parts by size**, or on a plate with
  no bed, it's a part whose narrow side is in the size range of
  [Cutting Settings](cutting-planner.md#cutting-settings) that has no tab.
- **Part spacing:** two parts closer than the plate's part spacing. The finding gives
  the measured gap.
- **Nested part order** and **Nested part leads:** a part cut inside another part's
  hole should be cut first, and leads mustn't run into it.
- **Pierce zones:** a pierce too close to a part for the plate's pierce diameter.
- **Common lines:** [joined parts](edit-plates.md#common-lines) that no longer share
  their edge one kerf apart, a group joined at a different kerf from the plate's, a lead
  that runs into the partner, or a shared edge that isn't cut exactly once.

Some posts reorder the cutting when they write the program. For those, the review adds
a warning that the final rapid sequence can't be fully checked, even when the nest has
no findings. The Cincinnati CL post writes a nest planned with **Plan Cutting** in the
order checked, so it gets no such warning, unless the post's part sub-programs or smart
rapids are turned on, or a part's etching comes after its cuts.

A part whose geometry can't be checked is reported as incomplete, never as passed.

!!! warning "These checks don't certify the machine"
    The checks look at the nest's parts and straight-line moves. They don't know your
    head height, slats, clamp height or tab strength, and a post or controller may
    change the route. Review the CNC program and the machine setup before cutting,
    even when the review is clear.
