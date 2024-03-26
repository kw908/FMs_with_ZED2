import os
import launch
from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration
import launch_ros

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='robot_localization').find('robot_localization')

    robot_localization_node = launch_ros.actions.Node(
       package='robot_localization',
       executable='ekf_node',
       name='ekf_filter_node',
       output='screen',
       parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}])
    return LaunchDescription([launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='False',
                                description='Flag to enable use_sim_time'),
                                robot_localization_node
    ])