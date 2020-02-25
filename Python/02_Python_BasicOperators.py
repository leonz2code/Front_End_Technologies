# ve Data Type Conversion si se necesita

*************************************
Python - Basic Operators
*************************************

#!/usr/bin/python

a = 21
b = 10
c = 0

c = a + b
print "Line 1 - Value of c is ", c

c = a - b
print "Line 2 - Value of c is ", c 

c = a * b
print "Line 3 - Value of c is ", c 

c = a / b
print "Line 4 - Value of c is ", c 

c = a % b
print "Line 5 - Value of c is ", c

a = 2
b = 3
c = a**b 
print "Line 6 - Value of c is ", c

a = 10
b = 5
c = a//b 
print "Line 7 - Value of c is ", c
When you execute the above program, it produces the following result −

Line 1 - Value of c is 31
Line 2 - Value of c is 11
Line 3 - Value of c is 210
Line 4 - Value of c is 2
Line 5 - Value of c is 1
Line 6 - Value of c is 8
Line 7 - Value of c is 2

*************************************
Python Comparison Operators
*************************************

Live Demo
#!/usr/bin/python

a = 21
b = 10
c = 0

if ( a == b ):
   print "Line 1 - a is equal to b"
else:
   print "Line 1 - a is not equal to b"

if ( a != b ):
   print "Line 2 - a is not equal to b"
else:
   print "Line 2 - a is equal to b"

if ( a <> b ):
   print "Line 3 - a is not equal to b"
else:
   print "Line 3 - a is equal to b"

if ( a < b ):
   print "Line 4 - a is less than b" 
else:
   print "Line 4 - a is not less than b"

if ( a > b ):
   print "Line 5 - a is greater than b"
else:
   print "Line 5 - a is not greater than b"

a = 5;
b = 20;
if ( a <= b ):
   print "Line 6 - a is either less than or equal to  b"
else:
   print "Line 6 - a is neither less than nor equal to  b"

if ( b >= a ):
   print "Line 7 - b is either greater than  or equal to b"
else:
   print "Line 7 - b is neither greater than  nor equal to b"
When you execute the above program it produces the following result −

Line 1 - a is not equal to b
Line 2 - a is not equal to b
Line 3 - a is not equal to b
Line 4 - a is not less than b
Line 5 - a is greater than b
Line 6 - a is either less than or equal to b
Line 7 - b is either greater than or equal to b

*************************************
Python Assignment Operators
*************************************

Live Demo
#!/usr/bin/python

a = 21
b = 10
c = 0

c = a + b
print "Line 1 - Value of c is ", c

c += a
print "Line 2 - Value of c is ", c 

c *= a
print "Line 3 - Value of c is ", c 

c /= a 
print "Line 4 - Value of c is ", c 

c  = 2
c %= a
print "Line 5 - Value of c is ", c

c **= a
print "Line 6 - Value of c is ", c

c //= a
print "Line 7 - Value of c is ", c
When you execute the above program, it produces the following result −

Line 1 - Value of c is 31
Line 2 - Value of c is 52
Line 3 - Value of c is 1092
Line 4 - Value of c is 52
Line 5 - Value of c is 2
Line 6 - Value of c is 2097152
Line 7 - Value of c is 99864


*************************************
Python Bitwise Operators
*************************************

Live Demo
#!/usr/bin/python

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print "Line 1 - Value of c is ", c

c = a | b;        # 61 = 0011 1101 
print "Line 2 - Value of c is ", c

c = a ^ b;        # 49 = 0011 0001
print "Line 3 - Value of c is ", c

c = ~a;           # -61 = 1100 0011
print "Line 4 - Value of c is ", c

c = a << 2;       # 240 = 1111 0000
print "Line 5 - Value of c is ", c

c = a >> 2;       # 15 = 0000 1111
print "Line 6 - Value of c is ", c
When you execute the above program it produces the following result −

Line 1 - Value of c is 12
Line 2 - Value of c is 61
Line 3 - Value of c is 49
Line 4 - Value of c is -61
Line 5 - Value of c is 240
Line 6 - Value of c is 15

*************************************
Python Logical Operators
*************************************

(a and b) is true.
(a or b) is true.
Not(a and b) is false.


*************************************
Python Membership Operators
*************************************

Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. 
There are two membership operators as explained below −

Operator		Description																												Example
in				Evaluates to true if it finds a variable in the specified sequence and false otherwise.									x in y, here in results in a 1 if x is a member of sequence y.
not in			Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.						x not in y, here not in results in a 1 if x is not a member of sequence y.

Example
Live Demo
#!/usr/bin/python

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "Line 1 - a is available in the given list"
else:
   print "Line 1 - a is not available in the given list"

if ( b not in list ):
   print "Line 2 - b is not available in the given list"
else:
   print "Line 2 - b is available in the given list"

a = 2
if ( a in list ):
   print "Line 3 - a is available in the given list"
else:
   print "Line 3 - a is not available in the given list"
When you execute the above program it produces the following result −

Line 1 - a is not available in the given list
Line 2 - b is not available in the given list
Line 3 - a is available in the given list

*************************************
Python Identity Operators
*************************************

Identity operators compare the memory locations of two objects. There are two Identity operators as explained below −

Operator			Description																													Example
is					Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.				x is y, here is results in 1 if id(x) equals id(y).
is not				Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.				x is not y, here is not results in 1 if id(x) is not equal to id(y).

Example
Live Demo
#!/usr/bin/python

a = 20
b = 20

if ( a is b ):
   print "Line 1 - a and b have same identity"
else:
   print "Line 1 - a and b do not have same identity"

if ( id(a) == id(b) ):
   print "Line 2 - a and b have same identity"
else:
   print "Line 2 - a and b do not have same identity"

b = 30
if ( a is b ):
   print "Line 3 - a and b have same identity"
else:
   print "Line 3 - a and b do not have same identity"

if ( a is not b ):
   print "Line 4 - a and b do not have same identity"
else:
   print "Line 4 - a and b have same identity"
When you execute the above program it produces the following result −

Line 1 - a and b have same identity
Line 2 - a and b have same identity
Line 3 - a and b do not have same identity
Line 4 - a and b do not have same identity

*************************************
Python Operators Precedence
*************************************

# search in web if need


continuar en Python - Decision Making








