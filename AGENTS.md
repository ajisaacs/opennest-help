# opennest-help agent instructions

User guides for OpenNest; see README.md for layout, build and capture steps.

- Write for shop users, not developers: what to click and why, in the app's own labels.
  Keep implementation detail in the OpenNest repo's `docs/`.
- Number markup callouts in the order the steps under the picture are written, and
  keep one numbered list per picture.
- `docs/topics.json` IDs are a contract with the app (`OpenNest/Help/HelpTopics.cs`):
  never rename or remove one; point it at a new page or `page.html#anchor`. Give
  targeted headings explicit anchors (`## Heading {#anchor}`).
- Run `python tools/build.py` before committing; it fails on broken links and on topics
  that point at missing pages.
- Never take captures in Database storage mode (it allocates real nest numbers): use
  `tools/launch-app.ps1`. Mask personal, customer or job data in captures.
- Commit raw captures and manifests, never `docs/images/`, `site/` or `dist/`.
