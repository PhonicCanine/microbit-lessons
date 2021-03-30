# Week 4 - Programming for the Microbit

This week, we'll work on a Magic 8-ball for the Microbit.

## Some more programming concepts

### Functions and Variables

In simple terms, a Variable is like a box, that we store information in. We can put anything inside this box, and whenever we write out the name of it in our program, the code will see whatever we have inside our box. To put things into our box, we can use assignment - `=`.

A function then, is like Amazon. We can tell it what we want, and it will give us a box with what we want in it.

Below is some more explanation.

#### Variables
Variables make programming easier by allowing us to store something and do things to it. For example, say we want to take a number and add 5 to it, then multiply it by half of itself plus 5:

without variables, we would have to do it like this:
```py
(10 + 5) * ((10 + 5) / 2)
```
but with variables, we can do this:
```py
ourNumber = 10 #10 is inside the "ourNumber" box
updatedNumber = ourNumber + 5 #this will store 15
newNumber = (ourNumber + 5) * ((ourNumber + 5) / 2) #the results of our maths are stored in the "newNumber" box
```
The second one is a lot more easy to read, and we can use variables for much more complicated stuff too, but it might not be obvious why this is a much better way of doing things. Imagine we wanted to use the number 5 in this instead of 10. Well, with the top example, it would end up looking like this:
```py
(5 + 5) * ((5 + 5) / 2)
```
We have to change two copies of the number 10, and worse than that, the code is now confusing - which 5 are we adding? Why wouldn't we just simplify `(5 + 5)` to `10`?

These problems can be solved with variables. With variables, we just change the 10 to a 5 when we are setting "ourNumber"
```py
ourNumber = 5 #5 is inside the "ourNumber" box
updatedNumber = ourNumber + 5 #this will store 10
newNumber = (ourNumber + 5) * ((ourNumber + 5) / 2) #the results of our maths are stored in the "newNumber" box
```
This way, we only need to change one number, and it makes a lot more sense. We could even let the user of our program set the number we are doing this to.
#### Functions
Functions allow us to get a block of code, and run it again, without needing to copy-paste the code. In Python, we write a function as follows:
```py
def functionName(<arguments>):
    '''code inside function goes here'''
```
That should probably look familiar, but let's look at what the `<arguments>` part is.

An argument is something that we pass into a function. The value of which goes into a variable. Say we have the function below:

```py
def sum():
    return 1 + 2
```

And to get the result, we go like this:

```py
sum() #3
```

Well, that function will always return 3. That's great if we always want our sum to be 3, but what about if we want to be able to use it for more than 1 + 2?

This is what arguments are for - here's another function:

```py
def sum(a,b):
    return a + b
```

Because we are using arguments here, the function needs to be accessed like this:
```py
sum(1,2) #3
```

What this is actually doing looks something like this:
```py
a = 1 #because 1 was the first argument, and a is first in the definition (sum(a,b))
b = 2 #because 2 was the second argument
sum = a + b #the "return" basically sets the result to a fake variable, which we can use in our code.
```

This is great though - we can now get the sum of any two numbers by calling our function like that.

The other important thing about functions, is that if they return, they are the same as just writing their response; that is to say:

```py
sum(1,sum(1,2))
```

will give 4, because first, we find that `sum(1,2)` is 3, and then calculate `sum(1,3)`, to get 4.
#### Arrays

An array is like a storage shelf. We can put as many boxes on it as we want, and we can take boxes off it if we need to. If we need to, we can even put a shelf on top of another shelf.

```
+---+---+
| 3 | 4 |
+---+---+

array = [3,4]
```

Above is an example of what our shelf might look like, and how it looks to Python.

If we want to pull objects off our shelf, we can do so like this:

```
array[0]
```
The most important thing is that when we're telling Python which object we want to get off our shelf, we start from the number 0 (meaning the leftmost box on the shelf).


## Magic 8 Ball

### Making a boring 8 Ball

Let's start by making an 8 Ball that just goes through a list.

Every time someone shakes the microbit, we'll display the next answer in the `answersArray`.

In order to do this, we'll store a variable -- `answer` -- and every time, after we show our text, we'll increase it by one.

```py
from microbit import *

answersArray = ["Most likely","As I see it, yes", "Very doubtful"] #You can add whatever you want to this list
answer = 0

while True:
    if accelerometer.current_gesture() == "shake":
        display.clear()
        display.scroll(answersArray[answer])

    sleep(100)
```

Make sure you understand why this code works (or why it doesn't!), and experiment with it a bit.

And think about what might happen if we try to access an item in our array, that's beyond the length of our array.

For instance, what might this do:
```py
arr = ["a","b","c"]
display.scroll(arr[10])
```

With this knowledge, let's try to fix the 8-ball.

### Making a more exciting 8 Ball

Now, let's make the 8-ball more exciting -- rather than cycling through a set of predictable outcomes, let's randomly choose one.

```py
from microbit import *
import random

answersArray = ["Most likely","As I see it, yes", "Very doubtful"] #You can add whatever you want to this list
answer = 0

while True:
    if accelerometer.current_gesture() == "shake":
        display.clear()
        display.scroll(answersArray[answer])
        answer = answer + 1
        
    if answer >= len(answersArray):
        answer = 0
    sleep(100)
```

Copy paste this code in -- you can of course change the answers in the answers array -- and see if you can make it select a random number each time.

Below are some hints! Try to figure this one out using the hints...

There will be prizes for people who can figure this out! And as always, it's fine if you work in groups -- so long as everyone in the group ends up with something that works, and everyone understands why it works.

### Hints

#### Getting a random number
In Python, we can use:

```py
random.randint(minimum,maximum)
```

to generate a random number, where both minimum and maximum are inclusive (the number can be minimum or maximum or anything in between).

We also have this function called `len()`, which takes a container (for example, an array), as its only parameter, and returns the number of elements in the container:

```py
harryPotterBooks = ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half Blood Prince", "Harry Potter and the Deathly Hallows"]

numberOfBooks = len(harryPotterBooks) # This will be 7
lastBook = harryPotterBooks[numberOfBooks - 1] # "Harry Potter and the Deathly Hallows"
```

Remember, for lastBook, we use `numberOfBooks - 1` because the computer counts from `0`.

## If you finish
Please talk to us if you finish
