from launch import LaunchDescription
from launch_ros.actions import Node
from nav2_common.launch import RewrittenYaml

def generate_launch_description():
    namespace = 'turtlebot4'
    param_substitutions = {
        'use_sim_time': 'True'
    }

    configured_params = RewrittenYaml(
        source_file='nav2_params.yaml',
        root_key=namespace,
        param_rewrites=param_substitutions,
        convert_types=True)

    return LaunchDescription([
        Node(
            package='nav2_controller',
            executable='controller_server',
            output='screen',
            parameters=[configured_params]
        ),
        Node(
            package='nav2_planner',
            executable='planner_server',
            output='screen',
            parameters=[configured_params]
        ),
        Node(
            package='nav2_recoveries',
            executable='recoveries_server',
            output='screen',
            parameters=[configured_params]
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'autostart': True},
                {'node_names': ['map_server', 'amcl', 'controller_server',
                                'planner_server', 'recoveries_server']}
            ]
        )
    ])
