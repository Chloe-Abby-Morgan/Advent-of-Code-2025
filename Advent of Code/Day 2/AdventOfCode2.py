ids = []
invalidIds = []
result = 0

with open(r"C:\Users\chloe\Desktop\Dev\Advent-of-Code-2025\Advent of Code\Day 2\input.txt") as f:
    pInput = f.read().strip()
pInput = pInput.split(",")

for i in pInput:
    start, end = map(int, i.strip().split("-"))
    ids.append((start, end))

def is_invalid(num):
    numb = str(num)
    if len(numb) % 2 == 0:
        mid = len(numb) // 2
        if numb[:mid] == numb[mid:]:
            return True
    return False

for start, end in ids:
    for i in range(start, end + 1):
        if is_invalid(i):
            invalidIds.append(i)

for i in invalidIds:
    result += i

print("The result is:",result)
