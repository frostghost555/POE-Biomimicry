#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain = Brain()

# Robot configuration code for 4 Motors
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)

drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)

# Sensor configuration: Bumper Switch plugged into 3-Wire Port A
bumper_a = Bumper(brain.three_wire_port.a)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()

def play_vexcode_sound(sound_name):
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

wait(200, MSEC)
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
#   Project:      Biomimicry Silly Walks Crawler (4-Motor)
#   Author:       PLTW Engineering & Student
#   Description:  Crawls continuously using a 4-motor linkage motion
#                 until the front bumper hits an obstacle, then stops,
#                 flashes the screen red, prints an alert, 
#                 and emits an insect warning buzz.
# 
# ------------------------------------------

# Set drivetrain speed
drivetrain.set_drive_velocity(25, PERCENT)

# Loop: Drive forward while the bumper switch is NOT pressed
while not bumper_a.pressing():
    drivetrain.drive(FORWARD)
    wait(20, MSEC)  # Small delay to allow processing

# Stop moving once the bumper switch contacts an obstacle
drivetrain.stop()

# Visual Alarm: Flash the Brain screen red and output status text
brain.screen.set_fill_color(Color.RED)
brain.screen.draw_rectangle(0, 0, 480, 240)
print("BUG ALERT: Obstacle hit!")

# Biomimicry Defense Buzz: Play a 3-pitch insect warning sound
brain.play_note(1, 7, 100)
wait(50, MSEC)
brain.play_note(1, 8, 100)
wait(50, MSEC)
brain.play_note(1, 9, 150)
