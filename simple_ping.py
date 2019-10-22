#!/usr/bin/python3


import scapy.all

print("pinging the target....")


dst_ip = input("IP ciblée: ")

ping_packet = scapy.all.IP(dst=dst_ip) / scapy.all.ICMP()

resp = scapy.all.sr1(ping_packet)

if resp == None:
    print("L'hôte est en ligne.")
else:
    print("L'hôte est hors-ligne.")
