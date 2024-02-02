<u><b>		0x08. Networking basics #1</b></u>
The task digs deep into networking as we indulge into phase 2 of the networking basics. In this section, we will get to learn more about networking concepts where the areas of concerns would be:

	1. Localhost
It refers to the current computer used to access it in computer networking and the name localhost is reserved for loopback purposes.
The Local loopback mechanism may be used to run a anetwork service on a host without requiring a phsical network interface, or without making th eservice accessible from the networks the computer may be connected to.
The name <b> Localhost</b> normally resolves to the IPv4 loopback address <b>127.0.0.1</b>, and to the IPv6 loopback address <b>::1</b>.
Also, the name may also be resolved by Domain Name System (DNS) servers, but there are special considerations which need to be put in place.

The processing of any packet sent to a loopback address, is implemented in the link layer of the TCP/IP stack. Such packets are never passed to any network interface controller (NIC) or hardware device driver and must not appear outside of a computing system, or be routed by any router. This permits software testing and local services, even in the absence of any hardware network interfaces.

<b> 	What is 0.0.0.0</b>

Official meaning and use
IANA, who allocate IP addresses globally, have allocated the single IP address 0.0.0.0[1] to RFC 1122 section 3.2.1.3. It is named as "This host on this network".

RFC 1122 refers to 0.0.0.0 using the notation {0,0}. It prohibits this as a destination address in IPv4 and only allows it as a source address under specific circumstances.

A host may use 0.0.0.0 as its own source address in IP when it has not yet been assigned an address, such as when sending the initial DHCPDISCOVER packet when using DHCP.

Operating system specific uses
Some operating systems have attributed special internal meanings to the address. These uses do not result in IPv4 packets containing 0.0.0.0 and so are not governed by RFC 1122. These meanings may not be consistent between OS.

In both Windows and Linux, when selecting which of a host's IP address to use as a source IP, a program may specify INADDR_ANY (0.0.0.0).

In Linux a program may specify 0.0.0.0 as the remote address to connect to the current host (AKA localhost).

Other non-standard uses
Besides the use by operating systems internally, other uses have been attributed to the address.

A non-routable meta-address used to designate an invalid, unknown or non applicable target
The address a host assigns to itself when address request via DHCP has failed, provided the host's IP stack supports this. This usage has been replaced with the APIPA mechanism in modern operating systems.
A way to explicitly specify that the target is unavailable.
A way to route a request to a nonexistent target instead of the original target. Often used for adblocking purposes. This can conflict with OS specific behaviour.

Routing
In routing tables, 0.0.0.0 can also appear in the gateway column. This indicates that the gateway to reach the corresponding destination subnet is unspecified. This generally means that no intermediate routing hops are necessary because the system is directly connected to the destination.

The CIDR notation 0.0.0.0/0 defines an IP block containing all possible IP addresses. It is commonly used in routing to depict the default route as a destination subnet. It matches all addresses in the IPv4 address space and is present on most hosts, directed towards a local router.

In IPv6
In IPv6, the all-zeros address is typically represented by :: (two colons), which is the short notation of 0000:0000:0000:0000:0000:0000:0000:0000.[10] The IPv6 variant serves the same purpose as its IPv4 counterpart.


Lastly, we do have the concetpt of Netcat or nc which is a networking utility for debugging and investigating the network. This utility can be used for creating TCP/UDP connections and investigating them. The biggest use of this utility is in the scripts where we need to deal with TCP/UDP sockets.More about this an their uses, attached examples and guidelines to follow through with can be found in <a href="https://www.thegeekstuff.com/2012/04/nc-command-examples/">Netcat examples</a> and will be of great help.

The man or help pages that will be of great assistance for this particular task are for:
i. ifconfig
ii. telnet
iii. nc
iv. cut
