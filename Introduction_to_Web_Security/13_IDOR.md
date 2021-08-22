# Insecure Direct Object Reference (IDOR)

This vulnerability occurs when the web application provides a direct access to objects based on user-input.

## Impact

IDOR vulnerability allows attackers to bypass authorization and access resources in the system directly using object reference.

## Testing

You need to identify where object references may occur.

1. **Example 1**

Assume we have a web application that allows you to write a document and gives you a reference to it in the URL.
```
http://example.com/docs/write?doc=1025
```
The doc parameter allows you to access your document using a number (1025).

You can simply try different values for this parameter and check if you can view documents not belonging to you.

You can do that manually or by writing your own script.

eg
![](images/idor1.png)

This script will check if it checks if it gets status code 200 after changing the number value every time.

2. **Example 2**
```
http://example.com/profile/user/3002/page.php
```

```
http://example.com/profile/?user=3002
```
Assume that we have a web application that identifies the user profile by a number reference.

If there is no validation against this reference or any security roles the attacker can easily gain access to users profiles using the number reference.

3. **Example 3**

Assume we have a web application that changes user password using the user id that refers to his record in the database.

Simply the attacker can abuse this functionality and try to change the password for another user account by modifying the id number, then he can easily gain full access to the user account.

## Mitigation

According to owasp prevention sheet , you need to use a hash value instead of a direct number value, this hash will be salted with a value defined at the application level.

This will prevent attacker from enumerating application resources (profiles, accounts etc )

## Challenges
1. Silly Doors
