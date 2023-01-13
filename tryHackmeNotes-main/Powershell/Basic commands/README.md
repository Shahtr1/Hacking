# Powershell

> Shahrukh Tramboo | March 6th, 2022

--------------------------------------

# What is Powershell?

Powershell is the Windows Scripting Language and shell environment that is built using the .NET framework.

Most Powershell commands, called cmdlets, are written in .NET.

The normal format of a cmdlet is represented using Verb-Noun; for example the cmdlet to list commands is called 

Windows powershell saves all previous commands into a file called 
```bash
ConsoleHost_history
```
This is located at 
```bash
%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```



```bash
Get-Command
```

Common verbs to use include:
-	Get
-	Start
-	Stop 
-	Read
-	Write
-	New
-	Out

------------------------------------------

# Basic Powershell Commands

1.	Using Get-Help
Get-Help displays information about a cmdlet. To get help about a particular command, run the following:

```bash
Get-Help Command-Name
```
You can also understand how exactly to use the command by passing in the
```bash
-examples
```
flag

2.	Using Get-Command
Get-Command gets all the cmdlets installed on the current Computer.

```bash
Get-Command Verb-* 
```
or 
```bash
Get-Command *-Noun
```

3.	Object Manipulation

The Pipeline(|) is used to pass output from one cmdlet to another. 
A major difference compared to other shells is that instead of passing text or string to the command after the pipe, powershell passes an object to the next cmdlet.
Verb-Noun | Get-Member

```bash
Get-Command | Get-Member -MemberType Method
```

4.	Creating Objects From Previous cmdlets

One way of manipulating objects is pulling out the properties from the output of a cmdlet and creating a new object.

This is done using the 
```bash
Select-Object
``` 
cmdlet. 

You can also use the following flags to select particular information:

-	first - gets the first x object
-	last - gets the last x object
-	unique - shows the unique objects
-	skip - skips x objects

5.	Filtering Objects
```bash
Where-Object
``` 
to filter based on the value of properties. the general format is
```bash
Verb-Noun | Where-Object -Property PropertyName -operator Value
```

Where -operator is a list of the following operators:
-	-Contains: if any item in the property value is an exact match for the specified value
-	-EQ: if the property value is the same as the specified value
-	-GT: if the property value is greater than the specified value

6.	Sort Object
You do this by pipe lining the output of a cmdlet to the 
```bash
Sort-Object 
```
cmdlet.

7.	Get child directories
```bash
Get-Childitem
```

8. What is the location of the file "interesting-file.txt"?
```bash
Get-ChildItem -Path C:\ -include *interesting-file.txt* -file -recurse
```

9. Specify the contents of this file
```bash
Get-Content "C:\Program Files\interesting-file.txt.txt"
```

10. How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?
```bash
Get-command | where-object -Property CommandType -eq Cmdlet | measure
```

11. Get the MD5 hash of interesting-file.txt
```bash
Get-FileHash -Path "C:\Program Files\interesting-file.txt.txt" -algorithm MD5
```

12. What is the command to get the current working directory?
```bash
Get-Location
```

13. Does the path "C:\Users\Administrator\Documents\Passwords" Exist(Y/N)?
```bash
Get-Location "C:\Users\Administrator\Documents\Passwords"
```

14. What command would you use to make a request to a web server?
```bash
Invoke-WebRequest
```

15. Base64 decode the file b64.txt on Windows. 
```bash
$file = "C:\input.txt"
$data = Get-Content $file
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($data)) | Out-File -Encoding "ASCII" out.html
```

16. Download from server
```bash
cmd.exe 

powershell -c "(new-object System.net.Webclient).DownloadFile('http://10.17.39.185:8000/hello.exe', 'C:\Users\dark\Desktop\hello.exe')"
```


