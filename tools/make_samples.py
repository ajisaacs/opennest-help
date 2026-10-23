"""Write the sample DXF parts used by the tutorials to samples/ (inches)."""

from pathlib import Path

import ezdxf

OUT = Path(__file__).resolve().parent.parent / "samples"


def new_doc():
    doc = ezdxf.new("R2010")
    doc.header["$INSUNITS"] = 1  # inches
    return doc, doc.modelspace()


def save(doc, name):
    OUT.mkdir(exist_ok=True)
    doc.saveas(OUT / f"{name}.dxf")
    print(name)


def mounting_plate():
    doc, msp = new_doc()
    msp.add_lwpolyline([(0, 0), (8, 0), (8, 5), (0, 5)], close=True)
    for x, y in [(0.75, 0.75), (7.25, 0.75), (7.25, 4.25), (0.75, 4.25)]:
        msp.add_circle((x, y), 0.25)
    msp.add_circle((4, 2.5), 1.0)
    save(doc, "Mounting Plate")


def l_bracket():
    doc, msp = new_doc()
    msp.add_lwpolyline([(0, 0), (6, 0), (6, 2), (2, 2), (2, 6), (0, 6)], close=True)
    msp.add_circle((1, 5), 0.3)
    msp.add_circle((5, 1), 0.3)
    save(doc, "L Bracket")


def gusset():
    doc, msp = new_doc()
    msp.add_lwpolyline([(0, 0), (5, 0), (0, 5)], close=True)
    msp.add_circle((1.2, 1.2), 0.3)
    save(doc, "Gusset")


def round_flange():
    doc, msp = new_doc()
    msp.add_circle((0, 0), 3.0)
    msp.add_circle((0, 0), 1.25)
    for x, y in [(2.25, 0), (-2.25, 0), (0, 2.25), (0, -2.25)]:
        msp.add_circle((x, y), 0.2)
    save(doc, "Round Flange")


if __name__ == "__main__":
    mounting_plate()
    l_bracket()
    gusset()
    round_flange()
