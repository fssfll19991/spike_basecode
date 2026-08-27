import umath

from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
left = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right = Motor(Port.F, Direction.CLOCKWISE)
function = Motor(Port.C, Direction.CLOCKWISE)
switch = Motor(Port.D, Direction.CLOCKWISE)
controller = XboxController()

# Wheel size, used to convert motor angle to distance driven.
WHEEL_DIAMETER = 55.5  # mm

# Distance between the centers of the left and right wheels, used to
# convert wheel angle to the angle the robot itself turned during a
# pivot turn.
TRACK_WIDTH = 80  # mm

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

# Initialize variables.
left_end = 0
right_end = 0
busy_switching = 1

async def switch_function(number):
    global busy_switching
    await wait(1)
    # This function takes care of moving the motor to positions 0, 1, 2, or 3:

    # 0: Blade up/down.
    # 1: Ripper.
    # 2: Ladder.
    # 3: Blade tilt.

    # First, indicate that we are going to be busy switching.
    busy_switching = 1
    for count in range(5):
        await wait(1)
        # Go to the target angle. But give up if it takes more
        # than 2 seconds, which means it's stuck for now.
        await multitask(switch.run_target(750, number * 90, Stop.COAST), wait(2000), race=True)
        # Let's check if we're on target.
        if abs(switch.angle() - number * 90) <= 10:
            # We are close to the target angle.
            # so we can exit this repeating loop.
            break
        # Otherwise, we're not done yet, so we must be stuck.
        # Let's wiggle the motor around to try to get it unstuck.
        switch.track_target(0)
        await wait(1000)
        switch.track_target(270)
        await wait(1000)
        switch.stop()
    # We're no longer busy switching, so we can drive again.
    busy_switching = 0

async def main1():
    # This main task will handle driving and the motor
    # that powers (not switches) the function gearbox.
    left.control.limits(acceleration=2500)
    right.control.limits(acceleration=2500)
    print_counter = 0
    active_direction = 0
    left_start = left.angle()
    right_start = right.angle()
    while True:
        await wait(1)
        # The dpad direction selects which way we drive. Releasing the
        # dpad (direction 0) does not reset the distance, so inching
        # ahead in the same direction with several short presses still
        # adds up. Only pressing an actual different direction resets it.
        direction = controller.dpad()
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
        if busy_switching:
            # If we are currently busy switching the function, we stop
            # driving and powering the function motor to be safe.
            left.stop()
            right.stop()
            function.stop()
        else:
            # Otherwise drive the motors based on the buttons that are pressed.
            # Use the bumpers for the function motor.
            if Button.RB in controller.buttons.pressed():
                function.dc(100)
            elif Button.LB in controller.buttons.pressed():
                function.dc(-100)
            else:
                function.stop()
            # Use the direction pad for driving.
            if controller.dpad() == 1:
                # Forward
                left.run(250)
                right.run(250)
            elif controller.dpad() == 2:
                # Forward / Right
                right.stop()
                left.run(250)
            elif controller.dpad() == 3:
                # Right
                left.run(250)
                right.run(-250)
            elif controller.dpad() == 4:
                # Reverse / Right
                right.run(-250)
                left.stop()
            elif controller.dpad() == 5:
                # Reverse
                left.run(-250)
                right.run(-250)
            elif controller.dpad() == 6:
                # Reverse / Left
                left.run(-250)
                right.stop()
            elif controller.dpad() == 7:
                # Left
                left.run(-250)
                right.run(250)
            elif controller.dpad() == 8:
                # Forward / Left
                right.run(250)
                left.stop()
            else:
                # Nothing, so stop.
                left.stop()
                right.stop()

async def main2():
    global right_end, left_end
    # This task will handle the motor that switches the function gearbox.
    # First it resets the gearbox by finding the start and end stops.
    await switch.run_until_stalled(500, Stop.COAST, 50)
    right_end = switch.angle()
    await switch.run_until_stalled(-500, Stop.COAST, 50)
    left_end = switch.angle()
    switch.reset_angle((left_end + 270 - right_end) / 2)
    await switch_function(0)
    # Now we run the main loop of operating the switch.
    while True:
        await wait(1)
        # Wait for the center switch to be pressed.
        while not any(controller.buttons.pressed()):
            await wait(1)
        # Then select the function based on which other button is pressed.
        if Button.X in controller.buttons.pressed():
            # Blade up/down function.
            await switch_function(0)
            while Button.X in controller.buttons.pressed():
                await wait(1)
        elif Button.A in controller.buttons.pressed():
            # Ripper function.
            await switch_function(1)
            while Button.A in controller.buttons.pressed():
                await wait(1)
        elif Button.Y in controller.buttons.pressed():
            # Ladder function.
            await switch_function(2)
            while Button.Y in controller.buttons.pressed():
                await wait(1)
        elif Button.B in controller.buttons.pressed():
            # Blade tilt function.
            await switch_function(3)
            while Button.B in controller.buttons.pressed():
                await wait(1)
        else:
            # No other button pressed, so don't switch.
            pass


async def main():
    await multitask(main1(), main2())

run_task(main())