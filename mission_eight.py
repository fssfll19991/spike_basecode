################################################################################
# mission_eight.py
#
# Description:
# start on the left side, solve the vine, then leaves, then root cover, then
# drive home to the right side
#
# Author(s): Abigail Hart
# Date: [YYYY-MM-DD]
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
# - helpers
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch
import helpers

def mission_eight(r: robot):
    print("Running Mission 8")
    # Your code goes here..

    helpers.turbo_mode(r)

    # Solve the vine
    r.robot.straight(450)
    r.robot.turn(50)
    r.robot.straight(450)
    r.robot.turn(-65)
    r.robot.straight(110)
    r.lam.run_angle(500, -30)
    r.robot.turn(-23)
    r.lam.run_angle(500, -10)
    r.robot.straight(-139)

    # Solve the leaves+ant

    r.robot.turn(-90)
    r.robot.straight(-250)
    r.robot.turn(45)
    r.robot.straight(-200)
    r.robot.turn(45)
    r.robot.straight(-160)
    r.robot.turn(-90)
    helpers.sloth_mode(r)
    r.robot.straight(-230)
    helpers.turbo_mode(r)
    r.robot.straight(170)

    # ELLA's mission
    r.robot.turn(82)
    r.robot.straight(-900)

    helpers.regular_mode(r)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
