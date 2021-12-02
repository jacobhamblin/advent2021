from puzzles import day01

from tests import helpers


expect = helpers.expect_equal


def test_sample_data():
    depths = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    expect(day01.numIncreases(depths), 7)


def test_real_input():
    my_file = open("input/day01.txt", "r")
    content = my_file.readlines()
    depths = [int(item.strip()) for item in content]
    expect(day01.numIncreases(depths), 1766)
