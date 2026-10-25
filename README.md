# OpenNest Help

User guides for [OpenNest](https://github.com/ajisaacs/OpenNest), written in Markdown
and built with MkDocs Material into plain HTML. OpenNest ships the built site in its
`Help` folder and shows it in a WebView2 window (Help menu, F1).

## Layout

| Path | What it is |
| --- | --- |
| `docs/*.md` | Pages. Add new ones to `nav` in `mkdocs.yml`. |
| `docs/topics.json` | Stable topic IDs the app opens. Never rename or remove an ID. |
| `shots/raw/*.png` | Unedited captures of the app (committed). |
| `shots/*.json` | Markup for each published image: crop, boxes, numbered callouts, arrows, labels, masks. |
| `docs/images/` | Generated from `shots/` by the build; not committed. |
| `samples/*.dxf` | Parts used by the tutorials (`tools/make_samples.py`). |
| `tools/` | Build, capture, markup and tutorial replay scripts. |
| `tools/seed/` | Made-up data and loaders for the throwaway screenshot server. |

## Build

```sh
pip install -r requirements.txt
python tools/build.py           # site/ (strict: broken links fail the build)
python tools/build.py --serve   # live preview at http://127.0.0.1:8000
python tools/build.py --zip     # dist/opennest-help.zip, as packaged with the app
```

To see local pages inside OpenNest, set `OPENNEST_HELP_DIR` to this repo's `site`
folder before starting the app.

## Screenshots

Captures come from a running OpenNest on Windows at 100% display scaling.

1. Start the app with `tools/launch-app.ps1 -Exe <path to OpenNest.exe>`. It sizes the
   window to 1280×820 and starts the app in File storage mode, so captures never take
   nest numbers from the shared nest server. Your storage setting is restored as soon
   as the app has started.
2. Replay a tutorial with `python tools/flows/first_nest.py` (it recaptures every step),
   or capture one window with `python tools/capture.py <name> --title "<window regex>"`.
   `capture.py --list` shows window titles.
3. Mark up the image in `shots/<name>.json` using raw-capture pixel coordinates (see
   `tools/render_shots.py`), then run `python tools/render_shots.py <name>` and check the
   result in `docs/images/`.

Blur anything personal or customer-specific with a `mask` annotation before committing a
raw capture.

### Database-mode screens

The Drawing Library, drawing sets, releases and **File > Open** pictures need a nest
server. Never capture them against a real or shared test server: customer names, job
numbers and notes show in nearly every column. Use a throwaway server on this PC filled
with made-up parts, customers and sets (`tools/seed/catalog.py`). Saved-by and made-by
are "AJ"; don't invent people.

Needs the .NET 8 SDK, an OpenNest source checkout and `pip install ezdxf`.

1. `tools/seed-server.ps1 -OpenNest <OpenNest checkout>` builds OpenNest.Server, runs it
   at `http://127.0.0.1:8095` with its own database in `.seed/` (ignored), and adds 24
   library drawings, 6 sets and the material list. `-Reset` starts it empty again.
2. `tools/launch-app.ps1 -Exe <OpenNest.exe> -ServerUrl http://127.0.0.1:8095` starts the
   app in Database mode against it. It refuses any server that isn't on this PC.
3. Make two releases in **File > Drawing Sets...** (find each set with **Search**):
    - **Utility trailer fender kit**, double-clicked twice (×2). Capture
      `release-new-nests`, then **Make Nests**.
    - With the two new drafts still open in tabs: **Tongue jack mount**, **Dock cleat
      backing** twice, and **Test Square 1 in** from the **Library** tab. Capture
      `release-draft-open`. Close the draft tabs, type the notes
      "Week 44 trailer and dock orders", capture `release-panel`, then **Make Nests**.
4. `python tools/seed/copy_nests.py http://127.0.0.1:8095 .seed/catalog.json` adds six
   saved nests in every status by copying the drafts' layouts, for **File > Open**.
5. Capture the other screens, then `tools/seed-server.ps1 -Stop`.

`tools/seed/Seeder` refuses a server that already has library drawings, and
`copy_nests.py` refuses one that isn't on this PC.

## Releases

Push a `vX.Y.Z` tag. The workflow builds the site and attaches `opennest-help.zip` and
its SHA-256 to a GitHub Release. OpenNest pins one release (tag and hash) in its
`scripts/help.json`, and its packaging scripts refuse a zip that doesn't match.

### Version numbers

Tags are `vMAJOR.MINOR.PATCH`, counted from the last tag on `main`:

| Bump | When the release |
| --- | --- |
| MINOR | adds a page, a section a topic ID points at, or a new `topics.json` ID |
| PATCH | only fixes, rewords or recaptures existing pages |
| MAJOR | stays 0 until the help covers the whole app; never for a removed ID (IDs are never removed) |

Tag only from `main`, after the OpenNest changes the pages describe are on OpenNest's
`master`, so the shipped help never describes unreleased behavior. In the same sitting,
wait for the release, then update `tag` and `sha256` in OpenNest's `scripts/help.json`
(the release attaches `opennest-help.zip.sha256`) and commit that to OpenNest `master`.
Several help commits can share one release; there is no fixed schedule.
