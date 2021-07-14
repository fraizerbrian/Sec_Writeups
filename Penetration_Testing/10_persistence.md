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

8. **Mysql-backdoor** (using User Defined Functions UDF)

UDF is a way to extend MySQL with a new function that works like a built-in MySQL; you write a library, put it into a system directory then create the function in MySQL.

**Creating the code**

For each function you would like to include in MySQL, 3 functions are written:

  1. _The Constructor_ : FunctionName_init( UDF_INIT*, UDF_ARGS*,char*);
  2. _The destructor_ : FunctionName_deinit(UDF_INIT*);
  3. _The main function_ : FunctionName( UDF_INIT*, UDF_ARGS*,char*,unsigned long*, char*, char*);
  
_The constructor_ is initialization code that will be executed **before** the _main function_, and is where you should perform input validation, allocate necessary memory, perform other setup tasks etc.

_The destructor_ is executed after your function and is where any cleanup instructions should be placed.

---------------------------
# writeup

###### Challenge Name : **Remote**

Challenge Category : Persistence

Challenge Level : easy

Challenge Description : You want to achieve persistence using Meterpreter’s persistence module by creating an autorun registry file and getting a shell automatically every time the user restarts the PC

Persistence options 

    Minutes after restarting the system: 7 
    Your Local port: 1337
    Your local host IP: 192.168.0.177

Flag format is: xxx xxxxxxx/xxxxx/xxxxxxxx xxxxx_xxxx=xxx  xxxxx=xxxx xxxxx=xxx.xxx.x.xxx

**Solution**

> flag :

