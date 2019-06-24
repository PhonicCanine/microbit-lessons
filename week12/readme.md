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

#### Some simple examples

Using our hashing algorithm above:

`Hello World` hashes to `660`

`Hello, World!` hashes to `c18`

`Hello Qorld` hashes to `460`

`Hello, World` hashes to `498`

`hELLO, wORLD` hashes to `798`

It's worth emphasising - this hashing algorithm is, actually, really terrible, so you're incredibly unlikely to see something quite this horrid in real life.

#### Pigeon Hole Principle

The pigeon hole principle is basically this:

Imagine you have 3 pigeon holes, and 4 pigeons. Assuming every pigeon is inside a pigeon hole, there must be at least one hole with more than 1 pigeon.

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

Another example in Python is with `\n`, which will become a newline when used in a string:

```python
var = "Hello,\nWorld!"
```

will become:

```
Hello,
World!
```

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

Our hackerman has also got the text that's currently in users.txt:

```
admin:9fc
```

## Exploits for this code

### Exploit 1: Getting the actual password (easy)

The first, and most obvious exploit is breaking the hash used for the `admin` account.

We can see that the current password hash is: `9fc`, so in order to break in, we only need to write a program that tries hashing different codes until it gets to one that results in `9fc`.

One way to go about this might be a `while` loop, that will loop while a working password hasn't been found, and increase an integer for use as a password, but there are other ways of doing this.

An example of some code that's pretty much done is below:

```python
def getCollision(v):
    collision = -1
    n = 0
    while collision == -1:
        n += 1
        if (getHash(n) == v):
            collision = n
    return collision
```

Here, `getCollision` is a function that takes a desired hash - for example `9fc`, and tries to find a password (a number) that will produce that hash.

### Exploit 2: Setting yourself to be logged in (medium)

As the code shows, there is a variable - `loggedIn` that determines whether the user is successfully logged in. We can find a way to write our username so that we can change the value of this variable.

Experiment with usernames such as `\n` (newline), and see what errors you get. You should be able to, almost without modification, use the exploit described in the section on [string escaping above](#escape-sequences).

### Exploit 3: Cheating the login checker (easy)

The vulnerability here is in this little section of code:

```python
(user + ":" + hashed).startswith(users[i])
```

You should be able to figure out how to break this, but if not the hint is this:

How is `(user + ":" + hashed).startswith(users[i])` different to `(user + ":" + hashed) == users[i]`? And how can we use that to our advantage?