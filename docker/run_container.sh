docker run --rm --name kafka -it -p 9092:9092 -e HOST_IP=$(hostname -I | awk '{print $1}') supercoder3000:kafka
