# Drawing sets

A drawing set is a named list of [library drawings](drawing-library.md), each with how
many one set needs: an assembly, a kit or a repeat order. Releasing a set makes the
nests for it, with every quantity multiplied by the number of kits. See
[Releases](releases.md).

Sets are kept on the [nest server](nest-server.md) and need Database mode. A set
always uses the newest revision of each drawing, so fixing a drawing in the library
fixes every set that lists it.

## Find a set {#sets-tab}

Choose **File > Drawing Sets...**. The window opens on the **Sets** tab.

![Sets tab with a set selected](images/drawing-sets.png)

1. **Search** by name, customer or notes. Tick **Show archived** to include archived
   sets.
2. **Set list.** Each set with its customer, how many drawings it has, its revision
   and who saved it last.
3. **Preview and notes.** The selected set's drawings drawn to one scale, each with
   its quantity per set.
4. **New Set...** and **Edit...** open the set editor. **Add to Release** adds the
   selected sets to the release panel (Ctrl- or Shift-click to select several).
   **More** holds **Archive**, **Restore**, **History...**, **Releases...** and
   **Import BOM...**. Right-click a set for the same commands.

Double-click a set to add one kit of it to the release panel. Double-click again for
another kit.

## Make or change a set {#set-editor}

Click **New Set...**, or select a set and click **Edit...**.

![Set editor with the library on the left and the set's drawings on the right](images/set-editor.png)

1. **Name**, **Customer** and **Notes** for the set.
2. **Drawing library.** Search it here without leaving the editor. Drawings already
   in the set are greyed out.
3. Enter **Qty per set**, select one or more drawings and click **Add to Set**. You can
   also double-click a drawing or press ++enter++.
4. **In this set.** Each drawing with its material and quantity per set. Click a
   quantity to change it. The **Note** column flags drawings that are archived in the
   library or have no material or thickness yet.
5. **Edit Drawing...** opens the selected drawing's
   [library details](drawing-library.md#edit-drawing). **Remove** takes it out of the
   set.
6. **Save** saves the set as a new revision. It stays greyed out until you change
   something.

**History...** lists the set's earlier revisions and what each one held. Archiving a
set hides it but keeps every revision. Nothing is ever deleted.

If someone else saved the set after you opened it, OpenNest says so and saves nothing.
Cancel, open the set again and redo your change.

## Make a set from a BOM {#import-bom}

**More > Import BOM...** (or **File > Import BOM...** in Database mode) turns a BOM
spreadsheet into a new set.

1. Choose the BOM (`.xlsx`) and the folder with its drawings. Check the **Set name**
   and enter the **Customer**, then click **Read BOM**.
2. OpenNest matches each drawing to the library. It uses a library drawing that's
   already the same, adds a revision when only the geometry changed, or adds a new
   library drawing. Rows it can't use are listed greyed out with the reason.
3. Click **Create Set...**. If the import changes the library, OpenNest lists every
   change and asks first. Then the set editor opens with the new set. Check it and
   click **Save**.

Drawings with no material or thickness in the BOM are still added. They're flagged in
the set editor, and a release refuses them until you fix them with **Edit Drawing...**.

## Turn a nest into a set {#nest-to-set}

To reuse an existing nest's parts as a set, right-click any drawing in the nest's
drawing list and choose **Add Library Drawings to Set...**. It takes every drawing in
the nest that came from this server's library, with its required quantity. Choose a
set or **New Set**, check the list in the set editor and click **Save**.
