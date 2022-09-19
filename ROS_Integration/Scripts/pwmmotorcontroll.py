#!/usr/bin/env python
import rospy # Python library for ROS
from std_msgs.msg import String, UInt16
from geometry_msgs.msg import Point
import RPi.GPIO as GPIO

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set variables for the GPIO motor driver pins
motor_left_fw_pin = 10
motor_left_bw_pin = 9
motor_right_fw_pin = 8
motor_right_bw_pin = 7

# PWM signal frequency in Hz
pwm_freq = 2000
# PWM % duty cycle
fw_bw_duty_cycle = 60
turn_duty_cycle = 40

# Set the GPIO Pin mode to output
GPIO.setup(motor_left_fw_pin, GPIO.OUT)
GPIO.setup(motor_left_bw_pin, GPIO.OUT)
GPIO.setup(motor_right_fw_pin, GPIO.OUT)
GPIO.setup(motor_right_bw_pin, GPIO.OUT)

# Create PWM objects to handle GPIO pins with 'pwm_freq' frequency
motor_left_fw = GPIO.PWM(motor_left_fw_pin, pwm_freq)
motor_left_bw = GPIO.PWM(motor_left_bw_pin, pwm_freq)
motor_right_fw = GPIO.PWM(motor_right_fw_pin, pwm_freq)
motor_right_bw = GPIO.PWM(motor_right_bw_pin, pwm_freq)

# Start PWM with a duty cycle of 0 by default
motor_left_fw.start(0)
motor_left_bw.start(0)
motor_right_fw.start(0)
motor_right_bw.start(0)

# Global variables for storing received ROS messages
received_command = ''
last_received_command = ''
received_coord = Point(0, 0, 0)
target_radius = None
MIN_TGT_RADIUS_PERCENT = 0.05
image_width = 0
CENTER_WIDTH_PERCENT = 0.30

# Motor driving functions
def forward():
motor_left_fw.ChangeDutyCycle(fw_bw_duty_cycle)
motor_left_bw.ChangeDutyCycle(0)
motor_right_fw.ChangeDutyCycle(fw_bw_duty_cycle)
motor_right_bw.ChangeDutyCycle(0)

def backward():
motor_left_fw.ChangeDutyCycle(0)
motor_left_bw.ChangeDutyCycle(fw_bw_duty_cycle)
motor_right_fw.ChangeDutyCycle(0)
motor_right_bw.ChangeDutyCycle(fw_bw_duty_cycle)

def left():
motor_left_fw.ChangeDutyCycle(0)
motor_left_bw.ChangeDutyCycle(turn_duty_cycle)
motor_right_fw.ChangeDutyCycle(turn_duty_cycle)
motor_right_bw.ChangeDutyCycle(0)

def right():
motor_left_fw.ChangeDutyCycle(turn_duty_cycle)
motor_left_bw.ChangeDutyCycle(0)
motor_right_fw.ChangeDutyCycle(0)
motor_right_bw.ChangeDutyCycle(turn_duty_cycle)

def stopMotors():
motor_left_fw.ChangeDutyCycle(0)
motor_left_bw.ChangeDutyCycle(0)
motor_right_fw.ChangeDutyCycle(0)
motor_right_bw.ChangeDutyCycle(0)

# The node's main entry function
def listener():
rospy.init_node('motor_driver', anonymous=True)
rospy.Subscriber('/command', String, commandCallback)
rospy.Subscriber('/target_coord', Point, targetCoordCallback)
rospy.Subscriber('/target_radius', UInt16, targetRadiusCallback)
rospy.Subscriber('/image_width', UInt16, imageWidthCallback)
rospy.spin()

# Callback functions to process incoming ROS messages
def commandCallback(message):
global received_command
global last_received_command

received_command = message.data

if received_command == 'forward':
forward()
elif received_command == 'backward':
backward()
elif received_command == 'left':
left()
elif received_command == 'right':
right()
elif received_command == 'stop':
stopMotors()
elif received_command == 'auto':
autonomous()
else:
print('Unknown command!')

if received_command != last_received_command:
print('Received command: ' + received_command)
last_received_command = received_command

def imageWidthCallback(message):
global image_width
image_width = message.data

def targetRadiusCallback(message):
global target_radius
target_radius = message.data