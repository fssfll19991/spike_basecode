################################################################################
# mission_nine.py
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

def mission_nine(r: robot):
    print("Running Mission 9")
    # Your code goes here...
    r.robot.straight(300)
    r.robot.turn(-90)
    r.robot.straight(600)
    r.lam.run_angle(-500,90)
    r.robot.straight(-20)
    r.lam.run_angle(500,90)
    r.robot.turn(-5)
    r.robot.straight(20)
    r.lam.run_angle(-500,90)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
