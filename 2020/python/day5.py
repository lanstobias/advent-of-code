row_numbers, col_numbers = [], []
row_numbers.extend(range(0, 127 + 1))
col_numbers.extend(range(0, 7 + 1))

def read_seats():
    seats = []
    with open('input/day5.txt') as infile:
        for seat in infile:
            seats.append(seat.strip('\n'))
    return seats

def split_list(row_num_list, part):
    half = int(len(row_num_list)/2)
    if part == 'upper':
        return row_num_list[half:]
    if part == 'lower':
        return row_num_list[:half]

def find_number(chars, full_number_list):
    numbers = full_number_list
    split_by = ''
    i = 0
    while len(numbers) > 1:
        if (chars[i] == 'L' or chars[i] == 'F'):
            split_by = 'lower'
        elif (chars[i] == 'R' or chars[i] == 'B'):
            split_by = 'upper'
        numbers = split_list(numbers, split_by)
        i+= 1
    return int(numbers[0])

def read_seat_ids():
    seat_ids = []
    for seat in read_seats():
        rows = seat[:7]
        cols = seat[-3:]
        row_num = find_number(rows, row_numbers)
        col_num = find_number(cols, col_numbers)
        seat_id = (row_num * 8 + col_num)
        seat_ids.append(int(seat_id))
    return seat_ids

seat_ids = read_seat_ids()
def find_my_seat():
    seat_ids.sort()
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] > (seat_ids[i] + 1):
            return (seat_ids[i] + 1)

print('Part 1: {}'.format(max(seat_ids)))
print('Part 2: {}'.format(find_my_seat()))

