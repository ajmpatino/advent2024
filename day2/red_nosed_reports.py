# Input is one report per line
# Each report is a list of numbers called levels, separated by a space
# Determine safety:
# Levels must be either all increasing or all decreasing
# Difference between any 2 adjacent levels must be >= 1 <= 3
# Determine how many reports are safe
EXAMPLE_REPORTS = "inputs/day2/example.txt"
EXAMPLE_SAFE = 2
REPORTS = "inputs/day2/reports.txt"
SAFE = 660


def get_safe_reports(input):
    reports = read_input(input)
    safe_reports = []
    for report in reports:
        report = report.split(" ")
        report = [int(n) for n in report]
        consistent_direction = check_consistent_direction(report)
        allowable_increments = False
        if consistent_direction:
            allowable_increments = check_allowable_increments(report)
        if consistent_direction and allowable_increments:
            safe_reports.append(report)
    return len(safe_reports)


def read_input(input):
    with open(input, "r") as f:
        data = f.readlines()
    return [report.strip() for report in data]


def check_consistent_direction(report):
    ascending = report[0] < report[1]
    if not ascending:
        return check_descending(report)
    return check_ascending(report)


def check_descending(report):
    for n in range(0, len(report) - 1):
        if report[n] < report[n + 1]:
            return False
    return True


def check_ascending(report):
    for n in range(0, len(report) - 1):
        if report[n] > report[n + 1]:
            return False
    return True


def check_allowable_increments(report):
    for n in range(0, len(report) - 1):
        if abs(report[n] - report[n + 1]) < 1 or abs(report[n] - report[n + 1]) > 3:
            return False
    return True


if __name__ == "__main__":
    print(get_safe_reports(REPORTS))
