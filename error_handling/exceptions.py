"""
a  = 10
a = b 
"""

"""
a = 21 
try:
    a = b
except:
    print("this variable has not been assigned!")
"""
"""
a = 32
try:
    a = b
except NameError as ex:
    print(ex)
"""
"""
try:
    result = 1 / 0
except ZeroDivisionError as ex:
    print("Please enter the demoninator grater then zero")
"""
"""
try:
    num = float(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("Enter denominator greater than zero")
except Exception as ex:
    print(ex)
else:
    print(result)
finally:
    print("Execution complete!")
    
 """  
 ## file handling and exception handling
try:
    with open("example1.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file doesn't exists")
finally:
    print("file closed")
