program = []
with open("input/day8_test.txt") as lines:
    instr = []
    for line in lines:
        line = line.strip()
        instruction = line.split(' ')
        instruction.append(0)
        program.append(instruction)

def run_program(program):
    COUNTER = 2
    acc = 0
    ptr = 0
    running = True
    while running == True:
        operator = program[ptr][0]
        argument = program[ptr][1][0]
        value = int(program[ptr][1][1:])

        print(program[ptr])
        print('ptr: {}'.format(ptr))
        print('acc: {}'.format(acc))

        if ptr > len(program):
            print('end, acc: {}'.format(acc))
            return False

        if program[ptr][COUNTER] > 0:
            print('second run, acc: {}'.format(acc))
            return True

        if operator == 'acc':
            program[ptr][COUNTER] += 1
            if argument == '+':
                acc += value
            elif argument == '-':
                acc -= value
            ptr += 1

        if operator == 'jmp':
            program[ptr][COUNTER] += 1
            if argument == '+':
                ptr = ptr + value
            elif argument == '-':
                ptr = ptr - value

        if operator == 'nop':
            program[ptr][COUNTER] += 1
            ptr += 1


def run_program2(program):
    COUNTER = 2
    acc = 0
    pc = 0
    while pc < len(program):
        operator = program[pc][0]
        argument = program[pc][1][0]
        value = int(program[pc][1][1:])
        print(pc)

        if program[pc][COUNTER] > 0:
            return None

        if pc == (len(program) - 1):
            # print('END, acc: {}'.format(acc))
            return acc

        # print(program[pc])
        # print('pc: {}'.format(pc))
        # print('acc: {}'.format(acc))

        if operator == 'acc':
            program[pc][COUNTER] += 1
            if argument == '+':
                acc += value
            elif argument == '-':
                acc -= value
            pc += 1

        if operator == 'jmp':
            program[pc][COUNTER] += 1
            if argument == '+':
                pc += value
            elif argument == '-':
                pc -= value

        if operator == 'nop':
            program[pc][COUNTER] += 1
            pc += 1

    return acc

def manipulate_program(program, i, new_operator):
    program[i][0] = new_operator
    return program

for i in range(len(program)):
    if program[i][0] == 'acc':
        continue

    if program[i][0] == 'nop':
        new_operator = 'jmp'
    elif program[i][0] == 'jmp':
        new_operator = 'nop'

    print(program)
    new_program = manipulate_program(program, i, new_operator)
    print(new_program)
    print('--------------')
    ret = run_program2(new_program)
    if ret is not None:
        print(ret)

