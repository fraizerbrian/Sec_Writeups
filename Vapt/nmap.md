# NMAP

Nmap is an open source utility for network discovery and security auditing.

Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering , what operating systems and OS versions they are running.

When a computer runs a network service, it opens ports to receive the connection.

Ports are necessary for making multiple network requests or having multiple services available.

Network connections are made between 2 ports; an _open listening port_ on the server and a _randomly selected port_ on ones computer.

Every computer has a total of 65535 available ports, however many are registered as standard ports.

Ports can be either: 
  
  1. Open
  2. Closed
  3. Filtered(by firewall)
  
## How to use Nmap

**Command Line**

```
nmap [Scan Type(s)] [Options] {target specification}
```

#### Basic scanning techniques

The `-s` switch determines the type of scan to perform.

| Nmap Switch | Description |
|-------------|-------------|
| -sA | ACK scan |
| -sF | FIN scan |
| -sI | IDLE scan |
| -sL | DNS scan/list scan |
| -sN |	NULL scan |
| -sO |	Protocol scan |
| -sP |	Ping scan |
| -sR |	RPC scan |
| -sS |	SYN scan |
| -sT |	TCP connect scan |
| -sW |	Windows scan |
| -sX |	XMAS scan |

#### Types of scans
| Scan Type | nmap command |
|-----------|--------------|
| Single Target | `nmap [target]` |
| Multiple Targets | `nmap [target1, target2, target3]`|
| List of Targets | `nmap -iL [list.txt]` |
| Range of Hosts | `nmap [range of IPs]` |
| Entire Subnet | `nmap [ip address/cdir]` |
| Random Hosts | `nmap -iR [number]` |
| Exclude Targets | `nmap [targets] --exclude [targets]` |
| Exclude using a list | `nmap [targets] --excludefile [list.txt]` |
| Perform an Aggresive Scan | `nmap -A [target]` |
| Scan an IPv6 Target | `nmap -6 [target]` |
| Run all default scripts | `nmap -sC [target]` |

#### Port Scanning Options
| Scan option | Nmap command |
|-------------|--------------|
| Perform a fast scan | `nmap -F [target]` |
| Scan specific ports | `nmap -p [port(s)] [target]` |
| Scan ports by name | `nmap -p [port name(s)] [target]` |
| Scan ports by protocol | `nmap -sU -sT -p U:[ports],T:[ports] [target]` |
| Scan All ports | `nmap -p 1-65535 [target]` |
| Scan Top Ports | `nmap --top-ports [number] [target]` |
| Perform a sequential port scan | `nmap -r [target]` |
| Attempt to guess an unknown OS | `nmap -O --oscan-guess [target]` |
| Service Version Detection | `nmap -sV [target]` |
| Troubleshoot version scan | `nmap -sV --version-trace [target]` |
| Perform a RPC scan | `nmap -sR [target]` |

#### Discovery Options

**Host Discovery** the `-p` switch determines the type of ping to perform.
| Nmap Switch | Description |
|-------------|-------------|
| -PI | ICMP ping |
| -Po | No ping |
| -PS | SYN ping |
| -PT | TCP ping |


| Ping option | Nmap command |
|-------------|--------------|
| Perform a Ping Only Scan | `nmap -sn [target]` |
| Do not ping | `nmap -Pn [target]` |
| TCP SYN ping | `nmap -PS [target]` |
| TCP ACK ping | `nmap -PA [target]` |
| UDP ping | `nmap -PU [target]` |
| SCTP INIT ping | `nmap -PY [target]` |
| ICMP echo ping | `nmap -PE [target]` |
| ICMP timestamp ping | `nmap -PP [target]` |
| ICMP Address mask ping | `nmap -PM [target]` |
| IP protocol ping | `nmap -PO [target]` |
| ARP ping | `nmap -PR [target]` |
| Traceroute | `nmap --traceroute [target]` |
| Force Reverse DNS resolution | `nmap -R [target]` |
| Disable Reverse DNS resolution | `nmap -n [target]` |
| Alternative DNS lookup | `nmap --system-dns [target]` |
| Manually specify DNS server | `nmap --dns-server [servers] [target]` |
| Create a Host List | `nmap -sL  [targets]` |


#### Firewall Evasion Techniques

