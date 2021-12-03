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
