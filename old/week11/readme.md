# Week 11

Now that we've (hopefully) got a working animation gallery, let's finally learn how to make some animations.

(If you didn't finish the gallery, the finished code is below)
```py
from microbit import *

images = [[Image.HAPPY], [Image.MEH], [Image.SAD], [Image.FABULOUS], [Image.CLOCK12,Image.CLOCK12,Image.CLOCK12,Image.CLOCK3,Image.CLOCK3,Image.CLOCK3,Image.CLOCK6,Image.CLOCK6,Image.CLOCK6,Image.CLOCK9,Image.CLOCK9,Image.CLOCK9]]

selected = 0
fcounter = 0

unpressed = True

while True:
    if button_b.is_pressed() and unpressed:
        selected = (selected + 1) % len(images)
        fcounter = 0
        unpressed = False
    elif button_a.is_pressed() and unpressed:
        selected = (selected + len(images) - 1) % len(images)
        fcounter = 0
        unpressed = False
    elif not (button_a.is_pressed() or button_b.is_pressed()):
        unpressed = True
    
    fcounter = (fcounter + 1) % len(images[selected])
    
    display.show(images[selected][fcounter])
    sleep(50)
```

As mentioned a while ago, when talking about arrays (shelves), an image is simply a matrix of pixels. For example, a happy face:

```
     
 █ █

█   █
 ███
```
may be stored in the computer as:
```
[[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[1,0,0,0,1],[0,1,1,1,0]]
```
where every 0 is blank, and every 1 is a filled in square.

This should sort of make sense: by reformatting our array above, we can start to see how the image is formed:

```
[[0,0,0,0,0],
 [0,1,0,1,0],
 [0,0,0,0,0],
 [1,0,0,0,1],
 [0,1,1,1,0]]
```

If we replace all the 1's with blocks, and the 0's with spaces, it becomes even more clear:

```
[[ , , , , ],
 [ ,█, ,█, ],
 [ , , , , ],
 [█, , , ,█],
 [ ,█,█,█, ]]
```

On the microbit, we do something like this to create the images, except, rather than a shelf, full of shelves, with 1's and 0's, we use a single string with numbers from 0-9 in it, separated by a colon (:) every 5 characters. This happy face would thus be:

```py
happy = Image("00000:09090:00000:90009:09990")
```

This should make sense - the colons are just the commas that we would have between shelves if we were instead using a shelf full of shelves, and the individual numbers need not be separated, because they can only be one digit each. Again, we can reformat this string to show what's happening:

```
"00000:
 09090:
 00000:
 90009:
 09990"
```

and if we replace all the 0's with a blank space, and all the 9's with a block, we get this again:

```
"     :
  █ █ :
      :
 █   █:
  ███ "
```

Have a go at making your own image. It's probably worth trying to put something together in an art program first, and then translate it to the microbit.

## Part 2 - Animating

As we went through last week, animations are just a series of images. Try working by yourself or in groups to develop an animation to show on the Microbit display.

Try to have fun with it!