topic record commands: ros2 bag record -o single_node_1 /sensing/lidar/concatenated/pointcloud /clock /parameter_events

Rewrite: launch file: the topic name of input point cloud, frame id
         src file: the frame id are changed from map to base_link
         src file: delete the check of subscribe node
