successful = False


start = """
import io
import os


def getHash(v):
    vl = str(v)
    s = 0
    sz = 4096
    for i in range(0,len(vl)):
        s += (ord(vl[i]) * (s + 1)) % (sz * 4)
    
    for i in range(0,len(vl)):
        s = (s + (s ^ (ord(vl[i]) * ((i * 2) + 1))) - (sz ^ ord(vl[i])) + sz) % sz

    return str(hex(s)).replace("0x","")

dire = os.getcwd()
f = open(dire + "\\\\users.txt")
fc = f.read()

users = fc.splitlines()

loggedIn = False

user = """

middle = """
pword = """

end = """
hashed = getHash(pword)

for i in range(0,len(users)):
    if ((user + ":" + hashed).startswith(users[i])):
        loggedIn = True


if loggedIn:
    successful = True
"""

user = input("enter username:").replace("\\n","\n")
password = input("enter password:").replace("\\n","\n")

#print(start + "\"" + user + "\"" + middle + "\"" + password + "\"" + end)

exec(start + "\"" + user + "\"" + middle + "\"" + password + "\"" + end)

if successful:
    print("Good job, you're in")
else:
    print("Sorry, you're not in yet.")