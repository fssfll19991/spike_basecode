################################################################################
# mission_seven.py
#
# Description:
# Flip the rock
#
# Author(s): Braydon
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
import helpers

def mission_seven(r: robot):
    print("Running Mission 7")
    # Your code goes here...
    # Mission Model 3, Flip the Rock

    helpers.turbo_mode(r)

    r.robot.straight(400)
    r.lam.run_angle(60,120)
    r.robot.straight(-400)
    r.lam.run_angle(-500,45)

    helpers.turbo_mode(r)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
