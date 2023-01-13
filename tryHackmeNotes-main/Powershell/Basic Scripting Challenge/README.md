> Shahrukh Tramboo | March 13th, 2022

--------------------------------------

# Using Powershell ISE

1.	Given a list of port numbers, we want to use this list to see if the local port is listening.
```bash
$system_ports = Get-NetTCPConnection -State Listen

$text_port = Get-Content -Path C:\Users\Administrator\Desktop\ports.txt

foreach($port in $text_port){

    if($port -in $system_ports.LocalPort){
        echo $port
     }

}
```

2.	Make a script to know, How many open ports did you find between 130 and 140(inclusive of those two)?
```bash
$target = 'localhost'
for ($port = 130; $port -le 140; $port++){
    Test-NetConnection -InformationLevel "Detailed" -Port $port
}
```
