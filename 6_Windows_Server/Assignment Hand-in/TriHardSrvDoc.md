# Filserver - TriHardSrv1


## Location
TriHard Office, PepegaStreet 25

## Hardware
- Processor: 2x AMD EPYC™ 72F3 Processor 8-core 3.70GHz 256MB Cache (180W)
- RAM: 	8x 16GB PC4-23400 2933MHz DDR4 ECC RDIMM
- Boot drive: 960GB Micron 5400 PRO Series 2.5" SATA 6.0Gb/s Solid State Drive
- Storage drives: 12x 10TB SAS 3.0 12.0Gb/s 7200RPM - 3.5" - Ultrastar™ DC HC330 (512e)
    - For more hardware info see FileServerSpecs.pdf
## Configuration
- OS: Windows Server 2022 Server Standard
- Build: 21H2 20348.169
- Display Resolution: 1024x768

## Network Configuration:
  - IP adress 10.6.68.176
  - Subnet mask: 255.255.255
  - Default gateway 10.6.68.1
  - Preferred DNS server: 10.6.68.175
  - Alternate DNS server: *None*


## Storage Services
- Storage Pool 1
  - Name: RAID5
  - Physical Disks: 12x 10TB

## Roles and Features
  - Print Server

## Shared Folders

### \\TriHardSrv1\Private$
- Share Permissions:
  - Authenticated Users: Full Control
- NTFS Permissions:
  - System (Allow)
    - Full Control
    - This folder, subfolders and files
  - Administrators (Allow)
    - Full Control
    - This folder, subfolders and files
  - Creator Owner (Allow)
    - Full Control
    - Subfolders and fils only
  - Domain users (Allow)
    - Traverse folder / execute file
    - List folder / read data
    - Create folders / append data
    - This folder only
  - TriHardIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - TriHardAccounting (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardSales (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardConsultant (Allow)
    - Read, write & execute
    - This folder, subfolders and files


### \\TriHardSrv1\TriHardShared
- Share Permissions:
  - Authenticated Users: Full Control
- NTFS Permissions:
  - System (Allow)
    - Full Control
    - This folder, subfolders and files
  - Administrators (Allow)
    - Full Control
    - This folder, subfolders and files
  - Creator Owner (Allow)
    - Full Control
    - Subfolders and fils only
  - TriHardIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - TriHardAccounting (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardSales (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardConsultant (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\TriHardSrv1\TriHardAccounting
- Share Permissions:
  - Authenticated Users: Full Control
- NTFS Permissions:
  - System (Allow)
    - Full Control
    - This folder, subfolders and files
  - Administrators (Allow)
    - Full Control
    - This folder, subfolders and files
  - Creator Owner (Allow)
    - Full Control
    - Subfolders and fils only
  - TriHardIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - TriHardAccounting (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files


### \\TriHardSrv1\TriHardConsultant
- Share Permissions:
  - Authenticated Users: Full Control
- NTFS Permissions:
  - System (Allow)
    - Full Control
    - This folder, subfolders and files
  - Administrators (Allow)
    - Full Control
    - This folder, subfolders and files
  - Creator Owner (Allow)
    - Full Control
    - Subfolders and fils only
  - TriHardIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - TriHardConsultant (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\TriHardSrv1\TriHardSales
- Share Permissions:
  - Authenticated Users: Full Control
- NTFS Permissions:
  - System (Allow)
    - Full Control
    - This folder, subfolders and files
  - Administrators (Allow)
    - Full Control
    - This folder, subfolders and files
  - Creator Owner (Allow)
    - Full Control
    - Subfolders and fils only
  - TriHardIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - TriHardSales (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - TriHardManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\TriHardSrv1\TriHardManagement
- Share Permissions:
  - Authenticated Users: Full Control
- NTFS Permissions:
  - System (Allow)
    - Full Control
    - This folder, subfolders and files
  - Administrators (Allow)
    - Full Control
    - This folder, subfolders and files
  - Creator Owner (Allow)
    - Full Control
    - Subfolders and fils only
  - TriHardIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - TriHardManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\TriHardSrv1\TriHardIT
- Share Permissions:
  - Authenticated Users: Full Control
- NTFS Permissions:
  - System (Allow)
    - Full Control
    - This folder, subfolders and files
  - Administrators (Allow)
    - Full Control
    - This folder, subfolders and files
  - Creator Owner (Allow)
    - Full Control
    - Subfolders and fils only
  - TriHardIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - TriHardManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

## Mapped Drives

1. TriHardAccounting
  - Folder: \\TriHardSrv1\TriHardAccounting
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) TriHardAccounting 
    - OR (Security Group) TriHardManagement
    - OR (Security Group) TriHardIT
2. TriHardConsultant
  - Folder: \\TriHardSrv1\TriHardConsultant
  - Mount as Network Drive
  - Drive letter: First available from I:
    - Item Level Targeting: 
    - (Security Group) TriHardConsultant
    - OR (Security Group) TriHardManagement
    - OR (Security Group) TriHardIT
3. TriHardSales
  - Folder: \\TriHardSrv1\TriHardSales
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) TriHardSales
    - OR (Security Group) TriHardManagement
    - OR (Security Group) TriHardIT
4. TriHardManagement
  - Folder: \\TriHardSrv1\TriHardManagement
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) TriHardSales
    - OR (Security Group) TriHardManagement
    - OR (Security Group) TriHardIT
5. TriHardIT
  - Folder: \\TriHardSrv1\TriHardIT
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) TriHardSales
    - OR (Security Group) TriHardManagement
    - OR (Security Group) TriHardIT
1. TriHardShared  
  - Folder: \\TriHardSrv1\TriHardShared
  - Mount as Network Drive
  - Drive letter: First available from S:
   - Item Level Targeting: 
    - (Security Group) TriHardAccounting
    - OR (Security Group) TriHardConsultant
    - OR (Security Group) TriHardSales
    - OR (Security Group) TriHardManagement
    - OR (Security Group) TriHardIT

## Printers
1. TriHardPrinter
  - IP: 10.6.68.178
  - Deploy with GPO Per Machine to respective OU
  - Driver: Microsoft OpenXPS Class Driver 2
  - Noteable Permissions:
    - Allow TriHardEmployees: Print
    - Allow TriHardIT: Print, Manage this printer, Manage documents
    - Allow Creator Owner: Manage documents





