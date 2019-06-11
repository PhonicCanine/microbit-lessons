# Week 10 - Improving our Gallery

Showing images is cool, but you know what's even better? Showing animated images.

Here's the code we should have ended up with last week:

```py
from microbit import *

images = [Image.HAPPY, Image.MEH, Image.SAD, Image.CLOCK9, Image.CLOCK3]

selected = 0

while True:
    if button_b.is_pressed():
        selected = (selected + 1) % len(images)
    elif button_a.is_pressed():
        selected = (selected + len(images) - 1) % len(images)
    
    
    display.show(images[selected])
    sleep(100)
```

Every animation will have a new frame every 100ms, and we need to be able to switch to another "image" while the animation is still running.

An example of some animation code is here:

```py
from microbit import *

#set up the animation

frames = [Image.CLOCK12,Image.CLOCK3,Image.CLOCK6,Image.CLOCK9]

#code for running the animation

fcounter = 0

while True:
    display.show(frames[fcounter])
    sleep(100)
    fcounter = (fcounter + 1) % len(frames)
```

To make this work for a gallery, instead of for one specific image, you'll need to figure out how to store the frames for each specific animation (Think Shelves inside Shelves).

## Extension
See if you can get the following, more complex animation to run inside your gallery:

```py
#set up a more complex animation

#scene 1
f1 = Image("00000:90900:99900:90900:99990")
f2 = Image("00900:90900:90900:90400:99990")
f3 = Image("00900:90900:94440:90400:99990")
f4 = Image("00900:94440:90400:90000:99990")
f5 = Image("04440:90400:90000:90000:99990")
f6 = Image("00400:90000:90000:90000:99990")

#scene 2
f7 = Image("00009:40000:00000:09004:00000")
f8 = Image("00009:90000:00000:04009:00000")
f9 = Image("00004:40000:00000:04009:00000")

#scene 3
f10 = Image("00900:09090:09090:09090:00900")
f11 = Image("00990:00990:00990:00990:09900")
f12 = Image("00949:00949:09449:94490:44900")

#scene 4
f13 = Image("93093:93096:99996:96096:96096")

#scene 5
f14 = Image("00000:00000:00900:00000:00000")
f15 = Image("00000:00000:01810:00000:00000")
f16 = Image("00000:00000:13531:00000:00000")
f17 = Image("00000:00000:15351:00000:00000")
f175 = Image("00000:00000:23132:00000:00000")
f18 = Image("00000:00000:00000:00000:00000")

#different overlays
rb = Image("00000:00000:00000:00000:00900")
rsb = Image("00000:00000:00000:00900:00000")
rm = Image("00000:00000:00900:00000:00000")
rst = Image("00000:00900:00000:00000:00000")
rt = Image("00900:00000:00000:00000:00000")

#putting all the frames together
frames = [f1,f2,f3,f4,f5,f6,f7,f8 + rb,f9 + rsb,f8 + rm,f9 + rst,f7 + rt,f10,f10,f10,f11,f11,f11,f12,f12,f12,f13,f13,f13,f13,f13,f13,f13,f14,f15,f16,f17,f175,f18,f18,f18,f18]
```