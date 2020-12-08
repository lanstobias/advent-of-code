import copy

program = []
with open("input/day8.txt") as lines:
    instr = []
    for line in lines:
        line = line.strip()
        instruction = line.split(' ')
        instruction.append(0)
        program.append(instruction)

def run(prog):
    COUNTER = 2
    acc = 0
    pc = 0
    while pc < len(prog):
        operator = prog[pc][0]
        argument = prog[pc][1][0]
        value = int(prog[pc][1][1:])

        # Part 1
        if prog[pc][COUNTER] > 0:
            return acc, False

        if operator == 'acc':
            prog[pc][COUNTER] += 1
            if argument == '+':
                acc += value
            elif argument == '-':
                acc -= value
            pc += 1

        if operator == 'jmp':
            prog[pc][COUNTER] += 1
            if argument == '+':
                pc += value
            elif argument == '-':
                pc -= value

        if operator == 'nop':
            prog[pc][COUNTER] += 1
            pc += 1

    return acc, True

# acc, ret = run(program)
# if not ret:
    # print('Part 1: {}'.format(acc))

# Extremely inefficient brute force, maybe refactor it if I have time
def part2():
    for i in range(len(program)):
        if program[i][0] == 'acc':
            continue
        if program[i][0] == 'nop':
            new_operator = 'jmp'
        elif program[i][0] == 'jmp':
            new_operator = 'nop'

        new_program = copy.deepcopy(program)
        new_program[i][0] = new_operator

        acc, ret = run(new_program)
        if ret:
            return acc

print('Part 2: {}'.format(part2()))
