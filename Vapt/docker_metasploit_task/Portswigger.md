# Portswigger writeup

- [ ] **Server Side Attacks**
	- [ ] SQL injection 
	- [ ] Authentication
	- [ ] Directory Traversal
	- [ ] Command Injection
	- [ ] Business Logic Vulnerabilities
	- [ ] Information Disclosure
	- [ ] Access Control
	- [ ] Server-Side Request Forgery
	- [ ] XXE Injection
- [ ] **Client Side Attacks**
	- [ ] Cross-site scripting (XSS)
	- [ ] Cross-site request forgery (CSRF)
	- [ ] Cross-origin resource sharing (CORS)
	- [ ] Clickjacking
	- [ ] DOM-based vulnerabilities
	- [ ] WebSockets
- [ ] **Advanced**
	- [ ] Insecure Deserialization
	- [ ] Server-side template injection
	- [ ] Web cache poisoning
	- [ ] HTTP Host header attacks
	- [ ] HTTP request smuggling
	- [ ] OAuth authentication
	

-----------------------------------------------------------------------------------------

## SQL Injection

> SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database.

An attacker can escalate an SQL injection attack to compromise the underlying server or other back-end infrastructure, or perform a denial-of-service attack.

**Types Of SQLi**

1. **In-band SQLi (Classic SQLi)** - Occurs when an attacker is able to use the same communication channel to both launch the attack and gather results.
	1. `Error-based SQLi` - Relies on error messages thrown by the database server to obtain information about the structure database.
	2. `Union-based SQLi` - Leverages the **UNION** SQL operator to combine the results of two or more **SELECT** statements into a single result which is then returned as part of the HTTP response.
2. **Inferential SQLi (Blind SQLi)** - An attacker is able to reconstruct the database structure by sending payloads, observing the web apps response and the resulting behaviour of the server.
	1. `Boolean-based (content-based) Blind SQLi` - Relies on sending an SQL query to the database which forces the app to return a different result depending on whether the query returns a TRUE or FALSE result.
	2. `Time-based Blind SQLi` - Relies on sending an SQL query to the database which forces the database to wait for a specified amount of time before responding. Response time will indicate to the attacker whether the result of the query is TRUE or FALSE.
3. **Out-of band SQLi** - Depends on features being enabled on the database server being used by the web app and Occurs when an attacker is unable to use the same channel to launch the attack and gather results.

**Detecting SQL injection vulnerabilities**
1. Submitting the single quote character ' and looking for errors or other anomalies.
2. Submitting some SQL-specific syntax that evaluates to the base value of the entry point and to a different value.
3. Submitting Boolean conditions such as  "OR 1=1" and "OR 1=2" and looking for differences in the application's responses.
4. Submitting payloads designed to trigger time delays when executed wuthin an SQL query, and looking for differences in the time taken to respond.
5. Submitting OAST payloads designed to trigger an out-of-band network interaction when executed within an SQL query, and monitoring for any resulting interactions.

**SQL injection in different parts of the query**
1. In *UPDATE* statements within the updated vales or the WHERE clause.
2. In *INSERT* statements within the inserted values.
3. In *SELECT* statements within the table or column name.
4. In *SELECT* statements within the ORDER BY clause.



### **Lab 1: SQL injection UNION attack, determining the number of columns returned by the query**

