import RPi.GPIO as GPIO
import os
import sys

class Motor: #Define motor class
	def __init__(self):
		#Attributs: Pins
		self.IN1_Pin = 20
		self.IN2_Pin = 21
		self.IN3_Pin = 19
		self.IN4_Pin = 26
		self.ENA_Pin = 16
		self.ENB_Pin = 13
		#Attributs: State
		self.IN1 = GPIO.LOW	#Left motor rotational direction
		self.IN2 = GPIO.LOW	# IN1=HIGH && IN2=LOW: Forward
		self.IN3 = GPIO.LOW	
		self.IN4 = GPIO.LOW	
		self.ENA = GPIO.HIGH	
		self.ENB = GPIO.HIGH	
		#Attributs: Direction
		self.direction = ""
		#self.LW_speed_factor = 0
		#self.RW_speed_factor = 0
	def motor_init(self):
		global pwm_ENA
		global pwm_ENB
		GPIO.setup(self.ENA_Pin,GPIO.OUT,initial=GPIO.HIGH)
		GPIO.setup(self.IN1_Pin,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.IN2_Pin,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.ENB_Pin,GPIO.OUT,initial=GPIO.HIGH)
		GPIO.setup(self.IN3_Pin,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.IN4_Pin,GPIO.OUT,initial=GPIO.LOW)

		#Set the PWM pin and frequency is 2000hz
		pwm_ENA = GPIO.PWM(self.ENA_Pin, 2000)
		pwm_ENB = GPIO.PWM(self.ENB_Pin, 2000)
		pwm_ENA.start(0)
		pwm_ENB.start(0)


	def forward(self):
		GPIO.output(self.IN1_Pin, GPIO.HIGH)
		GPIO.output(self.IN2_Pin, GPIO.LOW)
		GPIO.output(self.IN3_Pin, GPIO.HIGH)
		GPIO.output(self.IN4_Pin, GPIO.LOW)
		pwm_ENA.ChangeDutyCycle(5)
		pwm_ENB.ChangeDutyCycle(5)
		self.direction = "F"
		#return self.direction

	def backward(self):
		GPIO.output(self.IN1_Pin, GPIO.LOW)
		GPIO.output(self.IN2_Pin, GPIO.HIGH)
		GPIO.output(self.IN3_Pin, GPIO.LOW)
		GPIO.output(self.IN4_Pin, GPIO.HIGH)
		pwm_ENA.ChangeDutyCycle(5)
		pwm_ENB.ChangeDutyCycle(5)
		self.direction = "B"
		#return self.direction

	def left(self):
		GPIO.output(self.IN1_Pin, GPIO.HIGH)
		GPIO.output(self.IN2_Pin, GPIO.LOW)
		GPIO.output(self.IN3_Pin, GPIO.HIGH)
		GPIO.output(self.IN4_Pin, GPIO.LOW)
		pwm_ENA.ChangeDutyCycle(5)
		pwm_ENB.ChangeDutyCycle(20)
		#Vitesse de rotation variant selon la vitesse de rotation des deux ensembles de roues
		#pwm_ENA.ChangeDutyCycle(LW_speed_factor)
		#pwm_ENB.ChangeDutyCycle(RW_speed_factor)
		self.direction = "L"
		#return self.direction

	def right(self):
		GPIO.output(self.IN1_Pin, GPIO.HIGH)
		GPIO.output(self.IN2_Pin, GPIO.LOW)
		GPIO.output(self.IN3_Pin, GPIO.HIGH)
		GPIO.output(self.IN4_Pin, GPIO.LOW)
		pwm_ENA.ChangeDutyCycle(20)
		pwm_ENB.ChangeDutyCycle(5)
		#Vitesse de rotation variant selon la vitesse de rotation des deu$
		#pwm_ENA.ChangeDutyCycle(LW_speed_factor)
		#pwm_ENB.ChangeDutyCycle(RW_speed_factor)
		self.direction = "R"
		#return self.direction

	def stop(self):
		GPIO.output(self.IN1_Pin, GPIO.LOW)
		GPIO.output(self.IN2_Pin, GPIO.LOW)
		GPIO.output(self.IN3_Pin, GPIO.LOW)
		GPIO.output(self.IN4_Pin, GPIO.LOW)
		pwm_ENA.start(0)
		pwm_ENB.start(0)
		self.direction = "S"
		#return self.direction

