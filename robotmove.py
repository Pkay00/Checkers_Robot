from machine import Pin
from machine import Pin, Timer
import time

# Outputs
compressor_pin = Pin(15, Pin.OUT)
valve_pin = Pin(16, Pin.OUT)
horiz_out = Pin(12, Pin.OUT)
horiz_in = Pin(11, Pin.OUT)
vert_down = Pin(10, Pin.OUT)
vert_up = Pin(9, Pin.OUT)
rot_clk = Pin(13, Pin.OUT)
rot_cclk = Pin(14, Pin.OUT)
led = Pin("LED", Pin.OUT)

# Inputs
rotencoderb = Pin(7, Pin.IN, Pin.PULL_DOWN)
rotencodera = Pin(8, Pin.IN, Pin.PULL_DOWN)
vertencoderb = Pin(3, Pin.IN, Pin.PULL_DOWN)
vertencodera = Pin(4, Pin.IN, Pin.PULL_DOWN)
rotlimit = Pin(2, Pin.IN, Pin.PULL_DOWN)
vertlimit = Pin(0, Pin.IN, Pin.PULL_DOWN)
horizencoderb = Pin(5, Pin.IN, Pin.PULL_DOWN)
horizencodera = Pin(6, Pin.IN, Pin.PULL_DOWN)
horizlimit = Pin(1, Pin.IN, Pin.PULL_DOWN)


def move_down(duration):
    vert_down.value(1)
    time.sleep(duration)
    vert_down.value(0)

def move_up(duration):
    vert_up.value(1)
    time.sleep(duration)
    vert_up.value(0)

def move_left(duration):
    horiz_in.value(1)
    time.sleep(duration)
    horiz_in.value(0)

def move_right(duration):
    horiz_out.value(1)
    time.sleep(duration)
    horiz_out.value(0)

def move_clockwise(duration):
    rot_cclk.value(1)
    time.sleep(duration)
    rot_cclk.value(0)

def move_anticlockwise(duration):
    rot_clk.value(1)
    time.sleep(duration)
    rot_clk.value(0)

# Define vacuum functions
def turn_on_vacuum(duration):
    compressor_pin.on()
    valve_pin.on()
    time.sleep(duration)

def turn_off_vacuum():
    valve_pin.off()
    compressor_pin.off()
    
# Define BoxFunctions class
class BoxFunctions:
    def box_move(self, box_num):
        if box_num == 1:
            move_down(4)
        elif box_num == 2:
            move_clockwise(0.38)
            move_right(0.18)
            move_down(4)
        elif box_num == 3:
            move_clockwise(0.75)
            move_right(0.6)
            move_down(4)
        elif box_num == 4:
            move_clockwise(1)
            move_right(1.2)
            move_down(4)

        elif box_num == 5:
            move_clockwise(0.23)
            move_right(0.7)
            move_down(4)
        elif box_num == 6:
            move_clockwise(0.52)
            move_right(1)
            move_down(4)
        elif box_num == 7:
            move_clockwise(0.77)
            move_right(1.45)
            move_down(4)
        elif box_num == 8:
            move_clockwise(1)
            move_right(2.1)
            move_down(4)
        elif box_num == 9:
            move_right(1.4)
            move_down(4)
        elif box_num == 10:
            move_clockwise(.34)
            move_right(1.5)
            move_down(4)
        elif box_num == 11:
            move_clockwise(0.6)
            move_right(1.75)
            move_down(4)
        elif box_num == 12:
            move_clockwise(0.83)
            move_right(2.2)
            move_down(4)
        elif box_num == 13:
            move_clockwise(0.18)
            move_right(1.95)
            move_down(4)
        elif box_num == 14:
            move_clockwise(0.43)
            move_right(1.97)
            move_down(4)
        elif box_num == 15:
            move_clockwise(0.66)
            move_right(2.6)
            move_down(4)
        elif box_num == 16:
            move_clockwise(0.86)
            move_right(3.2)
            move_down(4)
        elif box_num == 17:
            move_right(2.7)
            move_down(4)
        elif box_num == 18:
            move_clockwise(0.27)
            move_right(2.55)
            move_down(4)
        elif box_num == 19:
            move_clockwise(0.45)
            move_right(2.65)
            move_down(4)
        elif box_num == 20:
            move_clockwise(0.7)
            move_right(3.3)
            move_down(4)
        elif box_num == 21:
            move_clockwise(0.15)
            move_right(3.1)
            move_down(4)
        elif box_num == 22:
            move_clockwise(0.25)
            move_right(4.2)
            move_down(4)
        elif box_num == 23:
            move_clockwise(0.55)
            move_right(3)
            move_down(4)
        elif box_num == 24:
            move_clockwise(0.75)
            move_right(4.1)
            move_down(4)
        elif box_num == 25:
            move_right(3.5)
            move_down(4)
        elif box_num == 26:
            move_clockwise(0.25)
            move_right(3.75)
            move_down(4)
        elif box_num == 27:
            move_clockwise(0.45)
            move_right(4.1)
            move_down(4)
        elif box_num == 28:
            move_clockwise(0.63)
            move_right(4.43)
            move_down(4)
        elif box_num == 29:
            move_clockwise(0.25)
            move_right(4.4)
            move_down(4)
        elif box_num == 30:
            move_clockwise(0.31)
            move_right(4.6)
            move_down(4)
        elif box_num == 31:
            move_clockwise(0.5)
            move_right(5.1)
            move_down(4)
        elif box_num == 32:
            move_clockwise(0.67)
            move_right(5.5)
            move_down(4)
        
                

# Define home function
def go_home():
    while True:
        # Check the limit switches
        horiz_limit = horizlimit.value()
        vert_limit = vertlimit.value()
        rotl_limit = rotlimit.value()

        # If any of the limit switches is not activated, move towards it until it is activated
        if not horiz_limit:
            horiz_in.value(1)
        if not vert_limit:
            vert_up.value(1)
        if not rotl_limit:
            rot_clk.value(1)

        # If all limit switches are activated, break the loop and return to the home position
        if horiz_limit and vert_limit and rotl_limit:
            horiz_in.value(0)
            vert_up.value(0)
            rot_clk.value(0)
            break
    
    print("Robot is now at home position")

# Main loop
while True:
    # Get user input
    user_input = input("Enter movement directions and durations (e.g. 'u3 d2 l1 r2', enter 'h' for home, enter 'q' to quit): ")

    # Check if user wants to quit
    if user_input == 'q':
        break
    
    # Check if user input is for a box movement
    if ',' in user_input:
        # Parse input
        boxes = user_input.split(',')
        start_box = int(boxes[0])
        end_box = int(boxes[1])

        # Move robot to start box
        BoxFunctions().box_move(start_box)

        # Pick up checker piece
        compressor_pin.on()
        time.sleep(1)
        valve_pin.on()
        move_up(2)
        go_home()

        # Move robot to end box
        BoxFunctions().box_move(end_box)

        # Release checker piece
        valve_pin.off()
        compressor_pin.off()
        time.sleep(1)
        move_up(3)
        go_home()

    # Move based on input
    if user_input == 'h':
        go_home()
