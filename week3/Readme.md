# Week 3 - Programming!

This week we're going to do some actual programming, but first we're going to go over some code we've looked at before.

## Here's some code

```py
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        display.show(Image.ARROW_E)
    else:
        display.clear()
```

We've talked about this code in previous weeks, but we're going to talk about exactly how this code works for a little.
First, we have a `while True` -- this ensures that the code keeps going forever; we need this in order to keep the program running.

Try replacing the `while True` with an `if True`, and see what happens instead... Why do you think this happens? What happens if you hold a button when your microbit is in the process of flashing?

## Make some modifications!

Next, let's try to make it show a different image -- an up arrow (`Image.ARROW_N`) -- when both buttons are being pressed.

Here's some code that tries to do that:

```py
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        display.show(Image.ARROW_E)
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ARROW_N)
    else:
        display.clear()
```

Why doesn't this work?

Try to make a version of this code that works correctly, and think about why it worked correctly.

## Let's make something new!

Now, we're going to make something that counts the number of times that a user presses the `a` button, and displays that value when the user presses the `b` button.

In order to do this, we're going to need to learn a few things:

First, we need to learn about variables.

### Variables

Variables allow us to store a value in code, and give it a name.

For instance, we can make a variable `name` that stores our name -- for instance `Alex` by saying:

```py
name = "Alex"
```

Now, if we want to show `Alex` on the display, we can use `display.scroll(name)` instead of `display.scroll("Alex")`.

We can have variables of different types too; for instance, we can store a number:

```py
x = 10
```

Importantly, we can then change the value we're storing in a variable.

```py
x = 10
x = x + 1
display.scroll(x)
```

In the above example, what do you think will be displayed on your microbit?

Give it a try, and make sure you understand why this is the case. As always, feel free to ask if something doesn't make sense.

```py
x = 10
y = 20
x = x + y
display.scroll(x)
```

What do you think will be shown this time? Give it a go and see if you're right...


Now, hopefully you've got a basic grasp on how all this works...

### Back to our counter

Now, let's try making that counter we talked about before -- to recap:

The program should count the number of times that a user presses the `a` button, and displays that value when the user presses the `b` button.

As a basic scafolding, here's some code:

```py
from microbit import *

x = 1
while True:
    if button_b.is_pressed():
        display.scroll(x)
```

Try to make this increase the counter every time button a is pressed. Good Luck!

And as always, let us know if you need a hand!

## Extension

As an extension task, take the code you've written for your counter, and modify it so that it automatically counts up once a second.

If the user presses the `a` button the counter should stop; or if the timer is already stopped, it should start again from `0`.

If they press the `b` button, as before, the current value should be displayed.