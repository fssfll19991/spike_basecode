################################################################################
# mission_two.py
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

def mission_two(r: robot):
    print("Running Mission 2")
    # Your code goes here...
    r.robot.straight(350)
    r.robot.turn(90)
    r.robot.straight(712)
    #motor.run_for_degrees(port.A, -90, 100)
    #r.ram.run_time(-270,5000)
    r.lam.run_time(271,700)
    r.lam.run_time(-100,750)
    r.robot.straight(-100)


################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

