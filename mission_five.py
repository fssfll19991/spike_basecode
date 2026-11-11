################################################################################
# mission_five.py
#
# Description:
# Solves Drone Survey
#
# Author(s): Maeve
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

def mission_five(r: robot):
    print("Running Mission 5")
    # Your code goes here...

    helpers.turbo_mode(r)

    r.robot.straight(700)
    r.robot.straight(-800)

    helpers.regular_mode(r)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
