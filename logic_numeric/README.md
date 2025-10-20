# Logic + Numeric Thinking (Core Python)

This folder contains clean, traditional Python implementations that exercise:
- Index reasoning (`range(start, stop, step)`, `enumerate`)
- Accumulators and counters
- Lists of lists (tabular-style data)
- Dictionaries and nested dictionaries (JSON-style data)
- Max-tracking patterns (top performer)

These are foundational skills used later in AI/ML data handling and training loops.

## Files
- `day6_indices_enumerate.py` — index control, enumerate, reverse (copy + in-place)
- `day7_list_of_lists.py` — totals and averages per row
- `day7_dicts.py` — dictionary iteration + top-performer logic
- `day7_nested_dicts.py` — nested dict aggregation, best subject, class math average
## Day 8 – Simulation and State Control
- Practiced modeling simple systems using loops and conditionals.
- Implemented:
  - **Traffic Light Sequence** — repeated color cycling.
  - **Pedestrian Crossing** — conditional behavior based on light color.
  - **ATM Simulation** — state tracking and conditional branching.
- Reinforced concepts of:
  - Control variables (`cycles`, `balance`, `lights`)
  - State changes over time
  - `while` loops with `break` conditions

## Day 9 – Refactoring to Functions
- Practiced encapsulating logic into functions for reusability.
- Learned:
  - How to define and call functions with parameters.
  - Difference between `return` vs. `print`.
  - How multiple helper functions work together (composition).
- Implemented:
  - `compute_total()` – sum of a list.
  - `compute_average()` – average using total helper.
  - `find_top_student()` – finds highest performer from a dictionary.
- Reinforced modular design and clean functional flow.

## Day 10 – Logical Synthesis (Library Checkout System)
- End-to-end mini system using functions + loops + conditionals.
- Features:
  - Show books with availability
  - Checkout (validates availability)
  - Return (validates state)
- Highlights: state stored in a dictionary, clean function boundaries, simple console menu.

## Notes
- Code favors clarity over compact syntax (no list comprehensions; no “magical” one-liners).
- Variable names are explicit; loops are step-by-step and easy to trace.