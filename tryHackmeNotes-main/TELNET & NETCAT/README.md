# TELNET & NETCAT

> Shahrukh Tramboo | January 28th, 2022

--------------------------------------

**telnet**

```bash
telnet 10.10.248.160 80
Trying 10.10.248.160...
Connected to MACHINE_IP.
Escape character is '^]'.
GET / HTTP/1.1
host: telnet
```

**netcat**
```bash
nc 10.10.151.136 80
GET / HTTP/1.1
host: netcat
```
Note that you might need to press SHIFT+ENTER after the GET line.