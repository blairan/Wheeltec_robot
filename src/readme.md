### 1.Turn_on_wheeltec_robot[机器人底层驱动(不含雷達,相機)]

`ros2 launch turn_on_wheeltec_robot turn_on_wheeltec_robot.launch.py`

### **2.啟動所有傳感器和機器人底盤**

`ros2 launch turn_on_wheeltec_robot wheeltec_sensors.launch.py`

### **3.相機串流到網頁伺服器[網路監控]**

啟動相機

`ros2 launch turn_on_wheeltec_robot wheeltec_camera.launch.py`

啟動web_video_server

`ros2 run web_video_server web_video_server`

- 打開網頁，輸入192.168.xxx.xxx:8080

### 4.Wheeltec_robot_slam[2D 建图]

#### 4-1-1 gmapping 建图

＃啟動slam_gmapping

`ros2 launch slam_gmapping slam_gmapping.launch.py`

4-1-2 slam_toolbox 建图

`ros2 launch wheeltec_slam_toolbox online_async_launch.py`

#### 4-1-3 cartographer 建图

`ros2 launch wheeltec_cartographer cartographer.launch.py`

#### 4-3 運動控制

#开启键盘控制
`ros2 run wheeltec_robot_keyboard wheeltec_keyboard`

#### 4-4 保存地圖

`ros2 run nav2_map_server map_saver_cli –f ~/wheeltec_ros2/src/wheeltec_robot_nav2/map/house`

#### 5. Wheeltec_robot_rtab[RTAB 建图导航]

相機使用astra pro或astra pro plus,須修改wheeltec_camera.launch.py裡的參數

`ros2 launch wheeltec_robot_rtab wheeltec_slam_rtab.launch.py`
