print("My name is Gopal Mahato!\nI am using Fedora 42 Workstation!")
print("A function that returns total vowels and consonent in a string")
def total_vc(s):
    total_v = 0
    total_c = 0
    vowels = list("aeiou")
    consonents = list("qwrtypsdfghjklzxcvbnm")
    for i in s.lower():
        if i in vowels:
            total_v += 1
        elif i in consonents:
            total_c += 1
    return total_v, total_c    
print(total_vc("MynameisGopalMahato"))


#### comparing List comprehension vs. loop
"""
>>> square_of_nums = [x**2 for x in range(21)]
>>> square_of_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
>>> 
>>> squares_of_nums2 = []
... for i in range(21):
...     squares_of_nums2.append(i*i)
...        
>>> squares_of_nums2
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
"""

### right angle star pattern
"""
>>> def right_angle_star(n):
...     for i in range(1,n + 1):
...         print("*" * i)
...         
>>> right_angle_star(4)
*
**
***
****
>>> 
"""
###### lets creating python number guessing game
import random
def number_guess_main():    
    try:
        user = int(input("Enter a number: "))
    except:
        print("Enter a valid number!")
    number_to_guess = random.randint(1,100)
    print(f"You: {user} guess: {number_to_guess}")
if __name__ == "__main__":
    number_guess_main()
        

            


