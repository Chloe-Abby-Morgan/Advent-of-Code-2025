ranges = []
values = []
fresh = 0

with open (r"C:\Users\chloe\Desktop\Dev\Advent-of-Code-2025\Advent of Code\Day 5\input.txt") as f:
    for line in f:
        if "-" in line.strip():
            ranges.append(line.strip().split("-"))
        elif line.strip() != "":
            values.append(line.strip())

for value in values:
    for elt in ranges:
        if int(elt[0]) <= int(value) and int(value) <= int(elt[1]):
            fresh += 1
            break

print("The total number of fresh ingredients is: ",fresh)