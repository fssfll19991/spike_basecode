################################################################################
# mission_nine.py
#
# Description:
# Fungus
#
# Author(s): Lincoln
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

def mission_nine(r: robot):
    print("Running Mission 9")
    # Your code goes here...

    helpers.turbo_mode(r)

   # r.robot.straight(-925)
    r.robot.straight(-960)
    r.lam.run_angle(-1000,100)
    r.robot.straight(1000)

    helpers.regular_mode(r)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
