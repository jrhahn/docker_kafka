from os import system

_host_ip = system("hostname -I | awk '{print $1}'")

# bootstrap_servers = 'localhost:9092'
bootstrap_servers = f'{_host_ip}:9092'
topic = 'grid_search'
num_partitions = 2
