# Sniffing

> Sniffing attack or a sniffer attack, in context of network security, corresponds to theft or interception of data by capturing the network traffic using a sniffer (an application aimed at capturing network packets). 
    
When data is transmitted across networks, if the data packets are not encrypted, the data within the network packet can be read using a sniffer.

Using a sniffer application, an attacker can analyze the network and gain information to eventually cause the network to crash or to become corrupted, or read the communications happening across the network.

## Sniffing Tools

1. **Wireshark** : An opensource packet capturer and analyzer. It supports Windows, Linux etc. and is a GUI based tool (alternate to Tcpdump). It used pcap to monitor and capture the packets from the network interface. The packets can be filtered basis IP, protocol, and many other parameters.

2. **dSniff** : It is used for network analysis and password sniffing from various network protocols. It can analyze a variety of protocols (FTP, Telnet, POP, rLogin, Microsoft SMB, SNMP, IMAP etc) for getting the information.

3. **Debookee** : It is a paid tool that can be used to monitor and analyze the network. It is able to intercept and analyze the traffic from devices that are in that subnet, irrespective of the device type (Laptop, devices, TV etc).

### Some of the Sniffing Attack Implementations
1. **MAC flooding** : Flood the CAM table with fake MAC addresses so it overflowed the table, and the sniffing could be done.
2. **DNS cache poisoning** : Altering the DNS cache records so that it redirects the request to a malicious website where the attacker can capture the traffic.
3. **MAC spoofing**: The attacker can gather the MAC address(s) that are being connected to the switch. The sniffing device is set with the same MAC address so that the messages that are intended for the original machine are delivered to the sniffer machine since it has the same MAC address set. 

## Man in The Middle

> A man-in-the-middle attack (MITM) is an attack where the attacker secretly relays and possibly alters the communications between two parties who believe that they are directly communicating with each other.

####Types of Man-in-the-Middle Attacks
1. **IP spoofing** : The act of creating an IP packet with a forged source IP address for the purpose of hiding the true source IP address, usually for the purpose of launching special types of distributed denial-of-service (DDoS attacks)or an attacker can trick you into thinking you’re interacting with a website or someone you’re not.
2. **Email hijacking**: The hacker compromises and gain access to a target’s email account. The attacker then silently monitors the communications between the client and the provider and uses the information for malicious purposes.
3. **Wi-Fi eavesdropping**: Also known as an “_evil twin_” attack, that tricks unsuspecting victims into connecting to a malicious Wi-Fi network. To perform Wi-Fi eavesdropping, a hacker sets up a Wi-Fi hotspot near a location where people usually connect to a public Wi-Fi network. This can be a hotel, a restaurant, or your local Starbucks. The hacker then names the hotspot after the actual public network that people use in that location (thus the name “evil twin”).
4. **Stealing browser cookies** : A cybercriminal can hijack browser cookies. Since cookies store information from your browsing session, attackers can gain access to your passwords, address, and other sensitive information.

#### Man-in-the-Middle Attacks Tool
This tool [https://github.com/SySS-Research/Seth](https://github.com/SySS-Research/Seth)attempts to downgrade the connection in order to extract clear text credentials. 

----------------------------------------------------------
# Writeups
## Challenge Name : Capture

Challenge Category : General Information

Challenge Level : easy

Challenge Description : Network analysis tool used to captured packets and present it in readable format

> Flag : wireshark
