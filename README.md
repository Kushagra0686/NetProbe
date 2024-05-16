**NetProbe: Network Packet Analyzer**

**Overview**

NetProbe is a powerful Python script designed to function as a network packet analyzer or sniffer. It leverages the Scapy library to capture and inspect network traffic flowing through your selected interface. 

**Features**

- **Cross-Protocol Analysis:** Deciphers packets across various protocols, including TCP (Transmission Control Protocol), UDP (User Datagram Protocol), and ICMP (Internet Control Message Protocol).
- **Detailed Packet Information:** Provides comprehensive details for each captured packet, encompassing source and destination IP addresses, ports, protocols, and payload data (both in hexadecimal and decoded formats, if possible).
- **User-Friendly Interface Selection:** Guides you through the selection of your network interface for capturing packets.
- **Optional Service Protocol Filtering:** Offers the option to filter captured packets based on a specific service protocol (TCP, UDP, or ICMP) for a more focused analysis.
- **Customizable Packet Capture:** Allows you to specify the number of packets to capture (enter 0 for continuous capture; press Ctrl+C to exit).
- **Clear Output Formatting:** Presents captured packet information in a well-organized and visually appealing format using color coding for better readability.

**Requirements**

- Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- Scapy Library ([https://scapy.readthedocs.io/en/latest/](https://scapy.readthedocs.io/en/latest/)) - Installation: `pip install scapy`

**Important Note**

Running NetProbe requires elevated privileges (root or administrator access) due to its interaction with network interfaces.

**Installation**

1. Clone this repository using `git clone https://github.com/Kushagra0686/NetProbe`.
2. Navigate to the cloned directory: `cd NetProbe`.
3. Install the required Scapy library: `pip install scapy`.

**Usage**

1. Execute the script: `python netprobe.py`.
2. Follow the on-screen prompts:
   - Select the network interface you want to sniff on by entering the corresponding index.
   - Optionally, specify a service protocol (TCP, UDP, or ICMP) to filter captured packets.
   - Choose the number of packets to capture (0 for continuous capture).

**Example Output**

```
Available Interfaces:
1. eth0
2. lo

Enter the index of the interface to sniff on: 1

---------------------------------------------------------------------------------------------------

Enter the service protocol to filter (TCP/UDP/ICMP): tcp

Enter the number of packets to capture (enter 0 for continuous capture, if selected press Ctrl+C to exit): 5

---------------------------------------------------------------------------------------------------

                    ░▒▓█ PACKET 1 █▓▒░

Source IP:          ░▒▓█ REDACTED █▓▒░  -->  Destination IP:        ░▒▓█ REDACTED █▓▒░
Protocol:           TCP
Source Port:        12345           -->  Destination Port:     80
Payload (Hex):
  00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff 00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff
  00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff 00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff

Decoded Payload:
This is an example of a TCP payload.

                    ░▒▓█ PACKET 2 █▓▒░ (and so on...)
```

**Contributing**

We welcome contributions to improve NetProbe! Feel free to submit pull requests for bug fixes, feature enhancements, or documentation improvements.

**Disclaimer**

Use NetProbe responsibly and ethically. It's intended for educational and network analysis purposes only. Do not violate any privacy laws or regulations while using this script.
