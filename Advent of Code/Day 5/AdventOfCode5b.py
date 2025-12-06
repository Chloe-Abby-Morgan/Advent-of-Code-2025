ranges = []
values = []
checkedIDs = []
fresh = 0

with open (r"C:\Users\chloe\Desktop\Dev\Advent of Code\Day 5\input.txt") as f:
    for line in f:
        if "-" in line.strip():
            ranges.append(line.strip().split("-"))
        elif line.strip() != "":
            values.append(line.strip())

ranges = [(int(i[0]), int(i[1])) for i in ranges]
ranges.sort()

for elt in ranges:
    if not checkedIDs or elt[0] > checkedIDs[-1][1]:
        checkedIDs.append([elt[0], elt[1]])
    else:
        checkedIDs[-1][1] = max(checkedIDs[-1][1], elt[1])

for elt in checkedIDs:
    fresh += (elt[1] - elt[0] + 1)

print("The total number of valid IDs is: ", fresh)