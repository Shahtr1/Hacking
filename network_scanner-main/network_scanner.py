#!/usr/bin/env python

import scapy.all as scapy
# import optparse # deprecated optparse
import argparse


def get_arguments():
    # parser = optparse.OptionParser() # deprecated optparse
    parser = argparse.ArgumentParser()
    # parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.") # deprecated optparse
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    # (options, arguments) = parser.parse_args() # deprecated optparse
    (options) = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # print(arp_request.summary())

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    # print(broadcast.summary())

    # scapy.ls(scapy.Ether()) # list the variables of class

    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show() # more details
    # print(arp_request_broadcast.summary())

    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] # as we don't want unanswered_list
    # by srp we can send custom Ether part otherwise we can also use sr()

    # print(answered_list.summary())
    # print(unanswered_list.summary())

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

