# Curl commands

> Shahrukh Tramboo | January 26th, 2022

--------------------------------------

**SSRF Examples**

payload ending in 
```bash
&x=
``` 

being used to stop the remaining path from being appended to the end of the attacker's URL and instead turns it into a parameter (?x=) on the query string.


**Finding SSRF**

1.	When a full URL is used in a parameter in the address bar:
```bash
https://website.thm/form?server=http://server.website.thm/store
```

2.	A hidden field in a form:
```bash
<input type="hidden" name="server" value="http://server.website.thm/store">
```

3.	A partial URL such as just the hostname:
```bash
https://website.thm/form?server=api
```


4.	Or perhaps only the path of the URL:	
```bash
https://website.thm/form?dst=/forms/contact
```

NOTE: use requestbin.com for HTTP logging

In a cloud environment, it would be beneficial to block access to the IP address 169.254.169.254, which contains metadata for the deployed cloud server, including possibly sensitive information. 




