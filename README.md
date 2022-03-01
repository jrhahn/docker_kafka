# docker_kafka

I. Set up the broker
1. cd docker
2. ./build_image.sh
3. ./run_image.sh  

II. Run producer and client
1. cd python
2. virtualenv venv
3. source venv/bin/activate
4. pip install -r requirements
5. python producer.py
6. python consumer.py
