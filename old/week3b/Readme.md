# Week 3 - Programming for the Microbit

This week, we'll work on a Magic 8-ball for the Microbit.

## Some more programming concepts

### Functions and Variables

In simple terms, a Variable is like a box, that we store information in. We can put anything inside this box, and whenever we write out the name of it in our program, the code will see whatever we have inside our box. To put things into our box, we can use assignment - `=`.

A function then, is like Amazon. We can tell it what we want, and it will give us a box with what we want in it.

Below is some more explanation.

#### Functions
Functions allow us to get a block of code, and run it again, without needing to copy-paste the code. In Python, we write a function as follows:
```py
def functionName(<arguments>):
    '''code inside function goes here'''
```
That should probably look familiar, but let's look at what the `<arguments>` part is.

An argument is something that we pass into a function. Say we have the function below:

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

This is great though - we can now get the sum of any two numbers by calling our function like that.

The other important thing about functions, is that if they return, they are the same as just writing their response; that is to say:

```py
sum(1,sum(1,2))
```

will give 4, because first, we find that `sum(1,2)` is 3, and then calculate `sum(1,3)`, to get 4.

#### Variables
Variables are like functions - they make programming easier by allowing us to store something and do things to it. For example, say we want to write a function that will take a number and add 5 to it, then multiply it by half of itself plus 1:

without variables, we would have to do it like this:
```py
def doAThing(n):
    return (n + 1) * ((n + 1) / 2)
```
but with variables, we can do this:
```py
def doAThing(n):
    x = n + 1
    return x * (x / 2)
```
The second one is a lot more easy to read, and we can use variables for much more complicated stuff too. If we wanted to edit an image that will display on the microbit, for example, we could do it like this:
```py
Image.HAPPY.set_pixel(0,0,9).set_pixel(1,0,9).set_pixel(2,0,9)
```
or with variables (and a loop):
```py
img = Image.HAPPY
for i in range(0,2): #'i' will start at 0, then become 1, then become 2, and the code below will run each time
    img.set_pixel(i,0,9)
```

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

#### 2 Dimensional Arrays

A 2 dimensional array is like a table, or a shelf filled with shelves. Let's look at our previous array:
```
+---+---+
| 3 | 4 |
+---+---+

array = [3,4]

table = [array,array]
```
So what does our table array look like?

```
+---------+---------+
| +-----+ | +-----+ |
| |  3  | | |  3  | |
| +-----+ | +-----+ |
| |  4  | | |  4  | |
| +-----+ | +-----+ |
+---------+---------+
```
We can visualise it like this, where we have one large shelf turned on it's side, and another smaller shelf in each space of the larger shelf.

So now what does `table[0]` mean?

Well, we need to get the leftmost box in table, which is just:

```
+-----+
|  3  |
+-----+
|  4  |
+-----+
```

So then, what about `table[0][0]`?

Well, `table[0]` gives us
```
+-----+
|  3  |
+-----+
|  4  |
+-----+
```
We haven't tried to use an array like that before, but for now, we'll just say that in order to get box out, we need to rotate our shelf so it's horizontal. We always do this by pushing it to the left:

```
+---+---+
| 3 | 4 |
+---+---+
```
That should look familiar - and we know what element `0` of that is - it's `3`.

Now why do we do it like this?

While we can *visualise* a 2D array as a table, or a shelf filled with shelves, to the computer it's a sideways shelf, filled with sideways shelves.

```
+-----------+-----------+
| +---+---+ | +---+---+ |
| | 3 | 4 | | | 3 | 4 | |
| +---+---+ | +---+---+ |
+-----------+-----------+

table = [[3,4],[3,4]]
```

This should be more easy to read - `table[0][0]`, is just the leftmost box inside out table, then the leftmost box inside that - so `3`.

You may wonder now though, why we bothered with the other way of thinking about it. Well, the hint is in the name - two dimensional array.

In short, there are many times when we will want to store two dimensional information - for example, a picture, or a map, or a game board. For these examples, thinking of it as vertical shelves inside a horizontal shelf is really useful.

We're going to talk about a tic tac toe board, as an example:

```
+---+---+---+
| O +   + X |
+---+---+---+
|   + X + O |
+---+---+---+
| X + O +   |
+---+---+---+
```
If I ask you what is in the first column, first row, you should be able to pretty quickly see that it is `O`. To represent this board in Python, we would do it like this:

```
board = [[O,,X],[,X,O],[X,O,]]
```
(the blank spaces are in there too)

Now, as I've said before, the more accurate way of representing this is as follows:

```
+---------------+---------------+---------------+
| +---+---+---+ | +---+---+---+ | +---+---+---+ |
| | O |   | X | | |   | X | O | | | X | O |   | |
| +---+---+---+ | +---+---+---+ | +---+---+---+ |
+---------------+---------------+---------------+
```
That obviously works, but it's a bit harder to see, for example, that X has won the game.

You should be able to see that `board[0][0]` is `O`, like we said above.

An easier way to visualise this though, so that we can think about what's happening in our heads is like this:

```
+---------------+
| +---+---+---+ |
| | O |   | X | |
| +---+---+---+ |
+---------------+
| +---+---+---+ |
| |   | X | O | |
| +---+---+---+ |
+---------------+
| +---+---+---+ |
| | X | O |   | |
| +---+---+---+ |
+---------------+
```

Now it's sort of easier to see what's happening

We can see that `board[0]` will give us the box in the top of the shelf, which is another shelf.

Then, we should be able to see that `board[0][2]` will give us the 3rd box in the shelf in the first space, meaning it will contain `X`.

So we can simplify this more - `board[row][column]` is now a way we can think about this.

Another way of saying that we're using row first, and column second, is to say that we are accessing the 2D array with `[y][x]`.

There will be times when `[y][x]` makes more sense to you, but generally we use `[x][y]`, meaning `board[column][row]`. If we had decided to do that, this board would be represented like this:

```
+-------+-------+-------+
| +---+ | +---+ | +---+ |
| | O | | |   | | | X | |
| +---+ | +---+ | +---+ |
| |   | | | X | | | O | |
| +---+ | +---+ | +---+ |
| | X | | | O | | |   | |
| +---+ | +---+ | +---+ |
+-------+-------+-------+

board = [[O,,X],[,X,O],[X,O,]]
```

As you can see, the only difference here is in which shelves are rotated. Now to get the middle element on the bottom row, we would use `board[1][2]`, where in the other example, we would use `board[2][1]`.

_Well done getting through this, now we'll get to some fun stuff_

## Magic 8 Ball

### About comments and how we're going to do things like this

Really quickly, it's worth explaining a few things:

```py
'''This is a multilined python comment'''
# And this is a single-lined comment
```

For coding activities, most of the time, we will use pre-prepared python files. They will almost always contain comments in them. We're going to use the single-line comments for explanations of how the code works.

However, we will use multilined comments to mark areas where you have to write some code to make things work. There will be a description of what to do, and you've just got to figure out how to do it, for example, this might be a section of code:

```py
number = 1 + 5

'''check if the number is 6, and display a happy face if it is'''
```

And the solution would be:

```py
number = 1 + 5

'''check if the number is 6, and display a happy face if it is'''
if number == 6:
    display.show(Image.HAPPY)
```

### The actual 8-Ball

```py
from microbit import *
import random

answersArray = ["Most likely","As I see it, yes", "Very doubtful"] #You can add whatever you want to this list

while True:
    if accelerometer.current_gesture() == "shake":
        display.clear()
        '''get a random number, and display a piece of text from answersArray'''


    sleep(100)
```

Copy this code into a python file, and complete what the comment says to do.

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
