"""Netwrok Protocol Analyzer -- Packet Sniffer By KUSHAGRA VERMA"""
# This Script Requires Elevated Prvileges
from scapy.all import *




def packet_handler(packet, service_protocol):
    print()
    print("\033[3;91;40mIP ADDRESS HIDDEN FOR PRIVACY\033[m")
    print()
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print("-" * 100)
        print(f"\033[1;92;40m{'Source IP:':<15}\033[m \033[1;93;40m {src_ip:<15}\033[m --> \033[1;92;40m{'Destination IP:':<15}\033[m \033[1;91;40m{dst_ip:<15}\033[m")

        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = packet[TCP].payload
        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            payload = packet[UDP].payload
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            src_port = None
            dst_port = None
            payload = packet[ICMP].payload

        print(f"\033[1;91;40m{'Protocol:':<15} \033[m \033[1;91;40m {protocol:<15}\033[m")
        if src_port and dst_port:
            print(f"\033[1;92;40m{'Source Port:':<15} \033[m \033[1;93;40m {src_port:<15} \033[m--> \033[1;92;40m{'Destination Port:':<15} \033[m \033[1;91;40m{dst_port:<15}\033[m")

        print("\033[1;95;40mPayload (Hex):\033[m")
        payload_hex_dump = ' '.join(f"\033[1;91;40m{i:02x}\033[m" for i in bytes(payload))
        print(format_payload(payload_hex_dump))

        print("\033[1;93;40mDecoded Payload:\033[m")
        try:
            decoded_payload = payload.decode()
            print(decoded_payload)
        except Exception as e:
            print()
            print("\033[3;91;40m-- Payload is in Raw Format --\033[m")
            print()
            print("-"*100)


def format_payload(payload_hex_dump):
    formatted_payload = ""
    for i in range(0, len(payload_hex_dump), 32):
        chunk = payload_hex_dump[i:i + 32]
        formatted_payload += ' '.join([chunk[j:j + 2] for j in range(0, len(chunk), 2)]) + '\n'
    return formatted_payload.strip()



#MAIN
print("""\033[1;32;40m
$$\   $$\            $$\     $$$$$$$\                      $$\                 
$$$\  $$ |           $$ |    $$  __$$\                     $$ |                
$$$$\ $$ | $$$$$$\ $$$$$$\   $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  
$$ $$\$$ |$$  __$$\\_$$  _|  $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ \$$$$ |$$$$$$$$ | $$ |    $$  ____/ $$ |  \__|$$ /  $$ |$$ |  $$ |$$$$$$$$ |
$$ |\$$$ |$$   ____| $$ |$$\ $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$   ____|
$$ | \$$ |\$$$$$$$\  \$$$$  |$$ |      $$ |      \$$$$$$  |$$$$$$$  |\$$$$$$$\ 
\__|  \__| \_______|  \____/ \__|      \__|       \______/ \_______/  \_______|
---BY KUSHAGRA VERMA ---\033[m                                                                               
""")
print("*"*100)
print()
print("\033[1;31;40mAvailable Interfaces:\033[m")
interfaces = get_if_list()
for idx, interface in enumerate(interfaces, start=1):
    print(f"{idx}. {interface}")
print()
interface_index = int(input("\033[3;93;40mEnter the index of the interface to sniff on: \033[m"))
selected_interface = interfaces[interface_index - 1]
print("-"*100)
print()
service_protocol = input("\033[1;91;40mEnter the service protocol to filter (TCP/UDP/ICMP): \033[m").upper()
if service_protocol == '' :
    print("USAGE : TCP/UDP/ICMP select one.")
    exit()

print()
num_packets = int(input("\033[1;92;40mEnter the number of packets to capture (enter 0 for continuous capture, if selected press Ctrl+C to exit): \033[m"))
print("-"*100)

conf.iface = selected_interface


packet_count = 0

while True:

    if num_packets != 0 and packet_count >= num_packets:
        break
    packet = sniff(count=1)[0]
    packet_handler(packet, service_protocol)
    packet_count += 1
