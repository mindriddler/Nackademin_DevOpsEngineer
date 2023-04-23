## Part 1

Which command displays the statistics for all interfaces configured on a router?
* show interfaces

Which command displays the information about the Serial 0/0/0 interface only?
* show interfaces Serial 0/0/0

Enter the command to display the statistics for the Serial 0/0/0 interface on R1 and answer the following questions:
* What is the IP address configured on R1?
* * 209.165.200.225/30
* What is the bandwidth on the Serial 0/0/0 interface?
* * BW 1544 Kbit

Enter the command to display the statistics for the GigabitEthernet 0/0 interface and answer the following questions:
* What is the IP address on R1?
* * There is no IP Address for this interface
* What is the MAC address of the GigabitEthernet 0/0 interface?
* * 000d.bd6c.7d01
* What is the bandwidth on the GigabitEthernet 0/0 interface?
* * BW 1000000 Kbit

Which command displays a brief summary of the current interfaces, statuses, and IP addresses assigned to them?
* show ip interface brief

Enter the command on each router and answer the following questions:
* How many serial interfaces are there on R1 and R2?
* * R1 = 2
* * R2 = 2
* How many Ethernet interfaces are there on R1 and R2?
* * R1 = 6
* * R2 = 2
* Are all the Ethernet interfaces on R1 the same? If no, explain the difference(s).
* * No, 4 or the Ethernet interfaces are FastEthernet and 2 and GigabitEthernet which means the support a different theoreticly maximum speed

What command displays the content of the routing table?
*  show ip route

Enter the command on R1 and answer the following questions:
* How many connected routes are there (uses the C code)?
* * 1
* Which route is listed?
* * 209.165.200.224/30 is directly connected, Serial0/0/0
* How does a router handle a packet destined for a network that is not listed in the routing table?
* * A router will only send packets to a network listed in the routing table. If a network is not listed, the packet will be dropped

Save the configuration files on both routers to NVRAM. What command did you use?
* copy running-config startup-config

## Part 3

How many interfaces on R1 and R2 are configured with IP addresses and in the “up” and “up” state?
* R1 = 3
* R2 = 3

What part of the interface configuration is NOT displayed in the command output?
* Subnet mask

What commands can you use to verify this part of the configuration?
* show run, show interfaces, show protocols

How many connected routes (uses the C code) do you see on each router?
* R1 = 3 
* R2 = 3

How many EIGRP routes (uses the D code) do you see on each router?
* R1 = 2 
* R2 = 2

If the router knows all the routes in the network, then the number of connected routes and dynamically learned routes (EIGRP) should equal the total number of LANs and WANs. How many LANs and WANs are in the topology?
* There are 4 lan and 1 wan in the topology

Does this number match the number of C and D routes shown in the routing table?
* Yes