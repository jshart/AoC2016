# load a text file
# read file input.txt into an array of strings
file1 = open('Day4/data/input_test.txt', 'r')
lines = file1.readlines()

masterLine=[]
roomCode=[]
sectorCode=[]
checkSum=[]
checkSumSize=7

total=0
for i,l in enumerate(lines):
    crossCheck=dict()

    # Lets get rid of return codes and then break into the parts based on the dash "-"
    print(l.strip())
    l=l.strip()
    # Lets capture the stripped line so we can decode it later
    masterLine.append(l)
    parts=l.split("-")

    # Rebuild all the roomCode by joining any of the dashed parts minus the last bit
    # that contains the sector and checksum
    roomCode.append("")
    for j in range(0,len(parts)-1):
        roomCode[i]+=parts[j]

    # split the sector and checksum, add the sector to the list
    parts=parts[-1].split("[")
    sectorCode.append(parts[0])

    # add the checksum to the list, remove the trailing ]
    checkSum.append(parts[1][:-1])

    print(roomCode[i],end=" -- ")
    print(sectorCode[i],end=" -- ")
    print(checkSum[i])
    
    # count up how many incidents of each letter/number we have in the room code
    for c in roomCode[i]:
        if c=='-':
            continue
        if not c.isalpha():
            continue

        if c in crossCheck:
            crossCheck[c]+=1
        else:
            crossCheck[c]=1

    # sort the dictionary by value using lambda magic, so that the sortedCheckSum
    # is ordered based on the value (i.e. the number of occurrences of the letter/number)
    sortedCheckSum=sorted(crossCheck.items(), key=lambda x: x[1], reverse=True)

    hashMap=dict()
    for s in sortedCheckSum:
        #print(s[0],"=",s[1])
        if s[1] in hashMap:
            hashMap[s[1]].append(s[0])
        else:
            hashMap[s[1]]=[s[0]]

        hashMap[s[1]].sort()

        

    # we've now created a hashmap of the number of occurrences of each letter/number
    compareCheckSum=""
    for k,v in hashMap.items():
        print(k,v)

        for c in v:
            compareCheckSum+=c
            if len(compareCheckSum)==checkSumSize-2:
                break

        if len(compareCheckSum)==checkSumSize-2:
            break

    print("Compare Checksum:"+compareCheckSum)
    if compareCheckSum==checkSum[i]:
        print("Checksum matches!")
        total+=int(sectorCode[i])

# print the final result
print("Total:",total)