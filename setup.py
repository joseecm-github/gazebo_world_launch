import os
from glob import glob
from setuptools import setup

package_name = 'gazebo_world_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),

        # Las siguientes líneas incluyen las rutas de los archivos que
        # existen en las carpetas que hemos añadido al paquete para que
        # se incluyan en la instalación. 
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share', package_name, 'models/ground_plane'), glob('models/ground_plane/*.*')),
        (os.path.join('share', package_name, 'models/sun'), glob('models/sun/*.*')),
        (os.path.join('share', package_name, 'models/table'), glob('models/table/*.*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