[https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing an SQL injection UNION attack that returns an additional row containing null values. 

> Solution :

A UNION operator concatenates the results of two queries into a single result set.

Basic Rules for combining results of two queries by using UNION according to [microsoft](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/set-operators-union-transact-sql?view=sql-server-ver15): 

1. The number and the order of the columns must be the same in all queries.
2. The data types must be compatible.

_ORDER BY_ sorts data returned by a query in sql Server. This clause, according to [microsoft]() us used to:

1. Order the result set of a query by the specified column list and limit the rows returned to a specified range.
2. Determine the order in which ranking function values are applied to the result set.

To identify whether the page is prone to SQLi, I can introduce a character to the link such as `'` eg [https://ac511f871e48758f808d4a0e000f0051.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories' ](https://ac511f871e48758f808d4a0e000f0051.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories' )

I get an internal server error hence is susceptible to an SQLi attack.
![](images/sqli/lab1c.png)

I can input a correct character such as `'--` and I have a successful input.

I can check the number of columns using `' UNION select NULL--` whereby NULL represents the number of columns. 

This leads to an internal server error, hence there could be more than one column.

I continue to increase the `NULL` value until the page loads successfully on the third NUL value without breaking.

![](images/sqli/lab1d.png)

### **Lab 2: SQL injection UNION attack finding a column containing text**

[https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform an SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data. 

> Solution:

First of, find the number of columns by using `'+UNION+select+NULL--` till I find the correct number of columns by the number of NULLS used.

I get 3 columns present since I use `'+UNION+select+NULL+NULL+NULL--`
![](images/sqli/lab2a.png)

![](images/sqli/lab2b.png)

![](images/sqli/lab2c.png)

Since I am required to retrieve the text `'de6riv'`, I will be replacing the NULL value with the given text till the page does not crash.
![](images/sqli/lab2d.png)
![](images/sqli/lab2e.png)
![](images/sqli/lab2f.png)

The second column gives a successful load hence the column containing text.

### **Lab 3: SQL injection UNION attack, retrieving data from other tables**
[https://ac1a1fe71f751a9b817192a1004000b4.web-security-academy.net/](https://ac1a1fe71f751a9b817192a1004000b4.web-security-academy.net/)

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform an SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user. 

> Solution:
![](images/sqli/lab3.png)
I'm going to first determine te number of columns available using the `UNION` method or `ORDER BY 1--`
![](images/sqli/lab3a.png)

There are 2 columns since when I add a third column I get an internal server error.

Next up, confirm if the columns accept string values by using `'+UNION+select+'a',+NULL--`. This runs successfully hence first column accepts string values, next confirm the second column together with the first one using `'+UNION+select+'a',+'a--'`

![](images/sqli/lab3b.png)
![](images/sqli/lab3c.png)

I want to retrieve the username and password so that i can be able to login using the administrator user, use `'+UNION+select+username,+password+FROM+users--`

![](images/sqli/lab3d.png)
![](images/sqli/lab3e.png)

Use the Aministrator credentials to  log in 
![](images/sqli/lab3f.png)
![](images/sqli/lab3g.png)

### **Lab 4: SQL injection UNION attack, retrieving multiple values in a single column**

### **Lab 5: SQL injection attack, querying the database type and version on Oracle**

### **Lab 6: SQL injection attack, querying the database type and version on MySQL and Microsoft**

### **Lab 7: SQL injection attack, listing the database contents on non-Oracle databases**

### **Lab 8: SQL injection attack, listing the database contents on Oracle**

### **Lab 9: Blind SQL injection with conditional responses**

### **Lab 10: Blind SQL injection with conditional errors**

### **Lab 11: Blind SQL injection with time delays**

### **Lab 12: Blind SQL injection with time delays and information retrieval**

### **Lab 13: Blind SQL injection with out-of-band interaction**

### **Lab 14: Blind SQL injection with out-of-band data exfiltration**

### **Lab 15: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data**

[https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)

> Solution :
![](images/sqli/lab1a.png)

![](images/sqli/lab1b.png)

When a gift category is selected in the page, eg tech gifts, link would be: `https://ac371f081e4fc1da80be130e00960029.web-security-academy.net/filter?category=Tech+gifts`

The SQL query to retrieve the info would be: `SELECT * FROM products WHERE category = 'Tech gifts' AND released = 1`

Adding a single quote at the end of the query string would result to the following: `?category=Tech+gifts'`

In the SQL query: `SELECT * FROM products WHERE category = 'Tech gifts'' AND released = 1`

This will cause an error as there is one single quote that is not closed

Adding double dash after the quote "--": `?category=Tech+gifts'-- `

In the query string: `SELECT * FROM products WHERE category = 'Tech gifts'--' AND released = 1 `

This would result in showing in all products of category, Tech gifts both released and unreleased would be shown.

To fully show everything in the database:
```
?category=Tech+gifts' or 1=1-- 
SELECT * FROM products WHERE category = 'Tech gifts' or 1=1--' AND released = 1 
```

**Lab: SQL injection vulnerability allowing login bypass**

