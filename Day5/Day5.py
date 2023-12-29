import hashlib

done=False

i=0
j=0
while j<8:
    i+=1
    inputToHash="cxdnnyjw"+str(i)
    #print(inputToHash,end=" = ")
    result = hashlib.md5(inputToHash.encode())
    #print(result.hexdigest())

    if result.hexdigest()[0:5] == "00000":
        j+=1
        print(result.hexdigest())

        done=True

# f77a0e6e