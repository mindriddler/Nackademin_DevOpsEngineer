# Filserver - PepeLaughSrv1


## Location
PepeLaugh Office, PogChampStreet 76

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
  - IP adress 10.6.68.177
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

### \\PepeLaughSrv1\Private$
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
  - PepeLaughIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - PepeLaughAccounting (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughSales (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughConsultant (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\PepeLaughSrv1\PepeLaughShared
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
  - PepeLaughIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - PepeLaughAccounting (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughSales (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughConsultant (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\PepeLaughSrv1\PepeLaughAccounting
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
  - PepeLaughIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - PepeLaughAccounting (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files


### \\PepeLaughSrv1\PepeLaughConsultant
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
  - PepeLaughIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - PepeLaughConsultant (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\PepeLaughSrv1\PepeLaughSales
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
  - PepeLaughIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - PepeLaughSales (Allow)
    - Read, write & execute
    - This folder, subfolders and files
  - PepeLaughManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\PepeLaughSrv1\PepeLaughManagement
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
  - PepeLaughIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - PepeLaughManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

### \\PepeLaughSrv1\PepeLaughIT
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
  - PepeLaughIT (Allow)
    - Full Control
    - This folder, subfolders and files
  - PepeLaughManagement (Allow)
    - Read, write & execute
    - This folder, subfolders and files

## Mapped Drives

1. PepeLaughAccounting
  - Folder: \\PepeLaughSrv1\PepeLaughAccounting
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) PepeLaughAccounting 
    - OR (Security Group) PepeLaughManagement
    - OR (Security Group) PepeLaughIT
2. PepeLaughConsultant
  - Folder: \\PepeLaughSrv1\PepeLaughConsultant
  - Mount as Network Drive
  - Drive letter: First available from I:
    - Item Level Targeting: 
    - (Security Group) PepeLaughConsultant
    - OR (Security Group) PepeLaughManagement
    - OR (Security Group) PepeLaughIT
3. PepeLaughSales
  - Folder: \\PepeLaughSrv1\PepeLaughSales
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) PepeLaughSales
    - OR (Security Group) PepeLaughManagement
    - OR (Security Group) PepeLaughIT
4. PepeLaughManagement
  - Folder: \\PepeLaughSrv1\PepeLaughManagement
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) PepeLaughSales
    - OR (Security Group) PepeLaughManagement
    - OR (Security Group) PepeLaughIT
5. PepeLaughIT
  - Folder: \\PepeLaughSrv1\PepeLaughIT
  - Mount as Network Drive
  - Drive letter: First available from I:
  - Item Level Targeting: 
    - (Security Group) PepeLaughSales
    - OR (Security Group) PepeLaughManagement
    - OR (Security Group) PepeLaughIT
1. PepeLaughShared  
  - Folder: \\PepeLaughSrv1\PepeLaughShared
  - Mount as Network Drive
  - Drive letter: First available from S:
   - Item Level Targeting: 
    - (Security Group) PepeLaughAccounting
    - OR (Security Group) PepeLaughConsultant
    - OR (Security Group) PepeLaughSales
    - OR (Security Group) PepeLaughManagement
    - OR (Security Group) PepeLaughIT

## Printers
1. PepeLaughPrinter
  - IP: 10.6.68.179
  - Deploy with GPO Per Machine to respective OU
  - Driver: Microsoft OpenXPS Class Driver 2
  - Noteable Permissions:
    - Allow PepeLaughEmployees: Print
    - Allow PepeLaughIT: Print, Manage this printer, Manage documents
    - Allow Creator Owner: Manage documents





