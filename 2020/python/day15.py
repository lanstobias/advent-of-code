from collections import defaultdict

inp = "15,5,1,4,7,0"
game = defaultdict(int)

def start_game(start_numbers):
    game.clear()
    numbers = map(int, start_numbers.split(","))
    last_num = numbers[-1]
    for i, num in enumerate(numbers):
        if num == last_num:
            return num
        game[num] = i + 1

def run_game(start_numbers, turns):
    current_num = start_game(start_numbers)
    turn = len(game) + 1
    while turn < turns:
        if current_num not in game:
            game[current_num] = turn
            current_num = 0

        elif current_num in game:
            new_number = turn - game[current_num]
            game[current_num] = turn
            current_num = new_number

        turn += 1

    return current_num

print("Part 1: {}".format(run_game(inp, 2020)))
print("Part 2: {}".format(run_game(inp, 30000000)))
