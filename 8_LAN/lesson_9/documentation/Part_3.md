## Router Boston

Router> enable
Router# conf t
Router(config)# hostname RouterBoston
RouterBoston(config)# enable secret cisco

RouterBoston(config)# interface serial0/0
RouterBoston(config-if)# description Link to RouterBuffalo (Subnet B)

RouterBoston(config)# line console 0
RouterBoston(config-line)# password class
RouterBoston(config-line)# login
RouterBoston(config-line)# exit
RouterBoston(config)# line vty 0 4
RouterBoston(config-line)# password class
RouterBoston(config-line)# login
RouterBoston(config-line)# exit
RouterBoston(config)# line aux 0
RouterBoston(config-line)# password class
RouterBoston(config-line)# login
RouterBoston(config-line)# exit

RouterBoston(config)# service password-encryption
RouterBoston(config)# banner motd #Authorized personnel only#

RouterBoston# show running-config
(?)RouterBoston# copy running-config startup-config

## Router Buffalo

Router> enable
Router# conf t
Router(config)# hostname RouterBuffalo
RouterBuffalo(config)# enable secret cisco

RouterBuffalo(config)# interface serial0/0
RouterBuffalo(config-if)# description Link to RouterBoston (Subnet B)

RouterBuffalo(config)# line console 0
RouterBuffalo(config-line)# password class
RouterBuffalo(config-line)# login
RouterBuffalo(config-line)# exit
RouterBuffalo(config)# line vty 0 4
RouterBuffalo(config-line)# password class
RouterBuffalo(config-line)# login
RouterBuffalo(config-line)# exit
RouterBuffalo(config)# line aux 0
RouterBuffalo(config-line)# password class
RouterBuffalo(config-line)# login
RouterBuffalo(config-line)# exit

RouterBuffalo(config)# service password-encryption
RouterBuffalo(config)# banner motd #Authorized personnel only#

RouterBuffalo# show running-config
(?)RouterBuffalo# copy running-config startup-config

## Switch Boston

Switch> enable
Switch# conf t
Switch(config)# hostname SwitchBoston
SwitchBoston(config)# enable secret cisco

SwitchBoston(config)# line console 0
SwitchBoston(config-line)# password class
SwitchBoston(config-line)# login
SwitchBoston(config-line)# exit
SwitchBoston(config)# line vty 0 4
SwitchBoston(config-line)# password class
SwitchBoston(config-line)# login
SwitchBoston(config-line)# exit
SwitchBoston(config)# line aux 0
SwitchBoston(config-line)# password class
SwitchBoston(config-line)# login
SwitchBoston(config-line)# exit

SwitchBoston(config)# service password-encryption
SwitchBoston(config)# banner motd #Authorized personnel only#

SwitchBoston# show running-config
(?)SwitchBoston# copy running-config startup-config

## Switch Buffalo

Switch> enable
Switch# conf t
Switch(config)# hostname SwitchBuffalo
SwitchBuffalo(config)# enable secret cisco

SwitchBuffalo(config)# line console 0
SwitchBuffalo(config-line)# password class
SwitchBuffalo(config-line)# login
SwitchBuffalo(config-line)# exit
SwitchBuffalo(config)# line vty 0 4
SwitchBuffalo(config-line)# password class
SwitchBuffalo(config-line)# login
SwitchBuffalo(config-line)# exit
SwitchBuffalo(config)# line aux 0
SwitchBuffalo(config-line)# password class
SwitchBuffalo(config-line)# login
SwitchBuffalo(config-line)# exit

SwitchBuffalo(config)# service password-encryption
SwitchBuffalo(config)# banner motd #Authorized personnel only#

SwitchBuffalo# show running-config
(?)SwitchBuffalo# copy running-config startup-config
