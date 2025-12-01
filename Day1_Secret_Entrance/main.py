input = open("input.txt","r").read().splitlines()

x = []
for i in input:
    x.append((i[0:1], int(i[1:])))

pos = 50
clicks = 0

for i in x:
    if(i[0] == 'R'):
        for j in range(i[1]):
            pos += 1
            if pos >= 100:
                pos -= 100
            if pos == 0:
                clicks += 1
    else:
        for j in range(i[1]):
            pos -= 1
            if pos < 0:
                pos = 100 + pos
            if pos == 0:
                clicks += 1

    print(f"POS {i}:\t{pos}")

print()
print(f"Clicks: {clicks}")

