with open("input/day9.txt", 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

preambles = 25
def get_sums(i):
    sums = []
    for m in range(i - (preambles), i):
        for n in range(i - (preambles), i):
            if (m == n):
                continue
            sums.append(numbers[n] + numbers[m])
    return sums

def find_invalid_number():
    for i in range(preambles + 1, len(numbers)):
        sums = get_sums(i)
        if numbers[i] not in sums:
            return numbers[i]

invalid_number = find_invalid_number()
print('Part 1: {}'.format(invalid_number))

# Brute force mathafacka
def find_weakness():
    nums = [x for x in numbers if x <= invalid_number]
    s = 0
    for m in range(len(nums)):
        s += nums[m]
        for n in range(m + 1, len(nums)):
            if (m == n):
                continue
            s += nums[n]
            # print('m: {}, n: {}, sum: {}'.format(m, n, s))
            if s == invalid_number:
                print('found sum: {}'.format(s))
                resulting_nums = []
                for i in range(m, n + 1):
                    resulting_nums.append(nums[i])
                print(resulting_nums)
                a = max(resulting_nums)
                b = min(resulting_nums)
                print('a: {}'.format(a))
                print('b: {}'.format(b))
                return a + b
        s = 0

print(find_weakness())
