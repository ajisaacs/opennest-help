"""Capture an OpenNest window (Windows only) into shots/raw/.

Grabs the window's on-screen pixels, so open menus, drop-downs and tooltips
over the window are included. The window is brought to the front first.

Usage:
    python tools/capture.py first-nest-main                  # main window
    python tools/capture.py auto-nest-dialog --title "Auto Nest"
    python tools/capture.py nest-menu --margin 0,0,0,400      # extra room below for a menu
    python tools/capture.py open-dialog --title "^Open$" --blur 0,115,240,360
    python tools/capture.py --list                            # show visible window titles
"""

import argparse
import ctypes
import re
import sys
import time
from ctypes import wintypes
from pathlib import Path

from PIL import ImageFilter, ImageGrab

RAW = Path(__file__).resolve().parent.parent / "shots" / "raw"

user32 = ctypes.windll.user32
dwmapi = ctypes.windll.dwmapi
DWMWA_EXTENDED_FRAME_BOUNDS = 9

# Physical pixels everywhere, whatever the display scaling.
ctypes.windll.shcore.SetProcessDpiAwareness(2)


def visible_windows():
    found = []

    @ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def callback(hwnd, _):
        if user32.IsWindowVisible(hwnd):
            length = user32.GetWindowTextLengthW(hwnd)
            if length:
                buffer = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buffer, length + 1)
                found.append((hwnd, buffer.value))
        return True

    user32.EnumWindows(callback, 0)
    return found


def window_rect(hwnd):
    rect = wintypes.RECT()
    dwmapi.DwmGetWindowAttribute(hwnd, DWMWA_EXTENDED_FRAME_BOUNDS, ctypes.byref(rect), ctypes.sizeof(rect))
    return rect.left, rect.top, rect.right, rect.bottom


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("name", nargs="?", help="output name, saved as shots/raw/<name>.png")
    parser.add_argument("--title", default=r"^OpenNest", help="window title regex (default: main window)")
    parser.add_argument("--margin", default="0,0,0,0", help="extra pixels left,top,right,bottom")
    parser.add_argument("--delay", type=float, default=0.4, help="seconds to wait after raising the window")
    parser.add_argument("--no-raise", action="store_true", help="don't bring the window forward (keeps menus open)")
    parser.add_argument("--blur", action="append", default=[], metavar="X,Y,W,H",
                        help="blur this image region before saving (personal data); repeatable")
    parser.add_argument("--list", action="store_true", help="list visible window titles and exit")
    args = parser.parse_args()

    windows = visible_windows()
    if args.list:
        for _, title in windows:
            print(title)
        return
    if not args.name:
        parser.error("name is required")

    pattern = re.compile(args.title)
    matches = [hwnd for hwnd, title in windows if pattern.search(title)]
    if not matches:
        sys.exit(f"No visible window matches {args.title!r}; try --list.")
    hwnd = matches[0]
    if not args.no_raise:
        user32.SetForegroundWindow(hwnd)
    time.sleep(args.delay)

    left, top, right, bottom = window_rect(hwnd)
    ml, mt, mr, mb = (int(v) for v in args.margin.split(","))
    image = ImageGrab.grab(bbox=(left - ml, top - mt, right + mr, bottom + mb), all_screens=True)

    # Raw captures are committed, so personal data is blurred before it reaches disk.
    for region in args.blur:
        x, y, w, h = (int(v) for v in region.split(","))
        box = (x, y, x + w, y + h)
        image.paste(image.crop(box).filter(ImageFilter.GaussianBlur(8)), box[:2])

    RAW.mkdir(parents=True, exist_ok=True)
    target = RAW / f"{args.name}.png"
    image.save(target, optimize=True)
    # Screen position of the image's top-left pixel, for converting UI Automation
    # rectangles (screen coordinates) to manifest coordinates.
    print(f"{target} {image.width}x{image.height} origin={left - ml},{top - mt}")


if __name__ == "__main__":
    main()
