result = 0
with open(r"C:\Users\chloe\Desktop\Dev\Advent of Code\Day 3\input.txt") as f:
    batteries = [line.strip() for line in f]

def findVol(num):
    highest = [-1 for i in range(12)]
    positions = [-1 for i in range(12)]


    #Yanderedev ass function but I cannot be bothered to figure it out right now

    if highest[0] == -1:
        for i in range(9, -1, -1):
            try:
                positions[0] = num.find(str(i), 0, len(num)-11)
                if positions[0] != -1:
                    highest[0] = num[positions[0]]
                    break
            except:
                continue

    if highest[1] == -1:
        for i in range(9, -1, -1):
            try:
                positions[1] = num.find(str(i), positions[0]+1, len(num)-10)
                if positions[1] != -1:
                    highest[1] = num[positions[1]]
                    break
            except:
                continue
    if highest[2] == -1:
        for i in range(9, -1, -1):
            try:
                positions[2] = num.find(str(i), positions[1]+1, len(num)-9)
                if positions[2] != -1:
                    highest[2] = num[positions[2]]
                    break
            except:
                continue
    
    if highest[3] == -1:
        for i in range(9, -1, -1):
            try:
                positions[3] = num.find(str(i), positions[2]+1, len(num)-8)
                if positions[3] != -1:
                    highest[3] = num[positions[3]]
                    break
            except:
                continue

    if highest[4] == -1:
        for i in range(9, -1, -1):
            try:
                positions[4] = num.find(str(i), positions[3]+1, len(num)-7)
                if positions[4] != -1:
                    highest[4] = num[positions[4]]
                    break
            except:
                continue

    if highest[5] == -1:
        for i in range(9, -1, -1):
            try:
                positions[5] = num.find(str(i), positions[4]+1, len(num)-6)
                if positions[5] != -1:
                    highest[5] = num[positions[5]]
                    break
            except:
                continue

    if highest[6] == -1:
        for i in range(9, -1, -1):
            try:
                positions[6] = num.find(str(i), positions[5]+1, len(num)-5)
                if positions[6] != -1:
                    highest[6] = num[positions[6]]
                    break
            except:
                continue

    if highest[7] == -1:
        for i in range(9, -1, -1):
            try:
                positions[7] = num.find(str(i), positions[6]+1, len(num)-4)
                if positions[7] != -1:
                    highest[7] = num[positions[7]]
                    break
            except:
                continue
    
    if highest[8] == -1:
        for i in range(9, -1, -1):
            try:
                positions[8] = num.find(str(i), positions[7]+1, len(num)-3)
                if positions[8] != -1:
                    highest[8] = num[positions[8]]
                    break
            except:
                continue

    if highest[9] == -1:
        for i in range(9, -1, -1):
            try:
                positions[9] = num.find(str(i), positions[8]+1, len(num)-2)
                if positions[9] != -1:
                    highest[9] = num[positions[9]]
                    break
            except:
                continue

    if highest[10] == -1:
        for i in range(9, -1, -1):
            try:
                positions[10] = num.find(str(i), positions[9]+1, len(num)-1)
                if positions[10] != -1:
                    highest[10] = num[positions[10]]
                    break
            except:
                continue
    
    if highest[11] == -1:
        for i in range(9, -1, -1):
            try:
                positions[11] = num.find(str(i), positions[10]+1, len(num))
                if positions[11] != -1:
                    highest[11] = num[positions[11]]
                    break
            except:
                continue 

    return int("".join(highest))

for i in batteries:
    result += findVol(i)
print("The result is: ", result)