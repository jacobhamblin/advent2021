def helper(age, days_rem, memo):
    spawn = days_rem - age
    family = 0
    while spawn >= 1:
        if memo[spawn]:
            family += memo[spawn]
        else:
            memo[spawn] = 1 + helper(8, spawn - 1, memo)
            family += memo[spawn]
        spawn -= 7
    return family


def fish_simulate(ages, days):
    memo = [None for _ in range(300)]
    total = 0
    for age in ages:
        total += 1 + helper(age, days, memo)
    return total
