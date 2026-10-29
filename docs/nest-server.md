# Shared nest server

OpenNest can keep nests on your own PC as `.nest` files, or on a **nest server** that
every PC in the shop shares. With the server, a nest saved on one PC can be opened on
any other, every save is kept as a version you can go back to, and new nests get
numbers from one shared counter, so two PCs never hand out the same number.

The server also holds the shared [Drawing Library](drawing-library.md),
[drawing sets](drawing-sets.md) and [releases](releases.md). Those commands only work
in Database mode.

This page has two parts:

- [Set up the server](#set-up-the-server): done once, by whoever looks after the shop's
  computers.
- [Connect a PC to the server](#connect-a-pc): done on each PC that runs OpenNest.

## File mode and Database mode {#storage-modes}

| | File mode (default) | Database mode |
| --- | --- | --- |
| **Save** | Writes a `.nest` file where you choose. | Saves to the server. The first save makes a new record; later saves update it. |
| **Save As** | Writes a new file. | Makes a separate copy on the server. |
| **Open** | Shows the Windows Open dialog. | Shows the server's saved nests, with search, sorting and a preview. |
| **History** | None. | Every save is a version. You can open, download or restore an earlier one. |
| **Delete** | Delete the file in Windows. | Hides the nest. It can be recovered from **Deleted nests...**. |

In either mode you can:

- Drag `.nest` files onto the main window to open them from disk.
- Use **File > Export .nest...** to write a local copy to share or back up. Exporting
  doesn't change where **Save** goes.

## Set up the server {#set-up-the-server}

The server is a small web service that runs in Docker on any always-on machine in the
shop, such as a Linux server or a NAS. It keeps everything in one database on that
machine.

!!! warning "Keep it inside the shop network"
    The server has no passwords. Anyone who can reach it can open, change and delete
    nests. Run it only on your trusted shop network, never on the internet, and make
    sure your firewall lets in only shop PCs.

### What you need

- A machine with Docker and Docker Compose that stays on while the shop works.
- A fixed address for it on your network, such as `192.168.1.20` or `nestserver.lan`.
- The OpenNest server image. Use the release version your OpenNest desktop version
  was tested with. To build it yourself instead, run this from a copy of the
  [OpenNest source](https://github.com/ajisaacs/OpenNest):

    ```sh
    docker build --pull -f OpenNest.Server/Dockerfile -t opennest-server:local .
    ```

### Start it

1. Make a folder for the server on the Docker machine. Copy two files into it from the
   OpenNest source: `compose.server.yaml` and `OpenNest.Server/server.env.example`.
2. Rename `server.env.example` to `server.env` and edit it:

    | Setting | What to enter |
    | --- | --- |
    | `OPENNEST_SERVER_IMAGE` | The server image, for example `ghcr.io/ajisaacs/opennest-server:1.2.3` or `opennest-server:local`. |
    | `OPENNEST_BIND_ADDRESS` | This machine's shop-network address, so shop PCs can reach it. Use `127.0.0.1` to try it on this machine only. Don't use `0.0.0.0`. |
    | `OPENNEST_HOST_PORT` | The port PCs connect to. `8090` unless something else uses it. |
    | `OPENNEST_DATA_VOLUME` | Leave as `opennest-data`. This is where the nests are stored. |

    Don't put passwords or tokens in this file.

3. Start the server from that folder:

    ```sh
    docker compose --env-file server.env -f compose.server.yaml up -d
    ```

4. Check that it is running. After a few seconds, `docker compose ... ps` should show
   **(healthy)**, and opening `http://<address>:<port>/healthz` in a browser on a shop
   PC should show `{"status":"ok"}`.

The server starts again by itself after the machine restarts.

!!! danger "Never run `docker compose down -v`"
    The `-v` deletes the data volume, and every nest with it. To stop the server, use
    `docker compose --env-file server.env -f compose.server.yaml stop`.

### Back it up {#backups}

All nests, versions, drawings and sets live in the `opennest-data` Docker volume.

- **Back up with the server stopped.** Copying the database while the server runs
  does not make a usable backup.
- **Back up before every upgrade.** A newer server upgrades the database, and an older
  server can't open it again. The backup is the only way back.
- **Restore into a new volume**, never over the one in use, and check the restored
  copy before you switch to it.

The OpenNest source has ready-made backup and restore-check steps in
[docs/nest-storage.md](https://github.com/ajisaacs/OpenNest/blob/master/docs/nest-storage.md#backup-restore-and-upgrade).

### Upgrade it

1. Take a backup with the server stopped (see above). Keep a copy of `server.env`.
2. Change `OPENNEST_SERVER_IMAGE` in `server.env` to the new version.
3. Run `docker compose --env-file server.env -f compose.server.yaml up -d` again.

Upgrade the server before the shop PCs. A newer OpenNest may need features an older
server doesn't have. When that happens it says the server must be updated, and it
saves nothing.

## Connect a PC to the server {#connect-a-pc}

Do this on each PC that runs OpenNest. Ask whoever set up the server for its address,
for example `http://192.168.1.20:8090`.

![File menu with the server commands](images/server-file-menu.png)

1. **Drawing Library...**, **Drawing Sets...** and **Releases...** open the shared
   library. They need Database mode.
2. **Storage Mode...** switches between File and Database mode.

Choose **File > Storage Mode...**:

![Storage Mode dialog set to Database mode](images/storage-mode.png)

1. Select **Database — save/open through a shared nest server**.
2. In **Server URL**, type the server's address, starting with `http://`. Type only the
   address and port, nothing after them (not `/healthz`).
3. Click **OK**.

**Save**, **Open** and the other commands in the table [above](#storage-modes) now use
the server. Nests you saved as files before stay where they are. To put one on the
server, drag the `.nest` file onto OpenNest and click **Save**.

To go back to files, choose **File > Storage Mode...** and select **File**.

## Open a saved nest {#open-saved-nests}

In Database mode, **File > Open** shows the nests saved on the server.

![Open Nest window listing the server's nests, with a plate preview](images/nest-browser.png)

1. **Nests.** 100 at a time, newest first. Click a column heading to sort every nest
   by it; click again to reverse. OpenNest remembers your choice.
2. **Nest Information...** changes the selected nest's name, customer, status and
   other details without opening it. It saves at once, as a new version.
3. **Details** of the highlighted nest: its **Plates**, its **Drawings** with how many
   are nested, and **Versions**, every earlier save. From **Versions** you can open an
   old version read-only, download it, or restore it as the newest version.
4. **Preview** of one plate. The arrows under it step through the plates.
5. **Find** searches name, customer, material, made by, comments and status. It
   starts searching when you stop typing.
6. **Deleted nests...** lists nests that were deleted, so you can recover them.

Double-click a nest, or press ++enter++, to open it. ++esc++ closes the window.

Right-click a nest for **Delete...**. Deleting hides the nest but keeps every version.

### Change the server address only {#change-server-address}

If the server moves, update the address without changing the mode:

1. Choose **Tools > Options**.
2. Under **Nest server URL**, type the new address.
3. Click **Set / Change Server**. The address is saved at once, even if you then click
   **Cancel** in Options.

This only changes where OpenNest looks. It doesn't move any nests from the old server.

## Nest status {#nest-status}

Every nest has a **Status**, set in **Nest > Edit** or with **Nest Information...** in
the Open window:

| Status | Means |
| --- | --- |
| **Draft** | Made but not ready yet, such as a nest a [release](releases.md) made before it's checked. Releases add parts only to Draft nests. |
| **Quote** | Nested to price a job. New nests start here. |
| **To Be Cut** | Ready for the machine. |
| **Has Been Cut** | Cut and done. |

## Shared settings {#shared-settings}

In Database mode the server also keeps one copy of the settings that decide how nests
are made and posted, so every PC nests and posts the same way:

- the machines in **Tools > Machine Configuration** (materials, thicknesses, lead-ins,
  kerf, cut-offs, support bed)
- each post processor's settings
- the machine clamp defaults
- **Tools > Nest Defaults**

The first time a PC opens in Database mode and the server lacks some of these, OpenNest
lists them and offers to upload them. Click **Yes** on the PC whose settings are right.
Uploading never replaces settings the server already has, so other PCs only add what's
missing (a post installed on just one PC, for example). Click **No** to keep using this
PC's own settings; it asks again next time.

Once the server has a setting, every PC uses the server's copy and saves changes back to
it. The title of **Tools > Machine Configuration** says whether it's editing the shared
machines, this PC's own (not shared yet), or a read-only copy.

- **Server unreachable.** OpenNest uses the last copy it read, tells you once, and won't
  let you change shared settings until the server is back.
- **Someone else saved first.** Nothing is overwritten. For post settings, the post stops
  and loads the other PC's settings; post again to see them. For machines, reopen
  **Machine Configuration** to see the other changes.

File mode always uses this PC's own settings.

## MaterialLedger holds {#ledger-holds}

If the PC is set up for [MaterialLedger](auto-nest.md#materialledger), the status bar
shows how many of a saved server nest's sheets are held in the ledger, for example
**Ledger: 4 of 4 sheets held** or **Ledger: 2 of 4 held, 2 short**. It turns red when
sheets are short or the ledger can't be reached. Point at it to list each hold; click it
to check again. OpenNest only reads holds; make and close them in MaterialLedger.

When you change a nest's status to **Has Been Cut** and it still has open holds, a note
reminds you to close them out, with a link to the nest in MaterialLedger. It never stops
you saving or posting.

## When something goes wrong {#troubleshooting}

**OpenNest can't reach the server.** Open `http://<address>:<port>/healthz` in a
browser on that PC. If it doesn't show `{"status":"ok"}`, the server is stopped, the
address or port is wrong, or the firewall is blocking the PC.

**Save says the nest was changed on the server.** Another PC saved the same nest after you
opened it. Nothing was overwritten. Reopen the nest to get the newer version, or use
**Save As** to keep yours as a separate copy.

**A save failed partway, such as when the network dropped.** The save may or may not
have reached the server. Click **Save** again: OpenNest checks the server first and
never stores the same nest twice.

**A very large nest won't save.** The server accepts nests up to just under 30 MB. Larger saves fail and store nothing.
