# from re import template
# import string
# import datetime


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



# template1=string.Template("Answer is : $x > $y")
# str1=template1.substitute(x=22 ,y=18)
# print(str1)

#=======================================================================================
from datetime import date, time, datetime,timedelta


# print(date.today())
# print(datetime.now())

# date1=date(1998,2,2)
# print(date1)


# time1=time( 23,59,56) # we fan add hour  min  and  second too
# print(time1)


# datetime1=datetime(2012,4,1,14,20,20,233333)
# year month  day   hour minute  seond microSec
# print(datetime1)



# datetime1=datetime(2012,4,1,14,20,20,233333)
# print(datetime1.month)




# print(datetime.now())
# print(datetime.utcnow())


# print(datetime.now().strftime("%Y / %m  %H:%M:%S"))



# To design our  date time:

# date3=datetime.strptime("8/18/2021","%m/%d/%Y")
# print(date3.year)
# print(date3.month)
# print(date3.day)



# date3=datetime.strptime("2022-16-2 20:12:25","%Y-%d-%m  %H:%M:%S")
# print(date3.hour)


#===============Library for  TimeZone=======================
import pytz
#Base on any country the momentum time of each country can be used

#Time zone for America  is:
# print(datetime.now(pytz.timezone('US/Central')))

# to add  two dates  time hours  :
date1=datetime(2022,2,18,13,25,25)
timedelta1=timedelta(days=2,hours=5,minutes=20,seconds=10)
date3=date1+timedelta1
print(date1)
print(date3)


# To measure  exact YOu  Age  based on this prog:

# date1=datetime(1979,11,8)
# date2=datetime(2022,2,18)
# daydiff=date2-date1
# print(daydiff)
# # to avoide negative number:
# daydiff=abs(date1-date2)
# mindiff=abs(date1-date2).total_seconds/60
# hourdiff=abs(date1-date2).total_seconds()/(60*60)
# daydiff=abs(date1-date2).total_seconds()/(60*60*24)
# print(daydiff)




































