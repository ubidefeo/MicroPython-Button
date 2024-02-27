# MicroPython-Button

An easy to use [MicroPython](https://micropython.org) library to handle Buttons and other devices with digital (LOW/HIGH) output.

Instantiate an object of this Class to easily handle its behaviour via `PRESSED` and `RELEASED` events.

The instance supports a callback or just retrieving its `active` state using `instance.active`.
State will be `True` when activated (pressed) and `False` when deactivated (released) or not yet pressed.

By default the object instance assumes a __pull-down__ (external or internal) resistor, hence the `rest_state` is `False` (LOW). In case of __pull-up__ (external or internal), when the `Pin` is triggered shorting it to __GND__, create an instance adding the argument `rest_state = True`

In addition it is possible to leverage _internal pull-up__ or __pull-down__ resistors if the MicroPython implementation supports it.
By simply adding `internal_pullup = True` or `internal_pulldown = True` to the initialisation arguments, they will be internally set.
This also renders the need for `rest_state` redundant, since it will be set based on the above two options for __pull-up/down__.

The library supports debouncing with a default of 50ms, but for more finicky/noisy switches such as tilt sensors, a longer time to stabilise can be passed via the `debounce_time` parameter (see the `dual_debounced_button.py` example).

## Installation

The library can be installed in several ways:

### Manual

Simply copy the file `mp_button.py` to your board's `/lib` folder (or to any location which is part of the search path)

### mip

1. Make sure your board has a connection to internet
1. Open a REPL session and run the following commands

```
import mip
mip.install('github:ubidefeo/MicroPython-Button')
```

### mpremote mip

1. Make sure you have `mpremote` [installed](https://docs.micropython.org/en/latest/reference/mpremote.html)
1. Connect the board to your computer
1. Open a shell and run `mpremote mip install "github:ubidefeo/MicroPython-Button"`

## Examples

Button connected to __GPIO17__ with an __external pull-down__ resistor.
When using __external pull-down resistors__ the extra argument for `rest_state` is not required, since `rest_state` defaults to `False`.
Polling the `state`, not using a __callback__.

```python
from mp_button import Button
my_button = Button(17)

while(True):
    my_button.update()
    print(my_button.active)
```

Button connected to __GPIO17__ with an __external pull-up__ resistor.
When using __external pull-up resistors__ the extra argument for `rest_state` is mandatory, since `rest_state` defaults to `False` and a __pull-up__ would set it to `True`.
Polling the `state`, not using a __callback__.

```python
from mp_button import Button
my_button = Button(17, rest_state = True)

while(True):
    my_button.update()
    print(my_button.active)
```

Button connected to __GPIO17__ with an __external pull-down__ resistor.
When using __external pull-down resistors__ the extra argument for `rest_state` is not required, since `rest_state` defaults to `False`.
Using a __callback__ function.

```python
from mp_button import Button

def button_action(pin, event):
    print(f'Button connected to Pin {pin} has been {event}')
    if event == Button.PRESSED:
        print('Button pressed')
    if event == Button.RELEASED:
        print('Button released')

my_button = Button(17, callback = button_action)
while(True):
    my_button.update()

```

Button connected to __GPIO17__ with an __external pull-up__ resistor.
When using __external pull-up resistors__ the extra argument for `rest_state` is mandatory, since `rest_state` defaults to `False` and a __pull-up__ would set it to `True`.
Using a __callback__ function.

```python
from mp_button import Button

def button_action(pin, event):
    print(f'Button connected to Pin {pin} has been {event}')
    if event == Button.PRESSED:
        print('Button pressed')
    if event == Button.RELEASED:
        print('Button released')

my_button = Button(17, rest_state = True, callback = button_action)

while(True):
    my_button.update()
  
```

Button connected to __GPIO17__, __internal pull-down__ resistor enabled.
The argument `internal_pulldown = True` will override the default `rest_state`, hence passing in `rest_state = False` is not required and would anyway be overridden.
Using a __callback__ function.

```python
from mp_button import Button

def button_action(pin, event):
    print(f'Button connected to Pin {pin} has been {event}')
    if event == Button.PRESSED:
        print('Button pressed')
    if event == Button.RELEASED:
        print('Button released')

my_button = Button(17, callback = button_action, internal_pulldown = True)

while(True):
    my_button.update()
  
```

Button connected to __GPIO17__, __internal pull-up__ resistor enabled.
The argument `internal_pullup = True` will override the default `rest_state`, hence passing in `rest_state = True` is not required and would anyway be overridden.
Using a __callback__ function.

```python
from mp_button import Button

def button_action(pin, event):
    print(f'Button connected to Pin {pin} has been {event}')
    if event == Button.PRESSED:
        print('Button pressed')
    if event == Button.RELEASED:
        print('Button released')

my_button = Button(17, callback = button_action, internal_pullup = True)

while(True):
    my_button.update()
  
```
