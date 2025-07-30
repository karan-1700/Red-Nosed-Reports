
# Advent of Code 2024 – Day 2: Red-Nosed Reports

This repository contains the Python solution for **Day 2** of [Advent of Code 2024](https://adventofcode.com/2024/day/2) – *Red-Nosed Reports*.

## Problem Summary

You are given multiple reactor safety reports, each consisting of a list of numeric levels. A report is considered **safe** if:

1. All levels are either **strictly increasing** or **strictly decreasing**.
2. The absolute difference between any two adjacent levels is **at least 1 and at most 3**.

The goal is to determine how many reports are safe based on these two conditions.

---

## Example

Given the following reports:

```bash
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

Only 2 reports are safe:
- `7 6 4 2 1` (decreasing)
- `1 3 6 7 9` (increasing)

---

## Solution Overview

The solution involves:
- Parsing each line of levels into a list of integers.
- Computing adjacent differences.
- Checking if the differences are all positive (increasing) or all negative (decreasing).
- Ensuring each difference is within the allowed step range of 1 to 3.

---

## File Structure

├── `day02_red_nosed_reports.py` # Main solution code

└── `README.md` # This documentation

---

## How to Run

You can run the solution using `Python 3.9+`:

```bash
python day02_red_nosed_reports.py
```

---

# Author

Karansinh Padhiar

GitHub: @karan-1700
