def power_consumption(data):
    inverse = {"0": "1", "1": "0"}
    counts = [[0 for _ in range(len(data[0]))], [0 for _ in range(len(data[0]))]]
    for i in range(len(data[0])):
        for line in data:
            if line[i] == "0":
                counts[0][i] += 1
            if line[i] == "1":
                counts[1][i] += 1
    most_common = [
        "0" if counts[0][i] > counts[1][i] else "1" for i in range(len(counts[0]))
    ]
    least_common = [inverse[i] for i in most_common]
    gamma_rate = int("".join(most_common), 2)
    epsilon_rate = int("".join(least_common), 2)
    return gamma_rate * epsilon_rate


def compare_o2(counts):
    a, b = counts
    if a == b or b > a:
        return "1"
    if a > b:
        return "0"


def compare_co2(counts):
    a, b = counts
    if a == b or b > a:
        return "0"
    if a > b:
        return "1"


def recurse(values, index, compare):
    if len(values) == 1:
        return values[0]
    counts = [0, 0]
    for value in values:
        counts[int(value[index])] += 1
    return recurse(
        [v for v in values if v[index] == compare(counts)], index + 1, compare
    )


def life_support_rating(data):
    o2 = recurse(data, 0, compare_o2)
    co2 = recurse(data, 0, compare_co2)
    o2 = int("".join(o2), 2)
    co2 = int("".join(co2), 2)
    return o2 * co2
