#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import curses

from camera import Camera

#Definition of  motor pin 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

#advance
def run(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(10)
    pwm_ENB.ChangeDutyCycle(10)
    time.sleep(delaytime)

#back
def back(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(10)
    pwm_ENB.ChangeDutyCycle(10)
    time.sleep(delaytime)

#turn left
def left(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(5)
    pwm_ENB.ChangeDutyCycle(30)
    time.sleep(delaytime)

#turn right
def right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(30)
    pwm_ENB.ChangeDutyCycle(5)
    time.sleep(delaytime)

#turn left in place
def spin_left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)

#turn right in place
def spin_right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)

#brake
def brake(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)

#Delay 2s   
time.sleep(2)

robot_camera = Camera()

robot_camera.width = 1280
robot_camera.height = 720
robot_camera.path = '/home/pi/python/PFE_Autonomous_Robot/camera_images/'
robot_camera.camera_init()



#Curses Screen Initialization
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
#The robot car advance 1s，back 1s，turn left 2s，turn right 2s，turn left  in place 3s
#turn right  in place 3s，stop 1s。
try:
    motor_init()
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print ("up")
            run(0)
	    robot_camera.camera_capturing_image()
        elif char == curses.KEY_DOWN:
            print ("down")
	    robot_camera.camera_capturing_image()
            back(0)
        elif char == curses.KEY_RIGHT:
            print ("right")
	    robot_camera.camera_capturing_image()
            right(0)
        elif char == curses.KEY_LEFT:
            print ("left")
    	    robot_camera.camera_capturing_image()
            left(0)
        elif char == 10:
            print ("stop")
            brake(0)
            
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup() 


#except KeyboardInterrupt:
 #   pass
#pwm_ENA.stop()
#pwm_ENB.stop()
#GPIO.cleanup() 

