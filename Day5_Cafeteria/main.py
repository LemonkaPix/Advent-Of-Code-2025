input = open("input.txt","r").read().splitlines()

ranges = []

answer = 0

i = 0
while input[i] != "":
    splited = input[i].split('-')

    first = int(splited[0])
    second = int(splited[1])

    ranges.append([first, second])
    i += 1

# print(ranges)

ranges = sorted(ranges)

print(ranges)

colapsed = []

while ranges != []:
    if ranges[0][1] < ranges[1][0]:
        colapsed.append(ranges.pop(0))
    elif ranges[0][1] > ranges[1][1]:
        ranges.pop(1)
    elif ranges[1][0] <= ranges[0][1] <= ranges[1][1] :
        ranges[0][1] = ranges[1][1]
        ranges.pop(1)
    if len(ranges) == 1: colapsed.append(ranges.pop(0))

print(colapsed)

for i in colapsed:
    answer += i[1] - i[0] + 1

print(answer)