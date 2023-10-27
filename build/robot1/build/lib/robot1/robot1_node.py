#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led_pin = 24

# Define the GPIO pin that you've connected the servo to
servo_pin = 18

GPIO.setup(led_pin, GPIO.OUT)

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
        if led_state == 1:
            self.get_logger().info(str(led_state))
            GPIO.output(led_pin, GPIO.HIGH)
        elif led_state == 0:
            GPIO.output(led_pin, GPIO.LOW)
            self.get_logger().info(str(led_state))

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

    def forward_movement(self):
        self.get_logger().info("Moving Forward")
        #Moving forward CODE 

    def right_turn(self):
        self.get_logger().info("Taking right turn")
        #Taking RIGHT Code

    def left_turn(self):
        self.get_logger().info("Taking left turn")
        #Taking LEFT TURN CODE

    def reverse_movement(self):
        self.get_logger().info("Moving Reverse")
        #TAKING REVERSE CODE

    

def main(args=None):
    rclpy.init(args=args)
    node = Robot1Node()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=="__main__":
    main()