# Authentication Vulnerabilities

Among the most critical due to the relationship between authentication and security.

Also allows attackers direct access to sensitive data and functionality, expose additional attack surface for further exploits.

> Authentication is the process of verifying the identity of a given user or client.

There are three authentication factors into which different types of authentication can be categorized:
    1. Something you **know** eg password or answer to security question. Also referred to as `nowledge factors`.
    2. Something you **have** eg a physical object like a mobile phone or a security token. Also referred to as `possession factors`.
    3. Something you **are** or do eg biometrics or patterns of behaviour. Also referred to as `inherence factors`.
    
### Difference between authentication and authorization.
`Authentication` is the process of verifying that a user really is **who they claim to be** whereas `Authorization` involves verifying whether a user is **allowed to do something**
 
### Arising of authentication vulnerabilities.
They arise in one of two ways:
    1. The authentication mechanisms are weak because they fail to protect against brute-force attacks.
    2. Logic flaws or poor coding in the implementation allow the authentication mechanisms to be bypassed entirely by an attacker, also referred to as **broken authentication**.

In many areas of web development, logic flaws will cause the website to behave unexpectedly, which may or may not be a security issue however, the likelihood that flawed authentication logic exposes the website to security issues is elevated.

#### 1.Vulnerabilities in password-based login
Websites that adopt a password-based login process, users either register for an account themselves or they are assigned an account by an administrator, of which the accounts are associated with a unique `username` and `password` which the users use to authenticate themselves.

Can be compromised through:
1. `Brute-force attacks`
> A brute-force attack is when an attacker uses a system of trial and error to attempt to guess valid user credentials.

Attacks are automated using wordlists of usernames and passwords.

Websites that rely on password-based login as their sole method of authenticating users can be highly vulnerable if they do not implement sufficient brute-force protection.
        
2. `Brute-forcing usernames`

Usernames are easy to guess if they conform to a recognizable pattern, such as email address.

Eg it is common to see business logins in the format `firstname.lastname@company.com`. Even though there is no obvious pattern, sometimes even high-privileged accounts are created using predictable usernames such as `admin` or `administrator`.

During auditing, check whether the website discloses potential usernames publicly.

Check HTTP responses to see if any email addresses are disclosed.

Responses may contain email addresses of high-priviledged users like administrators and IT support.
    
3. `Brute-forcing passwords`

Passwords can be brute-forced with the difficulty varying based on the strength of the password.

Enforcing password involves using a:
  1. minimum number of characters.
  2. mixture of lower and uppercase letters.
  3. Atleast one special character.

While high entropy password are difficult for computers alone to crack, one can use a basic knowledge of human behavior to exploit the vulnerabilities that users unwittingly introduce to the system.

Where the policy requires users to change their passwords on a regular basis, it is common for users to to just make minor, predictable changes to their preferred passwords. Eg `Mypassword!` becomes `MyPassword1?` or `mypAssword2.!`
        
4. `Username enumeration`

> Username enumeration is when an attacker is able to observe changes in the website's behaviour in order to identify whether a given username is valid.

Occurs either on the login page or on registration forms when you enter a username that is already taken and greatly reduces the time and effort required to brute-force a login because the attacker is able to quickly generate a shortlist of valid usernames.

During attempts to brute-force a login page, pay attention to:
  1. Status codes.
  2. Error messages.
  3. Response times.
            
5. `Flawed brute-force protection`

The most common ways of preventing brute-force attacks:
   1. Locking the account that the remote user is trying to access if they make too many failed login attempts.
   2. Blocking the remote user's IP address if they make too many login attempts in a quick succession.
   		- Ip may be blocked if one logs in too many times. In some implementations, the counter for number of failed attempts resets if the IP owner logs in successfully.
        
a. `Account Locking`
    
Websites try to prevent brute-forcing is to lock the account if certain suspicious criteria are met, set at a number of failed logins.
    
Responses from the server indicating that an account is locked can also help an attacker to enumerate usernames.
    
Locking an account fails to adequately prevent brute-force attacks in which the attacker is just trying to gain access to any random account they can.
     
**Methods to work around this protection**

