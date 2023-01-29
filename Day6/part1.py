
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

    maxValue = 0
    maxKey = ''
    for key, value in decode.items():
        if value > maxValue:
            maxKey = key
            maxValue = value

    print(maxKey)

    # concatenate the string onto final
    final += maxKey

print(final)
