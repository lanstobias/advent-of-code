from os import path
import csv

# Tools
def readlines_int(filename):
    lines = []
    with open(filename) as infile:
        for line in infile:
            lines.append(int(line))
    return lines

def read_csv(filename, delim):
    with open(filename, newline='') as indata:
        return list(csv.reader(indata, delimiter=delim))

# Tests
def test_readlines_int():
    lines = readlines_int("input/test.txt")
    print(lines)

def test_read_csv():
    data = read_csv("input/test.csv", ",")
    for cell in data:
        print("{}".format(cell))

# test_readlines_int()
# test_read_csv()
