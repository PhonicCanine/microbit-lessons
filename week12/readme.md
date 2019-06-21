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