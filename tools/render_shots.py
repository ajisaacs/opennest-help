"""Render annotated screenshots from raw captures and JSON manifests.

Each `shots/<name>.json` describes one published image, `docs/images/<name>.png`:

    {
      "source": "raw/first-nest-main.png",   # relative to shots/
      "crop": [x, y, width, height],           # optional, in source pixels
      "max_width": 1100,                       # optional downscale after markup
      "annotations": [
        {"type": "dim", "keep": [[x, y, w, h], ...]},   # darken all but these
        {"type": "mask", "rect": [x, y, w, h]},          # blur sensitive data
        {"type": "box", "rect": [x, y, w, h]},           # highlight outline
        {"type": "arrow", "from": [x, y], "to": [x, y]},
        {"type": "callout", "n": 1, "at": [x, y]},       # numbered marker
        {"type": "label", "at": [x, y], "text": "..."}
      ]
    }

All coordinates are in raw-capture pixels, before cropping, so a manifest keeps
working when only the crop changes. Annotations are drawn in list order.

Usage: python tools/render_shots.py [name ...]   (default: every manifest)
"""

import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "shots"
OUT = ROOT / "docs" / "images"

ACCENT = (232, 89, 12)
WHITE = (255, 255, 255)
SHADOW = (0, 0, 0, 90)

CALLOUT_RADIUS = 14
STROKE = 3
FONT_CANDIDATES = [
    "C:/Windows/Fonts/segoeuib.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "DejaVuSans-Bold.ttf",
]


def load_font(size):
    for candidate in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rect_xyxy(rect):
    x, y, w, h = rect
    return [x, y, x + w, y + h]


def draw_dim(image, keep):
    shade = Image.new("RGBA", image.size, (0, 0, 0, 115))
    hole = ImageDraw.Draw(shade)
    for rect in keep:
        hole.rounded_rectangle(rect_xyxy(rect), radius=6, fill=(0, 0, 0, 0))
    image.alpha_composite(shade)


def draw_mask(image, rect):
    box = tuple(rect_xyxy(rect))
    region = image.crop(box).filter(ImageFilter.GaussianBlur(8))
    image.paste(region, box[:2])


def draw_box(layer, rect):
    x0, y0, x1, y1 = rect_xyxy(rect)
    layer.rounded_rectangle([x0 + 2, y0 + 2, x1 + 2, y1 + 2], radius=6, outline=SHADOW, width=STROKE)
    layer.rounded_rectangle([x0, y0, x1, y1], radius=6, outline=ACCENT, width=STROKE)


def draw_arrow(layer, start, end):
    layer.line([tuple(start), tuple(end)], fill=ACCENT, width=STROKE + 1)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    head = 14
    left = (end[0] - head * math.cos(angle - 0.45), end[1] - head * math.sin(angle - 0.45))
    right = (end[0] - head * math.cos(angle + 0.45), end[1] - head * math.sin(angle + 0.45))
    layer.polygon([tuple(end), left, right], fill=ACCENT)


def draw_callout(layer, at, number, font):
    x, y = at
    r = CALLOUT_RADIUS
    layer.ellipse([x - r + 2, y - r + 2, x + r + 2, y + r + 2], fill=SHADOW)
    layer.ellipse([x - r, y - r, x + r, y + r], fill=ACCENT, outline=WHITE, width=2)
    layer.text((x, y), str(number), fill=WHITE, font=font, anchor="mm")


def draw_label(layer, at, text, font):
    x, y = at
    left, top, right, bottom = layer.textbbox((x, y), text, font=font, anchor="lm")
    pad = 6
    layer.rounded_rectangle([left - pad, top - pad, right + pad, bottom + pad], radius=5, fill=ACCENT)
    layer.text((x, y), text, fill=WHITE, font=font, anchor="lm")


def render(manifest_path):
    spec = json.loads(manifest_path.read_text(encoding="utf-8"))
    image = Image.open(SHOTS / spec["source"]).convert("RGBA")
    callout_font = load_font(16)
    label_font = load_font(15)

    for note in spec.get("annotations", []):
        kind = note["type"]
        if kind == "dim":
            draw_dim(image, note["keep"])
            continue
        if kind == "mask":
            draw_mask(image, note["rect"])
            continue
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
        layer = ImageDraw.Draw(overlay)
        if kind == "box":
            draw_box(layer, note["rect"])
        elif kind == "arrow":
            draw_arrow(layer, note["from"], note["to"])
        elif kind == "callout":
            draw_callout(layer, note["at"], note["n"], callout_font)
        elif kind == "label":
            draw_label(layer, note["at"], note["text"], label_font)
        else:
            raise ValueError(f"{manifest_path.name}: unknown annotation type {kind!r}")
        image.alpha_composite(overlay)

    if "crop" in spec:
        image = image.crop(tuple(rect_xyxy(spec["crop"])))
    max_width = spec.get("max_width")
    if max_width and image.width > max_width:
        height = round(image.height * max_width / image.width)
        image = image.resize((max_width, height), Image.LANCZOS)

    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f"{manifest_path.stem}.png"
    image.convert("RGB").save(target, optimize=True)
    return target


def main(names):
    manifests = [SHOTS / f"{n}.json" for n in names] if names else sorted(SHOTS.glob("*.json"))
    if not manifests:
        print("No shot manifests found.")
        return
    for manifest in manifests:
        print(f"{manifest.stem}: {render(manifest).relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
