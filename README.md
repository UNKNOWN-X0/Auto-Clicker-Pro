# AutoClicker Pro

[![Checks](https://github.com/UNKNOWN-X0/Auto-Clicker-Pro/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/UNKNOWN-X0/Auto-Clicker-Pro/actions/workflows/checks.yml)
[![Version](https://img.shields.io/github/v/release/UNKNOWN-X0/Auto-Clicker-Pro?label=version)](https://github.com/UNKNOWN-X0/Auto-Clicker-Pro/releases)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

A Python desktop app for automating mouse clicks and recording simple mouse-and-keyboard macros. It uses a dark interface and saves its settings locally.

**[Download AutoClicker Pro →](https://github.com/UNKNOWN-X0/Auto-Clicker-Pro/releases)**

## Features

- **Precise timing:** click intervals down to milliseconds, with left, right, or middle clicks and double-clicks.
- **Repeat control:** click indefinitely or a fixed number of times.
- **Multi-point clicking:** cycle through several screen coordinates, with optional timing and position variation.
- **Hotkeys:** keyboard shortcuts to start and stop clicking.
- **Macros:** record and replay mouse and keyboard input sequences.
- **Saved settings:** restored automatically on the next launch.
- **Failsafe:** move the pointer to the top-left corner to stop PyAutoGUI immediately.

## Getting started

### Run it yourself

Requires Python 3.10 or later.

```sh
python -m pip install -r requirements.txt
python auto_clicker.py
```

On macOS, you may need to grant Accessibility permissions to the terminal or packaged app before it can control the mouse and keyboard. Platform permissions and input-library support can also affect behavior on other systems.

## Privacy

The app stores settings in `~/.autoclicker_config.json`. The project code does not include an analytics or telemetry service. Macro files can contain recorded key presses and screen coordinates, so review them before sharing.

## Development

### Build an executable

Run the build helper on the operating system you want to package for:

```sh
python build.py
```

The helper installs PyInstaller if needed, then writes the executable to `dist/`. Build artifacts are local; download-ready binaries are available only if published on the [Releases](https://github.com/UNKNOWN-X0/Auto-Clicker-Pro/releases) page.

## Tests

```sh
python -m unittest discover -s tests
```

The tests use fake input devices and do not move or click the real mouse. `.github/workflows/checks.yml` runs them, plus Pylint in errors-only mode, on Python 3.10 and 3.14 for every push and pull request.

## Project structure

```text
auto_clicker.py              Launcher
autoclicker/app.py           Desktop interface and event handlers
autoclicker/engine.py        Click and macro playback logic
autoclicker/config.py        App constants and local settings path
autoclicker/state.py         Shared runtime state
autoclicker/dependencies.py  UI and input-library setup
build.py                     Local executable packaging helper
tests/test_engine.py         Engine regression tests
```

## License

MIT. See [LICENSE](LICENSE).
