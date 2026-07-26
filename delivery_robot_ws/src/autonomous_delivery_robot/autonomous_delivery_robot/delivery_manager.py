#!/usr/bin/env python3

import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose

from autonomous_delivery_robot.delivery_tasks import (
    DELIVERY_TASKS,
    HOME_POSITION
)


class DeliveryManager(Node):

    def __init__(self):

        super().__init__('delivery_manager')

        # ==========================================
        # NAV2 ACTION CLIENT
        # ==========================================

        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            'navigate_to_pose'
        )

        self.get_logger().info(
            '================================'
        )

        self.get_logger().info(
            'Autonomous Delivery Manager Started'
        )

        self.get_logger().info(
            '================================'
        )

        # ==========================================
        # HOME POSITION
        # ==========================================

        self.home_x = HOME_POSITION['x']
        self.home_y = HOME_POSITION['y']

        # ==========================================
        # DELIVERY TASK QUEUE
        # ==========================================

        self.tasks = DELIVERY_TASKS.copy()

        self.current_task = None

        # Start mission after initialization
        self.start_delivery()


    # ==================================================
    # CREATE NAV2 GOAL
    # ==================================================

    def create_goal(self, x, y):

        goal = NavigateToPose.Goal()

        goal.pose = PoseStamped()

        # Map coordinate frame
        goal.pose.header.frame_id = 'map'

        # Current ROS time
        goal.pose.header.stamp = (
            self.get_clock().now().to_msg()
        )

        # Target position
        goal.pose.pose.position.x = float(x)
        goal.pose.pose.position.y = float(y)

        # No rotation
        goal.pose.pose.orientation.x = 0.0
        goal.pose.pose.orientation.y = 0.0
        goal.pose.pose.orientation.z = 0.0
        goal.pose.pose.orientation.w = 1.0

        return goal


    # ==================================================
    # START DELIVERY MISSION
    # ==================================================

    def start_delivery(self):

        self.get_logger().info(
            'Waiting for Nav2 navigation server...'
        )

        if not self.nav_client.wait_for_server(
            timeout_sec=10.0
        ):

            self.get_logger().error(
                'Nav2 navigation server not available!'
            )

            return

        self.get_logger().info(
            'Nav2 navigation server connected'
        )

        # Start first delivery task
        self.send_next_task()


    # ==================================================
    # SEND NEXT DELIVERY TASK
    # ==================================================

    def send_next_task(self):

        # Check if tasks are finished
        if len(self.tasks) == 0:

            self.get_logger().info(
                '================================'
            )

            self.get_logger().info(
                'All delivery tasks completed'
            )

            self.get_logger().info(
                'Returning robot to home position'
            )

            self.get_logger().info(
                '================================'
            )

            self.return_home()

            return


        # Get next task
        self.current_task = self.tasks.pop(0)

        task_name = self.current_task['name']
        task_x = self.current_task['x']
        task_y = self.current_task['y']


        self.get_logger().info(
            '================================'
        )

        self.get_logger().info(
            f'Starting Delivery Task: {task_name}'
        )

        self.get_logger().info(
            f'Target X: {task_x}'
        )

        self.get_logger().info(
            f'Target Y: {task_y}'
        )

        self.get_logger().info(
            '================================'
        )


        # Create navigation goal
        goal = self.create_goal(
            task_x,
            task_y
        )


        self.get_logger().info(
            'Sending navigation goal...'
        )


        # Send goal to Nav2
        future = self.nav_client.send_goal_async(
            goal
        )


        future.add_done_callback(
            self.goal_response_callback
        )


    # ==================================================
    # NAV2 GOAL RESPONSE
    # ==================================================

    def goal_response_callback(self, future):

        try:

            goal_handle = future.result()

        except Exception as e:

            self.get_logger().error(
                f'Error sending navigation goal: {e}'
            )

            return


        # Check goal acceptance
        if not goal_handle.accepted:

            self.get_logger().error(
                'Delivery goal rejected!'
            )

            self.get_logger().error(
                'Check map, localization, and Nav2.'
            )

            return


        self.get_logger().info(
            'Delivery goal accepted'
        )


        # Wait for navigation result
        result_future = (
            goal_handle.get_result_async()
        )


        result_future.add_done_callback(
            self.delivery_result_callback
        )


    # ==================================================
    # DELIVERY RESULT
    # ==================================================

    def delivery_result_callback(self, future):

        result = future.result()

        status = result.status


        # Nav2 status 4 = SUCCEEDED
        if status == 4:

            self.get_logger().info(
                '================================'
            )

            self.get_logger().info(
                f"{self.current_task['name']} Reached!"
            )

            self.get_logger().info(
                'Package Delivered Successfully'
            )

            self.get_logger().info(
                '================================'
            )


            # Wait before next task
            self.get_logger().info(
                'Waiting 5 seconds before next delivery...'
            )


            time.sleep(5)


            # Start next task
            self.send_next_task()


        else:

            self.get_logger().error(
                '================================'
            )

            self.get_logger().error(
                f'Delivery failed!'
            )

            self.get_logger().error(
                f'Nav2 Status Code: {status}'
            )

            self.get_logger().error(
                '================================'
            )


    # ==================================================
    # RETURN ROBOT HOME
    # ==================================================

    def return_home(self):

        self.get_logger().info(
            'Returning robot to Home Position'
        )


        # Create home goal
        goal = self.create_goal(
            self.home_x,
            self.home_y
        )


        # Send home goal
        future = self.nav_client.send_goal_async(
            goal
        )


        future.add_done_callback(
            self.home_response_callback
        )


    # ==================================================
    # HOME GOAL RESPONSE
    # ==================================================

    def home_response_callback(self, future):

        try:

            goal_handle = future.result()

        except Exception as e:

            self.get_logger().error(
                f'Error returning home: {e}'
            )

            return


        if not goal_handle.accepted:

            self.get_logger().error(
                'Return Home goal rejected!'
            )

            return


        self.get_logger().info(
            'Return Home goal accepted'
        )


        # Wait for result
        result_future = (
            goal_handle.get_result_async()
        )


        result_future.add_done_callback(
            self.home_result_callback
        )


    # ==================================================
    # HOME RESULT
    # ==================================================

    def home_result_callback(self, future):

        result = future.result()

        status = result.status


        # Nav2 status 4 = SUCCEEDED
        if status == 4:

            self.get_logger().info(
                '================================'
            )

            self.get_logger().info(
                'Robot Successfully Returned Home'
            )

            self.get_logger().info(
                'Delivery Mission Completed!'
            )

            self.get_logger().info(
                '================================'
            )


        else:

            self.get_logger().error(
                '================================'
            )

            self.get_logger().error(
                f'Robot failed to return home'
            )

            self.get_logger().error(
                f'Nav2 Status Code: {status}'
            )

            self.get_logger().error(
                '================================'
            )


# ==================================================
# MAIN FUNCTION
# ==================================================

def main(args=None):

    rclpy.init(args=args)

    node = DeliveryManager()


    try:

        rclpy.spin(node)


    except KeyboardInterrupt:

        node.get_logger().info(
            'Delivery Manager Stopped'
        )


    finally:

        node.destroy_node()

        if rclpy.ok():

            rclpy.shutdown()


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

if __name__ == '__main__':

    main()
