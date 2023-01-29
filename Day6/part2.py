
import math


textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2016\\day6\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()

final=''
for c in range(len(input[0])):
    decode = dict()

    for i in input:
        # print(i)

        if i[c] in decode:
            decode[i[c]] += 1
        else:
            decode[i[c]] = 1

    # print(decode)

    minValue = 1000000
    minKey = ''
    for key, value in decode.items():
        if value < minValue:
            minKey = key
            minValue = value

    print(minKey)

    # concatenate the string onto final
    final += minKey

print(final)
