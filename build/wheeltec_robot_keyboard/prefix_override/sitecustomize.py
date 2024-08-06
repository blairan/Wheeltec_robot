import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sunrise/wheeltec_robot_ws/install/wheeltec_robot_keyboard'
