import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from cv2 import aruco

class ArucoMarkerPublisher(Node):
    def __init__(self):
        super().__init__('aruco_marker_publisher')
        self.image_pub1 = self.create_publisher(Image, 'sky_aruco', 10)
        self.image_pub2 = self.create_publisher(Image, 'hand_aruco', 10)
        self.image_pub3 = self.create_publisher(Image, 'chest_aruco', 10)
        self.image_sub1 = self.create_subscription(Image, 'sky_camera', self.image_callback1, 10)
        self.image_sub2 = self.create_subscription(Image, 'hand_camera', self.image_callback2, 10)
        self.image_sub3 = self.create_subscription(Image, 'chest_camera', self.image_callback3, 10)
        self.bridge = CvBridge()
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.aruco_params = aruco.DetectorParameters_create()

    def image_callback1(self, msg):
        self.process_and_publish_image(msg, self.image_pub1)

    def image_callback2(self, msg):
        self.process_and_publish_image(msg, self.image_pub2)

    def image_callback3(self, msg):
        self.process_and_publish_image(msg, self.image_pub3)

    def process_and_publish_image(self, msg, publisher):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            corners, ids, _ = aruco.detectMarkers(cv_image, self.aruco_dict, parameters=self.aruco_params)
            cv_image_with_markers = aruco.drawDetectedMarkers(cv_image.copy(), corners, ids)
            output_image = self.bridge.cv2_to_imgmsg(cv_image_with_markers, encoding='bgr8')
            publisher.publish(output_image)
        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")

def main(args=None):
    rclpy.init(args=args)
    aruco_marker_publisher = ArucoMarkerPublisher()
    rclpy.spin(aruco_marker_publisher)
    aruco_marker_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
