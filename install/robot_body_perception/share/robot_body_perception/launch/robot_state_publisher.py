from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.substitutions import Command
import os

def generate_launch_description():

    package_name = 'robot_body_perception'
    urdf_file_path = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        'lidar_chassis_frames.urdf'
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            'urdf_file',
            default_value=urdf_file_path,
            description='Path to the urdf file'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description' : Command(['xacro ', LaunchConfiguration('urdf_file')])

            }]
        ),

        Node(
            package='robot_body_perception',
            executable='wrapper',
            name='wrapper',
        )
    ]) 