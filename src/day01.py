### ADVENT OF CODE -- DAY 01
# @Date: 01-Dec-25
# @Author: Art3mis

# ---Input import

with open("inputs/day01.txt", "r", encoding="utf-8") as f:
    data = f.read()

moves = data.split("\n")[:-1]
moves = [[move[0], int(move[1:])] for move in moves]

# ---Part 1

base = 50  # base value of the dial
numbers = 100  # numbers of digit on the dial


def step(dial, move):
    if move[0] == "R":  # adds to the dial
        dial = (dial + move[1]) % numbers

    else:
        dial = (dial - move[1]) % numbers

    return dial


def part1(moves):
    dial = base
    zeroCount = 0
    for move in moves:
        dial = step(dial, move)
        if dial == 0:
            zeroCount += 1

        # to help comprehension
        # print("Current move : {}, Dial : {}, Count : {}".format(move, dial, zeroCount))

    return zeroCount


# Part1 - Solve :
import time

start = time.perf_counter()  # for information purpose

print("Result for part 1 is : {}".format(part1(moves)))

end = time.perf_counter()

print("Excecuted part 1 in {} seconds".format(end - start))
