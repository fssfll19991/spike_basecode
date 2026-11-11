################################################################################
# helpers.py
#
# Description:
# Various helper functions
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

def turbo_mode(r: robot):
    print("Turbo mode on!!!")
    r.robot.settings(800,1000,500,400)

def regular_mode(r: robot):
    print("Regular mode on")
    r.robot.settings(400,300,300,200)

def sloth_mode(r: robot):
    print("Sloth mode on")
    r.robot.settings(100,100,300,200)
