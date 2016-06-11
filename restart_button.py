#!/usr/bin/python

import RPi.GPIO as GPIO, time, os, subprocess

GPIO.setmode(GPIO.BCM)
switch = 22
green_led = 25

GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

GPIO.output(green_led, 0)
try:
    GPIO.output(green_led, 1)
    while (True):
        if (not GPIO.input(switch)):
            GPIO.output(green_led, 0)
            subprocess.call("sudo python /home/pi/photobooth/button.py", shell=True)
            time.sleep(5)
            GPIO.output(green_led, 1)
            time.sleep(1)
finally:
    GPIO.cleanup()