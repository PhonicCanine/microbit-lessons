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