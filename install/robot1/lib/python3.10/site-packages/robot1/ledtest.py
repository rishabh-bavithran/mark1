import RPi
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#servo_pin = 18
led_pin = 18
#GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

import time

GPIO.output(led_pin, GPIO.HIGH)
print("LED ON NOW")
time.sleep(2)
GPIO.output(led_pin, GPIO.LOW)
time.sleep(2)
print("LED OFF NOW")

"""
p = GPIO.PWM(servo_pin, 100)
p.start(5)

p.ChangeDutyCycle(2.5)
time.sleep(5)
p.ChangeDutyCycle(11.5) # may need to be adjusted
time.sleep(5)
p.ChangeDutyCycle(20.5)
time.sleep(5)
p.ChangeDutyCycle(11.5) # may need to be adjusted

GPIO.cleanup()"""