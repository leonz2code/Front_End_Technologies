**************************************************
Python - Decision Making
**************************************************

Single Statement Suites
If the suite of an if clause consists only of a single line, it may go on the same line as the header statement.

Here is an example of a one-line if clause −

#!/usr/bin/python

var = 100
if ( var == 100 ) : print "Value of expression is 100"
print "Good bye!"
When the above code is executed, it produces the following result −

Value of expression is 100
Good bye!

------------
IF
------------

Live Demo
#!/usr/bin/python

var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1

var2 = 0
if var2:
   print "2 - Got a true expression value"
   print var2
print "Good bye!"
When the above code is executed, it produces the following result −

1 - Got a true expression value
100
Good bye!


------------
IF ELSE
------------

Live Demo
#!/usr/bin/python

var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1
else:
   print "1 - Got a false expression value"
   print var1

var2 = 0
if var2:
   print "2 - Got a true expression value"
   print var2
else:
   print "2 - Got a false expression value"
   print var2

print "Good bye!"
When the above code is executed, it produces the following result −

1 - Got a true expression value
100
2 - Got a false expression value
0
Good bye!

------------------------------------
The elif Statement
------------------------------------


The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.

Similar to the else, the elif statement is optional. However, unlike else, for which there can be at most one statement, there can be an arbitrary number of elif statements following an if.

syntax
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
Core Python does not provide switch or case statements as in other languages, but we can use if..elif...statements to simulate switch case as follows −

Example
Live Demo
#!/usr/bin/python

var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"
When the above code is executed, it produces the following result −

3 - Got a true expression value
100
Good bye!

