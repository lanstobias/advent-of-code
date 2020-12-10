adapters = []
with open("input/day10.txt", 'r') as f:
    adapters = [int(line) for line in f]
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()


def get_diffs():
    diff_one = diff_three = 0
    for i in range(len(adapters) - 1):
        if (adapters[i + 1] - adapters[i]) == 1:
            diff_one += 1
        if (adapters[i + 1] - adapters[i]) == 3:
            diff_three += 1
    return diff_one * diff_three


memo = {}
def calc_diff(i):
    if i == (len(adapters) - 1):
        return 1

    if i in memo:
        return memo[i]

    ans = 0
    for j in range(i + 1, len(adapters)):
        if adapters[j] - adapters[i] <= 3:
            ans += calc_diff(j)

    memo[i] = ans
    return ans


print('Part 1: {}'.format(get_diffs()))

i = 0
print('Part 2: {}'.format(calc_diff(0)))

