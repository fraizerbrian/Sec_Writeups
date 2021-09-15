# Information Gathering

## 1. Conduct Search Engine Discovery Reconnaissance for Information Leakage

| **ID** | WSTG-INFO-01 |

#### Testing

Use a search engine to search for potentially sensitive information including:
		- Network diagrams and configurations.
		- Archived posts and emails by administrators or other key staff.
		- Logon procedures and username formats.
		- Usernames, passwords and private keys.
		- Third-party or cloud service configuration files.
		- Revealing error message contents
		- Development, test, User Acceptance Testing (UAT) and staging versions of sites.

#### Search Engines

Search engine results can vary in a few ways, depending on when the engine last crawled content, and the algorithm the engine uses to determine relevant pages

Search engines to use include:
		- [Baidu](https://www.baidu.com/)
		- [Bing](https://www.bing.com/)
		- [binsearch.info](https://binsearch.info/)
		- [Common Crawl](https://commoncrawl.org/)
		- [DuckDuckGo](https://duckduckgo.com/)
		- [Google](https://www.google.com/)
		- [Internet Archive Wayback Machine](https://archive.org/web/)
		- [Startpage](https://www.startpage.com/)
		- [Shodan](https://www.shodan.io/)

#### Search Operators

> Is a special keyword or syntax that extends the capabilities of regular search queries, and can help obtain more specific results. 

They generally take the form of `operator:query`.

Commonly supported search operators:
		- `site:`
		- `inurl:`
		- `intitle:`
		- `intext:`
		- `filetype:`

eg: `site:owasp.org`

#### Viewing Cached Content

To search for content that has previously been indexed, use the `cache:operator`.

This is helpful for viewing content that may have changed since the time it was indexed, or that may no longer be available. Not all search engines provide cached content to search; the most useful source at time of writing is Google.

To view owasp.org as it is cached, the syntax is: `cache:owasp.org`

#### Google Hacking / Dorking

Operators can be chained to effectively discover specific kinds of sensitive files and information.

A database of dorks, such as Google Hacking Database, is a useful resource that can help uncover specific information. Some categories of dorks available on this database include:
		- Footholds
		- Files containing usernames
		- Sensitive Directories
		- Web Server Detection
		- Vulnerable Files
		- Vulnerable Servers
		- Error Messages
		- Files containing juicy info
		- Files containing passwords
		- Sensitive Online Shopping Info

#### Remediation

1. Carefully consider the sensitivity of design and configuration information before it is posted online.

2. Periodically review the sensitivity of existing design and configuration information that is posted online.

-----------------------------------------------------------------------------------------

## 2. Fingerprint Web Server

> Web server fingerprinting is the task of identifying the type and version of web server that a target is running on.

Discovering the type of web server that an application runs on can enable security testers to determine if the application is vulnerable to attack. 

Servers running older versions of software without up-to-date security patches can be susceptible to known version-specific exploits.

#### Test Objectives

Determine the version and type of a running web server to enable further discovery of any known vulnerabilities.

#### How to Test

Techniques for web server fingerprining include:
		- Banner grabbing
		- Eliciting responses to malformed requests
		- Using automated tools to perform more robust scans that use a combination of tactics.

1. **Banner Grabbing**

A `banner grab` is performed by sending an HTTP request to the web server and examining its response header accomplisheed by using tools such as `telnet`for HTTP requests or `openssl` for requests over SSL.

**Examples**

Response from an Apache Server
```
HTTP/1.1 200 OK
Date: Thu, 05 Sep 2019 17:42:39 GMT
Server: Apache/2.4.41 (Unix)
Last-Modified: Thu, 05 Sep 2019 17:40:42 GMT
ETag: "75-591d1d21b6167"
Accept-Ranges: bytes
Content-Length: 117
Connection: close
Content-Type: text/html
...
```

Response from nginx
```
HTTP/1.1 200 OK
Server: nginx/1.17.3
Date: Thu, 05 Sep 2019 17:50:24 GMT
Content-Type: text/html
Content-Length: 117
Last-Modified: Thu, 05 Sep 2019 17:40:42 GMT
Connection: close
ETag: "5d71489a-75"
Accept-Ranges: bytes
...
```
Response from lighttpd
```
HTTP/1.0 200 OK
Content-Type: text/html
Accept-Ranges: bytes
ETag: "4192788355"
Last-Modified: Thu, 05 Sep 2019 17:40:42 GMT
Content-Length: 117
Connection: close
Date: Thu, 05 Sep 2019 17:57:57 GMT
Server: lighttpd/1.4.54
```

The server type and version is clearly exposed. However, security-conscious applications may obfuscate their server information by modifying the header. eg

```
HTTP/1.1 200 OK
Server: Website.com
Date: Thu, 05 Sep 2019 17:57:06 GMT
Content-Type: text/html; charset=utf-8
Status: 200 OK
...
```

The following is the field order of an Apache server:
		1. Date
		2. Server
		3. Last-Modified
		4. ETag
		5. Accept-Ranges
		6. Content-Length
		7. Connection
		8. Content-Type

In both the nginx and obscured server exampls, the fields in common are:
		1. Server
		2. Date
		3. Content-Type

2. **Sending Malformed Requests**

Web servers may be identified by examining their error responses, and in the cases where they have not been customized, their default error pages.

One way to compel a server to present these is by sending intentionally incorrect or malformed requests.

EG from an Apache server
```
GET / SANTA CLAUS/1.1


HTTP/1.1 400 Bad Request
Date: Fri, 06 Sep 2019 19:21:01 GMT
Server: Apache/2.4.41 (Unix)
Content-Length: 226
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
</body></html>
```

Eg from nginx:
```
GET / SANTA CLAUS/1.1


<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.17.3</center>
</body>
</html>
```
As default error pages offer many differentiating factors between types of web servers, their examination can be an effective method for fingerprinting even when server header fields are obscured.

3. Using Automated Scanning Tools

Automated tools can compare responses from web servers much faster than manual testing, and utilize large databases of known responses to attempt server identification.

Some commonly used scan tools include:
		- Netcraft
		- Nikto
		- Nmap/Zenmap

#### Remediation

Exposed server information can also lead attackers to find version-specific server vulnerabilities that can be used to exploit unpatched servers.

1. Obscuring web server information in headers, such as with Apache’s mod_headers module.
2. Using a hardened reverse proxy server to create an additional layer of security between the web server and the Internet.
3. Ensuring that web servers are kept up-to-date with the latest software and security patches.

-----------------------------------------------------------------------------------------

## 3. Review Webserver Metafiles for Information Leakage

This section describes how to test various metadata files for information leakage of the web application’s path(s), or functionality.

The list of directories that are to be avoided
