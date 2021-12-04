def has_bingo(board, cur_nums):
    for line in board["values"]:
        selected_values = [v.get("value") for v in line if v.get("selected")]
        if len(selected_values) == 5:
            return True
    for j in range(len(board["values"][0])):
        col = [board["values"][i][j] for i in range(len(board["values"]))]
        selected_values = [v.get("value") for v in col if v.get("selected")]
        if len(selected_values) == 5:
            return True
    return False


def get_return_value(board, final_num):
    unmarked_sum = sum(
        [
            v.get("value")
            for line in board["values"]
            for v in line
            if not v.get("selected")
        ]
    )
    return unmarked_sum * final_num


def bingo(selected_nums, boards):
    boards_dict = {}
    for i in range(len(boards)):
        board = boards[i]
        data = {"presence": set(), "values": [], "locations": {}}

        # j is a row index
        for j in range(len(board)):
            line = board[j]
            values_line = []

            # k is a col index
            for k in range(len(line)):
                value = line[k]
                data["presence"].add(value)
                values_line.append({"value": value, "selected": False})
                data["locations"][value] = (j, k)
            data["values"].append(values_line)
        boards_dict[i] = data

    cur_nums = set()
    for num in selected_nums:
        cur_nums.add(num)

        # i is board index
        for i in range(len(boards_dict.keys())):
            board = boards_dict[i]
            if num in board["presence"]:
                row, col = board["locations"][num]
                board["values"][row][col]["selected"] = True
            if len(cur_nums) > 4:
                res = has_bingo(board, cur_nums)
                if res:
                    return get_return_value(board, num)
