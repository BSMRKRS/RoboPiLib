#!/usr/bin/python
import RoboPiLib as RoboPi
import time as time

RoboPi.RoboPiInit("/dev/ttyAMA0",115200)

for times in range(0,100):

  for adc in range(0,8):
    print adc, RoboPi.analogRead(adc)

  time.sleep(0.5)
  
RoboPi.RoboPiExit()