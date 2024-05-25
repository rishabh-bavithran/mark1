import RPi.GPIO as GPIO
import time


servo_pin_1 = 18
servo_pin_2 = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_1, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)

p = GPIO.PWM(servo_pin_1, 50)
q = GPIO.PWM(servo_pin_2, 50)

p.start(0)
q.start(0)

counter = 0
while(counter< 100):
    counter = counter + 1
    print(counter)
    p.ChangeDutyCycle(counter)
    q.ChangeDutyCycle(counter)
    time.sleep(0.1)


p.ChangeDutyCycle(7.5)
q.ChangeDutyCycle(7.5)
time.sleep(200)

# counter = 12
# while(counter> 8):
#     counter = counter - 0.1
#     print(counter)
#     p.ChangeDutyCycle(counter)
#     q.ChangeDutyCycle(counter)
#     time.sleep(1)

# p.ChangeDutyCycle(0)
# q.ChangeDutyCycle(0)
    

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
