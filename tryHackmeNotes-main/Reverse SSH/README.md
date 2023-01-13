# Reverse SSh

> Shahrukh Tramboo | February 15th, 2022

--------------------------------------

Reverse SSH port forwarding specifies that the given port on the remote server host is to be forwarded to the given host and port on the local side.

1.	-L is a local tunnel (YOU <-- CLIENT). If a site was blocked, you can forward the traffic to a server you own and view it

For example, if imgur was blocked at work, you can do 
```bash
ssh -L 9000:imgur.com:80 user@example.com.
``` 
Going to localhost:9000 on your machine, will load imgur traffic using your other server.

2.	-R is a remote tunnel (YOU --> CLIENT). You forward your traffic to the other server for others to view. Similar to the example above, but in reverse.

We will use a tool called ss to investigate sockets running on a host.

If we run 
```bash
ss -tulpn 
```
it will tell us what socket connections are running

Argument	Description
------------------------------------------
-t			Display TCP sockets
-u			Display UDP sockets
-l			Displays only listening sockets
-p			Shows the process using the socket
-n			Doesn't resolve service names


We can see that a service running on port 10000 is blocked via a firewall rule from the outside (we can see this from the IPtable list).

However, Using an SSH Tunnel we can expose the port to us (locally)!

From our local machine, run 
```bash
ssh -L 10000:localhost:10000 <username>@<ip>
```

Once complete, in your browser type "localhost:10000" and you can access the newly-exposed webserver.




