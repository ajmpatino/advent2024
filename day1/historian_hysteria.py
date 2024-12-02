# Read input (each line is a pair of numbers, separated by 3 spaces)
# Sort left numbers and right numbers separately
# Pair left numbers with right numbers in order of ascending
# Within each pair, figure out how far apart the two numbers are.  Example: pair:(1,3) has distance: 2
# Determine higher value within each pair, subtract lower value to determine distance
# Total distance is the sum of all distances
EXAMPLE_DISTANCE = 11


def get_total_distance(input_pairs):
    pairs = get_sorted_pairs(input_pairs)


def get_sorted_pairs(input_pairs):
    with open(input_pairs, "r") as f:
        pairs = f.readlines()

    left = []
    right = []
    for number in pairs:
        left.append(number.split("   ")[0].strip())
        right.append(number.split("   ")[1].strip())

    sorted_left = sorted(left)
    sorted_right = sorted(right)
    return list(zip(sorted_left, sorted_right))


if __name__ == "__main__":
    distance = get_total_distance("inputs/day1/example.txt")
    # assert distance == EXAMPLE_DISTANCE
