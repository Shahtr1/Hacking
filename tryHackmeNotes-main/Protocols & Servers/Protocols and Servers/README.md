# Protocols and Servers

> Shahrukh Tramboo | February 1st, 2022

--------------------------------------

**FTP**

FTP also sends and receives data as cleartext; therefore, we can use Telnet (or Netcat) to communicate with an FTP server and act as an FTP client.

A command like STAT can provide some added information. 
The SYST command shows the System Type of the target

PASV switches the mode to passive. It is worth noting that there are two modes for FTP:

1.	Active: In the active mode, the data is sent over a separate channel originating from the FTP server’s port 20.

2.	Passive: In the passive mode, the data is sent over a separate channel originating from an FTP client’s port above port number 1023.

The command TYPE A switches the file transfer mode to ASCII, while TYPE I switches the file transfer mode to binary.

However, we cannot transfer a file using a simple client such as Telnet because FTP creates a separate connection for file transfer.

let’s use an actual FTP client to download a text file
After logging in successfully, we get the FTP prompt, ftp>, to execute various FTP commands.

1.	We used ls to list the files and learn the file name;
2.	then, we switched to ascii since it is a text file (not binary).
3.	Finally, get FILENAME made the client and server establish another channel for file transfer.

----------------------------------------------------------

**Simple Mail Transfer Protocol (SMTP)**

Email delivery over the Internet requires the following components:

1.	Mail Submission Agent (MSA)
2.	Mail Transfer Agent (MTA)
3.	Mail Delivery Agent (MDA)
4.	Mail User Agent (MUA)

Steps:

1.	A Mail User Agent (MUA), or simply an email client, has an email message to be sent. The MUA connects to a Mail Submission Agent (MSA) to send its message.
2.	The MSA receives the message, checks for any errors before transferring it to the Mail Transfer Agent (MTA) server, commonly hosted on the same server.
3.	The MTA will send the email message to the MTA of the recipient. The MTA can also function as a Mail Submission Agent (MSA).
4.	A typical setup would have the MTA server also functioning as a Mail Delivery Agent (MDA).
5.	The recipient will collect its email from the MDA using their email client.

We need to rely on email protocols to talk with an MTA and an MDA. The protocols are:

1.	Simple Mail Transfer Protocol (SMTP)
2.	Post Office Protocol version 3 (POP3) or Internet Message Access Protocol (IMAP)

Simple Mail Transfer Protocol (SMTP) is used to communicate with an MTA server.
Because SMTP uses cleartext, where all commands are sent without encryption, we can use a basic Telnet client to connect to an SMTP server and act as an email client (MUA) sending a message.

SMTP server listens on port 25 by default.
To see basic communication with an SMTP server, we used Telnet to connect to it. Once connected, we issue 
```bash
helo hostname
``` 
and then start typing our email.

```bash
telnet 10.10.165.138 25
```

After helo, we issue 
```bash
mail from:
```
,
```bash
rcpt to:
``` 
to indicate the sender and the recipient. When we send our email message, we issue the command 
```bash
data
``` 
and type our message

----------------------------------------------------------

**Post Office Protocol 3 (POP3)**

Post Office Protocol version 3 (POP3) is a protocol used to download the email messages from a Mail Delivery Agent (MDA) server, as shown in the figure below. The mail client connects to the POP3 server, authenticates, downloads the new email messages before (optionally) deleting them.

POP3 default port 110.

Authentication is required to access the email messages; the user authenticates by providing his credentials

Using the command 
```bash
STAT
```
, we get the reply 
```bash
+OK 1 179
```
; based on RFC 1939, a positive response to STAT has the format 
```bash
+OK nn mm
```
, where nn is the number of email messages in the inbox, and mm is the size of the inbox in octets (byte). 

In general, your mail client (MUA) will connect to the POP3 server (MDA), authenticate, and download the messages.

Accessing the same mail account via multiple clients using POP3 is usually not very convenient as one would lose track of read and unread messages.
To keep all mailboxes synchronized, we need to consider other protocols, such as IMAP.

-------------------------------------------------------------

**Internet Message Access Protocol (IMAP)**

Internet Message Access Protocol (IMAP) is more sophisticated than POP3.

IMAP makes it possible to keep your email synchronized across multiple devices (and mail clients). In other words, if you mark an email message as read when checking your email on your smartphone, the change will be saved on the IMAP server (MDA) and replicated on your laptop when you synchronize your inbox.

Default Port 143

IMAP requires each command to be preceded by a random string to be able to track the reply. So we added c1, then c2, and so on.


Then we listed our mail folders using 
```bash
LIST "" "*"
```
before checking if we have any new messages in the inbox using 
```bash
EXAMINE INBOX
```





