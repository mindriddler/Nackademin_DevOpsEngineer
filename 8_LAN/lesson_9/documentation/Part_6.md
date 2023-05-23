## Configure OSPFv2 Routing

### RouterBoston

RouterBoston(config)# no ip route 172.16.10.0 255.255.255.128 s0/0

RouterBoston(config)# router ospf 1
RouterBoston(config-router)# network 172.16.10.128 0.0.0.63 area 0
RouterBoston(config-router)# network 172.16.10.192 0.0.0.3 area 0

RouterBoston# show ip route

In the routing table output, look for the "O" (OSPF) prefix next to the routes. 

### RouterBuffalo

RouterBuffalo(config)# no ip route 172.16.10.128 255.255.255.192 s0/0

RouterBuffalo(config)# router ospf 1
RouterBuffalo(config-router)# network 172.16.10.0 0.0.0.127 area 0
RouterBuffalo(config-router)# network 172.16.10.192 0.0.0.3 area 0

RouterBuffalo# show ip route

In the routing table output, look for the "O" (OSPF) prefix next to the routes. 
