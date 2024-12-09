import re
from math import prod


MULTIPLICATION_FORMULA = "mul\(\d{0,3},\d{0,3}\)"
DONT_DO_IT = "(?s)don't\(\).*?do\(\)"


def read_input(input):
    with open(input, "r") as f:
        return f.read()


def do_stupid_ugly_things(data):
    data = get_the_donts_outta_here(data)
    multiply_me = re.findall(MULTIPLICATION_FORMULA, data)
    product = 0
    for junk in multiply_me:
        slicey = junk.split(",")
        first_number = slicey[0].replace("mul(", "")
        second_number = slicey[1].replace(")", "")
        product += prod([int(first_number), int(second_number)])
    return product


def get_the_donts_outta_here(data: str):
    do_nots = re.findall(DONT_DO_IT, data, re.DOTALL)
    for no_thnx in do_nots:
        data = data.replace(no_thnx, "")
    return data


if __name__ == "__main__":
    data = read_input("inputs/day3/multipliers.txt")
    dumb = do_stupid_ugly_things(data)
    print(f"answer = {dumb}")
    assert dumb > 55835550
    assert dumb != 110319118
    assert dumb != 158051020
    assert dumb != 93729253
