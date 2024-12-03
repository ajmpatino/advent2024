# Read input (each line is a pair of numbers, separated by 3 spaces)
# Sort left numbers and right numbers separately
# Pair left numbers with right numbers in order of ascending
# Within each pair, figure out how far apart the two numbers are.  Example: pair:(1,3) has distance: 2
# Determine higher value within each pair, subtract lower value to determine distance
# Total distance is the sum of all distances
EXAMPLE_INPUT = "inputs/day1/example.txt"
EXAMPLE_DISTANCE = 11
INPUT_PAIRS = "inputs/day1/pairs.txt"


def get_total_distance(input_pairs):
    pairs = get_sorted_pairs(input_pairs)
    distances = get_distances(pairs)
    return sum(distances)


def get_sorted_pairs(input_pairs):
    with open(input_pairs, "r") as f:
        pairs = f.readlines()

    left = []
    right = []
    for number in pairs:
        left.append(int(number.split("   ")[0].strip()))
        right.append(int(number.split("   ")[1].strip()))

    sorted_left = sorted(left)
    sorted_right = sorted(right)
    return list(zip(sorted_left, sorted_right))


def get_distances(pairs):
    distances = []
    for pair in pairs:
        higher = max(pair[0], pair[1])
        lower = min(pair[0], pair[1])
        distances.append((higher - lower))
    return distances


if __name__ == "__main__":
    print(get_total_distance(INPUT_PAIRS))