| Option | Nmap command |
|--------|--------------|
| Fragment Packets | `nmap -f [target]` |
| Specify a specific MTU | `nmap --mtu [MTU] [target]` |
| Use a decoy | `nmap -D RND:[number] [target]` |
| Idle Zombie Scan | `nmap -sI [zombie] [target]` |
| Manually specify a source port | `nmap --source-port [port] [target]` |
| Append random data | `nmap --data-length [size] [target]` |
| Randomize target scan order | `nmap --randomize-hosts [target]` |
| Spoof MAC address | `nmap --spoof-mac [MAC|0|vendor] [target]` |
| Send bad checksums | `nmap --badsum [target]` |

#### Advanced Scanning functions

| Scan | Nmap command |
|------|--------------|
| Send raw ethernet packets | `nmap --send-eth [target]` |
| Send IP packets | `nmap --send-ip [target]` |
| Custom TCP scan | `nmap --scanflags [flags] [target]` |

#### Timing options
| Option | Nmap command |
|--------|--------------|
| Timing templates | `nmap -T[0-5] [target]` |
| Set the packet TTL | `nmap --ttl [time] [target]` |
| Minimum Number of parallel operations | `nmap --min-parallelism [number] [target]` |
| Maximum number of parallel operations | `nmap --max-parallelism [number] [target]` |
| Minimum host group size | `nmap --min-hostgroup [number] [targets]` |
| Maximum host group size | `nmap --max-hostgroup [number] [targets]` |
| Maximum RTT timeout | `nmap --initial-rtt-timeout [time] [target]` |
| Initial RTT timeout | `nmap --max-rtt-timeout [TTL] [target]` |
| Maximum number of Retries | `nmap --max-retries [number] [target]` |
| Host timeout | `nmap --host-timeout [time] [target]` |
| Minimum scan delay | `nmap --scan-delay [time] [target]` |
| Maximum scan delay | `nmap --max-scan-delay [time] [target]` |
| Minimum packet rate | `nmap --min-rate [number] [target]` |
| Defeat reset rate limit | `nmap --defeat-rst-ratelimit [target]` |


#### Output Options
| Nmap Switch | Description |
|-------------|-------------|
| -oN | Normal output |
| -oX | XML output |
| -oA | Normal, XML, and Grepable format all at once |

##### Other output options
| Option | Nmap command |
|--------|--------------|
| Save output to a Text File | `nmap -oN [scan.txt] [target]` |
| Save output to a XML file | `nmap -oX [scan.xml] [target]` |
| Grepable output | `nmap -oG [scan.txt] [target]` |
| Output all supported file types | `nmap -oA [path/filename] [target]` |
| Periodically display statistics | `nmap --stats-every [time] [target]` |
| 1337 Output | `nmap -oS [scan.txt] [target]` |

#### Compare Scans
| Option | Nmap Command |
|--------|--------------|
| Comparison Using Ndiff | `ndiff [scan1.xml] [scan2.xml]` |
| Ndiff verbose mode | `ndiff -v [scan1.xml] [scan2.xml]` |
| XML output mode | `ndiff --xml [scan1.xml] [scan2.xml]` |

#### Troubleshooting and Debugging
| Option | Nmap Command |
|--------|--------------|
| Get Help | `nmap -h` |
| Verbose Output | `nmap -v [target]` |
| Debugging | `nmap -d [target]` |
| Display Port state reason | `nmap --reason [target]` |
| Only display open ports | `nmap --open [target]` |
| Trace packets | `nmap --packet-trace [target]` |
| Display Host Networking | `nmap --iflist` |
| Specify a network interface | `nmap -e [interface] [target]` |

#### Nmap Scripting Engine
| Option | Nmap Command |
|--------|--------------|
| Execute Individual Scripts | `nmap --script [script.nse] [target]` |
| Execute Multiple Scripts | `nmap --script [expression] [target]` |
| Execute Scripts by category | `nmap --script [category] [target]` |
| Execute Multiple Script Categories | `nmap --script [category1, category2, etc]` |
| Troubleshoot scripts | `nmap --script [script] --script-trace [target]` |
| Update the Script Database | `nmap --script-updatedb` |


Nmap Practice [https://tryhackme.com/room/furthernmap](https://tryhackme.com/room/furthernmap)


