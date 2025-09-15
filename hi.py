ip = '192.168.1.1'
mask = '255.255.255.0'
from math import ceil
from conv import *

# Convert ip and subnet mask to list of bytes
ip_list = ip.split('.')
mask_list = mask.split('.')
print(ip_list,mask_list)

# Convert those lists to binary for AND operation
ip_binary = []
mask_binary = []
for binary in ip_list:
    ip_binary.append(toBinary(int(binary)))
for binary in mask_list:
    mask_binary.append(toBinary(int(binary)))

print(ip_binary,mask_binary)

# Now we need to perform the AND operation
NetworkIP = ['','','','']
