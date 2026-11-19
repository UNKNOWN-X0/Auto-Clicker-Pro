# Graph Report - Auto-Clicker-Pro  (2026-11-19)

## Corpus Check
- 13 files · ~2,995 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 113 nodes · 165 edges · 9 communities (5 shown, 4 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `54c92d7d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Application Interface
- Click and Macro Engine
- steps
- Input Engine Tests
- App Guide and Safety
- Build Configuration
- Input Event Listeners
- Project instructions

## God Nodes (most connected - your core abstractions)
1. `EngineTests` - 8 edges
2. `AutoClicker Pro desktop app` - 7 edges
3. `steps` - 5 edges
4. `click_loop()` - 5 edges
5. `macro_replay()` - 5 edges
6. `_refresh_status()` - 5 edges
7. `start_clicking()` - 5 edges
8. `stop_clicking()` - 5 edges
9. `click_loop()` - 5 edges
10. `main()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `click_loop()` --calls--> `click_loop()`  [EXTRACTED]
  autoclicker/app.py → autoclicker/engine.py
- `macro_replay()` --calls--> `macro_replay()`  [EXTRACTED]
  autoclicker/app.py → autoclicker/engine.py
- `Mouse and keyboard macro recording and replay` --conceptually_related_to--> `pynput keyboard and mouse input dependency`  [INFERRED]
  README.md → requirements.txt
- `Mouse click automation` --conceptually_related_to--> `PyAutoGUI input automation dependency`  [INFERRED]
  README.md → requirements.txt

## Import Cycles
- None detected.

## Communities (9 total, 4 thin omitted)

### Community 0 - "Application Interface"
Cohesion: 0.13
Nodes (16): add_current_pos(), clear_points(), click_loop(), macro_replay(), on_close(), on_press(), _refresh_points(), _refresh_status() (+8 more)

### Community 1 - "Click and Macro Engine"
Cohesion: 0.17
Nodes (4): click_loop(), do_click(), macro_replay(), AppState

### Community 2 - "steps"
Cohesion: 0.12
Nodes (15): jobs, test, python-version, name, on, name, run, uses (+7 more)

### Community 4 - "App Guide and Safety"
Cohesion: 0.17
Nodes (11): AutoClicker Pro desktop app, Top-left pointer emergency failsafe, Engine tests use fake input devices, Locally saved application settings, Mouse and keyboard macro recording and replay, Mouse click automation, Python package requirements, CustomTkinter UI dependency (+3 more)

### Community 6 - "Input Event Listeners"
Cohesion: 0.28
Nodes (8): hk_row(), listen(), on_change(), on_kp(), start_cap(), _key_str(), _start_recording(), on_kp()

## Knowledge Gaps
- **5 isolated node(s):** `Top-left pointer emergency failsafe`, `Engine tests use fake input devices`, `Locally saved application settings`, `CustomTkinter UI dependency`, `Pillow image library dependency`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 45 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `hk_row()` connect `Input Event Listeners` to `Application Interface`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `click_loop()` (e.g. with `_refresh_status()` and `_update_counter()`) actually correct?**
  _`click_loop()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Top-left pointer emergency failsafe`, `Engine tests use fake input devices`, `Locally saved application settings` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Application Interface` be split into smaller, more focused modules?**
  _Cohesion score 0.1282051282051282 - nodes in this community are weakly interconnected._
- **Why does `_start_recording()` connect `Input Event Listeners` to `Application Interface`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `macro_replay()` (e.g. with `_refresh_status()` and `_update_counter()`) actually correct?**
  _`macro_replay()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `steps` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._