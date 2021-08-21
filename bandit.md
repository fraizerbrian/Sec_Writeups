# Bandit

0. Bandit0

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game. 

> Commands you may need to solve this level:
>   ls, cd, cat, file, du, find

- ssh bandit0@bandit.labs.overthewire.org -p 2220
- Password : bandit0
```
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
bandit0@bandit:~$ 

```

1. Bandit1

The password for the next level is stored in a file called - located in the home directory 

> Commands you may need to solve this level:
>   ls, cd, cat, file, du, find


- ssh bandit1@bandit.labs.overthewire.org -p 2220 
- password : boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
bandit1@bandit:~$ 

```

2. Bandit2

The password for the next level is stored in a file called spaces in this filename located in the home directory 

> Commands you may need to solve this level:
>   ls, cd, cat, file, du, find

- ssh bandit2@bandit.labs.overthewire.org -p 2220
- password : CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat 'spaces in this filename'
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
bandit2@bandit:~$ 
```

3. Bandit3

The password for the next level is stored in a hidden file in the inhere directory. 

> Commands you may need to solve this level:
>   ls, cd, cat, file, du, find

- ssh bandit3@bandit.labs.overthewire.org -p 2220
- password : UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
bandit3@bandit:~/inhere$ 
```

4. Bandit4

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command. 

> Commands you may need to solve this level:
>   ls, cd, cat, file, du, find

- ssh bandit4@bandit.labs.overthewire.org -p 2220
- password : pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ file ./-*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
bandit4@bandit:~/inhere$ 
```

5. Bandit5

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
	- human-readable
	- 1033 bytes in size
	- not executable 

> Commands you may need to solve this level: 
> ls, cd, cat, file, du, find 

- ssh bandit5@bandit.labs.overthewire.org -p 2220
- password : koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ find -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

6. Bandit6

The password for the next level is stored somewhere on the server and has all of the following properties:
    - owned by user bandit7
    - owned by group bandit6
    - 33 bytes in size 

> Commands you may need to solve this level:
>  ls, cd, cat, file, du, find, grep

- ssh bandit6@bandit.labs.overthewire.org -p 2220
- password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```
bandit6@bandit:~$ ls
bandit6@bandit:~$ ls -al
total 20
drwxr-xr-x  2 root root 4096 May  7  2020 .
drwxr-xr-x 41 root root 4096 May  7  2020 ..
-rw-r--r--  1 root root  220 May 15  2017 .bash_logout
-rw-r--r--  1 root root 3526 May 15  2017 .bashrc
-rw-r--r--  1 root root  675 May 15  2017 .profile
bandit6@bandit:~$ find / -size 33c -group bandit6 -user bandit7
find: ‘/root’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
find: ‘/home/bandit27-git’: Permission denied
find: ‘/home/bandit29-git’: Permission denied
find: ‘/home/bandit31-git’: Permission denied
find: ‘/lost+found’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/etc/polkit-1/localauthority’: Permission denied
find: ‘/etc/lvm/archive’: Permission denied
find: ‘/etc/lvm/backup’: Permission denied
find: ‘/sys/fs/pstore’: Permission denied
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/26910/task/26910/fd/6’: No such file or directory
find: ‘/proc/26910/task/26910/fdinfo/6’: No such file or directory
find: ‘/proc/26910/fd/5’: No such file or directory
find: ‘/proc/26910/fdinfo/5’: No such file or directory
find: ‘/cgroup2/csessions’: Permission denied
find: ‘/boot/lost+found’: Permission denied
find: ‘/tmp’: Permission denied
find: ‘/run/lvm’: Permission denied
find: ‘/run/screen/S-bandit22’: Permission denied
find: ‘/run/screen/S-bandit0’: Permission denied
find: ‘/run/screen/S-bandit21’: Permission denied
find: ‘/run/screen/S-bandit4’: Permission denied
find: ‘/run/screen/S-bandit18’: Permission denied
find: ‘/run/screen/S-bandit3’: Permission denied
find: ‘/run/screen/S-bandit31’: Permission denied
find: ‘/run/screen/S-bandit23’: Permission denied
find: ‘/run/screen/S-bandit24’: Permission denied
find: ‘/run/screen/S-bandit25’: Permission denied
find: ‘/run/screen/S-bandit20’: Permission denied
find: ‘/run/shm’: Permission denied
find: ‘/run/lock/lvm’: Permission denied
find: ‘/var/spool/bandit24’: Permission denied
find: ‘/var/spool/cron/crontabs’: Permission denied
find: ‘/var/spool/rsyslog’: Permission denied
find: ‘/var/tmp’: Permission denied
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/polkit-1’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/log’: Permission denied
find: ‘/var/cache/apt/archives/partial’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
bandit6@bandit:~$ 
```

