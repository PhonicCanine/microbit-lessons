# Week 9 - Photo Gallery

This week, we'll be doing something more open ended:

## Design Brief

Someone wants you to make a Photo Gallery that runs on the Microbit.

It should do the following:

* Display photos (Images) on the Microbit's display
* Allow the user to switch between images using the buttons on the Microbit
* Have at least 5 photos in it
* Should not crash when the next photo is requested on the last photo

The person who wants this doesn't mind which photos you use. It's probably easiest to use images that are built in (IE, Image.HAPPY), but if you want to make your own pictures to put into your gallery, go ahead.

### Hints

1. Think about ways to store multiple images, and how you would get the images out of whatever data structure you're thinking of.

    Arrays (shelves) probably make sense for this task, but if you can think of something else, go ahead.

2. Think about ways to listen for input. We don't want our gallery to close, so you'll probably need to put some kind of loop somewhere.

## Extension

Using `shift_left` and `shift_right`, figure out how to animate the images changing.