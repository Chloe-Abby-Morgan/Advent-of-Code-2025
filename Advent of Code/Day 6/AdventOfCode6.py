total = 0

with open(r"C:\Users\chloe\Desktop\Dev\Advent-of-Code-2025\Advent of Code\Day 6\input.txt") as f:
    pInput = [list(line.strip("\n").split()) for line in f.readlines()]

for i in range(len(pInput[0])):
    if pInput[4][i] == "+":
        total += int(pInput[0][i]) + int(pInput[1][i]) + int(pInput[2][i]) + int(pInput[3][i])
    if pInput[4][i] == "*":
        total += (int(pInput[0][i]) * int(pInput[1][i]) * int(pInput[2][i]) * int(pInput[3][i]))

print("The total is: ", total)
