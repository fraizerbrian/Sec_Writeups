# VAPT

This is a documentation ofpart of my learning curve and the things that I shall be going through as a PenTester.

## Vapt
- [x] **Information Gathering**
	- [x] Network scan
	- [x] Identify web server, technologies and database
	- [x] Vulnerable versions
- [x] **Exploiting the Various ports**
				PORT      STATE    SERVICE     VERSION
	- [x] 21/tcp    open     ftp         vsftpd 2.3.4
	- [x] 22/tcp    open     ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
	- [x] 23/tcp    open     telnet      Linux telnetd
	- [x] 25/tcp    open     smtp        Postfix smtpd
	- [x] 80/tcp    open     http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
	- [x] 111/tcp   open     rpcbind     2 (RPC #100000)
		- [x] 36349/tcp open     status      1 (RPC #100024)
		- [x] 44733/tcp open     status      1 (RPC #100024)
	- [x] 139/tcp   open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
		- [x] 445/tcp   open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
	- [x] 512/tcp   open     exec        netkit-rsh rexecd
	- [x] 513/tcp   open     login
	- [x] 514/tcp   open     shell       Netapp ONTAP rshd
	- [x] 1099/tcp  open     java-rmi    GNU Classpath grmiregistry
		- [x] 44951/tcp open     java-rmi    GNU Classpath grmiregistry
	- [x] 1524/tcp  open     ingreslock?
	- [x] 2121/tcp  open     ftp         ProFTPD 1.3.1
	- [x] 3306/tcp  open     mysql       MySQL 5.0.51a-3ubuntu5
	- [x] 3632/tcp  open     distccd?
	- [x] 5900/tcp  open     vnc         VNC (protocol 3.3)
	- [x] 6000/tcp  open     X11         (access denied)
	- [x] 6667/tcp  filtered irc
	- [x] 6697/tcp  filtered ircs-u
	- [x] 8009/tcp  open     ajp13       Apache Jserv (Protocol v1.3)
	- [x] 8180/tcp  open     http        Apache Tomcat/Coyote JSP engine 1.1
	- [x] 8787/tcp  open     drb         Ruby DRb RMI (Ruby 1.8; path /usr/lib/ruby/1.8/drb)

## Penetration Testing Course
- [x] Penetration Testing
	- [x] Introduction
	- [x] Kali
	- [x] Recon
	- [x] Scanning
	- [x] Enumeration
	- [x] Metasploit
	- [x] Software Exploitation
	- [x] Post Exploitation
	- [x] Privilege Escalation
	- [x] Persistence
	- [x] Pivoting
	- [x] Sniffing
	- [x] Wifi Attacks
	- [x] Vulnerability Assessment
- [x] Introduction to Web Security
	- [x] Introduction to Web Security
	- [x] Web Application Basics
	- [x] Burp Suite
	- [x] PHP basics
	- [x] OWASP Top 10
	- [x] Server Side Request Forgery (SSRF)
	- [x] Remote Code Execution
	- [x] XXE
	- [x] Remote File Inclusion (RFI)
	- [x] Local File Inclusion (LFI)
	- [x] Unrestricted File Upload
	- [x] SQL Injection
	- [x] Insecure Deserialization
	- [x] IDOR
	- [x] XSS
	- [x] CSRF
	- [x] Attacking JWT
	- [x] Sensitive Data Exposure

## PortSwigger
- [ ] **Server Side Attacks**
	- [x] SQL injection 
	- [x] Authentication
	- [x] Directory Traversal 
	- [ ] Command Injection - _ongoing_
	- [ ] Business Logic Vulnerabilities
	- [ ] Information Disclosure
	- [ ] Access Control
	- [ ] Server-Side Request Forgery
	- [ ] XXE Injection
- [ ] **Client Side Attacks**
	- [ ] Cross-site scripting (XSS)
	- [ ] Cross-site request forgery (CSRF)
	- [ ] Cross-origin resource sharing (CORS)
	- [ ] Clickjacking
	- [ ] DOM-based vulnerabilities
	- [ ] WebSockets
- [ ] **Advanced**
	- [ ] Insecure Deserialization
	- [ ] Server-side template injection
	- [ ] Web cache poisoning
	- [ ] HTTP Host header attacks
	- [ ] HTTP request smuggling
	- [ ] OAuth authentication

## OWASP TOP 10
- [x] Injection
- [ ] Broken Authentication
- [ ] Sensitive Data Exposure
- [ ] XML External Entities (XXE)
- [ ] Broken Access Control
- [ ] Security Misconfiguration
- [ ] Cross-Site Scripting (XXS)
- [ ] Insecure Deserialization
- [ ] Using Components with know Vulnerabilities
- [ ] Insufficient Logging & Monitoring
- [ ] OWASP Documentation

## OWASP Bricks
- [x] Login Pages
- [ ] File Upload Pages
- [ ] Content Pages

## MITRE
- [ ] Mitre ATT&CK documentation

## Attack Vectors
- [ ] DVWA
	- [ ] Brute Fore
	- [ ] Command Execution
	- [ ] CSRF
	- [ ] File Inclusion
	- [ ] SQL Injection
	- [ ] SQL Injection (Blind)
	- [ ] Upload
	- [ ] XSS Reflected
	- [ ] XSS Stored
- [ ] Mutillidae
- [ ] WebDAV
- [ ] phpMyAdmin
- [ ] Twiki


## Networking
- [ ] Network Attacks
