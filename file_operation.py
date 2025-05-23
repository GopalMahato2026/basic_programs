####file operation in python
"""
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

### read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) #removes newline characteras
        
## writing a file
with open("example.txt", "w") as file:
    file.write("Hello  World!\nI am writing text")
    file.write("This is new line")
"""    
### without overwriting to write, We
'''
will user append function    

with open("example.txt", "a") as file:
    file.write("\nI am using append function\n")
    file.write("\nappend operation taking place")
'''
"""
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
#### lets overwrite them all 
with open("example.txt", "w") as file:
    file.write("My name is Gopal Mahato\nI am in my prime")
 """
"""
#writing list of lines
lines = ["first line \n", "second line\n", "third line\n"]
with open("example.txt", "a") as file:
    file.writelines(lines)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
"""
#print("Hello I am in a new part!")
###
"""
with open("my_file.txt", "r") as file:
    content = file.read()
    words = content.split()
    for word in words:
        print(word)
"""        
"""
hobbies = ["Coding", "Reading", "Watching football especially Following Manchester City", "Traveling(When i will have money i will travel Manchester)"]
with open("hobbies.txt", "w") as file:
    for hobby in hobbies:
        file.write(hobby + "\n")
        
with open("hobbies.txt", "a") as file:
    file.write("Learning Ethical Hacking\n")
search_word = "Coding"    
with open("hobbies.txt", "r") as file:
    content = file.read() 
    new_content = content.replace("Coding", "First Understanding Python programming more deeply")
    if search_word in content:
        print(search_word," find successfully!")
    else:
        print("Not found")
with open("hobbies.txt", "w") as file:
    file.write(new_content)   
    
    
with open("hobbies.txt", "r") as file:
    c = file.read()
    print(c)

"""
#binary files
# writing to a bainary files
"""
data = b"\x00\x01\x02\x03\x04"
with open("binary.bin", "wb") as file:
    file.write(data)
with open("binary.bin", "rb") as file:
    data = file.read()
    print(data)
"""
### Read a text file and count the numbers of lines, words and characters
'''
with open("test1.txt", "r") as file:
    content = file.read()
    print(content)   
    print("Total words:", len(content.split()))
    content_list = list(content)
    for i in content_list:
        if i == " " or i == "\t" or i == "\n":
            content_list.remove(i)
    print("Total characters: ", len(content_list))
'''
##### creating a new directory
"""
import os
new_directory = "packages"
os.mkdir(new_directory)
print(f"Directory {new_directory} created sucessfully!")
"""
#### listing files and folders
import os
items = os.listdir(".")
print(items)
### joining path
print("Current Working DIrectory:", os.getcwd())
##### 
path = "packages"
if os.path.exists(path):
    print(f"{path} exists!")
    if os.path.isfile(path):
        print(f"The path '{path}' is a file")
    elif os.path.isdir(path):
        print(f"The path '{path}' is a directory or folder!")
    else:
        print(f"The file path {path} neither a file nor a directory")
else:
    print(f"{path} doesn't exists")
    

