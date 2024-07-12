from scapy.all import *

target_host = 'cctv.thm'
payload = 'User-agent: Mozilla'

packet = IP(dst=target_host)/ICMP()/Raw(load=payload)

send(packet)
