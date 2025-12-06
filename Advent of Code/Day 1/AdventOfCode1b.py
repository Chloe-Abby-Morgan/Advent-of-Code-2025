dial = 50
timesZero = 0
tin = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

with open(r"C:\Users\chloe\Desktop\Dev\Advent-of-Code-2025\Advent of Code\Day 1\input.txt") as f:
    inputs = [line.strip() for line in f]

def rotation(direction):
    global dial, timesZero
    
    rotation = int(direction[1:])

    if direction.startswith("L"):
        dial += rotation
    else:
        dial -= rotation   
    while dial > 99:
        timesZero += 1
        dial -= 100
        
    while dial < 0:
        timesZero += 1
        dial += 100

for i in inputs:
    rotation(i)
print("The password is: " + str(timesZero))