print("My name is Gopal Mahato!\nI am using Fedora Workstation!")
gopalmahato@fedora:~$ python3 
Python 3.13.3 (main, Apr 22 2025, 00:00:00) [GCC 15.0.1 20250418 (Red Hat 15.0.1-0)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> text = "python"
>>> i = 0
>>> for alpha_ in text:
...     print(f"Character at position {i} is: {alpha_}")
...     i += 1
...     
Character at position 0 is: p
Character at position 1 is: y
Character at position 2 is: t
Character at position 3 is: h
Character at position 4 is: ogopalmahato@fedora:~$ python3 
Python 3.13.3 (main, Apr 22 2025, 00:00:00) [GCC 15.0.1 20250418 (Red Hat 15.0.1-0)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> text = "python"
>>> i = 0
>>> for alpha_ in text:
...     print(f"Character at position {i} is: {alpha_}")
...     i += 1
...     
Character at position 0 is: p
Character at position 1 is: y
Character at position 2 is: t
Character at position 3 is: h
Character at position 4 is: o
Character at position 5 is: n
>>> ##Write a program to count how many numbers between 1 an\
d 50 are divisible by 3, and then print that count.
>>> count = 0
>>> for i in range(1, 51):
...     if i % 3 == 0:
...         count += 1
... print("Count of numbers divisible by 3 between 1 to 50 is\
:",count")
...         
...         
  File "<python-input-5>", line 4
    print("Count of numbers divisible by 3 between 1 to 50 is:",count")
                                                                     ^
SyntaxError: unterminated string literal (detected at line 4)
>>> count = 0
>>> for i in range(1, 51):
...     if i % 3 == 0:
...         count += 1
... print("Count of numbers divisible by 3 between 1 to 50 is\
:",count)
... 
Count of numbers divisible by 3 between 1 to 50 is: 16
>>> ### task11 Write a program using a for loop to print a 5\
x5 square of * symbols like this:
>>> """
... *****
... *****
... *****
... *****
... *****
... """
'\n*****\n*****\n*****\n*****\n*****\n'
>>> for i in range(5):
...     for j in range(5):
...         print(j)
...         
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
>>> for i in range(5):
...     for j in range(5):
...         print("*"j)
...         
  File "<python-input-11>", line 3
    print("*"j)
          ^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> for i in range(5):
...     for j in range(5):
...         print("*"* j)
...         

*
**
***
****

*
**
***
****

*
**
***
****

*
**
***
****

*
**
***
****
>>> clear

>>> for i in range(5):
...     print("*" * i, end="")
...     
**********>>> clear













>>> for i in range(5):
...     for j in i:
...         print("*" * j)
...         
Traceback (most recent call last):
  File "<python-input-14>", line 2, in <module>
    for j in i:
             ^
TypeError: 'int' object is not iterable
>>> for i in range(5):
...     for j in range(i):
...         print("*" * j)
...         


*

*
**

*
**
***
>>> clear

>>> for i in range(5):
...     print("*" * 5)
...     
*****
*****
*****
*****
*****
>>> i = 5
>>> for index in range(i):
...     print("*", i)
...     
* 5
* 5
* 5
* 5
* 5
>>> i = 5
>>> for index in range(i):
...     print("*"* i)
...     
*****
*****
*****
*****
*****
>>> ##✅ Next up: Task 12: Print Right-Angled Triangle Patter
>>> i = 3
>>> for i in range(1,i + 1):
...     print("*" * i)
...     
*
**
***
>>> ##Write a program using a loop that prints numbers from 1\
 to 10 but stops printing when the number is greater than 7
>>> for i in range(1, 11):
...     if i == 7:
...         break
...     print(i)
...         
1
2
3
4
5
6
>>> for i in range(1, 11):
...     if i > 7:
...         break
...     print(i)
...     
1
2
3
4
5
6
7
>>> 


Character at position 5 is: n
>>> ##Write a program to count how many numbers between 1 an\
d 50 are divisible by 3, and then print that count.
>>> count = 0
>>> for i in range(1, 51):
...     if i % 3 == 0:
...         count += 1
... print("Count of numbers divisible by 3 between 1 to 50 is\
:",count")
...         
...         
  File "<python-input-5>", line 4
    print("Count of numbers divisible by 3 between 1 to 50 is:",count")
                                                                     ^
SyntaxError: unterminated string literal (detected at line 4)
>>> count = 0
>>> for i in range(1, 51):
...     if i % 3 == 0:
...         count += 1
... print("Count of numbers divisible by 3 between 1 to 50 is\
:",count)
... 
Count of numbers divisible by 3 between 1 to 50 is: 16
>>> ### task11 Write a program using a for loop to print a 5\
x5 square of * symbols like this:
>>> """
... *****
... *****
... *****
... *****
... *****
... """
'\n*****\n*****\n*****\n*****\n*****\n'
>>> for i in range(5):
...     for j in range(5):
...         print(j)
...         
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
>>> for i in range(5):
...     for j in range(5):
...         print("*"j)
...         
  File "<python-input-11>", line 3
    print("*"j)
          ^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> for i in range(5):
...     for j in range(5):
...         print("*"* j)
...         

*
**
***
****

*
**
***
****

*
**
***
****

*
**
***
****

*
**
***
****
>>> clear

>>> for i in range(5):
...     print("*" * i, end="")
...     
**********>>> clear













>>> for i in range(5):
...     for j in i:
...         print("*" * j)
...         
Traceback (most recent call last):
  File "<python-input-14>", line 2, in <module>
    for j in i:
             ^
TypeError: 'int' object is not iterable
>>> for i in range(5):
...     for j in range(i):
...         print("*" * j)
...         


*

*
**

*
**
***
>>> clear

>>> for i in range(5):
...     print("*" * 5)
...     
*****
*****
*****
*****
*****
>>> i = 5
>>> for index in range(i):
...     print("*", i)
...     
* 5
* 5
* 5
* 5
* 5
>>> i = 5
>>> for index in range(i):
...     print("*"* i)
...     
*****
*****
*****
*****
*****
>>> ##✅ Next up: Task 12: Print Right-Angled Triangle Patter
>>> i = 3
>>> for i in range(1,i + 1):
...     print("*" * i)
...     
*
**
***
>>> ##Write a program using a loop that prints numbers from 1\
 to 10 but stops printing when the number is greater than 7
>>> for i in range(1, 11):
...     if i == 7:
...         break
...     print(i)
...         
1
2
3
4
5
6
>>> for i in range(1, 11):
...     if i > 7:
...         break
...     print(i)
...     
1
2
3
4
5
6
7
>>> 