7. Bandit7

The password for the next level is stored in the file data.txt next to the word millionth 

> Commands you may need to solve this level:
>   grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- ssh bandit7@bandit.labs.overthewire.org -p 2220
- password : HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ cat data.txt | grep millionth
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
bandit7@bandit:~$ 
```

8. Bandit8

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once 

> Commands you may need to solve this level:
>    grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- ssh bandit8@bandit.labs.overthewire.org -p 2220
- password : cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

9. Bandit9

The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters. 

> Commands you may need to solve this level:
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- ssh bandit9@bandit.labs.overthewire.org -p 2220
- password : UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ strings data.txt | grep ==
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

10. Bandit10

The password for the next level is stored in the file data.txt, which contains base64 encoded data 

> Commands you may need to solve this level:
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- ssh bandit10@bandit.labs.overthewire.org -p 2220
- password : truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
bandit10@bandit:~$ 
```

11. Bandit11

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions 

> Commands you may need to solve this level:
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- ssh bandit11@bandit.labs.overthewire.org -p 2220
- password : IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
bandit11@bandit:~$ 
```

12. Bandit12

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

> Commands you may need to solve this level
> grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

- ssh bandit12@bandit.labs.overthewire.org -p 2220
- password : 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

```
bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ mkdir /tmp/fraize
bandit12@bandit:~$ cp data.txt  /tmp/fraize
bandit12@bandit:~$ cd /tmp/fraize
bandit12@bandit:/tmp/fraize$ xxd -r data.txt data.bin
bandit12@bandit:/tmp/fraize$ zcat data.bin | bzcat | zcat| tar xO | tar xO | bzcat | tar xO | zcat
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
bandit12@bandit:/tmp/fraize$ 
```

13. Bandit13

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

> Commands you may need to solve this level
> ssh, telnet, nc, openssl, s_client, nmap

- ssh bandit13@bandit.labs.overthewire.org -p 2220
- password : 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ ssh bandit14@localhost -i ~/sshkey.private
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
bandit14@bandit:~$ 
```

14. Bandit14

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.
> Commands you may need to solve this level
> ssh, telnet, nc, openssl, s_client, nmap

- ssh bandit14@bandit.labs.overthewire.org -p 2220
- password : 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```
bandit14@bandit:~$ ls
bandit14@bandit:~$ telnet localhost 3000
Trying 127.0.0.1...
telnet: Unable to connect to remote host: Connection refused
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr

Connection closed by foreign host.
bandit14@bandit:~$ 
```

15. Bandit15

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…
> Commands you may need to solve this level
> ssh, telnet, nc, openssl, s_client, nmap
- ssh bandit15@bandit.labs.overthewire.org -p 2220
- password : BfMYroe26WYalil77FoDi9qh59eK5xNr

