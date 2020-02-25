***********************************************
Python - Numbers
***********************************************

Number data types store numeric values. They are immutable data types, means that changing the value of a number data type results in a newly allocated object.

Number objects are created when you assign a value to them. For example −

var1 = 1
var2 = 10
You can also delete the reference to a number object by using the del statement. The syntax of the del statement is −

del var1[,var2[,var3[....,varN]]]]
You can delete a single object or multiple objects by using the del statement. For example −

del var
del var_a, var_b

Python supports four different numerical types −
-------------------------------
int (signed integers) − 
-------------------------------

They are often called just integers or ints, are positive or negative whole numbers with no decimal point.

-------------------------------
long (long integers ) − 
-------------------------------

Also called longs, they are integers of unlimited size, written like integers and followed by an uppercase or lowercase L.

-------------------------------
float (floating point real values) − 
-------------------------------

Also called floats, they represent real numbers and are written with a decimal point dividing the integer 
and fractional parts. Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).

-------------------------------
complex (complex numbers) − 
-------------------------------

are of the form a + bJ, where a and b are floats and J (or j) represents the square root of -1 (which is an imaginary number). 
The real part of the number is a, and the imaginary part is b. Complex numbers are not used much in Python programming.

///////////////////////////////////
Some Mathematical Functions
///////////////////////////////////

abs(x)
The absolute value of x: the (positive) distance between x and zero.

ceil(x)
The ceiling of x: the smallest integer not less than x

exp(x)
The exponential of x: ex

fabs(x)
The absolute value of x.

floor(x)
The floor of x: the largest integer not greater than x

max(x1, x2,...)
The largest of its arguments: the value closest to positive infinity

min(x1, x2,...)
The smallest of its arguments: the value closest to negative infinity

pow(x, y)
The value of x**y.

round(x [,n])
x rounded to n digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.

sqrt(x)
The square root of x for x > 0

/////////////////////////////////////////
some Random Number Functions
/////////////////////////////////////////

Random numbers are used for games, simulations, testing, security, and privacy applications. 
Python includes following functions that are commonly used.
----------------------
choice(seq)
A random item from a list, tuple, or string.
----------------------

#!/usr/bin/python
import random

print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A String') : ", random.choice('A String')
When we run above program, it produces following result −

choice([1, 2, 3, 5, 9]) :  2
choice('A String') :  n

----------------------
randrange ([start,] stop [,step])
A randomly selected element from range(start, stop, step)
----------------------

Following is the syntax for randrange() method −

randrange ([start,] stop [,step])
Note − This function is not accessible directly, so we need to import random module and then we need to call this function using random static object.

Parameters
start − Start point of the range. This would be included in the range.

stop − Stop point of the range. This would be excluded from the range.

step − Steps to be added in a number to decide a random number.

Return Value
This method returns a random item from the given range

Example
The following example shows the usage of randrange() method.

#!/usr/bin/python
import random

# Select an even number in 100 <= number < 1000
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

# Select another number in 100 <= number < 1000
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)
When we run above program, it produces following result −

randrange(100, 1000, 2) :  976
randrange(100, 1000, 3) :  520

--------------------------------------------------------------------
shuffle(lst)
Randomizes the items of a list in place. Returns None.
--------------------------------------------------------------------

Description
Python number method shuffle() randomizes the items of a list in place.

Syntax
Following is the syntax for shuffle() method −

shuffle (lst )
Note − This function is not accessible directly, so we need to import shuffle module and then we need to call this function using random static object.

Parameters
lst − This could be a list or tuple.

Return Value
This method does not return any value.

Example
The following example shows the usage of shuffle() method.

Live Demo
#!/usr/bin/python
import random

list = [20, 16, 10, 5];
random.shuffle(list)
print "Reshuffled list : ",  list

random.shuffle(list)
print "Reshuffled list : ",  list
When we run above program, it produces following result −

Reshuffled list :  [16, 5, 10, 20]
Reshuffled list :  [16, 5, 20, 10]












