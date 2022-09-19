#!/usr/bin/env python 3
# this will allow us to interface with ROS
import rospy

# allow us to use data types
from std_msgs.msg import String

# modules to allow us to read key presses
import sys, select, termios, tty

command = "stop"
last_command = "stop"
# display message when node begins of commands
msg = """
Reading from the keyboard and publishing to /command!
---------------------------
Moving around:
i
j k l
,
CTRL-C to quit
"""

# nodes core instruction
def talker():
    global command
    global last_command

    pub = rospy.Publisher("/command", String, queue_size=10)
    rospy.init_node("keyb_commander", anonymous=True)
    # node will execute 10 times a seconds
    rate = rospy.Rate(10)  # 10 hz the

    print(msg)

    # detect keys
    while not rospy.is_shutdown():
        key_timeout = 0.6  # seconds
        k = getKey(key_timeout)

        if k == "i":
            command = "forward"
        elif k == ",":
            command = "backward"
        elif k == "j":
            command = "left"
        elif k == "l":
            command = "right"
        elif k == "k":
            command = "stop"
        elif k == "\x03":  # To detect CTRL-C
            break

        if command != last_command:
            print("Published command: " + command)
            last_command = command
            pub.publish(command)
            rate.sleep()

            def getKey(key_timeout):
                tty.setraw(sys.stdin.fileno())

            rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
            if rlist:
                key = sys.stdin.read(1)
            else:
                key = ""
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
                return key


if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)
try:
    talker()
except rospy.ROSInterruptException:
    pass
