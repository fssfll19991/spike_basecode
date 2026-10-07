################################################################################
# mission_one.py
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

def mission_one(r: robot):
    print("Running Mission 111111")
    # Your code goes here...
    #r.robot.straight(230)
    #r.robot.turn(-50)
    #r.robot.straight(400)
    #r.lam.run_time(5000,500)
    #r.robot.straight(-400)
    #r.robot.turn(-20)
    #r.robot.straight(490)
    #r.robot.turn(45)
    #r.lam.run_time(-5000,5000)
    #r.robot.straight(630)
    r.robot.straight(300)
    r.lam.run_time(5000,500)
    r.robot.straight(-300)
    r.robot.turn(-30)
    r.robot.straight(400)
    r.robot.turn(53)
    r.lam.run_time(-5000,5000)
    r.robot.straight(-630)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
