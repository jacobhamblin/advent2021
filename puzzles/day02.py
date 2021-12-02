def navigate(commands):
    direction_map = {
        "forward": (0, 1),
        "down": (1, 1),
        "up": (1, -1),
    }

    # [horizontal position, depth]
    pos = [0, 0]
    for command in commands:
        direction_str, distance_str = command.split()
        plane, mod = direction_map[direction_str]
        pos[plane] += mod * int(distance_str)
    return pos[0] * pos[1]


def navigate_with_aim(commands):
    # [horizontal position, depth, aim]
    pos = [0, 0, 0]
    for command in commands:
        direction_str, distance_str = command.split()
        distance = int(distance_str)
        if direction_str == "down":
            pos[2] += distance
        if direction_str == "up":
            pos[2] -= distance
        if direction_str == "forward":
            pos[0] += distance
            pos[1] += pos[2] * distance
    return pos[0] * pos[1]
