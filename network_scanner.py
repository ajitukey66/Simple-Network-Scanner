from scapy.all import srp
from scapy.layers.l2 import ARP, Ether
import sys

target_network = sys.argv[1]

online_clients = []

ether = Ether(dst="ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = target_network)
probe  = ether/arp

result = srp(probe, timeout=3, verbose=0)

answered = result[0]

for sent, received in answered:
    online_clients.append({'ip' : received.psrc, 'mac' : received.hwsrc})

print("[+] Available hosts: ")
print("IP"+ " "*22 +"MAC")

for client in online_clients:
    print('{}\t\t{}'.format(client['ip'], client['mac']))