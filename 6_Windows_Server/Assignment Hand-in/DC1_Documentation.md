# Primary Domain Controllant - DC1

## Location
TriHard Office, PepegaStreet 25

## Hardware
  - RAM: 2x 32GB 4800MT/s
  - Processor: AMD EPYC 9124 3.0GHz, 16C/32T, 64M Cache (200W) DDR5-4800
  - Hard Drives: 480GB SSD SATA Read Intensive 6Gbps 512 2.5in Hot-plug AG Drive,3.5in HYB CARR, 1 DWPD
  - PSU: Dual, Hot-Plug, Fully Redundant Power Supply (1+1), 800W, Mixed Mode 
    - For more hardware info see DC_specs.pdf
## Configuration
  - OS: Windows Server 2022 Server Standard
  - Build: 21H2 20348.169
  - Display Resolution: 1024x768

## Network Configuration:
  - IP adress 10.6.68.175
  - Subnet mask: 255.255.255.0
  - Default gateway 10.6.68.1
  - Preferred DNS server: 127.0.0.1
  - Alternate DNS server: *None*
## Roles and Features
  - DNS
  - AD DS
  - GPMC

## DNS
- Zone name: ItsCrap.io
  - Static Records:
    - dc1.itscrap.io 10.6.68.175
  - Conditional Forwarder:
    - yven.se 10.6.68.190

## AD DS
- Domain Name: ItsCrap.io
- NetBIOS Domain Name: ITSCRAP

## OU-Structure
![OU-Structure](OU-Structure.png "Image")
### OU-Delegated-Control

PepeLaugh
```powershell
PepeLaughIT -> PepeLaugh.ItsCrap.io
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Create, delete and manage groups
  - Modify the membership of a group
```
```powershell
PepeLaughManagement -> Users.PepeLaugh.ItsCrap.io
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Modify the membership of a group
```
TriHard
```powershell
TriHardIT -> TriHard.ItsCrap.io
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Create, delete and manage groups
  - Modify the membership of a group
```
```powershell
TriHardManagement -> Users.TriHard.ItsCrap.io
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Modify the membership of a group
```
## Groups
[DL]: Domain Local Group [G]: Global Group
```powershell
[DL] PepeLaughEmployees -> Groups.PepeLaugh.ItsCrap.io
  - [G] PepeLaughIT
  - [G] PepeLaughManagement
  - [G] PepeLaughAccounting
  - [G] PepeLaughSales
  - [G] PepeLaughConsults
```
```powershell
[DL] TriHardEmployees -> Groups.TriHard.ItsCrap.io
  - [G] TriHardIT
  - [G] TriHardManagement
  - [G] TriHardAccounting
  - [G] TriHardSales
  - [G] TriHardConsultants
```
```powershell
[DL] Employees -> ResourceGroups.ItsCrap.io
  - PepeLaughEmployees
  - TriHardEmployees
```

## Group Policy Objects (GPO)
See GPOReportsAll.html
