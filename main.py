#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

brain = Brain()

# 4-Motor Drivetrain on Ports 1–4
left_motor_a = Motor(Ports.PORT1, False)
left_motor_b = Motor(Ports.PORT3, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT2, True)
right_motor_b = Motor(Ports.PORT4, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)

drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 200, 173, 76, MM, 1)

wait(30, MSEC)

def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
initializeRandomSeed()

def play_vexcode_sound(sound_name):
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

wait(200, MSEC)
print("\033[2J")
#endregion VEXcode Generated Robot Configuration

# Set drivetrain speed
drivetrain.set_drive_velocity(25, PERCENT)

# Crawl forward for 5 seconds
drivetrain.drive(FORWARD)
wait(5, SECONDS)

# Stop moving
drivetrain.stop()

# Visual Alarm: Fill the VEX IQ Brain screen red and print alert
brain.screen.set_fill_color(Color.RED)
brain.screen.draw_rectangle(0, 0, 160, 108)
print("BUG ALERT: Crawl complete!")

# Biomimicry Defense Buzz: Play 3-pitch warning sound on the Brain's speaker
brain.play_note(1, 7, 100)
wait(50, MSEC)
brain.play_note(1, 8, 100)
wait(50, MSEC)
brain.play_note(1, 9, 150)
