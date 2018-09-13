#!/usr/bin/python
import RoboPiLib as RoboPi
import time as time

INPUT = RoboPi.INPUT
OUTPUT = RoboPi.OUTPUT

LEFT_BUMPER  = 22
RIGHT_BUMPER = 23

LEFT_LED = 8
RIGHT_LED = 9

PRESSED = 0

RoboPi.RoboPiInit("/dev/ttyAMA0",115200)

RoboPi.pinMode(LEFT_BUMPER,  INPUT)
RoboPi.pinMode(RIGHT_BUMPER, INPUT)

RoboPi.pinMode(LEFT_LED,    OUTPUT)
RoboPi.pinMode(RIGHT_LED,   OUTPUT)

while 1:

  RoboPi.digitalWrite(LEFT_LED,RoboPi.digitalRead(LEFT_BUMPER))
  RoboPi.digitalWrite(RIGHT_LED,RoboPi.digitalRead(RIGHT_BUMPER))
  
RoboPi.RoboPiExit()