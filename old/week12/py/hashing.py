def getHash(v):
    vl = str(v)
    s = 0
    sz = 4096
    for i in range(0,len(vl)):
        s += (ord(vl[i]) * (s + 1)) % (sz * 4)
    
    for i in range(0,len(vl)):
        s = (s + (s ^ (ord(vl[i]) * ((i * 2) + 1))) - (sz ^ ord(vl[i])) + sz) % sz

    return str(hex(s)).replace("0x","")


nn = input("Gimme something to hash!")
print(getHash(nn))

#Code Cadets -- 485
#Halo Infinite -- 2778

def getCollision(v):
    collision = -1
    n = 0
    while collision == -1:
        n += 1
        if (getHash(n) == v):
            collision = n
    return collision

print(getCollision(getHash(nn)))