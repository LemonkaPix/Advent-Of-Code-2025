input = open("input.txt","r").read().splitlines()
print(input)

answer = 0
deleted = True
while deleted:
    deleted = False
    for y in range(len(input)):
        for x in range(len(input[y])):
            c = input[y][x]
            if c == "@":
                neighbours = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0: continue
                        ny = y + dy
                        nx = x + dx
                        if ny < 0 or ny >= len(input): continue
                        if nx < 0 or nx >= len(input[y]): continue
                        if input[ny][nx] == "@":
                            neighbours += 1
                if neighbours < 4:
                    input[y] = input[y][:x] + "." + input[y][x+1:]
                    answer += 1
                    deleted = True

print(answer)