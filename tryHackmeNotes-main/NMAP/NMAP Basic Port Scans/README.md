# NMAP Basic Port Scans

> Shahrukh Tramboo | January 29th, 2022

--------------------------------------

**TCP Flags**

Setting a flag bit means setting its value to 1. From left to right, the TCP header flags are:

1.	URG: Urgent flag indicates that the urgent pointer filed is significant. The urgent pointer indicates that the incoming data is urgent, and that a TCP segment with the URG flag set is processed immediately without consideration of having to wait on previously sent TCP segments.

2.	ACK: Acknowledgement flag indicates that the acknowledgement number is significant. It is used to acknowledge the receipt of a TCP segment.

3.	PSH: Push flag asking TCP to pass the data to the application promptly.

4.	RST: Reset flag is used to reset the connection. Another device, such as a firewall, might send it to tear a TCP connection. This flag is also used when data is sent to a host and there is no service on the receiving end to answer.

5.	SYN: Synchronize flag is used to initiate a TCP 3-way handshake and synchronize sequence numbers with the other host. The sequence number should be set randomly during TCP connection establishment.

6.	FIN: The sender has no more data to send.

------------------------------------------------

**TCP Connect Scan**

We are interested in learning whether the TCP port is open, not establishing a TCP connection. Hence the connection is torn as soon as its state is confirmed by sending a RST/ACK. You can choose to run TCP connect scan using -sT.

```bash
nmap -sT 10.10.17.129
```

Note that we can use -F to enable fast mode and decrease the number of scanned ports from 1000 to 100 most common ports.

It is worth mentioning that the -r option can also be added to scan the ports in consecutive order instead of random order. This option is useful when testing whether ports open in a consistent manner, for instance, when a target boots up.

-------------------------------------------------

**TCP SYN Scan**

Unprivileged users are limited to connect scan. However, the default scan mode is SYN scan, and it requires a privileged (root or sudoer) user to run it. SYN scan does not need to complete the TCP 3-way handshake; 
We can select this scan type by using the -sS option.

```bash
sudo nmap -sS 10.10.10.37
```

---------------------------------------------------

**UDP Scan**

```bash
sudo nmap -sU 10.10.39.78
```

----------------------------------------------------

**Fine-Tuning Scope and Performance**

1.	port list: -p22,80,443 will scan ports 22, 80 and 443.
2.	port range: -p1-1023 will scan all ports between 1 and 1023 inclusive, while -p20-25 will scan ports between 20 and 25 inclusive.
3.	You can request the scan of all ports by using -p-, which will scan all 65535 ports.
4.	If you want to scan the most common 100 ports, add -F
5.	 Using --top-ports 10 will check the ten most common ports.
6.	You can control the scan timing using -T<0-5>. -T0 is the slowest (paranoid), while -T5 is the fastest.
	According to Nmap manual page, there are six templates:
	paranoid (0)
	sneaky (1)
	polite (2)
	normal (3)
	aggressive (4)
	insane (5)
7.	you can choose to control the packet rate using --min-rate <number> and --max-rate <number>
8.	you can control probing parallelization using --min-parallelism <numprobes> and --max-parallelism <numprobes>

