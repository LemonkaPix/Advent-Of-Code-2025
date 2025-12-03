inputs = open("input.txt","r").read().split(',')

data = []

for input in inputs:
    pair = input.split('-')
    data.append((
        int(pair[0]),
        int(pair[1])
    ))

print(data)

answer = 0

for ran in data:
    for i in range(ran[0], ran[1]+1):
        ID = str(i)
        # print(f"ID: {ID}")
        # print(f"len ID: {len(ID)}")
        pattern = ""

        for j in range(len(ID) // 2):
            pattern = ID[:j+1]
            # print(f"\tpattern: {pattern}")

            invalid = True

            for k in range(0, len(ID), len(pattern)):
                piece = ID[k:k+len(pattern)]
                # print(f"\t\tpiece: {piece}")

                if piece != pattern:
                    invalid = False
                    break

            if invalid:
                answer += int(ID)
                print(f"ID: {ID}")
                break


        # print()

print(answer)