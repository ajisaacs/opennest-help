# Releases

A release turns [drawing sets](drawing-sets.md) and
[library drawings](drawing-library.md) into nests, ready to cut. OpenNest groups the
parts by material and makes one nest per material. Where a **Draft** nest of that
material is waiting, the parts go into it instead of a new nest. Every release is
recorded, so you can see what it made and undo it.

Releases need Database mode and the [nest server](nest-server.md).

## Build a release {#release-panel}

The release panel is on the right of the **Library** and **Sets** tabs in
**File > Drawing Sets...**.

- **Add a set:** double-click it on the **Sets** tab, or select it and click
  **Add to Release**. Each double-click adds one more kit.
- **Add a drawing on its own:** double-click it on the **Library** tab. It's added at
  the **Quantity** under the preview.

![Release panel with two sets and a drawing, merging into two drafts](images/release-panel.png)

1. **What's in the release.** The heading sums it up. Click a **Qty** to change it:
   kits for a set, pieces (**pcs**) for a drawing. **✕** removes a line.
2. **Customer** is filled in when every line has the same customer. **Notes** are
   saved with the release.
3. **Nests it will make.** One row per material, with how many parts it gets and
   **What happens**:
    - **merges into** a Draft nest of the same material, grade and thickness. The
      whole draft is nested again with the new parts.
    - **new Draft nest** when no draft matches.

    When several drafts match, the newest is chosen. Pick another, or
    **New Draft nest**, in the **Nest** list. Untick a row to leave that material out.

4. **Nest after release** runs Auto Nest on every nest the release makes or changes.
   Untick it to make the nests without sheets and nest them yourself later.
5. **Make Nests** makes the release. The number is how many nests it will make or
   change.

In this first release no drafts were waiting yet, so each material gets a new Draft
nest:

![Release panel making two new Draft nests](images/release-new-nests.png)

1. Two kits of one set.
2. Each row says **new Draft nest**.
3. **Make Nests (2)** makes both.

### When a draft is open {#draft-open}

A draft open in a tab of the main window might have changes that aren't saved yet,
so the release won't merge into it:

![Release panel waiting because the drafts are open in tabs](images/release-draft-open.png)

1. **What happens** names the open nest. Save and close its tab, or choose
   **New Draft nest** for that row.
2. **Make Nests** is greyed out until no row is waiting. The panel checks again when
   you come back to the window.

Rows that are refused say why, for example two drawings with the same name, or a
drawing with no material or thickness. Select the row and click **Fix Drawings...**
to [edit the drawings](drawing-library.md#edit-drawing).

## Make the nests {#make-nests}

Click **Make Nests**. With **Nest after release** ticked:

1. The main window comes forward. Each nest opens in its own tab and Auto Nest runs
   on it, one at a time, with the usual progress window.
2. When all of them are done, OpenNest saves them to the server and records the
   release.
3. Each row in **Nests it will make** shows what happened: **Created** or
   **Merged into** with the nest name, or why it failed.

**Stop**, in the progress window or the panel, stops the whole release before
anything is saved. Once saving has started it stops between nests, never halfway
through one.

New nests get the next nest number, the release's material and customer, and the
**Draft** status. Change the status in **Nest > Edit** when the nest is ready to cut.

## See and undo past releases {#releases-tab}

The **Releases** tab lists every release, newest first. **File > Releases...** opens
the window straight on it.

![Releases tab with a release selected and its nests listed](images/releases-tab.png)

1. **Releases.** When, who, what was released, how many nests and how many are cut
   so far, and the notes.
2. **Nests of the release.** Each nest's material, whether the release **Created** it
   or **Merged** into it, and its current status.
3. **Undo Release...** deletes the nests the release created and puts back the drafts
   it merged into. Deleted nests can still be recovered from **Deleted nests...** in
   **File > Open**.

If a nest was changed after the release, OpenNest lists it and offers to undo the
rest, leaving that nest as it is. Undo releases that share a nest newest first.

To see only the releases of one set, select it on the **Sets** tab and choose
**More > Releases...**. For a drawing released on its own, right-click it on the
**Library** tab and choose **Releases...**. **Clear Filter** shows every release again.

**Nest > Edit** shows which release made or last merged into the open nest.
