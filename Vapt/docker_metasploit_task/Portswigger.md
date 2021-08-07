# Portswigger writeup

**PortSwigger**
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

### SQL Injection

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



**Lab: SQL injection UNION attack, determining the number of columns returned by the query**

[https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing an SQL injection UNION attack that returns an additional row containing null values. 

**Lab: SQL injection UNION attack finding a column containing text**

**Lab: SQL injection UNION attack, retrieving data from other tables**

**Lab: SQL injection UNION attack, retrieving multiple values in a single column**

**Lab: SQL injection attack, querying the database type and version on Oracle**

**Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft**

**Lab: SQL injection attack, listing the database contents on non-Oracle databases**

**Lab: SQL injection attack, listing the database contents on Oracle**

**Lab: Blind SQL injection with conditional responses**

**Lab: Blind SQL injection with conditional errors**

**Lab: Blind SQL injection with time delays**

**Lab: Blind SQL injection with time delays and information retrieval**

**Lab: Blind SQL injection with out-of-band interaction**

**Lab: Blind SQL injection with out-of-band data exfiltration**

**Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data**
[https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)

> Solution :

- When a gift category is selected in the page, eg tech gifts, link would be: `https://ac371f081e4fc1da80be130e00960029.web-security-academy.net/filter?category=Tech+gifts`
- The SQL query to retrieve the info would be: `SELECT * FROM products WHERE category = 'Tech gifts' AND released = 1`
- Adding a single quote at the end of the query string would result to the following: `?category=Tech+gifts'`
- In the SQL query: `SELECT * FROM products WHERE category = 'Tech gifts'' AND released = 1`
- This will cause an error as there is one single quote that is not closed
- Adding double dash after the quote "--": `?category=Tech+gifts'-- `
- In the query string: `SELECT * FROM products WHERE category = 'Tech gifts'--' AND released = 1 `
- This would result in showing in all products of category, Tech gifts both released and unreleased would be shown.
- To fully show everything in the database:
```
?category=Tech+gifts' or 1=1-- 
SELECT * FROM products WHERE category = 'Tech gifts' or 1=1--' AND released = 1 
```

**Lab: SQL injection vulnerability allowing login bypass**

