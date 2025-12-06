dial = 50
timesZero = 0

with open(r"C:\Users\chloe\Desktop\Dev\Advent-of-Code-2025\Advent of Code\Day 1\input.txt") as f:
    inputs = []
    for line in f:
        inputs.append(line.strip())


def rotation(direction):
    global dial
    rotation = int(direction[1:])

    while dial > 99:
        dial -= 100
    while dial < 0:
        dial += 100
    while rotation > 99:
        rotation -= 100

    if direction.startswith("L"):
        dial -= rotation
    elif direction.startswith("R"):
        dial += rotation

    if dial < 0:
        dial += 100
    elif dial > 99:
        dial -= 100

for i in range(len(inputs)):
    rotation(inputs[i])
    if dial == 0:
        timesZero += 1

print("The password is: " + str(timesZero))

    
