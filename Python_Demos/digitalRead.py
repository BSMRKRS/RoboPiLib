#!/usr/bin/python
import RoboPiLib as RoboPi
import time as time

INPUT = RoboPi.INPUT

LEFT_BUMPER  = 22
RIGHT_BUMPER = 23

PRESSED = 0

RoboPi.RoboPiInit("/dev/ttyAMA0",115200)

RoboPi.pinMode(LEFT_BUMPER,  INPUT)
RoboPi.pinMode(RIGHT_BUMPER, INPUT)

while 1:

  if (RoboPi.digitalRead(LEFT_BUMPER) == PRESSED):
    print "Left Bumper Pressed"

  if (RoboPi.digitalRead(RIGHT_BUMPER) == PRESSED):
    print "Right Bumper Pressed"
    
  time.sleep(0.1)
  
RoboPi.RoboPiExit()