################################################################################
# mission_four.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): [Your Name(s)]
# Date: [YYYY-MM-DD]
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_four(r: robot):
    print("Running Mission 4")
    r.robot.straight(350)# Your code goes here...
    r.robot.turn(90)# Sample code: Test the speaker
    r.robot.straight(750)
    #r.robot.drive(0,10)
    r.lam.run_angle(-500,60)
    r.robot.straight(-100)
    r.robot.straight(-800)

    #r.robot.stop()
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
