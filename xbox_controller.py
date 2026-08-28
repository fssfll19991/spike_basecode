import umath

from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

# Wheel size, used to convert motor angle to distance driven.
WHEEL_DIAMETER = 55.5  # mm

# Distance between the centers of the left and right wheels, used to
# convert wheel angle to the angle the robot itself turned during a
# pivot turn, and by the drive base for gyro-corrected driving.
TRACK_WIDTH = 80  # mm

# Set up all devices.
left = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right = Motor(Port.F, Direction.CLOCKWISE)
function = Motor(Port.C, Direction.CLOCKWISE)
switch = Motor(Port.D, Direction.CLOCKWISE)
controller = XboxController()

# Used for forward/reverse driving, so the gyro can keep us driving
# straight. Left/right pivot turns and diagonal turns still drive the
# left/right motors directly, which automatically cancels the drive
# base's current maneuver.
drivebase = DriveBase(left, right, WHEEL_DIAMETER, TRACK_WIDTH)
drivebase.use_gyro(True)

# Linear speed for forward/reverse that matches the previous 250 deg/s
# wheel speed used for turning.
DRIVE_SPEED = 250 / 360 * umath.pi * WHEEL_DIAMETER  # mm/s

# Names of the dpad directions, for debug printing.
DIRECTION_NAMES = {
    1: "Forward",
    2: "Forward / Right",
    3: "Right",
    4: "Reverse / Right",
    5: "Reverse",
    6: "Reverse / Left",
    7: "Left",
    8: "Forward / Left",
}

# Targets for the switch (function-select) motor, in degrees:
# 0: Blade up/down.
# 90: Ripper.
# 180: Ladder.
# 270: Blade tilt.
SWITCH_TARGETS = {
    Button.X: 0,
    Button.A: 90,
    Button.Y: 180,
    Button.B: 270,
}

# Initialize variables.
left_end = 0
right_end = 0
switch_calibrated = False

async def main1():
    # This main task will handle driving and the motors that power
    # the function and switch mechanisms.
    left.control.limits(acceleration=2500)
    right.control.limits(acceleration=2500)
    print_counter = 0
    active_direction = 0
    left_start = left.angle()
    right_start = right.angle()
    while True:
        await wait(1)
        pressed = controller.buttons.pressed()
        # Only Forward (1), Right (3), Reverse (5), and Left (7) drive
        # the robot. Any other dpad tap (the diagonals) is ignored
        # entirely, as if the dpad were untouched.
        direction = controller.dpad()
        if direction not in (1, 3, 5, 7):
            direction = 0
        # The dpad direction selects which way we drive. Releasing the
        # dpad (direction 0) does not reset the distance, so inching
        # ahead in the same direction with several short presses still
        # adds up. Only pressing an actual different direction resets it.
        if direction and direction != active_direction:
            active_direction = direction
            left_start = left.angle()
            right_start = right.angle()
            print("Direction: {0}".format(DIRECTION_NAMES[direction]))
        # Print to the debug screen every 500 ms, measured since the
        # current direction was first selected. For Left/Right (pivot
        # turns), print the angle the robot turned. Otherwise, print
        # the distance driven.
        print_counter += 1
        if print_counter >= 500:
            print_counter = 0
            left_delta = left.angle() - left_start
            right_delta = right.angle() - right_start
            if active_direction in (3, 7):
                wheel_angle = abs(left_delta - right_delta) / 2
                # During a pivot turn, each wheel traces an arc around
                # the robot's center, which is TRACK_WIDTH / 2 away.
                # Scale the wheel's own rotation by the ratio of wheel
                # diameter to track width to get the robot's rotation.
                angle_turned = wheel_angle * WHEEL_DIAMETER / TRACK_WIDTH
                print("Angle turned: {0:.1f} deg".format(angle_turned))
            else:
                average_angle = (left_delta + right_delta) / 2
                distance = average_angle / 360 * umath.pi * WHEEL_DIAMETER / 10
                print("Distance driven: {0:.1f} cm".format(distance))
            # Also print the raw motor angle for the function and
            # switch motors, not converted to anything else, but only
            # while their corresponding controller buttons are pressed.
            if Button.RB in pressed or Button.LB in pressed:
                print("Function angle: {0} deg".format(function.angle()))
            if (Button.X in pressed or Button.A in pressed
                    or Button.Y in pressed or Button.B in pressed):
                print("Switch angle: {0} deg".format(switch.angle()))
        # Use the bumpers for the function motor: drive at fixed power
        # while held, stop immediately on release.
        if Button.RB in pressed:
            function.dc(100)
        elif Button.LB in pressed:
            function.dc(-100)
        else:
            function.stop()
        # Use X/A/Y/B for the switch motor, the same way as the
        # bumpers: drive at fixed power, toward that button's target
        # angle, while held, and stop immediately on release. Only
        # once main2() has finished calibrating it, so we don't issue
        # conflicting commands to the same motor during calibration.
        if switch_calibrated:
            switch_button = None
            for button in SWITCH_TARGETS:
                if button in pressed:
                    switch_button = button
                    break
            if switch_button is not None:
                target = SWITCH_TARGETS[switch_button]
                switch.dc(100 if target > switch.angle() else -100)
            else:
                switch.stop()
        # Use the direction pad for driving.
        if direction == 1:
            # Forward. Use the drive base so the gyro keeps us
            # driving straight.
            drivebase.drive(DRIVE_SPEED, 0)
        elif direction == 3:
            # Right
            left.run(50)
            right.run(-50)
        elif direction == 5:
            # Reverse. Use the drive base so the gyro keeps us
            # driving straight.
            drivebase.drive(-DRIVE_SPEED, 0)
        elif direction == 7:
            # Left
            left.run(-50)
            right.run(50)
        else:
            # Nothing (or an ignored diagonal tap), so stop.
            drivebase.stop()

async def main2():
    global right_end, left_end, switch_calibrated
    # This task calibrates the switch (function-select) gearbox by
    # finding its start and end stops. After that, X/A/Y/B in main1()
    # take over.
    await switch.run_until_stalled(500, Stop.COAST, 50)
    right_end = switch.angle()
    await switch.run_until_stalled(-500, Stop.COAST, 50)
    left_end = switch.angle()
    switch.reset_angle((left_end + 270 - right_end) / 2)
    switch_calibrated = True


async def main():
    await multitask(main1(), main2())

run_task(main())