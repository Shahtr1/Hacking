# NMAP Live Host Discovery

> Shahrukh Tramboo | January 28th, 2022

--------------------------------------

**Nmap Host Discovery Using ARP**

1.	When a privileged user tries to scan targets outside the local network, Nmap uses ICMP echo requests, TCP ACK (Acknowledge) to port 80, TCP SYN (Synchronize) to port 443, and ICMP timestamp request.

2.	When an unprivileged user tries to scan targets outside the local network, Nmap resorts to a TCP 3-way handshake by sending SYN packets to ports 80 and 443.


Nmap, by default, uses a ping scan to find live hosts, then proceeds to scan live hosts only.
If you want to use Nmap to discover online hosts without port-scanning the live systems, you can issue 

```bash
nmap -sn TARGETS
```
If you want Nmap only to perform an ARP scan without port-scanning, you can use
```bash
nmap -PR -sn TARGETS
```

where -PR indicates that you only want an ARP scan.
Example:
```bash
nmap -PR -sn MACHINE_IP/24
```

**ARP-SCAN**

A scanner built around ARP queries
```bash
arp-scan --localnet
```

or

```bash
arp-scan -l
```

This command will send ARP queries to all valid IP addresses on your local networks.

Moreover, if your system has more than one interface and you are interested in discovering the live hosts on one of them, you can specify the interface using -I.

-------------------------------------------------

**Nmap Host Discovery Using ICMP**

```bash
nmap -PE -sn MACHINE_IP/24
```
This scan will send ICMP echo packets to every IP address on the subnet.

Because ICMP echo requests tend to be blocked, you might also consider ICMP Timestamp or ICMP Address Mask requests to tell if a system is online.

Adding the -PP option tells Nmap to use ICMP timestamp requests. 
```bash
nmap -PP -sn MACHINE_IP/24
```

Similarly, Nmap uses address mask queries (ICMP Type 17) and checks whether it gets an address mask reply (ICMP Type 18).
```bash
nmap -PM -sn MACHINE_IP/24
```

---------------------------------------------------

**Nmap Host Discovery Using TCP and UDP**

1.	TCP SYN Ping:
We can send a packet with the SYN (Synchronize) flag set to a TCP port, 80 by default, and wait for a response. An open port should reply with a SYN/ACK (Acknowledge); a closed port would result in an RST (Reset).

```bash
nmap -PS21-25 -sn MACHINE_IP/24
```

Privileged users (root and sudoers) can send TCP SYN packets and don’t need to complete the TCP 3-way handshake even if the port is open, as shown in the figure below. Unprivileged users have no choice but to complete the 3-way handshake if the port is open.


2.	TCP ACK Ping:
As you have guessed, this sends a packet with an ACK flag set. You must be running Nmap as a privileged user to be able to accomplish this. If you try it as an unprivileged user, Nmap will attempt a 3-way handshake.
```bash
sudo nmap -PA -sn MACHINE_IP/24
```

3.	UDP Ping:
Sending a UDP packet to an open port is not expected to lead to any reply. However, if we send a UDP packet to a closed UDP port, we expect to get an ICMP port unreachable packet; 
```bash
sudo nmap -PU -sn 10.10.68.220/24
```

4.	Masscan:
to finish its network scan quickly, Masscan is quite aggressive with the rate of packets it generates.

```bash
masscan MACHINE_IP/24 -p443
masscan MACHINE_IP/24 -p80,443
masscan MACHINE_IP/24 -p22-25
masscan MACHINE_IP/24 ‐‐top-ports 100
```

----------------------------------------------------

**Using Reverse-DNS Lookup**
if you don’t want to send such DNS queries, you use -n to skip this step.

By default, Nmap will look up online hosts; however, you can use the option -R to query the DNS server even for offline hosts. If you want to use a specific DNS server, you can add the 
```bash
--dns-servers DNS_SERVER 
```
option.
