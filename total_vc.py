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

            


