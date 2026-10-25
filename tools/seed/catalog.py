"""Write the made-up data for a throwaway screenshot server: DXF parts (inches) and catalog.json.

Everything here is invented: four customers, 24 parts, six drawing sets and the example
saved nests copy_nests.py adds. People are never invented: saved-by and made-by are "AJ".

Usage: python tools/seed/catalog.py <output folder>
"""

import json
import math
import sys
from pathlib import Path

import ezdxf

SAVED_BY = "AJ"

A36_250 = ("Mild Steel", "A36", 0.25)
A36_125 = ("Mild Steel", "A36", 0.125)
SS_125 = ("Stainless Steel", "304", 0.125)
AL_125 = ("Aluminum", "5052", 0.125)

NORTH = "Northfield Trailers"
CEDAR = "Cedar Ridge Ag"
HARBOR = "Harbor Marine Supply"
SHOP = "Shop"


def corners(w, h, inset=0.75):
    return [(inset, inset), (w - inset, inset), (w - inset, h - inset), (inset, h - inset)]


def slot(msp, x, y, length, r):
    """Horizontal slot centered at (x, y)."""
    a, b = x - length / 2, x + length / 2
    msp.add_line((a, y - r), (b, y - r))
    msp.add_line((a, y + r), (b, y + r))
    msp.add_arc((a, y), r, 90, 270)
    msp.add_arc((b, y), r, 270, 90)


def rect_holes(w, h, holes=(), r=0.25, center=None):
    def draw(msp):
        msp.add_lwpolyline([(0, 0), (w, 0), (w, h), (0, h)], close=True)
        for x, y in holes:
            msp.add_circle((x, y), r)
        if center:
            msp.add_circle((w / 2, h / 2), center)
    return draw


def slotted_plate(w, h, slots):
    def draw(msp):
        msp.add_lwpolyline([(0, 0), (w, 0), (w, h), (0, h)], close=True)
        for x, y, length in slots:
            slot(msp, x, y, length, 0.2)
    return draw


def l_shape(w, h, leg, holes=()):
    def draw(msp):
        msp.add_lwpolyline([(0, 0), (w, 0), (w, leg), (leg, leg), (leg, h), (0, h)], close=True)
        for x, y in holes:
            msp.add_circle((x, y), 0.25)
    return draw


def triangle(a, b, holes=()):
    def draw(msp):
        msp.add_lwpolyline([(0, 0), (a, 0), (0, b)], close=True)
        for x, y in holes:
            msp.add_circle((x, y), 0.22)
    return draw


def flange(od, bore, bolts, bolt_r=0.22):
    def draw(msp):
        msp.add_circle((0, 0), od / 2)
        msp.add_circle((0, 0), bore / 2)
        pcd = (od / 2 + bore / 2) / 2
        for i in range(bolts):
            t = 2 * math.pi * i / bolts
            msp.add_circle((pcd * math.cos(t), pcd * math.sin(t)), bolt_r)
    return draw


def tab(w, h, hole):
    """Rectangle with one rounded end and a hole in it."""
    def draw(msp):
        r = h / 2
        msp.add_line((0, 0), (w - r, 0))
        msp.add_arc((w - r, r), r, 270, 90)
        msp.add_line((w - r, h), (0, h))
        msp.add_line((0, h), (0, 0))
        msp.add_circle((w - r, r), hole)
    return draw


def channel(w, h, holes=()):
    """U-channel flat pattern with notched corners."""
    def draw(msp):
        n = 0.25
        msp.add_lwpolyline([
            (n, 0), (w - n, 0), (w - n, n), (w, n), (w, h - n), (w - n, h - n), (w - n, h),
            (n, h), (n, h - n), (0, h - n), (0, n), (n, n)], close=True)
        for x, y in holes:
            msp.add_circle((x, y), 0.2)
    return draw


def cover(w, h, r):
    """Rounded-corner cover plate with corner holes and vent slots."""
    def draw(msp):
        msp.add_line((r, 0), (w - r, 0)); msp.add_arc((w - r, r), r, 270, 0)
        msp.add_line((w, r), (w, h - r)); msp.add_arc((w - r, h - r), r, 0, 90)
        msp.add_line((w - r, h), (r, h)); msp.add_arc((r, h - r), r, 90, 180)
        msp.add_line((0, h - r), (0, r)); msp.add_arc((r, r), r, 180, 270)
        for x, y in corners(w, h, r):
            msp.add_circle((x, y), 0.15)
        for i in range(4):
            slot(msp, w / 2, h * 0.3 + i * h * 0.13, w * 0.45, 0.12)
    return draw


