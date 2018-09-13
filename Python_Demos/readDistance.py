#!/usr/bin/python
import RoboPiLib as RoboPi
import time as time

RoboPi.RoboPiInit("/dev/ttyAMA0",115200)

HC_SR04 = 16

while 1:
  print "Distance is ", RoboPi.readDistance(HC_SR04)
  time.sleep(0.1)

RoboPi.RoboPiExit()