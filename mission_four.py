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
    r.robot.straight(925)
    r.lam.run_angle(500,90)


#r.robot.turn(90)
#r.robot.straight(740)
#r.robot.drive(0,10)
#r.lam.run_angle(-500,40)
#r.robot.straight(-100)
    #r.lam.run_angle(500,40)
    #r.robot.straight(-50)
    #r.lam.run_angle(-650,40)
    #r.robot.turn(-45)
    #r.robot.straight(300)
    #r.robot.turn(90)
    #r.robot.straight(200)
    #r.robot.straight(-650)
    #r.robot.turn(-90)
    #r.robot.straight(-350)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
