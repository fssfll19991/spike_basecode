################################################################################
# mission_three.py
#
# Description:
# Solves biocentric architecture
#
# Author(s): Olivia
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

def mission_three(r: robot):
    print("Running Mission 3")

    helpers.turbo_mode(r)

    r.robot.straight(1065)
    r.robot.turn(-90)
    r.robot.straight(100)
    r.robot.turn(-90)
    r.lam.run_time(100,1500)
    r.robot.turn(-27)
    r.lam.run_time(-120,1500)
    r.robot.turn(-10)
    r.robot.arc(300,90)
    #r.robot.straight(300)
    #r.robot.turn(90)
    #r.robot.straight(300)
    r.robot.turn(-85)
    r.robot.straight(-150)
    r.robot.turn(-40)
    r.robot.arc(900,50)
    #r.robot.straight(500)
    #r.robot.turn(50)
    #r.robot.straight(400)

    helpers.regular_mode(r)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