# Uploaded in this order, so the library lists them newest (last) first.
PARTS = [
    ("Fender Bracket", NORTH, A36_250, l_shape(6, 5, 1.75, [(0.9, 4.1), (5.1, 0.9)])),
    ("Fender Mount Plate", NORTH, A36_250, rect_holes(8, 4, corners(8, 4), center=0.6)),
    ("Fender Gusset", NORTH, A36_250, triangle(4, 4, [(1.0, 1.0)])),
    ("Jack Mount Plate", NORTH, A36_250, rect_holes(7, 7, corners(7, 7, 1.0), center=1.25)),
    ("Jack Mount Gusset", NORTH, A36_250, triangle(5, 3.5, [(1.2, 0.9)])),
    ("Tongue Clip", NORTH, A36_125, tab(3.5, 1.5, 0.28)),
    ("Light Bracket", NORTH, A36_125, l_shape(4, 3, 1.25, [(0.6, 2.4), (3.4, 0.6)])),
    ("Safety Chain Tab", NORTH, A36_250, tab(4, 2, 0.4)),
    ("Feeder Panel Stiffener", CEDAR, A36_125, channel(14, 3, [(2, 1.5), (7, 1.5), (12, 1.5)])),
    ("Feeder Corner Gusset", CEDAR, A36_125, triangle(6, 6, [(1.4, 1.4)])),
    ("Feeder Hinge Plate", CEDAR, A36_250, slotted_plate(6, 3, [(1.75, 1.5, 1.0), (4.25, 1.5, 1.0)])),
    ("Feeder Latch Tab", CEDAR, A36_125, tab(3, 1.25, 0.25)),
    ("Gate Hinge Strap", CEDAR, A36_250, slotted_plate(12, 2, [(2, 1, 1.5), (10, 1, 1.5)])),
    ("Cleat Backing Plate", HARBOR, SS_125, rect_holes(6, 2.5, [(1, 1.25), (5, 1.25)], r=0.2)),
    ("Rail Mount Flange", HARBOR, SS_125, flange(4, 1.25, 4)),
    ("Hatch Hinge Plate", HARBOR, SS_125, slotted_plate(5, 2.5, [(1.5, 1.25, 0.75), (3.5, 1.25, 0.75)])),
    ("Pump Cover", HARBOR, SS_125, cover(7, 5, 0.6)),
    ("Cart Shelf Bracket", SHOP, A36_125, l_shape(5, 5, 1.25, [(0.6, 4.4), (4.4, 0.6)])),
    ("Cart Caster Plate", SHOP, A36_250, rect_holes(5, 4, corners(5, 4, 0.6), r=0.22)),
    ("Cart Handle Gusset", SHOP, A36_125, triangle(3, 3, [(0.8, 0.8)])),
    ("Panel Cover", SHOP, AL_125, cover(10, 6, 0.75)),
    ("Sensor Mount", SHOP, AL_125, slotted_plate(4, 2, [(2, 1, 1.5)])),
    ("Duct Flange", SHOP, AL_125, flange(8, 5, 8, 0.18)),
    ("Test Square 1 in", SHOP, A36_250, rect_holes(1, 1)),
]

NOTES = {
    "Fender Bracket": "Deburr the inside corner.",
    "Pump Cover": "Brushed finish side up. Keep film on.",
    "Test Square 1 in": "Cut first to check kerf.",
}
CUT_FIRST = {"Test Square 1 in"}

# name, customer, notes, [(drawing, quantity per set)]
SETS = [
    ("Utility trailer fender kit", NORTH, "Both fenders for one trailer.",
     [("Fender Bracket", 4), ("Fender Mount Plate", 2), ("Fender Gusset", 4), ("Light Bracket", 2)]),
    ("Tongue jack mount", NORTH, "",
     [("Jack Mount Plate", 1), ("Jack Mount Gusset", 2), ("Tongue Clip", 2), ("Safety Chain Tab", 2)]),
    ("Hay feeder panel", CEDAR, "One panel; a feeder takes four.",
     [("Feeder Panel Stiffener", 3), ("Feeder Corner Gusset", 4), ("Feeder Hinge Plate", 2), ("Feeder Latch Tab", 1)]),
    ("Pasture gate hardware", CEDAR, "",
     [("Gate Hinge Strap", 2), ("Feeder Latch Tab", 2)]),
    ("Dock cleat backing", HARBOR, "Per cleat.",
     [("Cleat Backing Plate", 2), ("Rail Mount Flange", 1)]),
    ("Shop cart", SHOP, "Two-shelf rolling cart.",
     [("Cart Shelf Bracket", 8), ("Cart Caster Plate", 4), ("Cart Handle Gusset", 2)]),
]

# Saved nests copy_nests.py adds by copying a released Draft nest's layout of the same
# material and thickness: name, customer, status, comments, days ago.
NESTS = [
    ("N26-1QK", A36_250, NORTH, "hasBeenCut", "Fender brackets, order 3318", 12),
    ("N26-1QM", A36_125, CEDAR, "hasBeenCut", "Feeder stiffeners", 10),
    ("N26-1R4", SS_125, HARBOR, "toBeCut", "Keep film on", 6),
    ("N26-1RA", A36_250, SHOP, "toBeCut", "Cart parts", 4),
    ("N26-1RC", A36_125, CEDAR, "quote", "Quote 2291, 40 panels", 2),
    ("N26-1RF", SS_125, HARBOR, "quote", "Quote 2295", 1),
]


def main(out):
    parts = out / "parts"
    parts.mkdir(parents=True, exist_ok=True)
    drawings = []
    for name, customer, (material, grade, thickness), draw in PARTS:
        doc = ezdxf.new("R2010")
        doc.header["$INSUNITS"] = 1  # inches
        draw(doc.modelspace())
        path = parts / f"{name}.dxf"
        doc.saveas(path)
        drawings.append({
            "name": name, "customer": customer, "material": material, "grade": grade,
            "thickness": thickness, "notes": NOTES.get(name, ""), "cutFirst": name in CUT_FIRST,
            "file": str(path.resolve()),
        })
    catalog = {
        "savedBy": SAVED_BY,
        "drawings": drawings,
        "sets": [{"name": n, "customer": c, "notes": notes,
                  "members": [{"drawing": d, "quantity": q} for d, q in members]}
                 for n, c, notes, members in SETS],
        "nests": [{"name": n, "material": m, "grade": g, "thickness": t, "customer": c,
                   "status": s, "comments": comments, "daysAgo": days}
                  for n, (m, g, t), c, s, comments, days in NESTS],
    }
    (out / "catalog.json").write_text(json.dumps(catalog, indent=2))
    print(f"{len(drawings)} parts, {len(SETS)} sets, {len(NESTS)} example nests in {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]))
