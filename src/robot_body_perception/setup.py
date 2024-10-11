from setuptools import setup

package_name = 'robot_body_perception'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/robot_state_publisher.py']),
        ('share/' + package_name + '/urdf', ['urdf/lidar_chassis_frames.urdf']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vicky',
    maintainer_email='aarushjain33555@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wrapper = robot_body_perception.slam_toolbox_wrapper:main'
        ],
    },
)
