#### 旭日x3 SDK下的Tros

# 1.姿态检测

### 配置tros.b环境

`source /opt/tros/humble/setup.bash`

从tros.b的安装路径中拷贝出运行示例需要的配置文件。(只須執行一次)

`cp -r /opt/tros/{TROS\_DISTRO}/lib/mono2d/body/detection/config/  .`

### 配置USB摄像头

`export CAM_TYPE=usb`

### 启动launch文件

`ros2 launch hobot_falldown_detection hobot_falldown_detection.launch.py`

---

# 2.小车手势控制

### 配置tros.b环境

`source /opt/tros/humble/setup.bash`

从tros.b的安装路径中拷贝出运行示例需要的配置文件。(只須執行一次)

`cp -r /opt/tros/${TROS_DISTRO}/lib/mono2d_body_detection/config/ . `

`cp -r /opt/tros/${TROS_DISTRO}/lib/hand_lmk_detection/config/ . `

`cp -r /opt/tros/${TROS_DISTRO}/lib/hand_gesture_detection/config/ .`

### 配置usb摄像头

`export CAM_TYPE=usb`

### 启动launch文件

`ros2 launch gesture_control gesture_control.launch.py`

---


# 3.小车人体跟随

`source /opt/ros/humble/setup.bash`


### 配置tros.b环境

`source /opt/tros/humble/setup.bash`

### 从tros.b的安装路径中拷贝出运行示例需要的配置文件。

`cp -r /opt/tros/**\${TROS\_DISTRO}**/lib/mono2d\_body\_detection/config/  .`

### 配置USB摄像头

`export CAM_TYPE=usb`

### 启动launch文件

`ros2 launch body\_tracking body\_tracking\_without\_gesture.launch.py`
