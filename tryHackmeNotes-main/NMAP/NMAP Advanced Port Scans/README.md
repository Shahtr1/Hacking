# NMAP Advanced Port Scans

> Shahrukh Tramboo | January 30th, 2022

---

**Null Scan**

The null scan does not set any flag; all six flag bits are set to zero. You can choose this scan using the -sN option.

According to the RFC 793 specification (TCP), if a host receives a TCP packet with no flags set, it should not respond to it. In other words, it should silently drop the packet.

If you receive no response, it suggests that the port might be open, filtered, or that the target system is configured to drop packets silently. It does not definitively confirm that the port is closed.

If you receive an RST (Reset) response, it indicates that the port is closed. A closed port should respond with an RST packet, which is a standard behavior according to the TCP protocol.

```bash
sudo nmap -sN 10.10.243.170
```

---

**FIN Scan**

The FIN scan sends a TCP packet with the FIN flag set. You can choose this scan type using the -sF option.

Similarly, no response will be sent if the TCP port is open. Again, Nmap cannot be sure if the port is open or if a firewall is blocking the traffic related to this TCP port.

However, the target system should respond with an RST if the port is closed.

It's worth noting some firewalls will 'silently' drop the traffic without sending an RST.

```bash
sudo nmap -sF 10.10.243.170
```

---

**Xmas Scan**

The Xmas scan gets its name after Christmas tree lights. An Xmas scan sets the FIN, PSH, and URG flags simultaneously.

You can select Xmas scan with the option -sX.
Like the Null scan and FIN scan, if an RST packet is received, it means that the port is closed. Otherwise, it will be reported as open|filtered.

```bash
sudo nmap -sX 10.10.243.170
```

### Many firewalls are configured to drop incoming TCP packets to blocked ports which have the SYN flag set (thus blocking new connection initiation requests). By sending requests which do not contain the SYN flag, we effectively bypass this kind of firewall. Whilst this is good in theory, most modern IDS solutions are savvy to these scan types, so don't rely on them to be 100% effective when dealing with modern systems.

---

**TCP Maimon Scan**

In this scan, the FIN and ACK bits are set.
The target should send an RST packet as a response.
However, certain BSD-derived systems drop the packet if it is an open port exposing the open ports.

To select this scan type, use the -sM option.

```bash
sudo nmap -sM 10.10.252.27
```

---

**TCP ACK, Window, and Custom Scan**

an ACK scan will send a TCP packet with the ACK flag set. Use the -sA option to choose this scan.

The target would respond to the ACK with RST regardless of the state of the port. This behaviour happens because a TCP packet with the ACK flag set should be sent only in response to a received TCP packet to acknowledge the receipt of some data, unlike our case.

This kind of scan would be helpful if there is a firewall in front of the target.

```bash
sudo nmap -sA 10.10.172.246
```

---

**TCP Windows Scan**

TCP Window Size: In the TCP protocol, the window size is a field in the TCP header that indicates the size of the receive window, which is used for flow control. It represents the amount of data that can be sent before requiring an acknowledgment.

How It Works: In a TCP Window Scan, Nmap sends TCP packets with the ACK (Acknowledgment) flag set and a specific initial window size to target ports. The scan is based on how the target system responds to these packets.

Expected Responses:

- ### Open Port:

  If the port is open and actively accepting connections, the target system should respond with a certain window size value (typically non-zero) in the TCP header.

- ### Closed Port:

  If the port is closed, the target system may respond with a TCP RST (Reset) packet, indicating that the port is closed. Some closed ports may also respond with a zero window size.

- ### Filtered Port:

  If the port is filtered (e.g., by a firewall), the target system may not respond at all.

```bash
sudo nmap -sW 10.10.172.246
```

---

**Custom Scan**

if you want to set SYN, RST, and FIN simultaneously, you can do so using

```bash
nmap -p <port_number> --scanflags SYN,RST,FIN <target_ip>

```

---

**Spoofing and Decoys**

```bash
nmap -S SPOOFED_IP MACHINE_IP
```

Consequently, Nmap will craft all the packets using the provided source IP address SPOOFED_IP

The target machine will respond to the incoming packets sending the replies to the destination IP address SPOOFED_IP

For this scan to work and give accurate results, the attacker needs to monitor the network traffic to analyze the replies.

In general, you expect to specify the network interface using -e and to explicitly disable ping scan -Pn

```bash
nmap -e NET_INTERFACE -Pn -S SPOOFED_IP MACHINE_IP
```

When you are on the same subnet as the target machine, you would be able to spoof your MAC address as well

```bash
--spoof-mac SPOOFED_MAC
```

Spoofing only works in a minimal number of cases where certain conditions are met. Therefore, the attacker might resort to using decoys to make it more challenging to be pinpointed.

The concept is simple, make the scan appears to be coming from many IP addresses so that the attacker’s IP address would be lost among them.

```bash
nmap -D 10.10.0.1,10.10.0.2,RND,RND,ME MACHINE_IP
```

---

**Fragmented Packets**

Nmap provides the option -f to fragment packets.
Adding another -f (-f -f or -ff) will split the data into 16 byte-fragments instead of 8. You can change the default value by using the --mtu; however, you should always choose a multiple of 8.

```bash
sudo nmap -sS -p80 -f 10.20.30.144
```

if you prefer to increase the size of your packets to make them look innocuous, you can use the option

```bash
 --data-length NUM
```

---

**Idle/Zombie Scan**

The idle scan, or zombie scan, requires an idle system connected to the network that you can communicate with.

This is accomplished by checking the IP identification (IP ID) value in the IP header

```bash
nmap -sI ZOMBIE_IP MACHINE_IP
```

The idle (zombie) scan requires the following three steps to discover whether a port is open:

1. Trigger the idle host to respond so that you can record the current IP ID on the idle hos
2. Send a SYN packet to a TCP port on the target. The packet should be spoofed to appear as if it was coming from the idle host (zombie) IP address.
3. Trigger the idle machine again to respond so that you can compare the new IP ID with the one received earlier.

In the figure below, we have the attacker system probing an idle machine, a multi-function printer. By sending a SYN/ACK, it responds with an RST packet containing its newly incremented IP ID.

The attacker will send a SYN packet to the TCP port they want to check on the target machine in the next step. However, this packet will use the idle host (zombie) IP address as the source.

1. In the first scenario, shown in the figure below, the TCP port is closed; therefore, the target machine responds to the idle host with an RST packet. The idle host does not respond; hence its IP ID is not incremented.

2. In the second scenario, as shown below, the TCP port is open, so the target machine responds with a SYN/ACK to the idle host (zombie). The idle host responds to this unexpected packet with an RST packet, thus incrementing its IP ID.

3. In the third scenario, the target machine does not respond at all due to firewall rules. This lack of response will lead to the same result as with the closed port; the idle host won’t increase the IP ID.

4. For the final step, the attacker sends another SYN/ACK to the idle host. The idle host responds with an RST packet, incrementing the IP ID by one again. The attacker needs to compare the IP ID of the RST packet received in the first step with the IP ID of the RST packet received in this third step. If the difference is 1, it means the port on the target machine was closed or filtered. However, if the difference is 2, it means that the port on the target was open.

---

**Getting More Details**

You might consider adding --reason if you want Nmap to provide more details regarding its reasoning and conclusions
