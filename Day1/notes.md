#Types of Operators
1. Arithmetic operator: +,-,/,//,%,**
2. Relational Operators:==,!=,>,<,>=,<=
3. Assignment Operator:=,+=,-=,*=,/=,//=,**=
4. Logical Operators: and, or, not
5. Bitwise operator: &,|,^,~,<<,>>
6. Membership operators: in, not in
7. Identity Operator: is
8. Ternary Operator: 

Swap two variables
*without temp
*use bitwise
5 ways to swap
1.+,-
2.*,/
3.temp variable
4, bitwise
5.
q) find single number  using bit multiplication in leetcode
# Electricity bill calculator(Bottom approach)
1st 100 units -> 1.50/units
next 100 units -> 2.50/units
above 200 units -> 4/units
calculate bill
sample input:
units:75
output:(7581.50)=112.59
# Keprekar Number
1.find the square
2.convert it into string
3.dividing into two parts.
4.increment the size of first part and decrement the size of second.
5.if both numbers are equal, then it is a keprekar number.
# no of wheels and vehicles
v=200 
w=540
tw=130
fw=70
# Movie ticket discount
ticket>15 ->20% discount
2 category=1,0
if 1-> student ->5% discount
else no discount

# Rain
0-1 No rain
1-5 light
5-10 moderate
10-15 heavy

# Largest of 4 number
# second largest
# fancy number
1234-> inc fancy number
4321-> dec fancy number
1567-> not fancy  number

#product of digits
1234-> 1x 2x3x4=24
520=0
1. Diamond pattern
2. Heart pattern
3. hollow Rectangle

# greedy algorithm-without considering the future activities are done in the present
# Moorey Voting algorithm-Majority element leetcode169 
  majority of number is related to n/2 greater
# jwd algorithm for password 
 no of char -8
 no white spaces
 lower char, upper char, special char should be present
 # Strings
 text into code-known as data encryption
# types of collection in python
 1. list(heterogenous)
 2. tuple: immutable data structure
 3. dictionary: key-value pairs
 4. sets: stores only unique elements 
1.  List used in 2 ways
    1. User defined list=[]
    2. using list fn-list()
   /heterogenous - diff data types
   /store duplicates
   /mutable
2. Tuple-()
   ( ) or tuple()
   immutsble
3. Sets-
   { }, set()
   unique values
   set()- declares empty set
4. Dictionary
   {}, Dict{}
   key-value pair 
   {}-declares empty dictionary
Q. [101,102,103,104,102] 
make it a set and compare the length with the og set
# Leetcode 121-Kadane's algorithm
  find the difference between consecutive sub array
  compare those value with 0 and take the max between (0 and 1st value).
  add the current value with next value in diff array.
  compare values of i and i+1 and store the max in an array. the last value is max profit
