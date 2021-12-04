from puzzles import day04

from tests import helpers


expect = helpers.expect_equal


sample_selected_nums = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]

sample_boards = [
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
    [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ],
]

my_file = open("input/day04.txt", "r")
content = my_file.readlines()
lines = [item.strip() for item in content]
selected_nums = [int(num) for num in lines[0].split(",")]

boards = []
board = []
for line in lines[1:]:
    if line == "":
        if len(board):
            boards.append(board)
            board = []
    else:
        board.append([int(num) for num in line.split()])
boards.append(board)


def test_part1_sample_input():
    expect(day04.bingo(sample_selected_nums, sample_boards), 4512)


def test_part1_provided_input():
    expect(day04.bingo(selected_nums, boards), 4662)


def test_part2_sample_input():
    expect(day04.bingo(sample_selected_nums, sample_boards), 230)


def test_part2_provided_input():
    expect(day04.bingo(selected_nums, boards), 3379326)
