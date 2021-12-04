def has_bingo(board, cur_nums):
    for line in board:
        selected_values = [v for v in line if v in cur_nums]
        if len(selected_values) == 5:
            return True
    for j in range(len(board[0])):
        col = [board[i][j] for i in range(len(board))]
        selected_values = [v for v in col if v in cur_nums]
        if len(selected_values) == 5:
            return True
    return False


def get_return_value(board, cur_nums, final_num):
    unmarked_sum = sum([v for line in board for v in line if not v in cur_nums])
    return unmarked_sum * final_num


def first_bingo(selected_nums, boards):
    cur_nums = set()
    for num in selected_nums:
        cur_nums.add(num)

        for board in boards:
            res = has_bingo(board, cur_nums)
            if res:
                return get_return_value(board, cur_nums, num)


def last_bingo(selected_nums, boards):
    bingo_boards = set()
    cur_nums = set()
    for num in selected_nums:
        cur_nums.add(num)

        for i in range(len(boards)):
            board = boards[i]
            if not i in bingo_boards:
                res = has_bingo(board, cur_nums)
                if res:
                    bingo_boards.add(i)
                    if len(bingo_boards) == len(boards):
                        return get_return_value(board, cur_nums, num)
