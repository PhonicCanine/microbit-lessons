# Week 5 - recap

This week, to get everyone back into the groove, we're going to first go over some of the things we've done before, then try to make something new.

## Variables

We first covered variables a while ago - but they're really important so we will look at them (briefly) again.

[Week 4](../week4/readme.md#Variables)

As we said a few weeks ago, variables are effectively boxes. We can put whatever we want inside them, and whenever we want to use what's inside, we can. If we want to put something new inside, we can do that too.

Below is a piece of code.
```py
a = 5
b = 6

c = a + b
```

What is inside `c` after this code runs?

```py
a = 5
b = 6

c = a + b

c = 2
```

What's different now?

## Arrays

We have also covered arrays, but again, these are really important to programming.

[Week 4](../week4/readme.md#Arrays)

These are the shelves we have talked about. Like variables, we can put anything on any shelf of our array.

Below is another piece of code:
```py
array = [1,2,3]

c = array[1]
```

What is inside `c` after this runs?

```py
array = [1,2,3]

array[1] = 5

c = array[1]
```

What is different now? Is the array the same as before? Is `c` the same as before?

## Functions

Functions shouldn't be new either.

[Week 4](../week4/readme.md#Functions)

These are like maths equations, for example:

```
y = x + 2
```

which we can also write as:

```
f(x) = x + 2
```

Below is a piece of code in Python that works as a function:

```py
def myfunc(a,b):
    return a - b

c = myfunc(5,3)
```

What is `c` after this code runs?

```py
def myfunc(a,b):
    return a - b

c = myfunc(3,5)
```

Is this any different to what we have above? Is `c` the same as what we had before?

## Putting all that back together

Below is some (more) code.

```py
def pickBook(a):
    books = ["Harry Potter and the Philosopher's Stone","The Hunger Games","Paper Towns","Percy Jackson","Lord of the Rings","Mortal Instruments"]
    if a >= len(books):
        return "Couldn't find that book"
    else:
        return books[a]

book = pickBook(1)
```

Which book have we chosen? What would happen if we chose book `6`?

Here is another piece of code:

```py
def min(a,b):
    if a < b:
        return a
    else:
        return b

c = min(1,5)
```

What does this do? What would happen if we tried with `5` and `1` the other way around?

```py
def max(a,b):
    if a > b:
        return a
    else:
        return b

c = max(1,3)
d = max(2,c)
```

What does this do? What is `c`, and what does `d` become?

```py
def minm(a,b):
    if a > b:
        return a - 1
    else:
        return b - 1

c = minm(minm(5,4),6)
```

Finally, what does that do? Is `c`:

a. `c` = 2

b. `c` = 3

c. `c` = 4

d. `c` = 5

e. `c` = 6

## Activity

To polish it all off, we're going to do the tic-tac-toe activity from last term:

[Available here](https://github.com/PhonicCanine/microbit-lessons/tree/master/week4b)
