## Part 4: Configure ALL Devices with IP-Configuration. Verify IPv4 Connectivity

### PC in Subnet A:
* IP Address: 172.16.10.129
* Subnet Mask: 255.255.255.192
* Default Gateway: 172.16.10.190

### RouterBoston

RouterBoston(config)# interface f0/0
RouterBoston(config-if)# ip address 172.16.10.190 255.255.255.192
RouterBoston(config-if)# no shutdown
RouterBoston(config-if)# exit
RouterBoston(config)# int s0/0
RouterBoston(config-if)# ip address 172.16.10.193 255.255.255.252
RouterBoston(config-if)# no shutdown
RouterBoston(config-if)# exit

### RouterBuffalo

RouterBuffalo(config)# interface f0/0
RouterBuffalo(config-if)# ip address 172.16.10.126 255.255.255.128
RouterBuffalo(config-if)# no shutdown
RouterBuffalo(config-if)# exit
RouterBuffalo(config)# int s0/0
RouterBuffalo(config-if)# ip address 172.16.10.194 255.255.255.252
RouterBuffalo(config-if)# no shutdown
RouterBuffalo(config-if)# exit

### SwitchBoston

SwitchBoston(config)# interface VLAN1
SwitchBoston(config-if)# ip address 172.16.10.130 255.255.255.192
SwitchBoston(config-if)# no shutdown
SwitchBoston(config-if)# exit
SwitchBoston(config)# ip default-gateway 172.16.10.190

### SwitchBuffalo

SwitchBuffalo(config)# interface VLAN1
SwitchBuffalo(config-if)# ip address 172.16.10.2 255.255.255.128
SwitchBuffalo(config-if)# no shutdown
SwitchBuffalo(config-if)# exit
SwitchBuffalo(config)# ip default-gateway 172.16.10.126

## Verify

### PC in Subnet A

Ping the default gateway (RouterBoston): ping 172.16.10.190

### RouterBoston

Verify IP addresses: show ip interface brief
Ping SwitchBoston: ping 172.16.10.130
Ping RouterBuffalo (s0/0 interface): ping 172.16.10.194

### RouterBuffalo

Verify IP addresses: show ip interface brief
Ping SwitchBuffalo: ping 172.16.10.2
Ping RouterBoston (s0/0 interface): ping 172.16.10.193

### SwitchBoston

Verify IP addresses: show ip interface brief
Ping RouterBoston: ping 172.16.10.190

### SwitchBuffalo

Verify IP addresses: show ip interface brief
Ping RouterBuffalo: ping 172.16.10.126

