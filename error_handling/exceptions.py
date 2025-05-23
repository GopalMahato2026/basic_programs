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
try:
    result = 1 / 0
except ZeroDivisionError as ex:
    print("Please enter the demoninator grater then zero")
    
