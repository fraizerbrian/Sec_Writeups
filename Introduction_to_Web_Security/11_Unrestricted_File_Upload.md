# Unrestricted File Upload

> File upload vulnerability is a common security issue in most web applications that have a file upload feature without any security validation against the uploaded files , this vulnerability could allow attackers to upload a file with malicious code in it , which could be executed on the hosting server . 

 
## Impact
1. Uploading phishing pages into the website 
2. Compromising the hosting server by uploading a shell 
3. Uploading a permanent XSS payload which can compromise users access .
4. Injecting files with malicious paths which can overwrite existing files , as we could upload “.htaccess” file to execute specific files/scripts.

## File Upload Exploitation

