import RPi.GPIO as GPIO
import time


servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
p = GPIO.PWM(servo_pin, 50)
p.start(10)

counter = 8
while(counter< 12):
    counter = counter + 0.1
    print(counter)
    p.ChangeDutyCycle(counter)
    time.sleep(0.5)


p.stop()
time.sleep(5)
p.start(counter)
counter = 8
while(counter< 12):
    counter = counter + 0.1
    print(counter)
    p.ChangeDutyCycle(counter)
    time.sleep(0.5)


    

"""
counter = 1
while(counter<50):
    counter += 1
    p.ChangeDutyCycle(counter)
    time.sleep(0.1)
    print(counter)"""
#time.sleep(100)
#p.ChangeDutyCycle(10)
#time.sleep(200)
"""p.stop()

p.start(50)
p.ChangeDutyCycle(0)
time.sleep(2)
p.stop()"""
"""counter = 0
while True:
    counter = counter + 1
    print(counter)
    print("\n")
    p.ChangeDutyCycle(7.5)
    time.sleep(2)
    #p.stop()
    #p.ChangeDutyCycle(2.5)

    print("stopped")
    time.sleep(2)
    
    #GPIO.cleanup()
    #p.start(7.5)
    time.sleep(2)

    p.ChangeDutyCycle(5)
    print("restart")

    time.sleep(2)

    #p.stop()
    #p.ChangeDutyCycle(2.5)

    print("stopped")
    time.sleep(2)
    #p.start(7.5)

    #GPIO.cleanup()
    p.ChangeDutyCycle(7.5)  # You may need to adjust this value for your servo
    time.sleep(5)
    p.ChangeDutyCycle(20.5)
    time.sleep(5)
    p.ChangeDutyCycle(11.5)  # You may need to adjust this value for your servo"""

GPIO.cleanup()
