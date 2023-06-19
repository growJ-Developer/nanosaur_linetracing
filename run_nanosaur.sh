PS_NAME=ros_humble

xhost +

docker stop $PS_NAME 2>/dev/null
docker rm $PS_NAME 2>/dev/null

cat /proc/device-tree/model > /tmp/nv_jetson_model

docker run -it --privileged \
--runtime nvidia \
--env="QT_X11_NO_MITSHM=1" \
-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
-v /dev:/dev:rw \
-v /home/jetson/Robot_Programming/nanosaur_linetracing:/ws \
-v /tmp/argus_socket:/tmp/argus_socket \
-v /etc/enctune.conf:/etc/enctune.conf \
-v /etc/nv_tegra_release:/etc/nv_tegra_release \
-v /tmp/nv_jetson_model:/tmp/nv_jetson_model \
-e DISPLAY=$DISPLAY \
--hostname $(hostname) \
--group-add dialout \
--user root \
--network host \
--shm-size 4096m \
--name $PS_NAME addps5012/ros:humble_nano bash
