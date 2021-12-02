from puzzles import day02

from tests import helpers


expect = helpers.expect_equal


sample_commands = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]

my_file = open("input/day02.txt", "r")
content = my_file.readlines()
commands = [item.strip() for item in content]


def test_part1_sample_input():
    expect(day02.navigate(sample_commands), 150)


def test_part1_provided_input():
    expect(day02.navigate(commands), 1692075)


def test_part2_sample_input():
    expect(day02.navigate_with_aim(sample_commands), 900)


def test_part2_provided_input():
    expect(day02.navigate_with_aim(commands), 1749524700)
