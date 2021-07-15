# RCE - Remote Code Execution

> Is a vulnerability that can be exploited if user input is injected into a File or a String and executed/evaluated by the programming language's parser.

A Remote Code Execution can lead to a full compromise of the vulnerable web application and also web server.

A code evaluation can occur if you allow user input inside functions that are evaluating code in the respective programming language.

This can be implemented accidentally because user controlled input is not expected from the developer inside those functions.

 **Example of Code Evaluation Exploitaion**

You want to have dynamically generated variable names for every user and store its registration date. It looks as below:
```
eval("\$$user = '$regdate');
```

Since the username is generally user controlled input an attacker can generate a name as below:
```
x= 'y';phpinfo();//
```
The resulting php code would now look as below:
```
$x = 'y';phpinfo();// = '2016';
```
The variable is now called `x` and has the value `y`. After the attacker was able to assign that value to the variable he/she is able to start a new command by using the semicolo(;).

He can now comment out the rest of the string so he doesn't get syntax errors.

If he executes this code, the output of phpinfo will appear on the page. 

### Stored RCE
This method doesn't rely on any specific language function but on the fact that specific files are parsed by the language's interpreter.

Eg for this would be a configuration file that is included in a web application, avoid using user input files that are executed by an interpreter as this can lead to unwanted behaviour.

This kind of exploit technique is often seen in combination with an upload functionality that doesn't do the sufficient checks on file types and extensions.

**Example of Stored Code Evaluation Exploitation**

Develop a web application that has a control panel for every user.The control panel has some user specific settings such as the language variable, ie set depending on a parameter and then stored inside a configuration file.

An expected input could be as;

```
?language=de
```
The above will then be reflected as `$_lan_='de';` inside the configuration file. An attacker could now change the language parameter to something as below:
```
de';phpinfo()//
```
The above would result in the following code inside the file;
```
$lan = 'de';phpinfo()//';
```
The above will be executed when the configuration file is included in the web application, basically allowing the attackers to execute any command they want.

### Impacts of RCE
An attacker who is able to execute such a flaw is usually able to execute commands with the privileges of the programming language or the web server and can issue system commands, write, delete or read files or connect to databases.

### Preventing RCE 
Avoid using user input inside evaluated code.

Never let a user edit the content of files that might be parsed by the respective languages, including not letting a user decide the name and extensions of files he or she might upload or create in the web application.

### What Not to do to prevent RCE
1.


