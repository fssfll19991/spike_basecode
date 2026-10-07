################################################################################
# mission_eight.py
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

def mission_eight(r: robot):
    print("Running Mission 8")
    # Your code goes here...
    r.robot.drive(450)
    r.robot.turn(50)
    r.robot.drive(460)
    r.robot.turn(-58)
    r.robot.drive(-20)
    r.robot.turn(23)
    r.robot.drive(-50)





################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

/* Complete Mission Sequence:
--------------------------------------------------

Step 1:
  Type: DRIVE
  Direction: Forward
  Distance: 44.9 cm
  Raw data: {'distance_cm': 44.9215, 'type': 'drive', 'direction': 1}

Step 2:
  Type: TURN
  Direction: Right
  Angle: 49.9 degrees
  Raw data: {'angle_deg': 49.90286, 'type': 'turn', 'direction': 3}

Step 3:
  Type: DRIVE
  Direction: Forward
  Distance: 46.6 cm
  Raw data: {'distance_cm': 46.56822, 'type': 'drive', 'direction': 1}

Step 4:
  Type: TURN
  Direction: Left
  Angle: 55.7 degrees
  Raw data: {'angle_deg': 55.66064, 'type': 'turn', 'direction': 7}

Step 5:
  Type: DRIVE
  Direction: Forward
  Distance: 2.9 cm
  Raw data: {'distance_cm': 2.93019, 'type': 'drive', 'direction': 1}

Step 6:
  Type: DRIVE
  Direction: Reverse
  Distance: -4.9 cm
  Raw data: {'distance_cm': -4.891722, 'type': 'drive', 'direction': 5}

Step 7:
  Type: TURN
  Direction: Left
  Angle: 10.2 degrees
  Raw data: {'angle_deg': 10.17001, 'type': 'turn', 'direction': 7}

Step 8:
  Type: TURN
  Direction: Right
  Angle: 33.5 degrees
  Raw data: {'angle_deg': 33.53641, 'type': 'turn', 'direction': 3}

Step 9:
  Type: DRIVE
  Direction: Reverse
  Distance: -6.0 cm
  Raw data: {'distance_cm': -6.029895, 'type': 'drive', 'direction': 5}

Step 10:
  Type: DRIVE
  Direction: Forward
  Distance: 1.0 cm
  Raw data: {'distance_cm': 0.9928741, 'type': 'drive', 'direction': 1}

Step 11:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 126 degrees
  Delta: +5 degrees
  Button: Button.RB
  Raw data: {'angle_deg': 126, 'delta': 5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.RB'}

Step 12:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 131 degrees
  Delta: +5 degrees
  Button: Button.RB
  Raw data: {'angle_deg': 131, 'delta': 5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.RB'}

Step 13:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 136 degrees
  Delta: +5 degrees
  Button: Button.RB
  Raw data: {'angle_deg': 136, 'delta': 5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.RB'}

Step 14:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 141 degrees
  Delta: +5 degrees
  Button: Button.RB
  Raw data: {'angle_deg': 141, 'delta': 5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.RB'}

Step 15:
  Type: TURN
  Direction: Left
  Angle: 23.4 degrees
  Raw data: {'angle_deg': 23.4032, 'type': 'turn', 'direction': 7}

Step 16:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 147 degrees
  Delta: +5 degrees
  Button: Button.RB
  Raw data: {'angle_deg': 147, 'delta': 5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.RB'}

Step 17:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 142 degrees
  Delta: -5 degrees
  Button: Button.LB
  Raw data: {'angle_deg': 142, 'delta': -5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.LB'}

Step 18:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 138 degrees
  Delta: -5 degrees
  Button: Button.LB
  Raw data: {'angle_deg': 138, 'delta': -5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.LB'}

Step 19:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 135 degrees
  Delta: -5 degrees
  Button: Button.LB
  Raw data: {'angle_deg': 135, 'delta': -5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.LB'}

Step 20:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 128 degrees
  Delta: -5 degrees
  Button: Button.LB
  Raw data: {'angle_deg': 128, 'delta': -5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.LB'}

Step 21:
  Type: ATTACHMENT
  Motor: Left attachement
  Target Angle: 122 degrees
  Delta: -5 degrees
  Button: Button.LB
  Raw data: {'angle_deg': 122, 'delta': -5, 'type': 'attachment', 'attachment': 'Left attachement', 'button': 'Button.LB'}

Step 22:
  Type: DRIVE
  Direction: Forward
  Distance: 13.9 cm
  Raw data: {'distance_cm': 13.85181, 'type': 'drive', 'direction': 1}

Step 23:
  Type: DRIVE
  Direction: Reverse
  Distance: -61.6 cm
  Raw data: {'distance_cm': -61.5582, 'type': 'drive', 'direction': 5}

Step 24:
  Type: TURN
  Direction: Left
  Angle: 13.2 degrees
  Raw data: {'angle_deg': 13.21164, 'type': 'turn', 'direction': 7}

Step 25:
  Type: TURN
  Direction: Right
  Angle: 87.4 degrees
  Raw data: {'angle_deg': 87.4129, 'type': 'turn', 'direction': 3}

Step 26:
  Type: DRIVE
  Direction: Reverse
  Distance: -50.7 cm
  Raw data: {'distance_cm': -50.6608, 'type': 'drive', 'direction': 5}

Step 27:
  Type: DRIVE
  Direction: Forward
  Distance: 4.7 cm
  Raw data: {'distance_cm': 4.722207, 'type': 'drive', 'direction': 1}

Step 28:
  Type: TURN
  Direction: Left
  Angle: 109.4 degrees
  Raw data: {'angle_deg': 109.4407, 'type': 'turn', 'direction': 7}

Step 29:
  Type: DRIVE
  Direction: Forward
  Distance: 12.1 cm
  Raw data: {'distance_cm': 12.13244, 'type': 'drive', 'direction': 1}

Step 30:
  Type: TURN
  Direction: Left
  Angle: 27.4 degrees
  Raw data: {'angle_deg': 27.38309, 'type': 'turn', 'direction': 7}

--------------------------------------------------
==================================================


=== STARTING PLAYBACK ===
Playing back 30 movements...
[PLAYBACK 1/30] Driving 44.9215 cm
[PLAYBACK 2/30] Turning 49.90286 deg (gyro)
[PLAYBACK 3/30] Driving 46.56822 cm
[PLAYBACK 4/30] Turning 55.66064 deg (gyro)
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/fll/repos/spike_basecode/.venv/lib64/python3.12/site-packages/pybricksdev/__main__.py", line 9, in <module>
    main()
  File "/home/fll/repos/spike_basecode/.venv/lib64/python3.12/site-packages/pybricksdev/cli/__init__.py", line 620, in main
    asyncio.run(subparsers.choices[args.tool].tool.run(args))
  File "/usr/lib64/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/home/fll/repos/spike_basecode/.venv/lib64/python3.12/site-packages/pybricksdev/cli/__init__.py", line 240, in run
    await hub.run(script_path, args.wait or args.stay_connected)
  File "/home/fll/repos/spike_basecode/.venv/lib64/python3.12/site-packages/pybricksdev/connections/pybricks.py", line 629, in run
    await self._wait_for_user_program_stop()
  File "/home/fll/repos/spike_basecode/.venv/lib64/python3.12/site-packages/pybricksdev/connections/pybricks.py", line 813, in _wait_for_user_program_stop
    is_running = await self.race_disconnect(user_program_running.get())
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fll/repos/spike_basecode/.venv/lib64/python3.12/site-packages/pybricksdev/connections/pybricks.py", line 374, in race_disconnect
    raise HubDisconnectError("disconnected during operation")
pybricksdev.connections.pybricks.HubDisconnectError: disconnected during operation
((.venv) ) ((.venv) ) ^C
((.venv) ) ((.venv) )
*/
