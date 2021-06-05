# URL
> Is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.
URL includes: 
```
foo://example.com:8042/over?there?name=bar#nose
```
		1. Scheme - foo
		2. Authority - example.com:8042
		3. Path - over?there
		4. Query - name=bar
		5. Fragment - nose
	
## Types of Schemes and examples:
1. HTTP
```
  http://:/
  http://:@/path1/path2
  http://:@/path?q1=a&q2=b#URL fragment
```
2. File
```
  file:///etc/passwd
  file:///c:/WINDOWS/win.ini
```

## HTTP
- Application layer protocol used for transferring hyperdata such as HTML.
- Used to communicate between client browser and server.

`HTTP Methods`
1. GET : used to retrieve data from a specified resource, its parameter is included in the URL.
2. POST : used to submit data to the specified resource, data parameters are included in the request body.
3. HEAD : asks the specified resource for a response without a response body.
4. PUT : replaces the specified resource.
5. DELETE : deletes the specified resource.
6. OPTIONS : used to show the available methods for the specified resource.

`HTTP Headers`
1. Accept : indicates which content type the client browser is able to understand.
2. Accept-Language : decides which language the client side could understand.
3. Accept-Encoding : indicates which compression algorithm client side could understand.
4. User-Agent : identify client side OS, browser and version.
5. Host : indicates the target website domain.
6. referrer : provides the link of the previous page where the user came from.
7. Cookie : contains the user cookies names & values.
8. Content-Type : indicates the media type used.
9. Connection : indicates whether the network connection stays open or not after the current request finishes.

`HTTP status codes`
1. 1xx : Informational
2. 2xx : Successful 
3. 3xx : Redirection
4. 4xx : Client Error
5. 5xx : Server Error
- You can make an HTTP request from the terminal using **curl** command. eg :`curl [options] <URL>`

## Cookies
- Small piece of data sent from a website to offer a reliable mechanism for websites to remember stateful information.
- Are important in HTTP Header and can have important data and entry points.

`Cookies Vs Sessions`
**Cookies**
1. Stored on client side.
2. Live longer even if the browser is closed.
3. Less secure.
4. Can only store strings.

**Sessions**
1. Stored on server side.
2. Expire when browser is closed.
3. More secure.
4. Can store objects.
