from gpiozero import MotionSensor, Robot
from time import sleep

# Setup
pir = MotionSensor(17)  # GPIO17 is connected to OUT pin of PIR sensor
robot = Robot(left=(17, 18), right=(22, 23))  # Update with your motor pins

print("Waiting for motion...")

while True:
    pir.wait_for_motion()
    print("Motion detected! Moving...")
    robot.forward()
    sleep(2)
    robot.stop()
    print("Stopped. Waiting for next motion.")
