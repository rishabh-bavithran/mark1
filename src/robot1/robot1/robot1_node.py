#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led_pin = 24
GPIO.setup(led_pin, GPIO.OUT)


# Define the GPIO pin that you've connected the servo to

#RIGHT SERVO
servo_pin_right = 18
GPIO.setup(servo_pin_right, GPIO.OUT)
p = GPIO.PWM(servo_pin_right, 50)
#p.start(10)

#LEFT SERVO
servo_pin_left = 12
GPIO.setup(servo_pin_left, GPIO.OUT)
q = GPIO.PWM(servo_pin_left, 50)
#p.start(10)
p.start(10)
q.start(10)

#DUTY CYCLES FOR MOTIONS
halt_dc = 0
forward_dc_rm = 8
forward_dc_lm = 12
reverse_dc_rm = 12
reverse_dc_lm = 8
right_turn_dc_rm = 12
right_turn_dc_lm = 12
left_turn_dc_rm = 8
left_turn_dc_lm = 8 
forward_test_rm = 0 
forward_test_lm = 0


from example_interfaces.msg import Int64
from example_interfaces.msg import String
class Robot1Node(Node):
    
    def __init__(self):
        super().__init__("robot1_node")
        self.get_logger().info("robot1 node has started")
        self.create_subscription(Int64, "led_control", 
                                 self.led_control_callback, 10)
        self.create_subscription(String, "robot1_movement", 
                                 self.callback_robot1_movement,10)
        
    
    #TESTING PURPOSES
    def led_control_callback(self, msg):
        #led_state = Int64()
        led_state = msg.data
        # if led_state == 1:
        #     self.get_logger().info(str(led_state))
        #     GPIO.output(led_pin, GPIO.HIGH)
        # elif led_state == 0:
        #     GPIO.output(led_pin, GPIO.LOW)
        #     self.get_logger().info(str(led_state))
        forward_test_rm = forward_dc_rm + led_state
        forward_test_lm = forward_dc_lm - led_state
        


    def callback_robot1_movement(self,msg):
        robot_movement = msg.data 
        if robot_movement == "forward":

            self.forward_movement()
        elif robot_movement == "right":
            self.right_turn()
        elif robot_movement == "left":
            self.left_turn()
        elif robot_movement == "reverse":
            self.reverse_movement()
        elif robot_movement == "halt":
            self.halt_movement()

    def forward_movement(self):
        self.get_logger().info("Moving Forward")
        p.ChangeDutyCycle(forward_test_rm)
        q.ChangeDutyCycle(forward_test_lm)
        #Moving forward CODE 

    def right_turn(self):
        self.get_logger().info("Taking right turn")
        p.ChangeDutyCycle(right_turn_dc_rm)
        q.ChangeDutyCycle(right_turn_dc_lm)
        #Taking RIGHT Code

    def left_turn(self):
        self.get_logger().info("Taking left turn")
        p.ChangeDutyCycle(left_turn_dc_rm)
        q.ChangeDutyCycle(left_turn_dc_lm)
        #Taking LEFT TURN CODE

    def reverse_movement(self):
        self.get_logger().info("Moving Reverse")
        p.ChangeDutyCycle(reverse_dc_rm)
        q.ChangeDutyCycle(reverse_dc_lm)
        #TAKING REVERSE CODE

    def halt_movement(self):
        self.get_logger().info("Halted Movement")
        p.ChangeDutyCycle(halt_dc)
        q.ChangeDutyCycle(halt_dc)
        #p.stop()
        #q.stop()
        #HALTING CODE
    

def main(args=None):
    rclpy.init(args=args)
    node = Robot1Node()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=="__main__":
    main()


