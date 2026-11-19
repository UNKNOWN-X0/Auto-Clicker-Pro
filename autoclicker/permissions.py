"""macOS Accessibility permission check, so the app can say why clicks do nothing."""
import ctypes
import ctypes.util
import subprocess
import sys

SETTINGS_URL = "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"


def accessibility_trusted(platform=None, load_library=None):
    """True when the process may control the mouse and keyboard.

    Only macOS gates this; other platforms report True. When the check itself
    cannot run, report True so the app never nags on a guess.
    """
    platform = platform or sys.platform
    if platform != "darwin":
        return True
    try:
        load = load_library or (lambda: ctypes.cdll.LoadLibrary(ctypes.util.find_library("ApplicationServices")))
        lib = load()
        lib.AXIsProcessTrusted.restype = ctypes.c_bool
        return bool(lib.AXIsProcessTrusted())
    except (OSError, AttributeError, TypeError):
        return True


def open_accessibility_settings(run=subprocess.run):
    """Open System Settings at Privacy & Security > Accessibility."""
    run(["open", SETTINGS_URL], check=False)
