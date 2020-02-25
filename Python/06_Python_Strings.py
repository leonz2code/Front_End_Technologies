************************************
Python - Strings
************************************

Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes. 
Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable. For example −

var1 = 'Hello World!'
var2 = "Python Programming"

-------------------------------------
Accessing Values in Strings
-------------------------------------

Python does not support a character type; these are treated as strings of length one, thus also considered a substring.

To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring. For example −

Live Demo
#!/usr/bin/python

var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]
When the above code is executed, it produces the following result −

var1[0]:  H
var2[1:5]:  ytho

----------------------------------
Updating Strings
----------------------------------

You can "update" an existing string by (re)assigning a variable to another string. The new value can be related to its previous value or to a completely different string altogether. For example −

Live Demo
#!/usr/bin/python

var1 = 'Hello World!'
print "Updated String :- ", var1[:6] + 'Python'
When the above code is executed, it produces the following result −

Updated String :-  Hello Python

//////////////////////////////////////////////////
Guide for String elements we can use below
//////////////////////////////////////////////////
Escape Characters like + to concatenate
String Special Operators 
String Formatting Operator

---------------------------------------------
Triple Quotes
---------------------------------------------

Python's triple quotes comes to the rescue by allowing strings to span multiple lines, including verbatim NEWLINEs, TABs, and any other special characters.

The syntax for triple quotes consists of three consecutive single or double quotes.

Live Demo
#!/usr/bin/python

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str
When the above code is executed, it produces the following result. Note how every single special character has been converted to its printed form, right down 
to the last NEWLINE at the end of the string between the "up." and closing triple quotes. Also note that NEWLINEs occur either with an explicit carriage 
return at the end of a line or its escape code (\n) −

this is a long string that is made up of
several lines and non-printable characters such as
TAB (    ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [
 ], or just a NEWLINE within
the variable assignment will also show up.

------------------------------------------------
Unicode String
------------------------------------------------

Normal strings in Python are stored internally as 8-bit ASCII, while Unicode strings are stored as 16-bit Unicode. This allows for a more varied set of characters, 
including special characters from most languages in the world. I'll restrict my treatment of Unicode strings to the following −

Live Demo
#!/usr/bin/python

print u'Hello, world!'
When the above code is executed, it produces the following result −

Hello, world!
As you can see, Unicode strings use the prefix u, just as raw strings use the prefix r.

////////////////////////////////////////////////
some Built-in String Methods
////////////////////////////////////////////////


capitalize()
Capitalizes first letter of string

count(str, beg= 0,end=len(string))
Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.

len(string)
Returns the length of the string

lower()
Converts all uppercase letters in string to lowercase.

max(str)
Returns the max alphabetical character from the string str.

min(str)
Returns the min alphabetical character from the string str.

swapcase()
Inverts case for all letters in string.

upper()
Converts lowercase letters in string to uppercase.















