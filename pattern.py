"""
>>> ### printing square pattern
>>> n = 5
>>> for i in range(n):
...     for j in range(n):
...         print("*" * n, end= " ")
...     print()
...         
***** ***** ***** ***** ***** 
***** ***** ***** ***** ***** 
***** ***** ***** ***** ***** 
***** ***** ***** ***** ***** 
***** ***** ***** ***** ***** 
>>> for i in range(5):
...     print("*" * 5)
...     
*****
*****
*****
*****
*****
>>> for i in range(5):
...     print("*" * 5, end=" ")
...     
***** ***** ***** ***** ***** >>> 
>>> for i in range(5):
...     print("*" * 5, end="")
...     
*************************>>> clear

>>> for i in range(5):
...     for j in range(5):
...         print("*", end="")
...     print()
...         
*****
*****
*****
*****
*****
>>> for i in range(5):
...     for j in range(5):
...         print("*", end=" ")
...     print()
...     
* * * * * 
* * * * * 
* * * * * 
>>> for i in range(5):
...     for j in range(5):
...         print("*", end=" ")
...     print()
...     
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
>>> clear









>>> ####incresing triangle pattern
>>> """
... *
... **
... ***
... ****
... """
'\n*\n**\n***\n****\n'
>>> n = 5
>>> for i in range(n):
...     for j in range(i + 1):
...         print("*", end="")
...         
***************>>> 
>>> for i in range(n):
...     for j in range(i + 1):
...         print("*", end=" ")
...         
* * * * * * * * * * * * * * * >>> 
>>> for i in range(n):
...     for j in range(i + 1):
...         print("*", end=" ")
...     print()
...         
* 
* * 
* * * 
* * * * 
* * * * * 
>>> for i in range(n):
...     for j in range(i + 1):
...         print("*", end="")
...     print()
...     
*
**
***
****
*****
>>> for i in range(n):
...     for j in range(i + 1):
...         print("*", end=" ")
...     print()
...     
* 
* * 
* * * 
* * * * 
* * * * * 
>>> """
... *****
... ****
... ***
... **
... *
... """
'\n*****\n****\n***\n**\n*\n'
>>> r = 5
>>> for i in range(r, 0, -1):
...     for j in range(i + 1):
...         print("*", end=" ")
...     print()
...         
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
>>> for i in range(r, 0, -1):
...     for j in range(i):
...         print("*", end=" ")
...     print()
...     
* * * * * 
* * * * 
* * * 
* * 
* 
>>> rows = 5
>>> for i in range(n):
...     for j in range(i, rows):
...         print("#", end= " ")
...     print()
...         
# # # # # 
# # # # 
# # # 
# # 
# 
>>> clear

>>> """
...     *
...    **
...   ***
...  ****
...  """  
'\n    *\n   **\n  ***\n ****\n '
>>> ro = 5
>>> for i in range(ro):
...     for j in range(i, ro):
...         print(" ", end=" ")
...     for j2 in range(i+1):
...         print("*", end=" ")
...     print()
...             
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
>>> 


>>> #### stage2 
>>> """
... right sided triangle
... *****
...  ****
...   ***
...    **
...     *
... """    
'\nright sided triangle\n*****\n ****\n  ***\n   **\n    *\n'
>>> row = 5
>>> for i in range(row):
...  for j in range(i):
...   print(" ", end=" ")
...  for j2 in range(i, row):
...   print("*", end=" ")
...  print()
...    
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
>>> 

>>> """
...     *
...    ***
...   *****
...  *******
... *********
... """     
'\n    *\n   ***\n  *****\n *******\n*********\n'
>>> n = 5
>>> for i in range(5):
...     for j1 in range(i, n):
...         print(" ", end=" ")
...     for j2 in range(i):
...         print("*", end=" ")
...     for j3 in range(i + 1):
...         print("*", end=" ")
...     print()
...                 
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
>>> for i in range(5):
...     for j1 in range(i, n):
...         print(" ", end=" ")
...     for j2 in range(i + 1):
...         print("*", end=" ")
...     for j3 in range(i + 1):
...         print("*", end=" ")
...     print()
...     
          * * 
        * * * * 
      * * * * * * 
    * * * * * * * * 
  * * * * * * * * * * 
>>> for i in range(5):
...     for j1 in range(i, n):
...         print(" ", end=" ")
...     for j2 in range(i):
...         print("*", end=" ")
...     for j3 in range(i + 1):
...         print("*", end=" ")
...     print()
...     
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
>>> """
... lets try this one 
... *********
...  *******
...   *****
...    ***
...     *
...  """   
'\nlets try this one \n*********\n *******\n  *****\n   ***\n    *\n '
>>> for i in range(5, 0, -1):
...     for j1 in range(i, n):
...         print(" ", end=" ")
...     for j2 in range(i):
...         print("*", end=" ")
...     for j3 in range(i + 1):
...         print("*", end=" ")
...     print()
...     
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
>>> for i in range(n + 1, 0, -1):
...     for j1 in range(i, n):
...         print(" ", end=" ")
...     for j2 in range(i):
...         print("*", end=" ")
...     for j3 in range(i + 1):
...         print("*", end=" ")
...     print()
...     
* * * * * * * * * * * * * 
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
>>> for i in range(n,1, -1):
...     for j1 in range(i, n):
...         print(" ", end=" ")
...     for j2 in range(i):
...         print("*", end=" ")
...     for j3 in range(i + 1):
...         print("*", end=" ")
...     print()
...     
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
>>> for i in range(n,-1, -1):
...     for j1 in range(i, n):
...         print(" ", end=" ")
...     for j2 in range(i):
...         print("*", end=" ")
...     for j3 in range(i + 1):
...         print("*", end=" ")
...     print()
...     
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
>>> 



"""
for i in range(5 - 1):
    for j1 in range(i, n):
        print(" ", end=" ")
    for j2 in range(i):
        print("*", end=" ")
    for j3 in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n,-1, -1):
    for j1 in range(i, n):
        print(" ", end=" ")
    for j2 in range(i):
        print("*", end=" ")
    for j3 in range(i + 1):
        print("*", end=" ")
    print()

