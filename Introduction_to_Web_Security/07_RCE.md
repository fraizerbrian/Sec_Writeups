# Remote Code Execution (RCE)

> RCE or Remote Code Execution is a vulnerability that allows the attacker to run arbitrary code on the hosting server by sending OS commands or even a malicious code which will be executed by the server that finally would lead him to fully compromise the server resources .

There are two types , `code injection` and `command injection` , the main difference between both is that the **code injection** depends on the capabilities of the used programming language .

## Impact
1. Read, add, modify, delete server files
2. Change access privileges, passwords
3. Turn on/off configurations and services
4. Communicate to other servers

## RCE basics
Some languages like php provide several functions that allow shell command execution on the server .

The following is a list for the common used functions for this purpose :

Function | Description 
---------|------------
System | Executes a command and returns its output
shell_exec | Executes a command and displays the output immediately
passthru | Executes a command and displays the raw output
Backtick operator | Executes contents inside the backtick as a shell command
exec | Executes a command and returns the last line of the output
pcntl_exec | Executes a command or a program

```
<?php
	$dir = $_GET['dir'];
	$cmd = 'ls images/' , $dir;
	echo system($cmd);
?>
```

The above code snippet will get the directory name from the user and within the system function it will execute ls command .

There are some command separators can be used to inject OS commands in that code 

  - &
  - &&
  - |
  - ||
  - ;
  - Newline (0x0a or \n)

The attacker can send payload as below:
```
http://example.com/home/?dir=test ; cat /etc/passwd
```

This payload will end the used ls command in the application code and will execute the next command that we injected , which will return the content of the /etc/passwd file.

## Advanced bypass techniques
```
<?php
if(preg_match('/system|exec|passthru|[\"\'"]/', $_GET['cmd'])){
	echo "invalid syntax";
}else{
	eval($_GET['cmd']);
}
?>
```

The above code validates the user input against the specified php functions and double or single quotes.

The eval() function will execute its input as a PHP code.

One of the bypass techniques for this case is using dividing the function name into sections between each. We will put a dot eg:
```
?cmd=(sy.(st).em)(whoami);
```

This payload will bypass the preg_match() function and php will concatenate the function name then it will be executed .

### Wildcard technique

Some WAFs can detect RCE payloads like cat , ls , echo ,etc.

But there is another technique that can be used to bypass these WAFs .

There are some shell wildcards that can bypass the WAFs .

Get to know some basics of these wildcards :

  - ? : the question mark matches any single character 
  - * : the asterisk matches any number of characters or even zero .
  - [ ] : brackets enclose a set of characters that may match a single character at the specified position
  - [a - z] : this type of brackets uses the hyphen ( - ) , and it will match any character found in the specified range , like example from a to z .

### RCE through image file 

In some cases the web application could be using imagemagick to deal with the uploaded images .

There is a CVE-2016–3714 for imagemagick that could lead the attacker to RCE 

Attacker could upload the following file.mvg which would successfully execute OS commands on the application server.

## Mitigation
The best mitigation technique is to avoid using the command execution functions , however if it is necessary to use them you should make sure of the following :
- Sanitize and validate input
- Validate returned data
- Validate the user input against a whitelist 

