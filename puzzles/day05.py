def get_line_coords(a, b):
    ax, ay = a
    bx, by = b
    if ax == bx:
        start = ay if ay < by else by
        end = ay if ay > by else by
        coords = [(ax, new_y) for new_y in range(start, end + 1)]
    elif ay == by:
        start = ax if ax < bx else bx
        end = ax if ax > bx else bx
        coords = [(new_x, ay) for new_x in range(start, end + 1)]
    else:
        diff = abs(bx - ax)
        coords = []
        for i in range(diff + 1):
            cur_x = ax + i if ax < bx else ax - i
            cur_y = ay + i if ay < by else ay - i
            coords.append((cur_x, cur_y))
    return coords


def overlapping_lines_horiz_vert(lines):
    coords = {}
    for line in lines:
        a, b = line
        ax, ay = a
        bx, by = b
        if ax == bx or ay == by:
            line_coords = get_line_coords(a, b)
            for coord in line_coords:
                existing_val = coords.get(coord) or 0
                coords[coord] = existing_val + 1
    overlap_count = 0
    for key in coords.keys():
        if coords[key] > 1:
            overlap_count += 1
    return overlap_count


def overlapping_lines(lines):
    coords = {}
    for line in lines:
        a, b = line
        ax, ay = a
        bx, by = b
        line_coords = get_line_coords(a, b)
        for coord in line_coords:
            existing_val = coords.get(coord) or 0
            coords[coord] = existing_val + 1

    overlap_count = 0
    for key in coords.keys():
        if coords[key] > 1:
            overlap_count += 1
    return overlap_count
