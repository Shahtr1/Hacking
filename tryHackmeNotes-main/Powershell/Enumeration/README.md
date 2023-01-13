> Shahrukh Tramboo | March 13th, 2022

--------------------------------------

**Enumeration**

1.	How many users are there on the machine?
```bash
Get-LocalUser
```

2.	Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?
```bash
Get-LocalUser -sid "S-1-5-21-1394777289-3961777894-1791813945-501"
```

3.	How many users have their password required values set to False?
```bash
Get-LocalUser | where-object -Property PasswordRequired -Match false
```

4.	How many local groups exist?
```bash
Get-LocalGroup | measure
```

5.	What command did you use to get the IP address info?
```bash
Get-NetIPAddress
```

6.	How many ports are listed as listening?
```bash
Get-NetTCPConnection | where-object -Property State -eq Listen | measure
```

7.	How many patches have been applied?
```bash
Get-Hotfix | measure
```

8.	Find the contents of a backup file.
```bash
Get-Childitem -Path C:\ -include *.bak* -file -recurse
```

9.	Search for all files containing API_KEY
```bash
Get-ChildItem C:\* -Recurse | Select-String -pattern API_KEY
```

10.	What command do you do to list all the running processes?
```bash
Get-Process
```

11.	What is the path of the scheduled task called new-sched-task?
```bash
Get-ScheduledTask | Where-Object -Property TaskName -eq new-sched-task
```

12.	Who is the owner of the C:\?
```bash
Get-Acl C:\
```

