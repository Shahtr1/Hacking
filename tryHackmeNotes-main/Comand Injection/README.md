# Command Injection

> Shahrukh Tramboo | January 27th, 2022

--------------------------------------

**Remediating Command Injection**

Vulnerable Functions:

In PHP, many functions interact with the operating system to execute commands via shell; these include:

1.  Exec
2.	Passthru
3.	System

It should be processed like this, to prevent command injection

```bash
<input type="text" id="ping" name="ping" pattern="[0-9]+" />
<?php
echo passthru("/bin/ping -c 4 " . $_GET["ping"] . ");
```

Input sanitisation:
```bash
<?php
if(!filter_input(INPUT_GET, "number", FILTER_VALIDATE_NUMBER)){

}
```


Bypassing Filters:
An application may strip out quotation marks; we can instead use the hexadecimal value of this to achieve the same result.

```bash
$payload = "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"
```

