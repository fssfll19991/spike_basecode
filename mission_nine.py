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
   # r.robot.straight(-925)
    r.robot.settings(800,1000,500,400)
    r.robot.straight(-960)
    r.lam.run_angle(-1000,100)
    r.robot.straight(1000)
    r.robot.settings(400,300,300,200)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
