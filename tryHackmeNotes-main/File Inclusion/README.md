# File Inclusion

> Shahrukh Tramboo | January 12th, 2022

--------------------------------------

**Path Traversal**

Below are some common OS files you could use when testing.


contains a message or system identification to be printed before the login prompt.
```bash
/etc/issue
```


controls system-wide default variables, such as Export variables, File creation mask (umask), Terminal types, Mail messages to indicate when new mail has arrived
```bash
/etc/profile
```


specifies the version of the Linux kernel
```bash
/proc/version
```


has all registered user that has access to a system
```bash
/etc/passwd
```


contains information about the system's users' passwords
```bash
/etc/shadow
```


contains the history commands for root user
```bash
/root/.bash_history
```


contains global system messages, including the messages that are logged during system startup
```bash
/var/log/dmessage
```


all emails for root user
```bash
/var/mail/root
```


Private SSH keys for a root or any known valid user on the server
```bash
/root/.ssh/id_rsa
```


the accessed requests for Apache  webserver
```bash
/var/log/apache2/access.log
```


contains the boot options for computers with BIOS firmware
```bash
C:\boot.ini
```



The below function causes path traversal vulnerabilities in PHP
```bash
file_get_contents
allow_url_fopen  
allow_url_include
```






