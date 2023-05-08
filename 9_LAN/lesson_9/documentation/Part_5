## Part 5: Configure Static Routing with IPv4

### RouterBoston

RouterBoston(config)# ip route 172.16.10.0 255.255.255.128 s0/0

### RouterBuffalo

RouterBuffalo(config)# ip route 172.16.10.128 255.255.255.192 s0/0

## Test connectivity between both LANs by pinging the devices in the other LAN:

### PC(Subnet A) > SwitchBuffalo
ping 172.16.10.2

### SwitchBuffalo > PC(Subnet A
ping 172.16.10.129

## Verify in the routing tables that static routing is activated:

### RouterBoston
RouterBoston# show ip route

### RouterBuffalo
RouterBuffalo# show ip route

In the routing table output, look for the "S" (Static) prefix next to the routes you configured. 
