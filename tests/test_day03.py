from puzzles import day03

from tests import helpers


expect = helpers.expect_equal


sample_binary = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

my_file = open("input/day03.txt", "r")
content = my_file.readlines()
binary = [item.strip() for item in content]


def test_part1_sample_input():
    expect(day03.power_consumption(sample_binary), 198)


def test_part1_provided_input():
    expect(day03.power_consumption(binary), 693486)


def test_part2_sample_input():
    expect(day03.life_support_rating(sample_binary), 230)


def test_part2_provided_input():
    expect(day03.life_support_rating(binary), 230)
