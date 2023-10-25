import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that you've connected the servo to
servo_pin = 18

# Set up the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object with a frequency of 50Hz (standard for servos)
pwm = GPIO.PWM(servo_pin, 50)

# Start the PWM with a duty cycle of 0 (full anti-clockwise)
pwm.start(0)

while True:
    # Rotate the servo in one direction (e.g., clockwise)
    pwm.ChangeDutyCycle(7.5)  # Middle position (stop)
    time.sleep(5)  # Pause for 2 seconds

    #pwm.ChangeDutyCycle(2.5)  # Full anti-clockwise
    #time.sleep(2)  # Pause for 2 seconds

    # Rotate the servo in the other direction (e.g., counter-clockwise)
    """pwm.ChangeDutyCycle(7.5)  # Middle position (stop)
    time.sleep(2)  # Pause for 2 seconds

    pwm.ChangeDutyCycle(12.5)  # Full clockwise
    time.sleep(2)  # Pause for 2 seconds"""
pwm.stop()
GPIO.cleanup()
