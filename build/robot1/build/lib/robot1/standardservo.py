import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the servo control
servo_pin = 18

# Set the PWM frequency (Hz)
pwm_frequency = 50

# Initialize the GPIO pin for servo control
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object
pwm = GPIO.PWM(servo_pin, pwm_frequency)

# Start PWM with a duty cycle of 0 (servo at 0 degrees)
pwm.start(0)

try:
    while True:
        # Set the servo angle (0 to 180 degrees)
        angle = 90  # Change this value to set the desired angle
        duty_cycle = angle / 18.0 + 2.5
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(1)  # Delay to allow the servo to reach the desired angle

except KeyboardInterrupt:
    # Stop PWM and cleanup GPIO on Ctrl+C
    pwm.stop()
    GPIO.cleanup()
