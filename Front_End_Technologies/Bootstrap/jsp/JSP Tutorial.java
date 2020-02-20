What is JSP?
Java Server Pages (JSP) code is likely HTML with bits of Java code in it. Very basically, in order to create a JSP code, you can take any existing HTML page and change its extension to “.jsp” instead of “.html”. 
Then you can put Java code in it with some structures called Scriptlet, Directive, Expression. In the code below, the JSP file shows the current time:


Paths Followed By JSP
The following are the paths followed by a JSP −

Compilation
Initialization
Execution
Cleanup

JSP Compilation
When a browser asks for a JSP, the JSP engine first checks to see whether it needs to compile the page. If the page has never been compiled, or if the JSP has been modified since it was last compiled, the JSP engine compiles the page.

The compilation process involves three steps −

Parsing the JSP.
Turning the JSP into a servlet.
Compiling the servlet.
JSP Initialization
When a container loads a JSP it invokes the jspInit() method before servicing any requests. If you need to perform JSP-specific initialization, override the jspInit() method −

public void jspInit(){
   // Initialization code...
}
Typically, initialization is performed only once and as with the servlet init method, you generally initialize database connections, open files, and create lookup tables in the jspInit method.

JSP Execution
This phase of the JSP life cycle represents all interactions with requests until the JSP is destroyed.

Whenever a browser requests a JSP and the page has been loaded and initialized, the JSP engine invokes the _jspService() method in the JSP.

The _jspService() method takes an HttpServletRequest and an HttpServletResponse as its parameters as follows −

void _jspService(HttpServletRequest request, HttpServletResponse response) {
   // Service handling code...
}
The _jspService() method of a JSP is invoked on request basis. This is responsible for generating the response for that request and this method is also responsible for generating responses to all seven of the HTTP methods, i.e, GET, POST, DELETE, etc.

JSP Cleanup
The destruction phase of the JSP life cycle represents when a JSP is being removed from use by a container.

The jspDestroy() method is the JSP equivalent of the destroy method for servlets. Override jspDestroy when you need to perform any cleanup, such as releasing database connections or closing open files.

The jspDestroy() method has the following form −

public void jspDestroy() {
   // Your cleanup code goes here.
}

Elements of JSP
The elements of JSP have been described below −

The Scriptlet
A scriptlet can contain any number of JAVA language statements, variable or method declarations, or expressions that are valid in the page scripting language.

Following is the syntax of Scriptlet −

<% code fragment %>

Any text, HTML tags, or JSP elements you write must be outside the scriptlet. Following is the simple and first example for JSP −

<html>
   <head><title>Hello World</title></head>
   
   <body>
      Hello World!<br/>
      <%
         out.println("Your IP address is " + request.getRemoteAddr());
      %>
   </body>
</html>

=============================================================================================================================================================================

JSP Operators
JSP supports all the logical and arithmetic operators supported by Java. Following table lists out all the operators with the highest precedence appear at the top of the table, those with the lowest appear at the bottom.

Within an expression, higher precedence operators will be evaluated first.

Category	Operator	Associativity
Postfix	() [] . (dot operator)	Left to right
Unary	++ - - ! ~	Right to left
Multiplicative	* / %	Left to right
Additive	+ -	Left to right
Shift	>> >>> <<	Left to right
Relational	> >= < <=	Left to right
Equality	== !=	Left to right
Bitwise AND	&	Left to right
Bitwise XOR	^	Left to right
Bitwise OR	|	Left to right
Logical AND	&&	Left to right
Logical OR	||	Left to right
Conditional	?:	Right to left
Assignment	= += -= *= /= %= >>= <<= &= ^= |=	Right to left
Comma	,	

=============================================================================================================================================================================

JSP Literals
The JSP expression language defines the following literals −

Boolean − true and false

Integer − as in Java

Floating point − as in Java

String − with single and double quotes; " is escaped as \", ' is escaped as \', and \ is escaped as \\.

Null − null

=============================================================================================================================================================================

Seguir en JSP - Directives

