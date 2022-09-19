import pygame
from networktables import NetworkTables

pygame.init()
#creating networktable to send data to
NetworkTables.initialize(server='roborio-XXX-frc.local')
#creating object to interact with smartdashboard
smart_dashboard = NetworkTables.getTable('SmartDashboard')

#waiting for user to plug in controller
        
#connecting to controller and initialize
xboxcontroller = pygame.joystick.Joystick(0)
xboxcontroller.init()

#starting loop to obtain x and y controller analog values

#creating variables to hold x and y value from controller
left_analog_y_value = 0.0
right_analog_y_value = 0.0

while True:
    pygame.event.get()

    #storing analog input from x and y by converting to type float
    left_analog_y_value = float(format(xboxcontroller.get_axis(1)))
    right_analog_x_value = float(format(xboxcontroller.get_axis(4)))
    #uploading x and y analog values to network table
    smart_dashboard.putNumber('RightStickXValue', right_analog_x_value)
    smart_dashboard.putNumber('LeftStickYValue', left_analog_y_value)

    
    print("Left Analog Stick: {}\t Right Analog Stick: {}".format(xboxcontroller.get_axis(1),  # left stick y axis
                                                        xboxcontroller.get_axis(4)))  # right stick x axis
