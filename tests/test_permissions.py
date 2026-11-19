"""Permission check tests with fake system libraries; no real macOS calls."""
import unittest

from autoclicker.permissions import accessibility_trusted, open_accessibility_settings, SETTINGS_URL


class FakeLib:
    def __init__(self, trusted):
        self.trusted = trusted
        outer = self

        class Fn:
            restype = None

            def __call__(self):
                return outer.trusted

        self.AXIsProcessTrusted = Fn()


class PermissionTests(unittest.TestCase):
    def test_other_platforms_never_ask(self):
        self.assertTrue(accessibility_trusted(platform="win32"))
        self.assertTrue(accessibility_trusted(platform="linux"))

    def test_macos_reports_the_system_answer(self):
        self.assertFalse(accessibility_trusted(platform="darwin", load_library=lambda: FakeLib(False)))
        self.assertTrue(accessibility_trusted(platform="darwin", load_library=lambda: FakeLib(True)))

    def test_a_failed_check_does_not_nag(self):
        def broken():
            raise OSError("no ApplicationServices")
        self.assertTrue(accessibility_trusted(platform="darwin", load_library=broken))

    def test_open_settings_uses_the_privacy_pane(self):
        calls = []
        open_accessibility_settings(run=lambda args, check: calls.append(args))
        self.assertEqual(calls, [["open", SETTINGS_URL]])


if __name__ == "__main__":
    unittest.main()
