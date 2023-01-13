# YARA

> Shahrukh Tramboo | April 7th, 2022

--------------------------------------

**Introduction to Yara Rules**

Using a Yara rule is simple. Every yara command requires two arguments to be valid, these are:
1) The rule file we create
2) Name of file, directory, or process ID to use the rule for.

Every rule must have a name and condition.

```bash
yara myrule.yar somedirectory
```

yar file example:
```bash
rule examplerule {
	condition: true
}
```

The name of the rule in this snippet is `examplerule`, where we have one condition - in this case, the condition is `condition`.

Simply, the rule we have made checks to see if the file/directory/PID that we specify exists via `condition: true`. If the file does exist, we are given the output of `examplerule`

Let's give this a try on the file "some file" that we made in step one:
```bash
yara myfirstrule.yar somefile
```

-	Yara has a few conditions
	***Keyword***



	***Desc***
	you can use `desc`, short for description, to summarise what your rule checks for.


	***Meta***
	Anything within this section does not influence the rule itself. Similar to commenting code, it is useful to summarise your rule.



	***Strings***
	You can use strings to search for specific text or hexadecimal in files or programs.

	Of course, we need a condition here to make the rule valid. In this example, to make this string the condition, we need to use the variable's name. 
	In this case, `$hello_world`:


	the condition `any of them` allows multiple strings to be searched for,

	```bash
	rule helloworld_checker{
		strings:
			$hello_world = "Hello World!"
			$hello_world_lowercase = "hello world!"
			$hello_world_uppercase = "HELLO WORLD!"

		condition:
			any of them
	}
	```




	***Conditions***
	```bash
	<= less than or equal to
	>= more than or equal to
	!= not equal to
	```

	For example, the rule below would do the following:

	```bash
	rule helloworld_checker{
		strings:
			$hello_world = "Hello World!"

		condition:
			$hello_world <= 10
	}
	```

	The rule will now:
	- Look for the "Hello World!" string
	- Only say the rule matches if there are less than or equal to ten occurrences of the "Hello World!" string



	***Combining keywords***

	```bash
	and
	not
	or
	```

	if you wanted the rule to match if any .txt files with "Hello World!" is found, you can use a rule like below:

	```bash
	rule helloworld_textfile_checker{
		strings:
			$hello_world = "Hello World!"
			$txt_file = ".txt"

		condition:
			$hello_world and $txt_file
	}
	```

-------------------------------------------------------------

**LOKI**

LOKI is a free open source IOC (Indicator of Compromise) scanner created/written by Florian Roth.

Detection is based on 4 methods:

1.	File Name IOC Check
2.	Yara Rule Check (we are here)
3.	Hash Check
4.	C2 Back Connect Check


LOKI can be used on both Windows and Linux systems.

-----------------------------------------------------------------

**yarGen**

yarGen is a generator for YARA rules.

The main principle is the creation of yara rules from strings found in malware files while removing all strings that also appear in goodware files.

Therefore yarGen includes a big goodware strings and opcode database as ZIP archives that have to be extracted before the first use.

 If you are running yarGen on your own system, you need to update it first by running the following command: 
```bash
 python3 yarGen.py --update
```

To use yarGen to generate a Yara rule for file 2, you can run the following command:

```bash
python3 yarGen.py -m /home/cmnatic/suspicious-files/file2 --excludegood -o /home/cmnatic/suspicious-files/file2.yar
```

A brief explanation of the parameters above:

-	`-m` is the path to the files you want to generate rules for
-	`--excludegood` force to exclude all goodware strings (these are strings found in legitimate software and can increase false positives)
-	`-o` location & name you want to output the Yara rule

