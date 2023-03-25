from scapy.all import srp, Ether, ARP, conf
from sys import argv, exit

if (len(argv) != 2):
	print("Invalid number of arguments\nUsage arpScan.py [Network Range/subnet]") 
	exit(1)

conf.verb=0
a,u = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=argv[1]), timeout=2)
for s,r in a:
	print(r.sprintf("%Ether.src% %ARP.psrc%"))
