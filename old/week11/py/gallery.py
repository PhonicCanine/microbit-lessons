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