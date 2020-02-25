Usa Anaconda y de anaconada Spypder para ejecutar test en Python

***************************************************
Lines and Indentation
***************************************************

Python provides no braces to indicate blocks of code for class and function definitions or flow control.
Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example −

if True:
print "True"
else:
print "False"

***************************************************
Multi-Line Statements
***************************************************

Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character (\) to denote that the line should continue. For example −

total = item_one + \
item_two + \
item_three

Statements contained within the [], {}, or () brackets do not need to use the line continuation character. For example −

days = ['Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday']

***************************************************
Quotation in Python
***************************************************

Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all the following are legal −

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

***************************************************
Comments in Python
***************************************************

A hash sign (#) that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.

Live Demo
#!/usr/bin/python

# First comment
print "Hello, Python!" # second comment
This produces the following result −

Hello, Python!
You can type a comment on the same line after a statement or expression −

name = "Madisetti" # This is again comment
You can comment multiple lines as follows −

# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.
Following triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments:

'''
This is a multiline
comment.
'''
***************************************************
Using Blank Lines
***************************************************

A line containing only whitespace, possibly with a comment, is known as a blank line and Python totally ignores it.

In an interactive interpreter session, you must enter an empty physical line to terminate a multiline statement.

***************************************************
Waiting for the User
***************************************************

The following line of the program displays the prompt, the statement saying “Press the enter key to exit”, and waits for the user to take action −

#!/usr/bin/python

raw_input("\n\nPress the enter key to exit.")
Here, "\n\n" is used to create two new lines before displaying the actual line. Once the user presses the key, the program ends. This is a nice trick
to keep a console window open until the user is done with an application.

***************************************************
Multiple Statements on a Single Line
***************************************************

The semicolon ( ; ) allows multiple statements on the single line given that neither statement starts a new code block. Here is a sample snip using the semicolon −

import sys; x = 'foo'; sys.stdout.write(x + '\n')

***************************************************
Multiple Statement Groups as Suites
***************************************************

A group of individual statements, which make a single code block are called suites in Python. Compound or complex statements,
such as if, while, def, and class require a header line and a suite.

Header lines begin the statement (with the keyword) and terminate with a colon ( : ) and are followed by one or more lines which make up the suite.
For example −

if expression :
suite
elif expression :
suite
else :
suite

***************************************************
Assigning Values to Variables
***************************************************

Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example −

Live Demo
#!/usr/bin/python

counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "John" # A string

print counter
print miles
print name
Here, 100, 1000.0 and "John" are the values assigned to counter, miles, and name variables, respectively. This produces the following result −

100
1000.0
John

***************************************************
Multiple Assignment
***************************************************

Python allows you to assign a single value to several variables simultaneously. For example −

a = b = c = 1
Here, an integer object is created with the value 1, and all three variables are assigned to the same memory location. You can also assign multiple objects to multiple variables. For example −

a,b,c = 1,2,"john"
Here, two integer objects with values 1 and 2 are assigned to variables a and b respectively, and one string object with the value "john" is assigned to the variable c.

***************************************************
Standard Data Types
***************************************************
The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters.
Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

Python has five standard data types −

Numbers
String
List
Tuple
Dictionary

***************************************************
Python Numbers
***************************************************

Number data types store numeric values. Number objects are created when you assign a value to them. For example −

var1 = 1
var2 = 10

You can also delete the reference to a number object by using the del statement. The syntax of the del statement is −

del var1[,var2[,var3[....,varN]]]]
You can delete a single object or multiple objects by using the del statement. For example −

del var
del var_a, var_b

-------------------------------------------------------
Python supports four different numerical types −
-------------------------------------------------------

int (signed integers)
long (long integers, they can also be represented in octal and hexadecimal)
float (floating point real values)
complex (complex numbers)
Examples
Here are some examples of numbers −

int							long			float				complex

10							51924361L		0.0					3.14j
100							-0x19323L		15.20				 45.j
-786							0122L		-21.9		   9.322e-36j
080				0xDEFABCECBDAECBFBAEl		32.3+e18			.876j
-0490					535633629843L		-90.			-.6545+0J
-0x260				   -052318172735L		-32.54e100		   3e+26J
0x69				  -4721885298529L		70.2-E12		 4.53e-7j


Python allows you to use a lowercase l with long, but it is recommended that you use only an uppercase L to avoid confusion with the number 
1. Python displays long integers with an uppercase L.

A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj, where x and y are the real numbers and j is the imaginary unit.

*******************************************************
Python Strings
*******************************************************

Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. 
Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator. For example −

Live Demo
#!/usr/bin/python

str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string
This will produce the following result −

Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST

*******************************************************
Python Lists
*******************************************************

Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, 
lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. 
The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator. For example −

#!/usr/bin/python

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists
This produce the following result −

['abcd', 786, 2.23, 'john', 70.2]
abcd
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']

****************************************
Python Tuples
****************************************

A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. 
Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, 
while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. For example −

Live Demo
#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists
This produce the following result −

('abcd', 786, 2.23, 'john', 70.2)
abcd
(786, 2.23)
(2.23, 'john', 70.2)
(123, 'john', 123, 'john')
('abcd', 786, 2.23, 'john', 70.2, 123, 'john')

The following code is invalid with tuple, because we attempted to update a tuple, which is not allowed. Similar case is possible with lists −

#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

****************************************
Python Dictionary
****************************************


Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). For example −

Live Demo
#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
This produce the following result −

This is one
This is two
{'dept': 'sales', 'code': 6734, 'name': 'john'}
['dept', 'code', 'name']
['sales', 6734, 'john']
Dictionaries have no concept of order among elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.















