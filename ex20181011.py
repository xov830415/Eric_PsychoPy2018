from datetime import datetime

prompt = "\t>"

print("\tplease key in the date like this :'YYYYMMDD'")
print("\n\tWhat's the date today?")

date = input(prompt)
weekday = datetime.strptime(date,"%Y%m%d").isoweekday()

#datetime.strptime = creates a datetime object...
#from a string representing a date and time and a corresponding format string

#%Y = Year with century as a decimal number
#%m = Month as a zero-padded decimal number
#%d = Day of the month as a zero-padded decimal number

#datetime.isoweekday() ...
#Return the day of the week as an integer, where Monday is 1 and Sunday is 7.

# 把 1 -> 7轉換成 Mon. -> Sun.
if weekday == 1:
    x = "Mon."
    
if weekday == 2:
    x = "TUE."
    
if weekday == 3:
    x = "WED."
    
if weekday == 4:
    x = "THU."
    
if weekday == 5:
    x = "FRI."
    
if weekday == 6:
    x = "SAT."
    
if weekday == 7:
    x = "SUN."
    
print ("\n\tToday is %r" %x)
