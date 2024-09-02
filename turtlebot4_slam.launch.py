from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{'use_sim_time': True}]
        ),
        Node(
            package='turtlebot4_node',
            executable='turtlebot4_node',
            name='turtlebot4_node',
            output='screen'
        )
    ])
