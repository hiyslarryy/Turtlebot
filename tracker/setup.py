from setuptools import find_packages, setup

package_name = 'tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hiyslarry',
    maintainer_email='hiyslarry@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'face_detection = tracker.face_detection:main',  # Adjust this line as needed
            'people_detection = tracker.people_detection:main',  
            'stop_detection = tracker.stop_detection:main'
        ],
    },
)
