#!/usr/bin/python
import RoboPiLib as RoboPi
import time as time

SERVO = RoboPi.SERVO

LEFT_SERVO  = 0
RIGHT_SERVO = 1

SERVO_MIN   = 500
SERVO_MAX   = 2500
SERVO_REV   = (SERVO_MIN + SERVO_MAX)
SERVO_STEP  = 100

RoboPi.RoboPiInit("/dev/ttyAMA0",115200)

RoboPi.pinMode(LEFT_SERVO,  SERVO)
RoboPi.pinMode(RIGHT_SERVO, SERVO)

while 1:

  for pos in xrange(SERVO_MIN, SERVO_MAX, SERVO_STEP):

    RoboPi.servoWrite(LEFT_SERVO, pos)
    RoboPi.servoWrite(RIGHT_SERVO, SERVO_REV-pos)

    print "Left Servo = ",  RoboPi.servoRead(LEFT_SERVO)
    print "Right Servo = ", RoboPi.servoRead(RIGHT_SERVO)

    time.sleep(0.1)
    
RoboPi.RoboPiExit()

