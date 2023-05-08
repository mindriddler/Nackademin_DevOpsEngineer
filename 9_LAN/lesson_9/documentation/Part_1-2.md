##Part 1: Develop the IPv4 Address Scheme

### Subnet A 55 hosts
* 172.16.10.128 Subnet ID
* 172.16.10.129-190 Hosts
* 172.16.10.191 Broadcast
* 255.255.255.192 Subnetmask
* 0.0.0.63 Wildcardmask

### Subnet B 2 hosts
* 172.16.10.192 Subnet ID
* 172.16.10.193-194 Hosts
* 172.16.10.195 Broadcast
* 255.255.255.252 Subnetmask
* 0.0.0.3 Wildcardmask

### Subnet C 110 hosts
* 172.16.10.0 Subnet ID
* 172.16.10.1-126 Hosts
* 172.16.10.127 Broadcast
* 255.255.255.128 Subnetmask
* 0.0.0.127 Wildcardmask

### Subnet A
* Number of subnet bits: 2
* New subnet mask (decimal): 255.255.255.192
* Maximum usable hosts per subnet: 62
* Subnet ID: 172.16.10.128
* First IP Host address: 172.16.10.129
* Last IP Host address: 172.16.10.190

### Subnet B
* Number of subnet bits: 2
* New subnet mask (decimal): 255.255.255.252
* Maximum usable hosts per subnet: 2
* Subnet ID: 172.16.10.192
* First IP Host address: 172.16.10.193
* Last IP Host address: 172.16.10.194

### Subnet C
* Number of subnet bits= 1
* New subnet mask (decimal): 255.255.255.128
* Maximum usable hosts per subnet: 126
* Subnet ID: 172.16.10.0
* First IP Host address: 172.16.10.1
* Last IP Host address: 172.16.10.126

## Part 2: Assign devices with IPv4 addresses

### Host computers (first IP address in the subnet)
PC Subnet A: 172.16.10.129
PCs Default gateway: 172.16.10.190

### Switch Subnet A (second IP address in the subnet)
Switch Subnet A: 172.16.10.130

### Routers (last IP address in the subnet for LAN)
Router Boston Subnet A LAN interface f0/0: 172.16.10.190
Router Buffalo Subnet C LAN interface f0/0: 172.16.10.126

Router Boston Subnet B WAN interface (first IP address in the subnet for WAN) s0/0: 172.16.10.193
Router Buffalo Subnet B WAN interface (last IP address in the subnet for WAN) s0/0: 172.16.10.194

VLAN 1 (native VLAN) for the Buffalo switch is the second available IP address for Subnet C LAN: 172.16.10.2
VLAN 1 (native VLAN) for the Boston switch on Subnet A is the third available IP address: 172.16.10.131

## Connect all necessary cabling:

Connect the PC on Subnet A to the newly added switch on Subnet A.
Connect the newly added switch on Subnet A to the Router Boston Subnet A LAN interface f0/0.
Connect Router Boston Subnet B WAN interface s0/0 to Router Buffalo Subnet B WAN interface s0/0.
Connect Router Buffalo Subnet C LAN interface f0/0 to the Buffalo switch.
