# PHP

Is a common scripting language used in web development; used in blogging systems on the web(wordpress).

Used in many software frameworks like CakePHP, symfony, Laravel etc.

## PHP Variables and functions
`Variables`
Variables start witha dollar sign ($), there are two types of variables in PHP, user defined variables and built-in variables.
1. `User-defined variables`
```
[1]: $str_variable = "This is my text";
[2]: $numric_variable = 1;
[3]: $boolean_variable = True;
```
2. `Built-in variables`

They are reserved varables in PHP, which can be accessed from anywhere eg inside function, class or file.

They are also known as **PHP superglobals**.
  - $GLOBALS
  - $_SERVER
  - $_REQUEST
  - $_POST
  - $_GET
  - $_FILES
  - $_ENV
  - $_COOKIE
  - $_SESSION

`Functions`
There are two types of functions ie:
1. `User-defined functions`

To declare a function, you need to write the following:
```
function functionName(){
  code to be executed
}
```

2. `Built-in functions`

They are reserved functions that can be used anywhere in the php script.

To use these functions you need to call them by their name with (), and provide the call with the specified arguments for each function.

### PHP cookies and sessions
1. `Cookies`
**Cookies** are the small pieces of data that are stored on the user machine to allow the application server identify the user every time they use the application resources.

To set cookies, you need to use:
`setcookie(cookieName, cookieValue, expirationDate, path)function`
eg
```
setcookie("page_cookie","this is the cookie value", time()+(86400 * 30), "/");
```

To get the cookie value:
```
echo $_COOKIE['page_cookie']; //prints the page_cookie value.
```

2. `Session`
**Sessions** are stored on the server-side with the ability to store objects unline the normal cookies which only store strings.

To use php sessions, call the session_start() at the beginning of the php file.
```
session_start();
?>
```
And set a session
```
$_SESSION['username'] = "khaleed";
```
this creates a session variable with the value "khaleed"

To access this session in the php script you can use the session name.

```
echo $_SESSION['username'];
```

To remove all the session variables and destroy them, use **session_unset()** and **session_destroy()**

## Challenges
1. Cheers
