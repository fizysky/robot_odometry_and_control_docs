***************
ROS Integration
***************

Requirements
************

Each wheel velocity and steer angle is publish in ros messeges of type 
``mobie_robots_kinematic/VelocityWheel`` and calcuation are done base on input linear and 
angular velocity passed in ros messeges of type ``geometry_msgs/Twist``.

Odometry topic and transform are publish only when information about each wheel welocity are 
avaliable in ros topic of type *mobie_robots_kinematic/VelocityWheel*

By defaul this package:

* subscribe to:

  * /*robot_name*/cmd_vel
  
    * ``geometry_msgs/Twist``
  * /*robot_name*/wheel_feedback
  
    * ``mobie_robots_kinematic/VelocityWheel``

* publish

  * /*robot_name*/velocity
  
    * ``mobie_robots_kinematic/VelocityWheel``
  * /*robot_name*/odom 
  
    * ``nav_msgs/Odometry``

Each of names can be customized in configuration file.

Custom messege
**************

This package provide customized messeges that helps organize data in ros network

* ``mobie_robots_kinematic/VelocityWheel``
  
    * mobie_robots_kinematic/motor[] values
* ``mobie_robots_kinematic/VelocityWheel``

    * uint32 ID
    * float32 LinVelocity
    * float32 AngVelocity
    * float32 steerAngle 
