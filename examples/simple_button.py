from mp_button import Button


# we create a counter to increment as we press
# and one to increment as we release
counter_pressed = 0
counter_released = 0


# the following method (function) will be invoked
# when the button changes state
# the Button module expects a callback to handle 
# - pin number
# - event (Button.PRESSED | Button.RELEASED)
# the event contains a string 'pressed' or 'released'
# which can be used in your code to act upon
def button_change(button, event):
    global counter_pressed, counter_released
    print(f'button {button} has been {event}')
    if event == Button.PRESSED:
        counter_pressed += 1
    if event == Button.RELEASED:
        counter_released += 1
    print(f'pressed {counter_pressed} times')
    print(f'released {counter_released} times')


# we define a variable which holds a Button
# this Button object will be created using:
# - a pin number (GPIOx)
# - the state at rest (value() is False by default)
# - a callback to invoke when the button changes state (see above)
button_one = Button(17, False, button_change)

# a named parameter approach is also possible
# button_one = Button(17, rest_state = False, callback = button_change)

# during our loop we keep checking the button(s)
while(True):
    button_one.update()
