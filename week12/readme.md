# End of Semester 1 - ""Hacking""

## Technical things
### Hashes
A hash is a bit like a thumbprint - it's a unique number or code that we can generate to represent something, typically for verification purposes.

```py
def getHash(v):
    vl = str(v)
    s = 0
    sz = 4096
    for i in range(0,len(vl)):
        s += (ord(vl[i]) * (s + 1)) % (sz * 4)
    
    for i in range(0,len(vl)):
        s = (s + (s ^ (ord(vl[i]) * ((i * 2) + 1))) - (sz ^ ord(vl[i])) + sz) % sz

    return str(hex(s)).replace("0x","")
```

Above is an example hashing algorithm. It's not super important how it works - there's a lot of maths involved, and it's pretty boring, but the most important thing to note is that there's `4096` total hashes.

This is important because there are more than `4096` possible inputs.

#### Pigeon Hole Principle

The pigeon hole principle is basically this:

Imagine you have 3 pigeon holes, and 5 pigeons. Assuming every pigeon is inside a pigeon hole, there must be at least one hole with more than 1 pigeon.

This is relevant when we bring it back to our hashes, because we know that there are only `4096` possible hashes. Yet, there are far more than `4096` possible things we could hash. For example, there's `10000` 4 digit passcodes (0000-9999).

In real life, most hashing algorithms produce much larger hashes to prevent this issue from arising _as frequently_ as it will here, but by their very nature, this will always be an issue with hashes (although, an algorithm like MD5 has over 3 followed by 38 0's possible hashes! - that is 300,000,000,000,000,000,000,000,000,000,000,000,000 - more possible hashes than there are atoms in the Earth!).

Anyway, in the above hashing algorithm, for example:

```py
getHash("Hacking") == getHash("167696") and getHash("Hacking") == getHash("Hasking")
```
but
```py
getHash("Hacking") != getHash("Haskell")
```

### Escape sequences

Escape sequences are how we put control characters into a string. For example, in Python, we use `"` to open and close strings:

```py
myString = "legitimate hacking"
```

but what if we want to have quotes in our string, so when printed it says `legitimate "hacking"`. For that, we use an escape sequence. In Python, this is simply a backslash (`\`). We could write `legitimate "hacking"` as so:

```py
myString = "legitimate \"hacking\""
```

and when we print that, we will indeed get what we expect - `legitimate "hacking"`.

#### How is this useful?

Escaping from a string can do great things for us. Imagine we have code like this:

```python
somevariable = False
username = "" #some text that the user gets to directly type in, that gets put between the two quotes
```

now imagine we would like to set `somevariable` to `True`.

If we can enter any text into the username variable, and the text is not escaped, we can choose to set our username as:

```python
"
somevariable = True#
```

when Python places this variable into the correct position, the code from above will become this:

```python
somevariable = False
username = ""
somevariable = True#"
```

As you can see, now somevariable is set to True, and we don't have to worry about the original `"` that ended our string, because we've used a hash (`#`) to comment it out.

## The code you will be breaking into:

Another hacker before you has managed to get this from the server (you can skip this and do this yourself if you want, but we won't talk about how to do so), showing how the application security actually works:

```py
import io #users file needs to be read
import os


def getHash(v):
    vl = str(v)
    s = 0
    sz = 4096 #only 4096 possible password hashes (vulnerability 1)
    for i in range(0,len(vl)):
        s += (ord(vl[i]) * (s + 1)) % (sz * 4)

    for i in range(0,len(vl)):
        s = (s + (s ^ (ord(vl[i]) * ((i * 2) + 1))) - (sz ^ ord(vl[i])) + sz) % sz

    return str(hex(s)).replace("0x","")

dire = os.getcwd()
f = open(dire + "\\users.txt")
fc = f.read()

users = fc.splitlines() #split the users file into multiple lines

loggedIn = False #initialise a variable to False to signify that the user has not logged in (vulnerability 2)

user = "" #whatever text the user enters is put into the user variable - nothing is escaped out (vulnerability 2/3)
pword = ""
hashed = getHash(pword)

for i in range(0,len(users)):
    if ((user + ":" + hashed).startswith(users[i])): #vulnerability 3
        loggedIn = True #if the user:password combination is in the file, let the user in


if loggedIn:
    #successful login
else:
    #access denied
```