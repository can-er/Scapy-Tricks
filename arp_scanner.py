import sys
from scapy.all import *

if len (sys.argv) != 2:
	print('Utilisation: arp_scanner.py "192.168.1.0/24"')
	sys.exit(1)

try:

	alive, dead = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = sys.argv[1]), timeout = 2, verbose = 0)
	print("Adresse MAC - Adresse IP")

	for i in range(0, len(alive)):
		print(alive[i][1].hwsrc + "--" + alive[i][1].psrc)

except:
	print("Erreur")
	pass