```
bandit15@bandit:~$ cat /etc/bandit_pass/bandit15 | openssl  s_client -ign_eof -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEHxhZ+zANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjEwODA1MjEyMjEzWhcNMjIwODA1MjEyMjEzWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALqNmx6R
csRsPgzRcRsq5oQ4BC9AT/Yu473WbK4SRjHOWwuA4Oqk9w8SLKYZ39FrDEnXSZJw
xqKPR0AH72+l7Itv7X1H07VbeMTQoJVm6NsJm3cuyyxjRwfaIOUFsRtQQyvQlmw7
3CgTbd3wEk1CD+6jlksJj801Vd0uvZh1VVERAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBADjhbe3bTnDWsS4xt8FFg7PJIqNAxF6QjP+7xzJ4yMvWtPP6tVXo
F7SNI52juwH0nFDyM9KOrM/AknWqCYF+yfz6bLD7MaKZ+Kg3DiLaoVJOrVg6Y02+
0vq1rLsqGko5wamCFamx7X9CtFsV0WQjZdA53Na/VwehtlFpf/p20VAi
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: C896C48D954E03C1BE456D281D9C5A5EC526D07642ABA1260E6E350B28F5DC53
    Session-ID-ctx: 
    Master-Key: 150F726CCEE0EAC69AD784CC6EEED8FC66977E9D7F3FC2618F27D582D0C19C7D3E51F6B7599D73829C63FB08A7E0E481
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 3a a9 fe 3b 12 a1 ed 2b-8d a6 cf aa 23 c9 12 88   :..;...+....#...
    0010 - 9d da cb 5c 52 62 74 23-a3 da a9 eb ef 53 92 08   ...\Rbt#.....S..
    0020 - 3a 21 92 f4 ad 5d 30 0c-9d f2 5a 90 68 36 d7 99   :!...]0...Z.h6..
    0030 - 4c 16 d6 cd c8 99 7a 08-62 5c d9 42 71 88 0c 60   L.....z.b\.Bq..`
    0040 - 52 9c 5d 0b fb 2b a3 fe-7c b2 d8 48 24 be 30 1f   R.]..+..|..H$.0.
    0050 - 70 10 02 5a 18 41 31 62-78 e7 3c e5 44 67 f6 ed   p..Z.A1bx.<.Dg..
    0060 - de 33 6a b3 b5 5f eb 53-83 be 67 7b aa a0 58 c5   .3j.._.S..g{..X.
    0070 - ef 4d 49 78 5a a7 a7 c0-45 ee 24 f4 db a6 4c 3b   .MIxZ...E.$...L;
    0080 - 4d 8d 32 55 cb 78 20 81-4f 4f f0 bb e1 56 55 2d   M.2U.x .OO...VU-
    0090 - 16 82 cd 31 d9 4d fc 91-49 26 4b e7 96 04 8a 1d   ...1.M..I&K.....

    Start Time: 1629547745
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
bandit15@bandit:~$
```

16. Bandit16

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.
>Commands you may need to solve this level
>ssh, telnet, nc, openssl, s_client, nmap

- ssh bandit16@bandit.labs.overthewire.org -p 2220
- password : cluFn7wTiGryunymYOu4RcffSxQluehd
```
bandit16@bandit:~$ nmap -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2021-08-21 14:14 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00025s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31046 -quiet
140098101370944:error:141A10F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:284:
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31518 -quiet
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
cluFn7wTiGryunymYOu4RcffSxQluehd

^C
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31691 -quiet
139690499264576:error:141A10F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:284:
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31790 -quiet
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31960 -quiet
140688244412480:error:141A10F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:284:
bandit16@bandit:~$ rm -rf /tmp/name123
bandit16@bandit:~$ mkdir /tmp/name123
bandit16@bandit:~$ cd /tmp/name123
bandit16@bandit:/tmp/name123$ touch sshkey.private
bandit16@bandit:/tmp/name123$ nano sshkey.private 
Unable to create directory /home/bandit16/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

bandit16@bandit:/tmp/name123$ ssh -i sshkey.private bandit17@localhost
Could not create directory '/home/bandit16/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit16/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'sshkey.private' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "sshkey.private": bad permissions
bandit17@localhost's password: 
Permission denied, please try again.
bandit17@localhost's password: 

bandit16@bandit:/tmp/name123$ chmod 400 sshkey.private 
bandit16@bandit:/tmp/name123$ ssh -i sshkey.private bandit17@localhost
bandit17@bandit:~$ cat /etc/bandit_pass/bandit17
xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
bandit17@bandit:~$ 

```

17. Bandit17

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

>Commands you may need to solve this level
>cat, grep, ls, diff
- ssh bandit17@bandit.labs.overthewire.org -p 2220
- password : xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
```
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
bandit17@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
                                                                                               
┌──(kali㉿kali)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220                                       1 ⨯
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
Linux bandit.otw.local 5.4.8 x86_64 GNU/Linux

      ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org


Welcome to OverTheWire!

If you find any problems, please report them to Steven or morla on
irc.overthewire.org.

--[ Playing the games ]--

  This machine might hold several wargames.
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ and /proc/ is disabled
  so that users can not snoop on eachother. Files and directories with
  easily guessable or short names will be periodically deleted!

  Please play nice:

    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS!
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few usefull tools which you can find
 in the following locations:

    * gef (https://github.com/hugsy/gef) in /usr/local/gef/
    * pwndbg (https://github.com/pwndbg/pwndbg) in /usr/local/pwndbg/
    * peda (https://github.com/longld/peda.git) in /usr/local/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /usr/local/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)
    * checksec.sh (http://www.trapkit.de/tools/checksec.html) in /usr/local/bin/checksec.sh

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us through IRC on
  irc.overthewire.org #wargames.

  Enjoy your stay!

Byebye !
Connection to bandit.labs.overthewire.org closed.
```

18. Bandit18

The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

> Commands you may need to solve this level
> ssh, ls, cat
- ssh bandit18@bandit.labs.overthewire.org
- password : kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```
┌──(kali㉿kali)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat ~/readme"
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
Permission denied, please try again.
bandit18@bandit.labs.overthewire.org's password: 
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
                                                                                               
┌──(kali㉿kali)-[~]
└─$ 
```

19. Bandit19

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
- ssh bandit19@bandit.labs.overthewire.org -p 2220
- password : IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ls -al ./bandit20-do
-rwsr-x--- 1 bandit20 bandit19 7296 May  7  2020 ./bandit20-do
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ls /etc/bandit_pass/bandit*
/etc/bandit_pass/bandit0   /etc/bandit_pass/bandit2   /etc/bandit_pass/bandit30
/etc/bandit_pass/bandit1   /etc/bandit_pass/bandit20  /etc/bandit_pass/bandit31
/etc/bandit_pass/bandit10  /etc/bandit_pass/bandit21  /etc/bandit_pass/bandit32
/etc/bandit_pass/bandit11  /etc/bandit_pass/bandit22  /etc/bandit_pass/bandit33
/etc/bandit_pass/bandit12  /etc/bandit_pass/bandit23  /etc/bandit_pass/bandit4
/etc/bandit_pass/bandit13  /etc/bandit_pass/bandit24  /etc/bandit_pass/bandit5
/etc/bandit_pass/bandit14  /etc/bandit_pass/bandit25  /etc/bandit_pass/bandit6
/etc/bandit_pass/bandit15  /etc/bandit_pass/bandit26  /etc/bandit_pass/bandit7
/etc/bandit_pass/bandit16  /etc/bandit_pass/bandit27  /etc/bandit_pass/bandit8
/etc/bandit_pass/bandit17  /etc/bandit_pass/bandit28  /etc/bandit_pass/bandit9
/etc/bandit_pass/bandit18  /etc/bandit_pass/bandit29
/etc/bandit_pass/bandit19  /etc/bandit_pass/bandit3
bandit19@bandit:~$ ls /etc/bandit_pass/bandit20
/etc/bandit_pass/bandit20
bandit19@bandit:~$ cat /etc/bandit_pass/bandit20
cat: /etc/bandit_pass/bandit20: Permission denied
bandit19@bandit:~$ 
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
bandit19@bandit:~$ 

```

20. Bandit20

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think
> Commands you may need to solve this level
> ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)

- ssh bandit20@bandit.labs.overthewire.org -p 2220
- password : GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
bandit20@bandit:~$ ls -al ./suconnect
-rwsr-x--- 1 bandit21 bandit20 12088 May  7  2020 ./suconnect
bandit20@bandit:~$ echo "GbKksEFF4yrVs6il55v6gwY5aVje5f0j" | nc -l localhost -p 61337 &
[1] 27879
bandit20@bandit:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
bandit20  6016  0.0  0.1  21156  5052 pts/71   Ss   14:16   0:00 -bash
bandit20 10689  0.0  0.0  17004  2992 pts/71   S+   14:25   0:00 man nc
bandit20 10701  0.0  0.0   8196   908 pts/71   S+   14:25   0:00 pager
bandit20 11440  0.0  0.1  21148  4972 pts/87   Ss+  14:27   0:00 -bash
bandit20 23581  0.0  0.1  21148  4976 pts/98   Ss   14:40   0:00 -bash
bandit20 24468  0.0  0.1  21148  4964 pts/40   Ss+  14:43   0:00 -bash
bandit20 26450  0.0  0.1  21148  4908 pts/6    Ss   14:46   0:00 -bash
bandit20 27691  0.0  0.0  17004  2896 pts/98   S+   14:48   0:00 man nc
bandit20 27702  0.0  0.0   8196   876 pts/98   S+   14:48   0:00 pager
bandit20 27879  0.0  0.0   6300  1608 pts/6    S    14:49   0:00 nc -l localhost -p 61337
bandit20 27882  0.0  0.0  19188  2424 pts/6    R+   14:49   0:00 ps aux
bandit20@bandit:~$ ./suconnect 61337
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
bandit20@bandit:~$ gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```

21. Bandit21

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
> Commands you may need to solve this level
> cron, crontab, crontab(5) (use “man 5 crontab” to access this)

- ssh bandit21@bandit.labs.overthewire.org -p 2220
- password : gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```
bandit21@bandit:~$ cd /etc/cron.d
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
bandit21@bandit:/etc/cron.d$ 
```

22. Bandit22

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.
> Commands you may need to solve this level
> cron, crontab, crontab(5) (use “man 5 crontab” to access this)

- ssh bandit22@bandit.labs.overthewire.org -p 2220
- password : Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

```
bandit22@bandit:~$ ls
bandit22@bandit:~$ cd /etc/cron.d/
bandit22@bandit:/etc/cron.d$ ls
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:/etc/cron.d$ myname=bandit23
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh | grep echo mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
grep: mytarget=8ca319486bfbbc3663ea0fbe81326349: No such file or directory
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
bandit22@bandit:/etc/cron.d$ 
```

23. Bandit23

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…
> Commands you may need to solve this level
> cron, crontab, crontab(5) (use “man 5 crontab” to access this)

- ssh bandit23@bandit.labs.overthewire.org -p 2220
- password : jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```
bandit23@bandit:~$ cd /var/spool/bandit24
bandit23@bandit:/var/spool/bandit24$ touch bandit24test.sh
bandit23@bandit:/var/spool/bandit24$ nano bandit24test.sh
Unable to create directory /home/bandit23/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue

bandit23@bandit:/var/spool/bandit24$ chmod 777 bandit24test.sh
bandit23@bandit:/var/spool/bandit24$ cat /tmp/pleasework
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
bandit23@bandit:/var/spool/bandit24$ 
```

24. Bandit24

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

- ssh bandit24@bandit.labs.overthewire.org -p 2220
- password : UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```
bandit24@bandit:~$ ls
bandit24@bandit:~$ nc localhost 30002 UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ****
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.

Fail! You did not supply enough data. Try again.

^C
bandit24@bandit:/$ mkdir /tmp/mydir123
bandit24@bandit:/$ cd  /tmp/mydir123
bandit24@bandit:/tmp/mydir123$ touch bruteforce.sh
bandit24@bandit:/tmp/mydir123$ nano bruteforce.sh
Unable to create directory /home/bandit24/.nano: Permission denied
It is required for saving/loading search history or cursor positions.

Press Enter to continue
andit24@bandit:/tmp/mydir123$ chmod 700 bruteforce.sh
bandit24@bandit:/tmp/mydir123$ ./bruteforce.sh > combinations.txt
bandit24@bandit:/tmp/mydir123$ nc localhost 30002 < combinations.txt
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
...
Wrong! Please enter the correct pincode. Try again.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
bandit24@bandit:/tmp/mydir123$ 

```
copy the following to bruteforce.sh
```
#!/bin/bash
for i in {0000..9999}
do 
	echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i"
done
```
25. Bandit25

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.
> Commands you may need to solve this level
> ssh, cat, more, vi, ls, id, pwd

- ssh bandit25@bandit.labs.overthewire.org -p 2220
- password : uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

```

```
