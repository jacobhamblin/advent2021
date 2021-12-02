def num_increases(depths):
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1
    return count


def increases_sliding_window(depths):
    count = 0
    cur_window = 0
    i = 0
    for j in range(len(depths)):
        new_window = cur_window
        new_window += depths[j]
        if j - i > 2:
            new_window -= depths[i]
            i += 1
            if new_window > cur_window:
                count += 1
        cur_window = new_window
    return count
