import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fireproof/Documents/ros_demo/py_pubsub/install/py_pubsub'
