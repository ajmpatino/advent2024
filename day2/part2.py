# Input is one report per line
# Each report is a list of numbers called levels, separated by a space
# Determine safety:
# Levels must be either all increasing or all decreasing
# Difference between any 2 adjacent levels must be >= 1 <= 3
# Determine how many reports are safe

EXAMPLE_REPORTS = "inputs/day2/example.txt"
EXAMPLE_SAFE = 4
REPORTS = "inputs/day2/reports.txt"
SAFE = 689


def main(input):
    safe_reports = []
    dangerous_reports = []
    reports = read_input(input)
    for report in reports:
        report = normalize_report(report)
        if is_safe(report):
            safe_reports.append(report)
        else:
            dangerous_reports.append(report)
    dampener_reports = get_single_level_removed_reports(dangerous_reports)
    for report_index in dampener_reports:
        for variation in dampener_reports[report_index]["variations"]:
            if is_safe(variation):
                safe_reports.append(variation)
                break
    return len(safe_reports)


def read_input(input):
    with open(input, "r") as f:
        return f.readlines()
    return [report.strip() for report in input]


def normalize_report(report):
    report = report.split(" ")
    return [int(n) for n in report]


def is_safe(report):
    consistent_direction = check_consistent_direction(report)
    allowable_increments = check_allowable_increments(report)
    return all([consistent_direction, allowable_increments])


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


def get_single_level_removed_reports(dangerous_reports):
    report_index = 1
    every_possible_version = {}
    for report in dangerous_reports:
        every_possible_version[report_index] = {}
        every_possible_version[report_index]["variations"] = []
        for n in range(0, len(report)):
            variation = report.copy()
            del variation[n]
            every_possible_version[report_index]["variations"].append(variation)
        report_index += 1
    return every_possible_version


if __name__ == "__main__":
    safe = main(REPORTS)
    print(f"{safe = }")
    assert safe == SAFE
