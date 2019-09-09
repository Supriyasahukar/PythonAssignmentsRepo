#@author: kgsharathkumar from PathTech
''' Write and Execute a python program to find given string is palindrome or not?
'''
str=input("enter the string")
rev=[]
a=len(str)
rev=reversed(str)    
if list(str)==list(rev):
    print("palindrome")
else:
    print("not palindrome")

#alternate method
'''
input_string=input("enter any string:")
if input_string[0: ]==input_string[ ::-1]:
    print("string is Palindrome" )
else:
    print("string is not a Palindrome")
    '''
