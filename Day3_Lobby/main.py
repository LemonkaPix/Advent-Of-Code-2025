input = open("input.txt","r").read().splitlines()

print(input)

answer = 0

for data in input:

    digitIndexes = []

    for i in range(12):

        frag = ""
        for digit in range(9, 0, -1):
            try:
                if i == 0:
                    frag = data[:-11]
                    digitIndexes.append(frag.index(str(digit)))
                    break
                else:
                    startIndex = digitIndexes[i - 1] + 1
                    endIndex = -(12 - i) + 1

                    if endIndex != 0:
                        frag = data[startIndex : endIndex]
                        digitIndexes.append(
                            data.index(
                                str(digit),
                                startIndex,
                                endIndex
                            )
                        )
                    else:
                        frag = data[startIndex:]
                        digitIndexes.append(
                            data.index(
                                str(digit),
                                startIndex
                            )
                        )

                    break
            except:
                continue

    number = ""
    for i in range(12):
        number += data[digitIndexes[i]]
    print(number)
    answer += int(number)

print(f"Answer: {answer}")
