# Week 8

Again, this week we're going to be working on a few exercises to help you all become _Python gods_.

## Exercise 1 - Reversal

Imagine we have a shelf (Array):

`[1,2,3]`

How do we flip this shelf (or reverse this array)?

In this example, it's rather simple:

We just swap the first and last elements, to get `[3,2,1]`, but what would we do if the size of the array (the number of shelves) was larger?

Ultimately, all we are doing when we reverse something is reading through it from back to front.

Below is a python function that reads through an array, and writes it into another shelf:

```py
def readthrough(array):
    newArray = []
    length = len(array)
    for i in range(0,length): #range(n,x) starts from n and counts to (x-1)
        newArray.append(array[i])
    return newArray
```

Here, .append just adds an element onto a new shelf (a new array element). We can see that `readthrough([1,2,3])` returns `[1,2,3]`. So, how would we make this reverse?

We have to count from the last element of the array (`length - 1`) to the first element (`0`). Surely there's some maths we can do for that?

## Exercise 2 - Sum

Imagine we have another shelf, this time, with only numbers on it:

`[1,2,3,4,5]`

now, we want to find the sum of all of the numbers on a shelf of any length - how might we go about that?


## Exercise 3 - Factorial

A factorial is a special kind of multiplication on a shelf, if you will.

Say we want to find the factorial of 5.

Well, to do that, we just multiply each element on this shelf:

`[1,2,3,4,5]`

That's not the only way of thinking about it either.

We want to create a function `factorial(number)` that will calculate the factorial of any number we put in. Be careful to figure out what should happen if a negative number is put in.

## Exercise 3b - Factorial another way (optional extension)

As we've seen, you can call a function as so `function(argument)`. What happens if we call a function from inside itself though?

```py
def func(n):
    if (n <= 1):
        return 1
    else:
        return 1 + (func(n - 1))
```

Let's look at it case by case:

If we run this function with `-1`, we are going to get `1` out, because `-1` is less than or equal to `1`.

What about if we run it with `1`? Well, we'll get `1`, because `1` is equal to `1`.

Now for the exciting part - what if we run this with `2`?

Well, `2` is not less than or equal to `1` is it? So, we return `1` + `func(2 - 1)`. We already know that `func(1)` returns `1`, so we're just returning `1` + `1` (which is obviously `2`).

Here's another function:

```py
def another(n):
    if (n <= 1):
        return 1
    else:
        return n + another(n - 1)
```

What does that calculate?

How would we make it calculate the factorial?

(hint: you should only need to change one character)

This is _recursion_.

## End

If you finish all this, please talk to me and we'll talk about something else you can work on.