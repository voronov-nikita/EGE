from ipaddress import *

count:int = 0

for ip in ip_network('145.92.137.88/255.255.240.0'):
    if bin(int(ip))[2:].count("1") % 2 == 0:
        count += 1
    print(ip)
print(count)

# Для задания с определением адреса сети
ip = "145.92.137.88".split(".")
mask = "255.255.240.0".split(".")

answer = []

for i in range(len(ip)):
    answer.append(str(int(ip[i]) & int(mask[i])))
    
print('.'.join(answer))