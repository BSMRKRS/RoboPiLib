#!/usr/bin/python
import RoboPiLib as RoboPi
import time as time

INPUT  = RoboPi.INPUT
OUTPUT = RoboPi.OUTPUT
PWM    = RoboPi.PWM
SERVO  = RoboPi.SERVO

MOTORA_IA = 12
MOTORA_IB = 13
MOTORB_IA = 14
MOTORB_IB = 15

RoboPi.RoboPiInit("/dev/ttyAMA0",115200)

while 1:

    # set both motors to go forward

    RoboPi.pinMode(MOTORA_IA,PWM);
    RoboPi.pinMode(MOTORA_IB,OUTPUT);
                        
    RoboPi.pinMode(MOTORB_IA,PWM);
    RoboPi.pinMode(MOTORB_IB,OUTPUT);
    
    # slowly ramp up the sped

    for speed in xrange(0,256,2):
      RoboPi.analogWrite(MOTORA_IA,speed)
      RoboPi.analogWrite(MOTORB_IA,speed)
      time.sleep(0.1)
      
    # now ramp back town

    for speed in xrange(255,-1,-2):
      RoboPi.analogWrite(MOTORA_IA,speed)
      RoboPi.analogWrite(MOTORB_IA,speed)
      time.sleep(0.1)
      
    # set both motors to go reverse

    RoboPi.pinMode(MOTORA_IA,OUTPUT);
    RoboPi.pinMode(MOTORA_IB,PWM);
                        
    RoboPi.pinMode(MOTORB_IA,OUTPUT);
    RoboPi.pinMode(MOTORB_IB,PWM);
    
    # slowly ramp up the sped

    for speed in xrange(0,256,2):
      RoboPi.analogWrite(MOTORA_IB,speed)
      RoboPi.analogWrite(MOTORB_IB,speed)
      time.sleep(0.1)
      
    # now ramp back town

    for speed in xrange(255,-1,-2):
      RoboPi.analogWrite(MOTORA_IB,speed)
      RoboPi.analogWrite(MOTORB_IB,speed)
      time.sleep(0.1)
  
RoboPi.RoboPiExit()

