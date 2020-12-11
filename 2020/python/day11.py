import numpy
import copy

org_grid = []
with open('input/day11_example.txt') as f:
    for line in f:
        line = line.strip()
        x = []
        for c in line:
            x.append(c)
        org_grid.append(x)


def fill(grid, empty_grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            u, d, l, r, ul, ur, dl, dr = 0, 0, 0, 0, 0, 0, 0, 0
            seat = grid[i][j]

            if seat == '.':
                empty_grid[i][j] = '.'
                continue

            # Check up
            if i > 0 and grid[i - 1][j] == '#':
                u = 1

            # Check down
            if i + 1 < len(grid) and grid[i + 1][j] == '#':
                d = 1

            # Check left
            if j > 0 and grid[i][j - 1] == '#':
                l = 1

            # Check right
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '#':
                r = 1

            # Check up left
            if (i > 0) and (j > 0) and grid[i - 1][j - 1] == '#':
                ul = 1

            # Check up right
            if (i > 0) and (j + 1 < len(grid[0])) and grid[i - 1][j + 1] == '#':
                ur = 1

            # Check down left
            if (i + 1 < len(grid)) and (j > 0) and grid[i + 1][j - 1] == '#':
                dl = 1

            # Check down right
            if (i + 1 < len(grid)) and (j + 1 < len(grid[0])) and grid[i + 1][j + 1] == '#':
                dr = 1

            if seat == 'L':
                if (u + d + l + r + ul + ur + dl + dr) == 0:
                    empty_grid[i][j] = '#'
                else:
                    empty_grid[i][j] = 'L'
            elif seat == '#':
                if (u + d + l + r + ul + ur + dl + dr) >= 4:
                    empty_grid[i][j] = 'L'
                else:
                    empty_grid[i][j] = '#'

    return empty_grid


def count_until_chair(row) -> int:
    n = 0
    for seat in row:
        if seat == 'L':
            return n
        if seat == '#':
            n += 1
    return n


def fill2(grid, empty_grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            r, c, d = 0, 0, 0
            seat = grid[i][j]

            if seat == '.':
                empty_grid[i][j] = '.'
                continue

            # Check col
            gridA = numpy.array(grid)
            col = gridA[:,0]
            if '#' in col:
                c = count_until_chair(col.tolist())

            # Check row
            if '#' in grid[0]:
                r = count_until_chair(grid[0])

            # Check diagonals
            diag, anti_diag = get_diags(grid)
            if ('#' in diag) or ('#' in anti_diag):
                hej = diag.tolist()
                hej2 = anti_diag.tolist()
                d = count_until_chair(diag.tolist())
                d += count_until_chair(anti_diag.tolist())

            if seat == '#':
                r -= 1
                c -= 1
                d -= 1

            if seat == 'L':
                if (r + c + d) == 0:
                    empty_grid[i][j] = '#'
                else:
                    empty_grid[i][j] = 'L'
            elif seat == '#':
                if (r + c + d) >= 5:
                    empty_grid[i][j] = 'L'
                else:
                    empty_grid[i][j] = '#'

    return empty_grid


def same(A, B):
    a = numpy.array(A)
    b = numpy.array(B)
    return (a == b).all()


def get_diags(A):
    a = numpy.array(A)
    diag = a.diagonal()
    anti_diag = numpy.flipud(a).diagonal()
    return diag, anti_diag


def fill(grid, empty_grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            u, d, l, r, ul, ur, dl, dr = 0, 0, 0, 0, 0, 0, 0, 0
            seat = grid[i][j]

            if seat == '.':
                empty_grid[i][j] = '.'
                continue

            # Check up
            if i > 0 and grid[i - 1][j] == '#':
                u = 1

            # Check down
            if i + 1 < len(grid) and grid[i + 1][j] == '#':
                d = 1

            # Check left
            if j > 0 and grid[i][j - 1] == '#':
                l = 1

            # Check right
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '#':
                r = 1

            # Check up left
            if (i > 0) and (j > 0) and grid[i - 1][j - 1] == '#':
                ul = 1

            # Check up right
            if (i > 0) and (j + 1 < len(grid[0])) and grid[i - 1][j + 1] == '#':
                ur = 1

            # Check down left
            if (i + 1 < len(grid)) and (j > 0) and grid[i + 1][j - 1] == '#':
                dl = 1

            # Check down right
            if (i + 1 < len(grid)) and (j + 1 < len(grid[0])) and grid[i + 1][j + 1] == '#':
                dr = 1

            if seat == 'L':
                if (u + d + l + r + ul + ur + dl + dr) == 0:
                    empty_grid[i][j] = '#'
                else:
                    empty_grid[i][j] = 'L'
            elif seat == '#':
                if (u + d + l + r + ul + ur + dl + dr) >= 4:
                    empty_grid[i][j] = 'L'
                else:
                    empty_grid[i][j] = '#'

    return empty_grid

def count_occupied(A):
    a = numpy.array(A)
    return numpy.count_nonzero(a == '#')

def run(grid):
    different = True
    i = 0
    previous_grid = copy.deepcopy(grid)
    while different:
        empty_grid = numpy.empty([len(grid), len(grid[1])], dtype="str")
        new_grid = fill2(previous_grid, empty_grid)
        if same(previous_grid, new_grid):
            different = False
        else:
            previous_grid = copy.deepcopy(new_grid)
            i += 1
        print(new_grid)
    return count_occupied(new_grid)

print(run(org_grid))
