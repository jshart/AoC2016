import hashlib

done=False

i=0
j=0
doorKey=[" "] * 8
done=False
while not done:
    i+=1
    inputToHash="cxdnnyjw"+str(i)
    #print(inputToHash,end=" = ")
    result = hashlib.md5(inputToHash.encode())
    #print(result.hexdigest())

    s=result.hexdigest()

    if s[0:5] == "00000":
        j+=1
        if s[5].isdigit():
            #print(s[5],end="")
            d=int(s[5])
            if d<8:
                if doorKey[d] != " ":
                    continue
                doorKey[d]=s[6]
                print("Door key updated to:",end="")
                print(doorKey)

        if " " in doorKey:
            done=False
        else:
            done=True

# f77a0e6e