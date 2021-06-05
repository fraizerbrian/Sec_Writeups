# Burp suite

Web application testing and attack tool with alot of different features that help web pentesters in their testing process.

Burp's main feature is to intercept HTTP requests, you can modify the request and monitor the response to check any change, also you can try to bruteforce parameters values.

## Configuring browser proxy
1. Open firefox ie preferences - Network Settings - Settings
2. Select the **Manual Proxy COnfiguration** and enter **127.0.0.1** in the **HTTP Proxy** box.
3. Enter **8080** in the **Port** input box.
4. Clear the **No Proxy For** input box, and click **OK**.

## Burp Features
1. Target
  - You will find all visited domain that burp proxy intercepted.
2. Proxy 
  - You can monitor the intercepted requests here.
3. Intruder
  - Tool for automating customized attacks against web applications eg snipper attacks.
4. Repeater
  - Saves your time with proxy, to modify the same request for as many times as you ant and it will show you the response.
5. Decoder
  - One can decode/encode any type of the encoding scheme.
