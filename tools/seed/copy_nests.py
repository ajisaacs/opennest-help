"""Add the catalog's example saved nests to a throwaway screenshot server.

Each example copies the layout of a released Draft nest with the same material and
thickness, under its own name, customer, status and comments, so File > Open shows nests
in every status. Run it after the releases in README.md have made the Draft nests.
Names already on the server are skipped, so running it twice adds nothing.

Usage: python tools/seed/copy_nests.py <server url> <catalog.json>
"""

import datetime
import json
import sys
import urllib.parse
import urllib.request
import uuid


def get(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


def upload(server, metadata, archive):
    boundary = uuid.uuid4().hex
    body = (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"metadata\"\r\n"
        f"Content-Type: application/json\r\n\r\n{json.dumps(metadata)}\r\n"
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{metadata['name']}.nest\"\r\n"
        "Content-Type: application/zip\r\n\r\n"
    ).encode() + archive + f"\r\n--{boundary}--\r\n".encode()
    request = urllib.request.Request(f"{server}/api/nests", data=body,
                                     headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(request) as response:
        return response.status


def main(server, catalog_path):
    server = server.rstrip("/")
    if urllib.parse.urlparse(server).hostname not in ("127.0.0.1", "localhost", "::1"):
        sys.exit(f"{server} is not on this PC; copy nests only into a local throwaway server.")
    catalog = json.load(open(catalog_path))
    nests = json.loads(get(f"{server}/api/nests/query?limit=500"))["items"]
    names = {n["name"] for n in nests}
    drafts = [n for n in nests if n["status"] == "draft"]
    # Find every source first, so a missing release adds nothing rather than some.
    todo = []
    for example in catalog["nests"]:
        if example["name"] in names:
            continue
        source = next((d for d in drafts
                       if d["material"] == example["material"] and abs(d["thickness"] - example["thickness"]) < 1e-6), None)
        if source is None:
            sys.exit(f"No Draft nest of {example['material']} {example['thickness']} to copy for {example['name']}; "
                     "make the releases in README.md first.")
        todo.append((example, source))
    for example, source in todo:
        when = (datetime.datetime.now() - datetime.timedelta(days=example["daysAgo"])).isoformat()
        upload(server, {
            "id": str(uuid.uuid4()), "name": example["name"], "customer": example["customer"],
            "material": example["material"], "materialGrade": example["grade"], "thickness": example["thickness"],
            "status": example["status"], "comments": example["comments"], "madeBy": catalog["savedBy"],
            "dateCreated": when, "dateModified": when,
        }, get(f"{server}/api/nests/{source['id']}/file"))
    print(f"Added {len(todo)} example nests")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
