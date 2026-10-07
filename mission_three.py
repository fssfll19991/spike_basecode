################################################################################
# mission_three.py
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

def mission_three(r: robot):
    print("Running Mission 3")
    # Your code goes here...
    # Sample Code: Test running the attachment motor until stalled
    r.robot.straight(1070)
    r.robot.turn(-90)
    r.robot.straight(100)
    r.robot.turn(-90)
    r.lam.run_time(100, 1500)
    r.robot.turn(-25)
    r.lam.run_time(-100, 1500)
    r.robot.turn(-10)
    r.robot.straight(300)
    r.robot.turn(90)
    r.robot.straight(300)
    r.robot.turn(-85)
    r.robot.straight(-150)
    r.robot.turn(-10)
    r.robot.straight(500)
    r.robot.turn(50)
    r.robot.straight(400)


################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

