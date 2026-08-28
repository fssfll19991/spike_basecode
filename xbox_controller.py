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
left_attachement = Motor(Port.C, Direction.CLOCKWISE)
right_attachement = Motor(Port.D, Direction.CLOCKWISE)
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

async def main1():
    # This main task will handle driving and the motors that power
    # the left and right attachements.
    left.control.limits(acceleration=2500)
    right.control.limits(acceleration=2500)
    print_counter = 0
    active_direction = 0
    left_start = left.angle()
    right_start = right.angle()
    last_drive_value = None
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
            # Don't print distance/angle while the left or right
            # attachement is being operated, and don't print it again
            # if it hasn't changed since the last time.
            using_other_motor = (Button.RB in pressed or Button.LB in pressed
                                  or Button.X in pressed or Button.B in pressed)
            if not using_other_motor:
                left_delta = left.angle() - left_start
                right_delta = right.angle() - right_start
                if active_direction in (3, 7):
                    wheel_angle = abs(left_delta - right_delta) / 2
                    # During a pivot turn, each wheel traces an arc
                    # around the robot's center, which is
                    # TRACK_WIDTH / 2 away. Scale the wheel's own
                    # rotation by the ratio of wheel diameter to track
                    # width to get the robot's rotation.
                    drive_value = round(wheel_angle * WHEEL_DIAMETER / TRACK_WIDTH, 1)
                    if drive_value != last_drive_value:
                        last_drive_value = drive_value
                        print("Angle turned: {0:.1f} deg".format(drive_value))
                else:
                    average_angle = (left_delta + right_delta) / 2
                    drive_value = round(average_angle / 360 * umath.pi * WHEEL_DIAMETER / 10, 1)
                    if drive_value != last_drive_value:
                        last_drive_value = drive_value
                        print("Distance driven: {0:.1f} cm".format(drive_value))
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

async def attachment_stepper(motor, label, positive_button, negative_button):
    # While the button is held, step the motor 5 degrees, pause
    # 100 ms, and repeat until it's released. A quick tap results in
    # a single 5 degree step.
    while True:
        pressed = controller.buttons.pressed()
        if positive_button in pressed:
            await motor.run_angle(500, 5, Stop.HOLD, wait=True)
            print("{0} angle: {1} deg".format(label, motor.angle()))
            await wait(100)
        elif negative_button in pressed:
            await motor.run_angle(500, -5, Stop.HOLD, wait=True)
            print("{0} angle: {1} deg".format(label, motor.angle()))
            await wait(100)
        else:
            await wait(1)

async def main():
    await multitask(
        main1(),
        attachment_stepper(left_attachement, "Left attachement", Button.RB, Button.LB),
        attachment_stepper(right_attachement, "Right attachement", Button.X, Button.B),
    )

run_task(main())