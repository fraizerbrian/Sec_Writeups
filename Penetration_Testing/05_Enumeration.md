# ENUMERATION

Is a phase of pentesting including all the information collected and can be directly used for system exploitation.

It is the process of extracting usernames, machine names,NetBIOS, DNS details, network resources, shares, IP tables, routing tables, SNMP, and services from a system or network.

### Service Enumeration
Many scanners capable of performing TCP, UDP, SMTP, RPC and ICMP scans to identify the services, service pack and sessions informationfor clients, servers and applications.

Information collected from the service interaction with the port operating the role like:

| TCP 445 | SMB |
| TCP/UDP 389 | LDAP |
| TCP 137 | NetBIOS name |
| TCP 3389 | Terminal service and remote desktop |
| UDP 161 | SNMP |
| TCP 53 | DNS zone transfer |

### NetBIOS Enumeration

NetBIOS stands for Network Basic Input-Output System, originally an API for client software to access LAN resources.

Enumerating the target network using NetBIOS would extract a lot of sensitive information about the target such as users and network shares.

NetBios uses UDP port 137 (name services), UDP port 138 (datagram services), and TCP port 139 (session services).

NetBIOS is easy to exploit and run on Windows systems even when not in use.

**nbtscan Tool**

Is a command-line tool that scans for open NETBIOS could be installed in windows/Linux systems and running NETBIOS scan against machines on the local network.

### LDAP Enumeration


-----------------------------------
# Writeup
Challenge Name : Hidden

Challenge Category : Machines

Challenge Level : Basic

Challenge Description : 

Can you find the hidden directory on the target web app

Target IP: 3.67.198.136

flag just directory name 

> flag secret
