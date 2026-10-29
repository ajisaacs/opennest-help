# Check a nest

OpenNest has three ways to find problems before anything is cut:

| Check | What it finds | When to use it |
| --- | --- | --- |
| [Overlap Check](#overlap-check) | Parts whose material overlaps | After moving parts by hand, or keeping an Auto Nest result that failed its check |
| [Validate Nest](#validate-nest) | Overlaps, missing lead-ins and rapids that cross cut parts, on every plate | After planning the cutting, or any time you want a full check |
| [Check before posting](#before-posting) | Everything Validate Nest finds, and more | Runs by itself every time you post |

None of them changes the nest. They point at problems; you decide how to fix them.

## Overlap Check {#overlap-check}

The plate view can shade overlapping material in magenta. Use the **View > Overlap
Check** menu:

- **Check Active Plate** checks the plate you're looking at. **Cancel Check** stops a
  long check.
- **Display** chooses how overlaps are shown: **Areas** shades the shared material,
  **Markers** puts a marker on each overlap, **Both** does both, and **Off** hides
  them.

The result is shown in the top-left corner of the plate view, for example **No
material overlaps detected**. A part inside another part's hole doesn't count as an
overlap when it fits in the hole.

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

Validate Nest doesn't check spacing between parts, distance to the plate edge, or the
post processor's output. While the panel is open you can still zoom and pan the plate
view, but you can't edit the nest or post. Close the panel first.

## Check before posting {#before-posting}

When you post, OpenNest checks every plate after you accept the post settings and
before it asks where to save the program.

![Verify Nest Before Posting window](images/first-nest-verify.png)

1. A summary of the checks. **Overlapping parts and clamps**, **Missing lead-ins** and
   **Rapid crossings** are always listed; a green check means that check found nothing.
   Other checks are listed only when they find something (see below).
2. Each finding, by plate and part. Click one to read it in full.
3. To post despite the findings, tick the box saying you understand the risks. It
   applies to this one post only; the next post starts unticked.
4. **Post Anyway** writes the program once the box is ticked. **Cancel** (the default,
   and ++esc++) goes back without writing anything. When nothing is found, the button
   reads **Continue Posting** instead.

The extra checks, listed only when they find something:

- **Fixed leads:** a locked lead-in or lead-out that runs into a part or a clamp.
- **Part support:** a part the [support bed](machines.md#support-grid) can't hold
  level, with no tab to keep it in place. On a plate with no bed, it's a part whose narrow
  side is in the **On plates with no support bed** range of
  [Cutting Settings](cutting-planner.md#cutting-settings) that has no tab.
- **Part spacing:** two parts closer than the plate's part spacing. The finding gives
  the measured gap.
- **Nested part order** and **Nested part leads:** a part cut inside another part's
  hole should be cut first, and leads mustn't run into it.
- **Pierce zones:** a pierce too close to a part for the plate's pierce diameter.

Some posts reorder the cutting when they write the program. For those, the review adds
a warning that the final rapid sequence can't be fully checked, even when the nest has
no findings.

A part whose geometry can't be checked is reported as incomplete, never as passed.

!!! warning "These checks don't certify the machine"
    The checks look at the nest's parts and straight-line moves. They don't know your
    head height, slats, clamp height or tab strength, and a post or controller may
    change the route. Review the CNC program and the machine setup before cutting,
    even when the review is clear.
