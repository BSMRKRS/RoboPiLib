#!/usr/bin/python
try:
  import RPi.GPIO as gpio
except RuntimeError:
  print "Import Failed!"

import time as time

reset = 17

gpio.setmode(gpio.BCM)
gpio.setup(reset, gpio.OUT)

gpio.output(reset, false)
time.sleep(0.1)
gpio.output(reset, true)

