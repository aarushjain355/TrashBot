import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, QoSHistoryPolicy

class Lidar_Handler(Node):

    def __init__(self):
        super().__init__("lidar_handler")
        self.slam_publisher_ = self.create_publisher(LaserScan, "/scan", qos_profile=QoSProfile(depth=70))
        self.simulation_subscriber_ = self.create_subscription(LaserScan, "/scan/simulation", self.lidar_callback, qos_profile=QoSProfile(depth=70))
        self.simulation_subscriber_
        self.rate = self.create_rate(20)

    def lidar_callback(self, msg):
        msg.header.frame_id = "base_link"
        self.slam_publisher_.publish(msg)
        self.rate.sleep()

def main(args=None):
    rclpy.init(args=args)
    node = Lidar_Handler()
    rclpy.spin(node)
    node.destory_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

    