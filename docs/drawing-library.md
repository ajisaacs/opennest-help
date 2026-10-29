# Drawing Library

The Drawing Library keeps your parts on the [nest server](nest-server.md), so every PC
in the shop uses the same drawings. Each part is saved once with its customer,
material, thickness and nesting settings. Add it to any nest instead of importing the
DXF again.

The Drawing Library needs Database mode. In File mode its commands are greyed out and
say **Database mode only**.

## Browse the library {#browse}

Choose **File > Drawing Library...**. The library opens in its own window, beside the
main window.

![Drawing Library window with a part selected](images/drawing-library.png)

1. **Search.** Type part of a drawing's name, customer or notes.
2. **Drawing list.** Every active drawing with its customer, material, grade,
   thickness and cut type. **Previous** and **Next** page through a large library.
3. **Preview and details.** The selected drawing, its details, the last revision
   (when, and who saved it) and its notes.
4. **Add to Release.** Adds the selected drawing to the release panel on the right, at
   the **Quantity** you enter. You can also double-click the drawing. See
   [Releases](releases.md).
5. **Edit Drawing...** Changes the drawing's details and nesting settings (below).
6. **Release panel.** Turns drawings and [drawing sets](drawing-sets.md) into nests.

The window also has the **Sets** and **Releases** tabs, covered on their own pages.

## Add library drawings to a nest {#add-to-nest}

With a nest open, choose **Nest > Add from Drawing Library...**, or click the
**Library** button above the drawing list.

![Add from Drawing Library dialog, Drawings tab](images/add-from-library.png)

1. **Search.** The list starts with drawings of the nest's material, grade and
   thickness. Tick **Show all materials** to see the rest.
2. **Drawing list.** Click a drawing to select it.
3. **Preview and details** of the selected drawing.
4. Enter a **Quantity** and click **Add to Nest** (or double-click the drawing).
5. **In This Nest** lists what the nest already holds.

Before adding, OpenNest checks the drawing against the nest:

- **Different material, grade or thickness:** OpenNest names the differences and asks
  first. If you add it anyway, the nest's cutting settings are used for it.
- **Different units** (inches and millimeters): it isn't added.
- **Already in the nest:** only its quantity goes up.
- **Another drawing with the same name** in the nest: it isn't added. Rename one of
  them first.

The drawing in the nest is a copy. Editing it in the nest never changes the library.

![Add from Drawing Library dialog, In This Nest tab](images/add-from-library-in-nest.png)

1. Every drawing in the nest with its library revision, and how many are
   **Required**, **Nested** and **Remaining**. Click a **Required** number to change
   it. The change applies to the nest right away.
2. The totals for the whole nest.

## Save a drawing to the library {#save-to-library}

To put a drawing from the open nest into the library, right-click it in the drawing
list and choose **Save to Drawing Library...**.

The dialog fills in the name and customer from the drawing, and the material, grade,
thickness and units from the nest. Check them, choose the cut type and add any notes.
The drawing's nesting settings (Cut first, priority, rotation and color) are saved
with it.

OpenNest looks for library drawings with the same customer, name, material, grade,
thickness, units and cut type, and offers a choice in **Save as**:

- **No match:** it's saved as a new library drawing.
- **One match:** it's saved as the next revision of that drawing.
- **Several matches:** choose which one, or save a separate drawing.

If someone else saved that drawing after you opened the dialog, OpenNest says so and
saves nothing. Check the choices again and save.

## Edit a library drawing {#edit-drawing}

Click **Edit Drawing...** in the library, or right-click a drawing and choose
**Edit Drawing...**.

![Edit Drawing dialog](images/library-edit-drawing.png)

1. **Drawing:** name, customer, material, grade, thickness and cut type. Customer,
   material, grade and thickness list the values the library and the machines already
   use, so pick one to keep spellings matching; you can still type a new one. Units
   can't be changed, because that would change what the geometry means.
2. **Nesting**, used whenever the drawing is added to a nest:
    - **Cut first** sequences its parts before the others, for example a test square.
    - **Priority** works as it does in [Auto Nest](auto-nest.md).
    - **Color** is how its parts are drawn in the nest. Click the swatch to pick a color
      used in every color scheme; **Automatic** lets each nest's color scheme pick it
      again, and **Reset** puts back the color the drawing had.

3. **Rotation:** the angles the nesting engines may turn its parts to. Set **Start**,
   **End** and **Step**, or drag the dial's handles; the dial shades the range and ticks
   each angle tried, and the line below it says what the engines will do. With a
   **Step** of 0 the engines try 0°, 90°, 180° and 270°. **Allow 180° equivalent** also
   tries each angle turned half a turn.
4. **Save to Library** saves a new revision. It stays greyed out until you change
   something.

If your changes would make the drawing match another library drawing, OpenNest names
it and asks before saving. Nests that already hold the drawing keep their copy.
[Drawing sets](drawing-sets.md) always use the newest revision, so their next release
gets your changes.
