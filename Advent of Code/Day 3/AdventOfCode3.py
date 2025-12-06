result = 0

with open(r"C:\Users\chloe\Desktop\Dev\Advent of Code\Day 3\input.txt") as f:
    batteries = [line.strip() for line in f]

def findVol(num):
    fHighest = -1
    sHighest = -1

    for char in num:
        if fHighest == -1:
            for i in range(9, -1, -1):
                try:
                    fHighest = num[num[0:-1].index(str(i))]
                    break
                except:
                    continue

    if sHighest == -1:
        for char in num[num.index(fHighest)+1:]:
            for i in range(9, -1, -1):
                try:
                    sHighest = num[num.index(fHighest)+1:][num[num.index(fHighest)+1:].index(str(i))]
                    break
                except:
                    continue
    return int(str(fHighest) + str(sHighest))

for i in batteries:
    result += findVol(i)
print("The result is: ", result)