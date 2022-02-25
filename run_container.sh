docker run --rm --name kafka -it -e DISPLAY=$DISPLAY  -p 9092:9092 --privileged -v /tmp/.X11-unix:/tmp/.X11-unix supercoder3000:kafka
