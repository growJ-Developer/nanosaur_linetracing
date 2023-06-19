import os
import yaml
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch import LaunchDescription, LaunchContext
from launch.conditions import IfCondition
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    # nanosaur_hardware 패키지 내부의 nanosaur 노드 실행
    nanosaur_node = Node(
        package='nanosaur_hardware',
        executable='nanosaur',
        name='nanosaur',
        output='screen'
    )

    # image_pub 패키지 내부의 raw_image_pub.launch.py 실행
    image_pub_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            get_package_share_directory('image_pub'),
            '/launch/raw_image_pub.launch.py'
        ])
    )

    # teleop_twist_keyboard 패키지의 teleop_twist_keyboard 노드 실행
    """
    teleop_twist_keyboard_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        output='screen',
        remappings=[
            ('/nanosaur/cmd_vel', '/cmd_vel')
        ]
    )
    """

    # rover_line_follower 패키지의 rover_line_follower 노드 실행
    rover_line_follower_node = Node(
        package='rover_line_follower',
        executable='rover_line_follower',
        name='rover_line_follower',
        output='screen',
    )

    # 노드들을 그룹으로 묶어 실행
    nodes_group = GroupAction([
        nanosaur_node,
        image_pub_launch,
        #teleop_twist_keyboard_node,
        rover_line_follower_node
    ])

    return LaunchDescription([nodes_group])

# 런치 파일을 실행하는 엔트리 포인트입니다.
if __name__ == '__main__':
    ld = generate_launch_description()
    launch.actions.execute_action(ld)
