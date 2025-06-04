from ipaddress import *

for i in range(1,33):
    n = ip_network(f'130.140.241.137/{i}',0)
    print(i, n.network_address)
