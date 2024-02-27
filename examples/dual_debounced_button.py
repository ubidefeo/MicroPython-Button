# For particularly noisy buttons or tilt sensors
# it is advised to use a longer debounce time
# which will filter out the change of state between HIGH/LOW
# the Button object can be initialised using a custom debounce_time (in ms)

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
def button_action(button, event):
    global counter_pressed, counter_released
    print(f'debounced button {button} has been {event}')
    if event == Button.PRESSED:
        counter_pressed += 1
    if event == Button.RELEASED:
        counter_released += 1
    print(f'pressed {counter_pressed} times')
    print(f'released {counter_released} times')


# we define a variable which holds a Button
# this Button object will be created using:
# - the pin number (GPIOx)
# - rest_state: the state at rest (value() is False by default)
# - callback: the function to invoke when the button changes state (see above)
button_one = Button(7, rest_state = False, callback = button_action, debounce_time = 100)
button_two = Button(4, rest_state = False, callback = button_action, debounce_time = 100)
# during our loop we keep checking the button(s)
while(True):
    button_one.update()
    button_two.update()