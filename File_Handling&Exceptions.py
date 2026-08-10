'''
Tokens -->Identifiers,Variables,Keywords,Literals,Operators,Punctuators [],(),{}
Operators -->Datatypes -->Control Statements --> Functions --> Module (Userdefined/Built-in)
#Email Automation (Bulk mail (excel file)),Virtual Assistant
File Handling,Error Handling (try,except,finally) --> OOP -->Regular Expressions -->Web Scraping
'''
#Store the data -->Files (.txt files) --> open()
#File modes --> 'r','w','a'

#Default file mode --> open("file_name.txt",'r') #default we have 'r' 
file = open('example.txt')
#print(file)
#print(file.read()) #returns entire text from the file
#print(file.read(10)) #we can also mention the size
#print(file.readlines()) #returns in a list
#a = file.readlines()
#print(len(a))
#print(file.readline()) #returns single line from the file

#Check whether the file exists or not
import os
'''
if os.path.exists('example.txt'):
    f = open('example.txt').read()
    print(f)
    print(f'File is already present')
else:
    print("File not found")

#checking the file and its size
file_path = "example.txt"
if os.path.exists(file_path):
    print(f'File size is {os.path.getsize(file_path)}bytes')
    print(f'File Absolute path is {os.path.abspath(file_path)}')
else:
    print('File not found')

#'w' mode --> it will automatically creates a file and if same file name is present it
#overrides the content in previous file
a = open('agents.txt','w')
print(a)
a.write("AAA-HYD-001 students are good and cool.")
a.write("\n Yes it is True")
a.writelines("Agentic AI is the big thing happening.\t The world is progressing")
a.close() 

#if the file is already present 'w' mode will overrider the content
#we can use with statement
with open('example.txt','w') as file:
    #print(file.read()) raises an Error
    print(file)
    file.write("Agentic AI is the big thing happening.\t The world is progressing")
    #no need to mention close()

#'a' append mode holds the same content in the existing file
with open('example.txt','a') as f:
    print(f)
    f.write("\nPython Agents RAG..")

with open('rag.txt','a') as r:
    print(r)
    r.writelines("Agents,MCP,RAG GEN AI...")

with open('rag.txt','r+') as d:
    print(d.read())
    d.write('\n Claude,ChatGPT,Copilot...')
import os
d = os.listdir() #returns list of all directories and files
#print(d)
for file in d:
    if file.endswith('.txt'):
        print(file)'''
#Exception Handling --> Program (try,except,finally)
'''Syntax as below
try:
    base statement(s) which may raise error...
    ..........
except Exception (Error name) as e:
    ........... 
finally:
    statement(s) .....
'''   
#TypeError,ValueError,Index Error,Arithmetic Error,ZeroDivision Error,Attribute Errors
'''a,b = map(int,input("Enter the values").split(','))
try:
    result = a/b
    print(f'Result is {result}')
except ZeroDivisionError:
    print('Denominator cannot be zero')'''
'''
#Multiple Exceptions
try:
    a,b = map(int,input("Enter the values").split(','))
    result = a/b
    print(f'Result is {result}')
except ZeroDivisionError:
    print('Denominator cannot be zero')
except ValueError:
    print('Values to be of integer format only')
finally:
    print("Anyways this will be printed...")
'''
#Exceptions together
try:
    a,b = map(int,input("Enter the values").split(','))
    result = a/b
    print(f'Result is {result}')
except (ZeroDivisionError,ValueError) as e:
    print(f"The error occured : {e}")
finally:
    print("Anyways this will be printed...")