nacka_student
Och lösenordet
8&CFhYb&K6o!F84x

En liten server (10.0.1.25/32) är kopplad till Port 2 (10.0.1.4)

Uppgift 2

B) Port1: 10.0.0.4 (external)
   Port2: 10.0.1.4 (internal)

Uppgift 3 

Demotestarprov är en tunnel

Ip adresserna är

Kategorier som man kan sortera på
* Local Categories (Kategorier som man definierar själv)
* Potentially Liable
* Adult/Mature Content
* Bandwidth Consuming
* Security Risk
* General Interest - Personal
* General Interest - Business
* Unrated

Under secutirty profiles > Webfilter så finns det flera kategorier, där en av dem heter "unrated"
i "unrated" ingår allting som fortinet ännu INTE har kategoriserat
Ett exempel; 
* Låt oss säga att "github.com" inte är kategoriserad av fortinet, då hamnar den i "unrated" till då de har kategoriserat den.
* När den ör kategoriserad så kommer den att flyttas till en annan mer lämplig grupp


Det finns totalt 5864 IPS signatures
varav 11 av dessa är informational

remote gateway: 192.168.20.2
authentication: Pre-shared key, IKE V1
Första förslaget är AES128-SHA256
Metod for nyckelhantering: Diffie-Hellman Groups 14,5


-------------------------------------
TASK 2

Based on the provided information, here are the answers for Task 2:

A) Networks attached to each physical interface in the firewall:

port1: This physical interface is attached to the network 10.0.0.0/26, as suggested by its IP address 10.0.0.4 and subnet mask 255.255.255.192.

port2: This physical interface is attached to the network 10.0.1.0/26, as indicated by its IP address 10.0.1.4 and subnet mask 255.255.255.192.

B) IP addresses set for each interface in the firewall:

port1: The IP address set for this interface is 10.0.0.4.

port2: The IP address set for this interface is 10.0.1.4.

As for the management interface, it's not listed in the provided information. As explained before, management interfaces are often not listed with the other network interfaces because they're typically used for device administration and not for routing traffic. The management interface's IP address would typically be set separately and would be used for secure administrative access to the firewall.

TASK 3

Based on the provided information, the firewall policies can be interpreted as follows:

Policy: DemoTestarProv →port2

This policy applies to traffic passing through the "DemoTestarProv" VPN tunnel to the "port2" interface. It seems to apply to all sources and destinations (as indicated by "all"). It enables Network Address Translation (NAT), accepts the traffic, and applies security profiles under the Unified Threat Management (UTM) package. The services allowed include ALL_ICMP, DNS, HTTP, and HTTPS. The "no-inspection" likely means that these services are not subjected to deep packet inspection.

Policy: port1 →port2

This policy applies to traffic from "port1" to a specific destination "En liten server". Similar to the previous policy, NAT is enabled, the traffic is accepted, and UTM security profiles are applied. The services allowed in this policy are ALL_ICMP and HTTPS.

Policy: port2 →DemoTestarProv

This policy applies to all traffic from "port2" to the "DemoTestarProv" VPN tunnel. It also enables NAT, accepts the traffic, and applies UTM security profiles. The services allowed are ALL_ICMP, ALL_TCP, and ALL_UDP.

Implicit Policy

This is a default catch-all policy, applying to all traffic not covered by other policies. It denies all traffic and does not log the traffic (Log is disabled).

The "Stateful Packet Filter" and "Application Level Proxy" are firewall technologies. A stateful packet filter keeps track of the state of network connections and allows incoming packets that correspond to a known connection. An application-level gateway (also known as an application proxy) is more secure as it filters incoming resources based on various conditions at the application layer.

In your case, the stateful packet filtering can be inferred from the "ACCEPT" action in all the policies, as it allows incoming packets corresponding to a known connection. Application-level proxy can be seen in the use of specific services like HTTPS, DNS, ICMP, etc. However, it's important to note that these are generic interpretations, and the exact workings might vary based on your firewall's configuration.

TASK 4 

Based on the provided information, under the "default" web filtering profile, you can sort based on several categories:

Potentially Liable
Adult/Mature Content
Bandwidth Consuming
Security Risk
General Interest - Personal
General Interest - Business
Unrated
Each category represents a type of web content that you can control access to. For instance, you may choose to block "Adult/Mature Content" to prevent users from accessing inappropriate websites.

The "Unrated" category likely includes websites that haven't been evaluated or categorized yet by FortiGuard services. Due to the vast number of websites on the internet and the continuous creation of new ones, it's not uncommon for a website to be unrated.

Additional options under the "default" web filtering profile include allowing users to override blocked categories, blocking invalid and malicious URLs, content filtering, rating options, and proxy options. These features provide more granular control over web access and can enhance the network's overall security.