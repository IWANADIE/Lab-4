import hal.hal_led as led
import hal.hal_input_switch as switch
import time
from time import sleep

def main():
    # Initialize LED HAL driver


    #Set LED output level, 1 = ON, 0 = OFF
    while True:
        led.init()
        switch.init()
        switch_status = switch.read_slide_switch()
        if switch_status == 1:
            led.set_output(1, 1)
            time.sleep(0.2)
            led.set_output(0, 0)
            time.sleep(0.2)

        else:
            led.set_output(0, 0)

main()