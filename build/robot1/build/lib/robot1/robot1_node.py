#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
led_pin = 24
#GPIO.setup(led_pin, GPIO.OUT)

from example_interfaces.msg import Int64
class Robot1Node(Node):
    
    def __init__(self):
        super().__init__("robot1_node")
        self.get_logger().info("robot1 node has started")
        self.create_subscription(Int64, "led_control", self.led_control_callback, 10)

    def led_control_callback(self, msg):
        #led_state = Int64()
        led_state = msg.data
        if led_state == 1:
            self.get_logger().info(str(led_state))
            #GPIO.output(led_pin, GPIO.HIGH)
        elif led_state == 0:
            #GPIO.output(led_pin, GPIO.LOW)
            self.get_logger().info(str(led_state))

def main(args=None):
    rclpy.init(args=args)
    node = Robot1Node()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=="__main__":
    main()