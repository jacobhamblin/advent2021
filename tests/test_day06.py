from puzzles import day06

from tests import helpers


expect = helpers.expect_equal


sample = [3, 4, 3, 1, 2]

my_file = open("input/day06.txt", "r")
content = my_file.readlines()
lines = [item.strip() for item in content]
str_input = lines[0].split(",")
provided = [int(num) for num in str_input]


def test_part1_sample_input():
    expect(day06.fish_simulate(sample, 80), 5933)


def test_part1_provided_input():
    expect(day06.fish_simulate(provided, 80), 372300)


def test_part2_sample_input():
    expect(day06.fish_simulate(sample, 256), 26984457539)


def test_part2_provided_input():
    expect(day06.fish_simulate(provided, 256), 1675781200288)
