## Network Fundamentals

* Switch
* Router
* WAP & Controller
* Firewall / IPS

### Switch

* Central connection point from devices plugging into the network
* Third generation device
* Packed with ASIC chips
* Typically 24 or 48 port
* Daisy-chain to gain more ports

A HUB is a dumb device
First there was HUBs, a device used to generate and repeat network signals
Works by sending out the packet to all ports
Which is bad performance since every other device is on the network is bothered and need to check the packet to see if it belongs to them and for security since anyone can sniff the packet

Then became Bridge
A bridge can learn what device is connected to what port by using MAC address (Media Access Control)
* MAC Address is a 12 digit Hexadecimal
* First 6 digits is the vendor ID
* Last 6 digits is the serial number
* MAC Address is burned into the NIC (Network Interface Card)

So the bridge can know what port the packet should go to

bridges are flawed because they are software based

ASIC = Application Specific Integrated Circuitry
* ASIC is a chip that is designed to do one thing and one thing only

Switches are bridges with ASIC chips
* Switches are hardware based
* Switches are faster
* Switches are more reliable
* Switches are more expensive

Switches has console ports for management and uplink ports for daisy chains (Cisco think it looks cleaner)

They also have SFP ports that can take modules to get extra ethernet ports or maybe fiber optic modules

Some switch has a feature called "Stackwise"
* Stackwise is a feature that allows you to connect multiple switches together to act as one switch
* This is done by using a special cable that connects the switches together
* This is done to increase performance and redundancy

Layer 2 switches puts MAC addresses into its CAM table (Content Addressable Memory)
* CAM table is a table that contains MAC addresses and what port they are connected to
* CAM table is also called a MAC table

Layer 3 switches puts IP addresses into its routing table

### Router

* Contains Networks
* Moves data between netoworks
* Connects dissimilar networks
* software-based, feature rich

Routers are layer 3 devices

Routers are used to connect different networks together
Routers are usually centralized
Routers are usually connected to switches

UNICAST message
* A message that is sent to one device

BROADCAST message
* A message that is sent to all devices

MULTICAST message
* A message that is sent to a group of devices

Routers also have console ports
Also have Serial connections
* Serial connections are used to connect to other routers
* Serial connections are used to connect to the internet

Routers have routing tables
* Routing tables are tables that contain IP addresses and what port they are connected to
* Routing tables are also called routing information bases (RIB)

Routers have access control lists (ACL)
* ACLs are used to filter traffic
* ACLs are used to block traffic
* ACLs are used to allow traffic

Routers have NAT (Network Address Translation)
* NAT is used to translate private IP addresses to public IP addresses
* NAT is used to translate public IP addresses to private IP addresses

Routers have DHCP (Dynamic Host Configuration Protocol)
* DHCP is used to automatically assign IP addresses to devices
* DHCP is used to automatically assign subnet masks to devices
* DHCP is used to automatically assign default gateways to devices
* DHCP is used to automatically assign DNS servers to devices



