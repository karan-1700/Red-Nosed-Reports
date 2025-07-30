def is_safe(report_line: str) -> bool:
    levels = list(map(int, report_line.strip().split()))
    diffs = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]

    # Check that all diffs are either all positive or all negative
    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)
    
    # Check each diff is between 1 and 3 (inclusive) in magnitude
    valid_steps = all(1 <= abs(d) <= 3 for d in diffs)
    
    return valid_steps and (increasing or decreasing)

def count_safe_reports(input_lines: list[str]) -> int:
    return sum(1 for line in input_lines if is_safe(line))

# Example usage:
example_input = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9"
]

print("Safe reports:", count_safe_reports(example_input))  # Output: 2
