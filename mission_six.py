################################################################################
# mission_six.py
#
# Description:
# Solves exploding seeds
#
# Author(s): Cleo
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

def mission_six(r: robot):
    print("Running Mission 6")
    # Your code goes here...

    helpers.turbo_mode(r)

    #r.robot.straight(230)
    #r.robot.turn(-40)
    r.robot.straight(360)
    r.lam.run_time(-55,1000)
    r.robot.straight(-20)
    r.lam.run_time(-100,1000)
    r.robot.straight(-700)

    helpers.regular_mode(r)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
