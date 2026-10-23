"""Replay the "Your first nest" tutorial in a running OpenNest and capture each step.

Start the app with tools/launch-app.ps1 first (1280x820 main window at 40,40, 100%
display scaling). Clicks use window-relative positions measured from that layout,
so re-measure them if the UI moves. Each step saves shots/raw/<name>.png.

Usage: python tools/flows/first_nest.py [--until <step>]
"""

import argparse
import ctypes
import re
import subprocess
import sys
import time
from pathlib import Path

from pywinauto import keyboard, mouse

ROOT = Path(__file__).resolve().parents[2]
SAMPLES = ROOT / "samples"
user32 = ctypes.windll.user32
ctypes.windll.shcore.SetProcessDpiAwareness(2)


def window(title_re, timeout=30):
    rx = re.compile(title_re)
    deadline = time.time() + timeout
    while time.time() < deadline:
        found = []

        @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
        def callback(hwnd, _):
            if user32.IsWindowVisible(hwnd):
                buffer = ctypes.create_unicode_buffer(512)
                user32.GetWindowTextW(hwnd, buffer, 512)
                if rx.search(buffer.value):
                    found.append(hwnd)
            return True

        user32.EnumWindows(callback, 0)
        if found:
            return found[0]
        time.sleep(0.25)
    sys.exit(f"Timed out waiting for window {title_re!r}")


def origin(hwnd):
    rect = ctypes.wintypes.RECT()
    ctypes.windll.dwmapi.DwmGetWindowAttribute(hwnd, 9, ctypes.byref(rect), ctypes.sizeof(rect))
    return rect.left, rect.top


def click(hwnd, x, y, double=False):
    left, top = origin(hwnd)
    (mouse.double_click if double else mouse.click)(coords=(left + x, top + y))
    time.sleep(0.6)


def move(hwnd, x, y, width, height):
    user32.ShowWindow(hwnd, 9)
    user32.MoveWindow(hwnd, x, y, width, height, True)
    time.sleep(0.5)


def capture(name, title, *extra):
    subprocess.run([sys.executable, str(ROOT / "tools" / "capture.py"), name, "--title", title, *extra], check=True)


def run(until):
    import ctypes.wintypes  # noqa: F401  (RECT)

    main = window(r"^OpenNest - \[")
    capture("first-nest-empty", r"^OpenNest - \[")
    if until == "empty":
        return

    # Drawings tab > Import Drawings
    click(main, 26, 137)
    dialog = window(r"^Open$")
    from pywinauto import Application
    files = Application(backend="win32").connect(handle=dialog).window(handle=dialog)
    name_box = files.child_window(class_name="Edit", found_index=0)
    name_box.set_edit_text(str(SAMPLES))
    files.child_window(title="&Open", class_name="Button").click()
    time.sleep(1.5)
    name_box.set_edit_text('"Gusset.dxf" "L Bracket.dxf" "Mounting Plate.dxf" "Round Flange.dxf"')
    move(dialog, 120, 120, 900, 560)
    # Blur the navigation pane: it lists the capturing user's own folders.
    capture("first-nest-open-dialog", r"^Open$", "--blur", "0,115,240,360")
    files.child_window(title="&Open", class_name="Button").click()

    converter = window(r"^CAD Converter")
    time.sleep(2)
    move(converter, 40, 40, 1420, 860)
    for row_y, qty in [(55, 30), (103, 20), (151, 10), (199, 12)]:
        click(converter, 120, row_y)
        click(converter, 527, 778, double=True)
        keyboard.send_keys(f"^a{qty}{{TAB}}")
        time.sleep(0.4)
    click(converter, 120, 151)
    time.sleep(1)
    capture("first-nest-converter", r"^CAD Converter")
    click(converter, 1251, 826)  # Accept
    time.sleep(2)
    capture("first-nest-drawings", r"^OpenNest - \[")
    if until == "drawings":
        return

    click(main, 365, 74)  # Auto Nest toolbar button
    auto = window(r"^AutoNest$")
    time.sleep(1)
    capture("first-nest-autonest", r"^AutoNest$")
    click(auto, 88, 56)  # Plates tab
    capture("first-nest-autonest-plates", r"^AutoNest$")
    click(auto, 421, 563)  # Accept
    window(r"^Nesting Progress")
    time.sleep(1.5)
    capture("first-nest-progress", r"^Nesting Progress")
    review = window(r"^Review Auto Nest", timeout=180)
    time.sleep(1)
    capture("first-nest-review", r"^Review Auto Nest")
    click(review, 777, 489)  # Keep
    time.sleep(1.5)
    click(main, 861, 110)  # Zoom To Fit
    time.sleep(1)
    capture("first-nest-result", r"^OpenNest - \[")
    if until == "result":
        return

    click(main, 498, 74)  # Plan Cutting toolbar button
    time.sleep(8)
    capture("first-nest-plan-cutting", r"^OpenNest - \[")
    click(main, 918, 377)  # Apply
    time.sleep(3)

    click(main, 628, 74)  # Post drop-down arrow
    time.sleep(1)
    left, top = origin(main)
    mouse.move(coords=(left + 680, top + 104))
    time.sleep(1.2)
    capture("first-nest-post-menu", r"^OpenNest - \[", "--no-raise")
    click(main, 680, 104)  # first post processor
    settings = window(r"Settings$")
    time.sleep(1)
    capture("first-nest-post-settings", r"Settings$")
    click(settings, 332, 566)  # OK
    window(r"^Verify Nest Before Posting", timeout=120)
    time.sleep(10)
    capture("first-nest-verify", r"^Verify Nest Before Posting")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--until", choices=["empty", "drawings", "result", "verify"], default="verify")
    run(parser.parse_args().until)
