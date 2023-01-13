#!/usr/bin/env python

# use command (   iptables -I FORWARD -j NFQUEUE --queue-num 0   )
# to create a iptable queue for incoming connections that are forwarded

import  netfilterqueue


def process_packet(packet):
    print(packet)
    # packet.accept()
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
