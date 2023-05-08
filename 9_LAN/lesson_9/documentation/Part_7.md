## Part 7: Configure VLANs on Buffalo Switch

### SwitchBoston

SwitchBoston(config)# vlan 10
SwitchBoston(config-vlan)# name Administration
SwitchBoston(config-vlan)# exit
SwitchBoston(config)# interface range FastEthernet0/5-0/10
SwitchBoston(config-if-range)# switchport mode access
SwitchBoston(config-if-range)# switchport access vlan 10
SwitchBoston(config-if-range)# exit
SwitchBoston(config)# vlan 20
SwitchBoston(config-vlan)# name Engineering
SwitchBoston(config-vlan)# exit
SwitchBoston(config)# interface range FastEthernet0/11-0/16
SwitchBoston(config-if-range)# switchport mode access
SwitchBoston(config-if-range)# switchport access vlan 20
SwitchBoston(config-if-range)# exit
SwitchBoston(config)# interface FastEthernet0/24
SwitchBoston(config-if)# switchport mode trunk
(?)SwitchBoston(config-if)# switchport trunk allowed vlan 10,20
SwitchBoston(config-if)# exit

### SwitchBuffalo

SwitchBuffalo(config)# vlan 10
SwitchBuffalo(config-vlan)# name Administration
SwitchBuffalo(config-vlan)# exit
SwitchBuffalo(config)# interface range FastEthernet0/5-0/10
SwitchBuffalo(config-if-range)# switchport mode access
SwitchBuffalo(config-if-range)# switchport access vlan 10
SwitchBuffalo(config-if-range)# exit
SwitchBuffalo(config)# vlan 20
SwitchBuffalo(config-vlan)# name Engineering
SwitchBuffalo(config-vlan)# exit
SwitchBuffalo(config)# interface range FastEthernet0/11-0/16
SwitchBuffalo(config-if-range)# switchport mode access
SwitchBuffalo(config-if-range)# switchport access vlan 20
SwitchBuffalo(config-if-range)# exit
SwitchBuffalo(config)# interface FastEthernet0/24
SwitchBuffalo(config-if)# switchport mode trunk
(?)SwitchBuffalo(config-if)# switchport trunk allowed vlan 10,20
SwitchBuffalo(config-if)# exit

## Verify

SwitchBuffalo# show vlan brief
SwitchBuffalo# show interfaces trunk

SwitchBoston# show vlan brief
SwitchBoston# show interfaces trunk

