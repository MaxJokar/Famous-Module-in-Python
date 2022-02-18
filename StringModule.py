from re import template
import string
import datetime


# print(dir(string))
# print()

# print(dir(datetime))
# print(vars(datetime)) #More datailed
# print(datetime.__doc__ )
# print(datetime.__file__ ) #the address of  datetime Module in our system 
# print(datetime.__name__ ) 
# print(datetime.__cached__ ) 



#any info about  a  Module or  any class by:

# help(print)
# help(datetime.datetime.now)
# help(datetime.datetime)

# help(int)
#==============================================================

 
# print(string.ascii_letters):for number , Big Letter or small ones 

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation) # All  signs in Python
# print(string.printable)  # all things printable 

# str1=string.capwords("jack philiP londoN") # First Letter of a string converted to Capital and the other in to small
# print(str1)



template1=string.Template("Answer is : $x > $y")
str1=template1.substitute(x=22 ,y=18)
print(str1)