1. Establish a list of candidate usernames likely to be valid through username enumeration or list of common names.
2. Decide on a very small shortlist of passwords atleast a user is likely to have and must not exceed number of login attempts allowed.
3. Using tools such as [Burp](https://portswigger.net/burp) intruder, try each of the selected passwords with each of the candidate usernames.

Account locking also fails to protect against credential stuffing attacks which involves using a massive dictionary of `username:password` pairs composed of genuine login credentials stolen in data breaches.
        
b. `User rate limiting`
    
Here, making too many login requests within a short period of time causes your IP add to be blocked.
    
Ip can be unblocked through:
  1. Automatically after a certain period of time has elapsed.
  2. Manually by an administrator.
  3. Manually by the user after successfully completing a CAPTCHA.
  	- Is preferred to account locking due to being less prone to username enumeration and denial of service attacks.
    - As the limit is based on the rate of HTTP requests sent from the user's IP add, it is sometimes also possible to bypass this defense by working out how to guess multiple passwords with a single requests.
    
6. `HTTP basic authentication`

The client receives an authentication token from the server which is constructed by concatenating the username and password, and encoding it in Base64.

The token is stored and managed by the browser, which automatically adds it to the `Authorization` header of every subsequent request as follows:
```
Authorization: Basic base64(username:password)
```

Is not considered a secure authentication method because:

It involves repeatedly  sending the user's login credentials with every request unless the website also implements HSTS, user credentials are open to being captured in a MITM attack.

Implementations of HTTP basic authentication often don't support brute-force protection as the token consists exclusively of static values leaving it vulnerable to being brute-forced.


-----------------------------------------------------------------------------------------------------------

## Labs

Wordlists: 
- [Candidate usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)
- [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)
### **Lab 1: Username enumeration via different responses**

[https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)

This lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the above wordlists

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

> **Solution**

Load the page and open it up on burpsuite, send to intruder, I can enumerate and identify the username first, the payload options used is the one given by PortSwigger [Candidate usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)

![](images/authentication/lab1a.png)
![](images/authentication/lab1b.png)
![](images/authentication/lab1c.png)

The username is `at` since the response given has an `Incorrect password`

Next up is enumerating the password given the username

Place the position of the payload at the password, then load the password list that is given out by PortSwigger [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

![](images/authentication/lab1d.png)
![](images/authentication/lab1e.png)

The password is `tigger`, now is to log into the account

![](images/authentication/lab1f.png)

Successful login with username and email given.

### **Lab 2: Username enumeration via subtly different responses**

This lab is subtly vulnerable to username enumeration and password brute-force attacks.

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

> **Solution**

Run burp and login with incorrect logins then send to burp intruder, first off enumerate the usename by highlighting the incorrect username position, use the snipper attack type, add the usernames given on the payloads tab then on the options tab `Grep - Extract` and add the `Invalid username or password` response then start the attack. Do the same for the password then run the attack
![](images/authentication/lab2a.png)
![](images/authentication/lab2b.png)
![](images/authentication/lab2c.png)
![](images/authentication/lab2d.png)
![](images/authentication/lab2e.png)

The username is `applications` and the password is `pass`
![](images/authentication/lab2f.png)

### **Lab 3: Username enumeration via response timing**

This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

Your credentials: wiener:peter 

> **Solution**

Sending the page to Burp and trying to give multiple logins returns an error that times and gives access to another login after 30 minutes.
![](images/authentication/lab3b.png)

This indicates that ones IP is blocked after too many invalid login attempts. Identify that the X-Forwarded-For header is supported that allows one to spoof their address and bypass the IP-based brute-force protection.

Logging in with the username and password given `wiener:peter `, gives back a 302 redirection error page.
![](images/authentication/lab3c.png)
![](images/authentication/lab3d.png)

When the username is valid, the response time is roughly the same, however, when you enter a valid username `wiener` the response time is increased depending on the length of the password is entered.

Sending the request to Burp Intruder and select the attack type to **"Pitchfork"**, clear the selections and add _X-Forwarded-For_ header and the _username_ set the payload 1 to NUmbers range 1-100 with max fraction digits to 0. This will spoof your IP address preventing IP blocking. For the username add the usernames from the list given.

![](images/authentication/lab3e.png)
![](images/authentication/lab3f.png)

Once the attack is complete, click "Columns" and select "Response received" and "Response completed" options to add them in the results table. The correct username takes slightly longer than others.

![](images/authentication/lab3g.png)

Create a new attack to enumerate for the password, change the username to the found username ie `adserver`. For the passwords payload add from the password list given then start the attack.

Once the attack is done, find the response with a 302 status hence giving the password: `112233`.

Log in with the found username and password to solve the lab.
![](images/authentication/lab3h.png)
![](images/authentication/lab3i.png)

### **Lab 4: Broken brute-force protection, IP block**

![](images/authentication/lab4a.png)
![](images/authentication/lab4b.png)
![](images/authentication/lab4c.png)
![](images/authentication/lab4d.png)
![](images/authentication/lab4e.png)

### **Lab 5: Username enumeration via account lock**

![](images/authentication/lab5a.png)
![](images/authentication/lab5b.png)
![](images/authentication/lab5c.png)
![](images/authentication/lab5d.png)
![](images/authentication/lab5e.png)
![](images/authentication/lab5f.png)
![](images/authentication/lab5g.png)
![](images/authentication/lab5h.png)
![](images/authentication/lab5i.png)

### **Lab 6: Broken brute-force protection, multiple credentials per request**

![](images/authentication/lab6a.png)
![](images/authentication/lab6b.png)

### **Lab 7: 2FA simple bypass**

Log in to your own account ie `wiener:peter`. Your 2FA verification code will be sent to you by email. Click the `"Email client"` button to access your emails. 

Go to your account page and make a note of the URL. 

Log out of your account. 

Log in using the victim's credentials. 

When prompted for the verification code, manually change the URL to navigate to `/my-account?id=carlos`. 

The lab is solved when the page loads. 

### **Lab 8: 2FA broken logic**

With Burp running, log in to your own account and investigate the 2FA verification process. 

Notice that in the POST /login2 request, the verify parameter is used to determine which user's account is being accessed. 

Log out of your account and send the GET /login2 request to Burp Repeater.

Change the value of the verify parameter to carlos and send the request. This ensures that a temporary 2FA code is generated for Carlos. 

Go to the login page and enter your username and password then, submit an invalid 2FA code. 

Send the POST /login2 request to Burp Intruder. 

In Burp Intruder, set the verify parameter to carlos and add a payload position to the mfa-code parameter. 

Brute-force the verification code. Load the 302 response in your browser.

Click "My account" to solve the lab. 
![](images/authentication/lab8.png)
![](images/authentication/lab8a.png)
![](images/authentication/lab8b.png)
![](images/authentication/lab8c.png)

### **Lab 9: 2FA bypass using a brute-force attack**
### **Lab 10: Brute-forcing a stay-logged-in cookie**

This lab allows users to stay logged in even after they close their browser session. The cookie used to provide this functionality is vulnerable to brute-forcing.

To solve the lab, brute-force Carlos's cookie to gain access to his "My account" page.

  - Your credentials: wiener:peter
  - Victim's username: carlos 

Once a user is logged in, and sets the `Stay logged in` to **True**, a cookie is set for that session and the cookie is in **Base64**, once decoded, it comes in the form of `Username+":"+md5Hashpassword`
![](images/authentication/lab10a.png)
![](images/authentication/lab10b.png)
![](images/authentication/lab10c.png)
![](images/authentication/lab10d.png)
![](images/authentication/lab10e.png)
![](images/authentication/lab10f.png)
![](images/authentication/lab10g.png)

### **Lab 11: Offline password cracking**

This lab stores the user's password hash in a cookie. The lab also contains an XSS vulnerability in the comment functionality. To solve the lab, obtain Carlos's stay-logged-in cookie and use it to crack his password. Then, log in as carlos and delete his account from the "My account" page.

  - Your credentials: wiener:peter
  - Victim's username: carlos

This uses a similar functionalit to the stay-logged-in cookie. the stay-logged-in cookie is base64 encoded and is in the format `username+':'+md5hashpassword`

We can steal the victim's user cookie.

The exploit server contains also a stay-logged-in text which when decoded we get the cookie for Carlos' account:
![](images/authentication/lab11.png)

The comments section of the blogs is vulnerable to XSS using `stored XSS` hence one can use the following exploit:
![](images/authentication/lab11a.png)

Exploit the server and use the GET request from the victim containing their 'stay-logged-in' cookie

Using Burp decoder, the result will be:
![](images/authentication/lab11b.png)

copy the hash and use an md5 decoder and it decodes the password as `onceuponatime`
![](images/authentication/lab11y.png)

Log into the Victim's account, go to the victim's account and delete their account.
![](images/authentication/lab11y.png)

### **Lab 12: Password reset broken logic**

This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.

  - Your credentials: wiener:peter
  - Victim's username: carlos

When logging in, click the forgot password section to reset a new password, while running burp.

Click the email client button so as to view the reset password link and reset to any password.
![](images/authentication/lab12w.png)

Since this is intercepted, go to HTTP History and view the `POST /forgot-password-token` request. It contains the password but is hidden.
![](images/authentication/lab12x.png)

Send this to Burp Repeater and delete the _forgot-password-token_ parameter that is on the URL and request body.

Resend the same request from the HTTP history and change the _username_ parameter to _carlos_ and set the new password to any password the send the request.
![](images/authentication/lab12y.png)

In the browser, use the username and login to carlos' account using the reset password.
![](images/authentication/lab12z.png)

### **Lab 13: Password reset poisoning via middleware**

This lab is vulnerable to password reset poisoning. The user carlos will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account. You can log in to your own account using the following credentials: wiener:peter. Any emails sent to this account can be read via the email client on the exploit server.


### **Lab 14: Password brute-force via password change**

This lab's password change functionality makes it vulnerable to brute-force attacks. To solve the lab, use the list of candidate passwords to brute-force Carlos's account and access his "My account" page.

   - Your credentials: wiener:peter
   - Victim's username: carlos 

![](images/authentication/lab14a.png)
![](images/authentication/lab14b.png)
![](images/authentication/lab14c.png)
![](images/authentication/lab14d.png)
![](images/authentication/lab14e.png)
