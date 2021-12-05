from puzzles import day05

from tests import helpers


expect = helpers.expect_equal


sample_lines = [
    [(0, 9), (5, 9)],
    [(8, 0), (0, 8)],
    [(9, 4), (3, 4)],
    [(2, 2), (2, 1)],
    [(7, 0), (7, 4)],
    [(6, 4), (2, 0)],
    [(0, 9), (2, 9)],
    [(3, 4), (1, 4)],
    [(0, 0), (8, 8)],
    [(5, 5), (8, 2)],
]

my_file = open("input/day05.txt", "r")
content = my_file.readlines()
lines = [item.strip() for item in content]
new_lines = []
for line in lines:
    new_line = []
    coord, new_coord = line.split(" -> ")
    for loc in [coord, new_coord]:
        x, y = loc.split(",")
        new_line.append((int(x), int(y)))
    new_lines.append(new_line)
lines = new_lines


def test_part1_sample_input():
    expect(day05.overlapping_lines_horiz_vert(sample_lines), 5)


def test_part1_provided_input():
    expect(day05.overlapping_lines_horiz_vert(lines), 5608)


def test_part2_sample_input():
    expect(day05.overlapping_lines(sample_lines), 12)


def test_part2_provided_input():
    expect(day05.overlapping_lines(lines), 12080)
