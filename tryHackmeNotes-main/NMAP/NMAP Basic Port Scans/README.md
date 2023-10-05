# NMAP Basic Port Scans

> Shahrukh Tramboo | January 29th, 2022

---

**TCP Flags**

Setting a flag bit means setting its value to 1. From left to right, the TCP header flags are:

1. URG: Urgent flag indicates that the urgent pointer field is significant. The urgent pointer indicates that the incoming data is urgent, and that a TCP segment with the URG flag set is processed immediately without consideration of having to wait on previously sent TCP segments.

2. ACK: Acknowledgement flag indicates that the acknowledgement number is significant. It is used to acknowledge the receipt of a TCP segment.

3. PSH: Push flag asking TCP to pass the data to the application promptly.

4. RST: Reset flag is used to reset the connection. Another device, such as a firewall, might send it to tear a TCP connection. This flag is also used when data is sent to a host and there is no service on the receiving end to answer.

5. SYN: Synchronize flag is used to initiate a TCP 3-way handshake and synchronize sequence numbers with the other host. The sequence number should be set randomly during TCP connection establishment.

6. FIN: The sender has no more data to send.

---

**TCP Connect Scan (Full Open)**

A TCP Connect scan in Nmap involves initiating a TCP connection to the target port by sending a SYN packet.

If the port is open, the target system responds with a SYN-ACK, and Nmap completes the three-way TCP handshake by sending an ACK packet. After confirming the state of the port, Nmap then sends a RST/ACK (reset/acknowledgment) packet to gracefully close the connection.

The primary goal of the TCP Connect scan is to determine whether the TCP port is open, but it does establish a temporary connection during the scanning process.

You can choose to run TCP connect scan using -sT.

```bash
nmap -sT 10.10.17.129
```

Note that we can use -F to enable fast mode and decrease the number of scanned ports from 1000 to 100 most common ports.

It is worth mentioning that the -r option can also be added to scan the ports in consecutive order instead of random order. This option is useful when testing whether ports open in a consistent manner, for instance, when a target boots up.

---

**TCP SYN Scan (Half Open)**

Unprivileged users are limited to connect scan. However, the default scan mode is SYN scan, and it requires a privileged (root or sudoer) user to run it. SYN scan does not need to complete the TCP 3-way handshake;

- If the port is open, the target system responds with a SYN-ACK packet.
- If the port is closed, the target system responds with a RST (reset) packet

  We can select this scan type by using the -sS option.

```bash
sudo nmap -sS 10.10.10.37
```

---

**UDP Scan**

Nmap sends UDP packets to various UDP ports on the target system and analyzes the responses (if any).

```bash
sudo nmap -sU 10.10.39.78
```

Here's a more detailed explanation of how Nmap handles UDP port scanning:

- 1. ## Sending UDP Packets:
     Nmap sends UDP packets to various UDP port numbers on the target system. These packets are typically crafted to resemble legitimate UDP traffic but with an empty payload (no data).
     The port numbers chosen for scanning can be specified by the user or can be part of a predefined list in Nmap.

- 2.  ## Response Analysis:

      - ### Open Port:

        If a UDP port is open on the target system and is actively listening for UDP packets, it may respond in one of several ways:

        - It might respond with an ICMP Port Unreachable message. This can happen because the target system received the UDP packet but has no listening service on that port, so it sends a response indicating that the port is unreachable.

          However, some systems may not respond with ICMP Port Unreachable messages even if the port is open.

        - It might respond with a valid UDP response that can be analyzed by Nmap. For example, if the target has a DNS server running on a specific UDP port, it might respond with DNS-related data.

      - ### Closed Port:

        - If a UDP port is closed, it may also respond with an ICMP Port Unreachable message. This can occur because the target system's firewall or network stack is configured to respond with "port unreachable" for any incoming UDP packets to closed ports.

        - Nmap often distinguishes between open and closed UDP ports based on the timing and behavior of these ICMP responses. Closed ports may exhibit different timing patterns or behaviors compared to open ports, allowing Nmap to make educated guesses.

      - ### Filtered Port:

        - A "filtered" UDP port is one where Nmap doesn't receive any response at all. This can happen if a firewall or network filtering device silently drops UDP packets without responding.

        - Nmap cannot conclusively determine whether a UDP port is open or closed when it's "filtered" because it doesn't receive any response. In this case, it marks the port as "filtered."

- 3. ## Timing and Behavior Analysis:

     - Nmap uses various timing and behavior analysis techniques to differentiate between open and closed UDP ports. For example, open ports may respond more quickly, while closed ports might exhibit certain patterns in their responses or timing.

     - Nmap also considers the source of ICMP Port Unreachable messages. If the response comes from the target system itself, it may indicate a closed port. If it comes from an intermediate network device, it may indicate an open port.

---

**Fine-Tuning Scope and Performance**

1. port list: -p22,80,443 will scan ports 22, 80 and 443.
2. port range: -p 1-1023 will scan all ports between 1 and 1023 inclusive, while -p 20-25 will scan ports between 20 and 25 inclusive.
3. You can request the scan of all ports by using -p-, which will scan all 65535 ports.
4. If you want to scan the most common 100 ports, add -F
5. Using --top-ports 10 will check the ten most common ports.
6. You can control the scan timing using -T<0-5>. -T0 is the slowest (paranoid), while -T5 is the fastest.
   According to Nmap manual page, there are six templates:
   paranoid (0)
   sneaky (1)
   polite (2)
   normal (3)
   aggressive (4)
   insane (5)
7. You can choose to control the packet rate using --min-rate < number > and --max-rate < number >
8. You can control probing parallelization using --min-parallelism < numprobes > and --max-parallelism < numprobes >
