# NSLOOPKUP & DIG

> Shahrukh Tramboo | January 28th, 2022

--------------------------------------

**nsloopkup**

```bash
nslookup OPTIONS DOMAIN_NAME SERVER
```
These three main parameters are:
1.	OPTIONS contains the query type
	Querytype							Result
---------------------------------------------------------------
		A 								IPv4 Addresses
	   AAAA								IPv6 Addresses
	   CNAME							Canonical Name
	    MX								Mail Servers
	   	SOA								Start of Authority
	   	TXT								TXT Records

2.	DOMAIN_NAME is the domain name you are looking up.
3.	SERVER is the DNS server that you want to query. You can choose any local or public DNS server to query.
Cloudflare offers 1.1.1.1 and 1.0.0.1
Google offers 8.8.8.8 and 8.8.4.4
Quad9 offers 9.9.9.9 and 149.112.112.112

Example:
```bash
nslookup -type=A tryhackme.com 1.1.1.1
```

**dig**
```bash
dig @SERVER DOMAIN_NAME TYPE
```

1.	SERVER is the DNS server that you want to query.
2.	DOMAIN_NAME is the domain name you are looking up.
3.	TYPE contains the DNS record type, as shown in the table provided earlier.

Example:
```bash
dig @1.1.1.1 tryhackme.com MX
```