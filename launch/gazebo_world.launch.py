import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
 
def generate_launch_description():
 
  # Obtenemos la ruta del paquete Gazebo ROS.
  pkg_gazebo_ros = FindPackageShare(package='gazebo_ros').find('gazebo_ros')   
  
  # Obtenemos la ruta de instalación de nuestro paquete.
  pkg_install_path = FindPackageShare(package='gazebo_world_launch').find('gazebo_world_launch')
 
  # Obtenemos la ruta del archivo world, que está almacenado en la
  # carpeta worlds del paquete.
  world_file = 'table.world'
  world_path = os.path.join(pkg_install_path, 'worlds', world_file)
   
  # Obtenemos la ruta de la capeta models que es donde se encuentra
  # la información del modelo que es empleado en nuestro archivo world
  gazebo_models_path = os.path.join(pkg_install_path, 'models')
  os.environ["GAZEBO_MODEL_PATH"] = gazebo_models_path
   
  # Creamos una acción para ejecutar el archivo gzserver.launch.py,
  # que se encuentra dentro de la carpeta launch del paquete
  # Gazebo Ros. Lo que hace es arrancar el servidor de Gazebo
  # cargando el archivo world que pasamos como argumento.
  start_gazebo_server_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
    launch_arguments={'world': world_path}.items())
 
  # Creamos una acción para ejecutar el archivo gzclient.launch.py,
  # que se encuentra dentro de la carpeta launch del paquete
  # Gazebo Ros. Lo que hace es arrancar el cliente de Gazebo, que  
  # es la interfaz gráfica.
  start_gazebo_client_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')),
    )
 
  # Devolvemos un objeto LaunchDescription con las acciones que queremos realizar.
  return LaunchDescription([
    start_gazebo_server_cmd,
    start_gazebo_client_cmd
    ])