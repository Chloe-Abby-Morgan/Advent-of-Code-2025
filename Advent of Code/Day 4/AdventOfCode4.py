x = 0
y = 0
total = 0

with open(r"C:\Users\chloe\Desktop\Dev\Advent of Code\Day 4\input.txt") as f:
    pInput = [line.strip() for line in f]

for i in range(len(pInput)):
    for elt in pInput[i]:
        try:
            rollCount = 0

            if x > 0 and pInput[y][x-1] == "@":
                rollCount += 1
            if x < len(pInput[y]) - 1 and pInput[y][x+1] == "@":
                rollCount += 1

            if y > 0:
                if x > 0 and pInput[y-1][x-1] == "@":
                    rollCount += 1
                if pInput[y-1][x] == "@":
                    rollCount += 1
                if x < len(pInput[y-1]) - 1 and pInput[y-1][x+1] == "@":
                    rollCount += 1

            if y < len(pInput) - 1:
                if x > 0 and pInput[y+1][x-1] == "@":
                    rollCount += 1
                if pInput[y+1][x] == "@":
                    rollCount += 1
                if x < len(pInput[y+1]) - 1 and pInput[y+1][x+1] == "@":
                    rollCount += 1

            if pInput[y][x] == "@" and rollCount < 4:
                total += 1
            x += 1
        except:
            x += 1
            continue
    y += 1
    x = 0

print("The total is:", total)
