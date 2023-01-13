# NMAP Post Port Scans

> Shahrukh Tramboo | January 31st, 2022

--------------------------------------

**Service Detection**

Adding -sV to your Nmap command will collect and determine service and version information for the open ports.

You can control the intensity with --version-intensity LEVEL where the level ranges between 0, the lightest, and 9, the most complete.

-sV --version-light has an intensity of 2, while -sV --version-all has an intensity of 9.

It is important to note that using -sV will force Nmap to proceed with the TCP 3-way handshake and establish the connection.

The connection establishment is necessary because Nmap cannot discover the version without establishing a connection fully and communicating with the listening service.

```bash
sudo nmap -sV 10.10.70.158
```

------------------------------------------------------

**OS Detection and Traceroute**

Nmap can detect the Operating System (OS) based on its behaviour and any telltale signs in its responses. 

```bash
sudo nmap -sS -O 10.10.70.158
```

-------------------------------------------------------

**Traceroute**

Note that Nmap’s traceroute works slightly different than the traceroute command found on Linux and macOS or tracert found on MS Windows. Standard traceroute starts with a packet of low TTL (Time to Live) and keeps increasing until it reaches the target. Nmap’s traceroute starts with a packet of high TTL and keeps decreasing it.

```bash
nmap -sS --traceroute 10.10.70.158
```

----------------------------------------------------------

**Nmap Scripting Engine (NSE)**

You can choose to run the scripts in the default category using --script=default or simply adding -sC

Script Category								Description
----------------------------------------------------------

auth									Authentication related scripts
broadcast								Discover hosts by sending broadcast messages
brute									Performs brute-force password auditing against logins
default									Default scripts, same as -sC
discovery								Retrieve accessible information, such as database tables and DNS names
dos										Detects servers vulnerable to Denial of Service (DoS)
exploit									Attempts to exploit various vulnerable services
external								Checks using a third-party service, such as Geoplugin and Virustotal
fuzzer									Launch fuzzing attacks
intrusive								Intrusive scripts such as brute-force attacks and exploitation
malware									Scans for backdoors
safe									Safe scripts that won’t crash the target
version									Retrieve service versions
vuln									Checks for vulnerabilities or exploit vulnerable services

```bash
sudo nmap -sS -sC 10.10.42.100

sudo nmap -sS -n --script "http-date" 10.10.42.100
```
--------------------------------------------------------------

**Saving the Output**

Whenever you run a Nmap scan, it is only reasonable to save the results in a file.

The three main formats are:
1.	Normal
2.	Grepable (grepable)
3.	XML

NORMAL:
```bash
-oN FILENAME
```

GREPABLE:
```bash
-oG FILENAME
```

XML:
```bash
-oX FILENAME
```