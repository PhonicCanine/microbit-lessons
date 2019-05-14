# Week 6

## Quick recap from last week

```py
def doSomething(a,b):
    if a > b:
        return 1
    elif a == b:
        d = a + b
        return (d/a)
    else:
        return -1

c = doSomething(1,0)
d = doSomething(3,3)
e = doSomething(100,101)
```

What are `c`, `d` and `e`?

```py
def doSomethingElse(a):
    numbers = [1,1,2,3,5,8,13]
    return numbers[a]

c = doSomethingElse(5)
```

What is `c`?

## Loops

Now that we've had a recap, let's get on to something new!

```py
i = 0
while i <= 10:
    display.scroll(str(i))
    i = i + 1
```

What do we think this is going to do? How is it different from

```py
i = 0
if i <= 10:
    display.scroll(str(i))
    i = i + 1
```

that's right, `while` runs more than one time. Otherwise it's almost the same as `if`.

```py
for i in range(0,10):
    display.scroll(str(i))
```

What about this?

As it turns out both of these are the same. They will both display the numbers `0` through to `10` on the microbit display.

## Rock Paper Scissors

We're going to be fixing up a game of Rock-Paper-Scissors.

Everything is done, except the most important part - choosing what the play, and playing it.

To figure out how to fix it, we're going to have to quickly learn some maths.

### Modulo

```py
5 % 3 == 2 #True
```
Above is an example of Modulo.

It's very much like division, except instead of taking the number of times 3 will go into 5, we take the remainder. We can think of it as a really simple process:

```py
def modulo(number,by):
    while number >= by:
        number = number - by
    return number
```

Do we understand what this is doing?

Let's take `5` and `3`, for example.

```
number = 5
by = 3

is 5 >= 3? yes

number = 5 - 3

is 2 >= 3? no

return 2
```

Let's try again with `15` and `5`:

```
number = 15
by = 5

is 15 >= 5? yes

number = 15 - 5

is 10 >= 5? yes

number = 10 - 5

is 5 >= 5? yes

number = 5 - 5

is 0 >= 5? no

return 0
```

### Back to rock paper scissors

Most of the stuff this game has to do is already done.

We just have to let the player choose which thing they'd like to choose, and see if they have won.

To check who won, we have a handy function: `displayResult(player,enemy)`. We just need to call this with some values.

There are a bunch of hints as to how we might to this in the file. Just remember that you only have to write code in the `play()` function.

Get the file [here](python/rps.py)