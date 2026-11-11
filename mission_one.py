################################################################################
# mission_one.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): Ella
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

def mission_one(r: robot):
    print("Running Mission 1")
    # Your code goes here...
    helpers.turbo_mode(r)

    r.robot.straight(300)
    r.lam.run_time(5000,500)
    r.robot.straight(-300)
    r.lam.run_time(3000,300)
    r.robot.curve(290,115)
    r.robot.turn(20)
    r.robot.straight(40)
    r.lam.run_time(-300,800)
    r.robot.straight(-100)
    r.robot.turn(-100)
    r.robot.straight(-700)

    helpers.regular_mode(r)

    #this part of the mission is the seed :)
    #r.robot.turn(-30)
    #r.robot.straight(400)
    #r.robot.turn(60)
    #r.lam.run_time(-1000,500)
    #r.robot.turn(-30)
    #r.robot.straight(-630)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
