**************************************
Python - Lists
**************************************

The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. 
Important thing about a list is that items in a list need not be of the same type.

Creating a list is as simple as putting different comma-separated values between square brackets. For example −

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
Similar to string indices, list indices start at 0, and lists can be sliced, concatenated and so on.

--------------------------------------
Accessing Values in Lists
--------------------------------------

To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index. For example −

Live Demo
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
When the above code is executed, it produces the following result −

list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]

--------------------------------------
Updating Lists
--------------------------------------

You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, 
and you can add to elements in a list with the append() method. For example −

Live Demo
#!/usr/bin/python

list = ['physics', 'chemistry', 1997, 2000];
print "Value available at index 2 : "
print list[2]
list[2] = 2001;
print "New value available at index 2 : "
print list[2]
Note − append() method is discussed in subsequent section.

When the above code is executed, it produces the following result −

Value available at index 2 :
1997
New value available at index 2 :
2001
--------------------------------------
Delete List Elements
--------------------------------------


To remove a list element, you can use either the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know. For example −

Live Demo
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000];
print list1
del list1[2];
print "After deleting value at index 2 : "
print list1
When the above code is executed, it produces following result −

['physics', 'chemistry', 1997, 2000]
After deleting value at index 2 :
['physics', 'chemistry', 2000]
Note − remove() method is discussed in subsequent section.

----------------------------------
Basic List Operations
----------------------------------

Lists respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string.

In fact, lists respond to all of the general sequence operations we used on strings in the prior chapter


#Python Expression	                                Results	                                Description
len([1, 2, 3])	                                    3	                                    Length
[1, 2, 3] + [4, 5, 6]	                            [1, 2, 3, 4, 5, 6]	                    Concatenation
['Hi!'] * 4	                                        ['Hi!', 'Hi!', 'Hi!', 'Hi!']	        Repetition
3 in [1, 2, 3]	                                    True	                                Membership
for x in [1, 2, 3]: print x,	                    1 2 3	Iteration

----------------------------------------
Built-in List Functions & Methods
----------------------------------------

Python includes the following list functions −
cmp(list1, list2)
Compares elements of both lists.

len(list)
Gives the total length of the list.

max(list)
Returns item from the list with max value.

min(list)
Returns item from the list with min value.

list(seq)
Converts a tuple into list.


Python includes following list methods -

list.append(obj)
Appends object obj to list

list.count(obj)
Returns count of how many times obj occurs in list

list.insert(index, obj)
Inserts object obj into list at offset index

list.pop(obj=list[-1])
Removes and returns last object or obj from list

list.remove(obj)
Removes object obj from list

list.reverse()
Reverses objects of list in place

	list.sort([func])
Sorts objects of list, use compare func if given

