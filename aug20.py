'''
Regular Expressions --> re module -->re.search(),re.findall(),re.match(),re.fullmatch(),re.fulliter(),
re.sub(),re.split(),re.compile(),re.escape()

re.compile(pattern) --> when we want to use the pattern multiple times we can compile the pattern

data = "Codegnan marks its 8 th Anniversary,founded in 2018"
import re
pattern = re.compile(r'\d+')
print(pattern)
result = pattern.findall(data)
print(result)
f = pattern.search(data)
print(f)
print(f.group())

#re.escape() -->we use this to escape special characters such as (.,*,?..) to treat as normal characters,
#adds backslash before special characters
import re
file_name = "data.txt"
g = re.escape(file_name)
print(g)
'''
#Form Validations using re -->Email Validation,Mobile Number Validation,PAN Validation,Aadhar Validation...abs

#saketh@codegnan.com, aakash.reddy123@yahoo.in,22x51a3237@srecnandyal.edu.in 

#if we observe the pattern as below
import re
'''pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
#Email ID Validation
email_id = input("Enter the MailID:")
g = re.fullmatch(pattern,email_id)
print(g)
print(g.group())

#Mobile Number Validation --> 8106429771, 6303711464 , 9182782324 , 7569395968

pattern = r'^[6-9]\d{9}$'
mobile_number = input("Enter the mobile number:")
h = re.fullmatch(pattern,mobile_number)
print(h)
print(h.group())

#PAN Validation --> DFPPK1543P , REWPS3699N , CVWPN3935N

pattern =r'^[A-Z]{5}[0-9]{4}[A-Z]$'
pan = input("Enter the PAN ID:")
j = re.fullmatch(pattern,pan)
print(j)
print(j.group())
'''
#Aadhar Validation 12 digits ,PIN Validation  6 digits,Username Validation (alphabets,_,numbers,no special characters)

pattern = r'^[A-Za-z0-9_]+$'
username = input("Enter the username:")
k = re.fullmatch(pattern,username)
print(k)
print(k.group())






