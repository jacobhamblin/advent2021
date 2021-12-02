from puzzles import day01

from tests import helpers


expect = helpers.expect_equal


sample_depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

my_file = open("input/day01.txt", "r")
content = my_file.readlines()
depths = [int(item.strip()) for item in content]


def test_part1_sample_input():
    expect(day01.num_increases(sample_depths), 7)


def test_part1_provided_input():
    expect(day01.num_increases(depths), 1766)


def test_part2_sample_input():
    expect(day01.increases_sliding_window(sample_depths), 5)


def test_part2_provided_input():
    expect(day01.increases_sliding_window(depths), 1797)
