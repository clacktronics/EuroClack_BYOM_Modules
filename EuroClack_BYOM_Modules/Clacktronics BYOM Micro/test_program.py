import time
import board
import digitalio, analogio, pwmio, busio
import audiocore
import audiopwmio
import microcontroller
from random import randrange

#map function
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#gate setup
gate_out = digitalio.DigitalInOut(board.GP5)
gate_out.direction = digitalio.Direction.OUTPUT

gate_in = digitalio.DigitalInOut(board.GP2)
gate_in.direction = digitalio.Direction.INPUT
gate_in.pull = digitalio.Pull.UP

# CV setup
cv_in = analogio.AnalogIn(board.GP26)
cv_out = pwmio.PWMOut(board.GP6, frequency=100000)

# Potentiometer setup
pot1 = analogio.AnalogIn(board.GP27)
pot2 = analogio.AnalogIn(board.GP28)

# Set LEDs as either PWM
led1 = pwmio.PWMOut(board.GP3, frequency=100000)
led2 = pwmio.PWMOut(board.GP4, frequency=100000)

# Digital LED setup
#led1 = digitalio.DigitalInOut(board.GP3)
#led1.direction = digitalio.Direction.OUTPUT
#led2 = digitalio.DigitalInOut(board.GP4)
#led2.direction = digitalio.Direction.OUTPUT


# Basic examplke of pots
"""
while True:
    led1.duty_cycle = pot1.value
    led2.duty_cycle = pot2.value
""" 
# Digital led example
"""
while True:
    led1.value = not led1.value
    led2.value = not led1.value
    time.sleep(1)
"""
# PWM LED example
"""
while True:
    for i in range(65535):
        led1.duty_cycle = i
        led2.duty_cycle = 65535-i
    for i in range(65535, 0, -1):
        led1.duty_cycle = i
        led2.duty_cycle = 65535-i
"""


# CV out test
"""
while True:
    for i in range(0,65535,1000):
        cv_out.duty_cycle = i
        led1.duty_cycle = i
        time.sleep(pot1.value/1000000)
    for i in range(65535, 0, -1000):
        cv_out.duty_cycle = i
        led1.duty_cycle = i
        time.sleep(pot2.value/1000000)
"""

#Simple VCO to proove CV input
# CV in test, Saw on CV output and square on Gate out
"""
while True:
    for i in range(0,65535, 1000):
        cv_out.duty_cycle = i
        if(i >= pot2.value): gate_out.value = True
        else: gate_out.value = False
        microcontroller.delay_us(int(cv_in.value/100))
"""


# Sequencer
"""
sequence = [5,1,2,3,5,1,0]
x = 0
last_val = 0
while True:
    cv_out.duty_cycle = sequence[x] * 10000
    print(sequence[x] * 100)
    if gate_in.value == False and last_val == True:
        x+=1
        led1.duty_cycle = 65535
        time.sleep(0.2)
        led1.duty_cycle = 0
        if x >= 7: x = 0
    last_val = gate_in.value
"""

        


        




    