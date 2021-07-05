# PERSISTENCE

After a system is compromised, you will need to ensure that you don't loose the shell.

If used an exploit that messes with the machine the user might want to reboot, and if so happens then you will loose your shell.

If the way to compromise the machine is really complicated or noisy and you don't want to go throught the hassle of doing it all again, create a _backdoor_ that can be used to enter fast and easily.

### Stages of persistence
1. Initial access
  - Exploit, stolen password etc
2. Decisions - what tools to use
  - FUZZY - OS, Environment, Target dependent.
3. Setup
4. Re-accessing of target
5. Cleanup
  - When no longer accessing the machine, cleanup or you will be caught. **Leave no trace**

### Persistence techniques
1. **Create a new user**

If you are root, or someone with that privilege, create a user so you can come back whenever you want.

`adduser Elliot`

`adduser Elliot sudo`

If the machine has ssh you will be able to ssh into the machine.

2. **Crack the password of existing user**

Try to crack the passwords in `/etc/shadow` file. This way is only persistent up until the user changes their password.

3. **SSH Key**

Add key to existing ssh-account.

4. **Cronjob NC**

You can create a cronjob that connects to your machine every 10 minutes.

Read: [ https://ostechnix.com/a-beginners-guide-to-cron-jobs/ ]( https://ostechnix.com/a-beginners-guide-to-cron-jobs/), [http://kaoticcreations.blogspot.com/2012/07/backdooring-unix-system-via-cron.html ](http://kaoticcreations.blogspot.com/2012/07/backdooring-unix-system-via-cron.html)
Use the following tool: [https://crontabgenerator.org/ ](https://crontabgenerator.org/)

5. **Metasploit Persistence module**

Create a binary with malicious content inside.

Run that, get meterpreter shell, run metasploit persistence.

[https://www.offensive-security.com/metasploit-unleashed/binary-linux-trojan/](https://www.offensive-security.com/metasploit-unleashed/binary-linux-trojan/)


6. **Backdoor in webserver**

You can put a cmd or shell-backdoor in a webserver.

Put backdoor on a webserver, either in separate file or in hidden in another file.

7. **Admin account to CMS**

Add an admin account to CMS.

8. **Mysql-backdoor**

[https://pure.security/simple-mysql-backdoor-using-user-defined-functions/ ](https://pure.security/simple-mysql-backdoor-using-user-defined-functions/ )
