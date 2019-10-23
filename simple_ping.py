#!/usr/bin/python3

"""

Scapy is a tool made to use in command line so please run "simple_ping.py" in command prompt: 

system32> python3 simple_ping.py
or 
root@debian:~# python simple_ping.py

"""

import scapy.all

dst_ip = input("IP ciblée: ")

print("Envoi du ping à la cible %s" % (dst_ip))

ping_packet = scapy.all.IP(dst=dst_ip) / scapy.all.ICMP()

resp = scapy.all.sr1(ping_packet)

if resp == None:
    print("L'hôte est en ligne.")
else:
    print("L'hôte est hors-ligne.")
