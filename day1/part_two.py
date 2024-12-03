from historian_hysteria import read_input, split_pairs, EXAMPLE_INPUT

# Figure out exactly how often each number from the left list appears in the right list
# Multiply each number in the left list by the number of times it appears in the right list
# Add the multiplied numbers to get similarity score
EXAMPLE_SIMILARITY_SCORE = 31


def get_similarity_score(input_pairs):
    pairs = read_input(input_pairs)
    left, right = split_pairs(pairs)
    return do_math_magic(left, right)


def do_math_magic(left, right):
    multiplied = []
    for number in left:
        count = right.count(number)
        multiplied.append(number * count)
    return sum(multiplied)


if __name__ == "__main__":
    similarity = get_similarity_score(EXAMPLE_INPUT)
    assert similarity == EXAMPLE_SIMILARITY_SCORE
