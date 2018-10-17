from datetime import datetime

prompt = ">"

print("\tplease key in the date like this :'YYYYMMDD'")
print("\n\tWhat's the date today?")

Y = input(prompt)
weekday = datetime.strptime(Y,"%Y%m%d").isoweekday()

#datetime.strptime = creates a datetime ...
#object from a string representing a date and time and a corresponding format string

#datetime.isoweekday() ...
#Return the day of the week as an integer, where Monday is 1 and Sunday is 7.


if weekday == 1:
    x = "Mon."
    
elif weekday == 2:
    x = "TUE."
    
elif weekday == 3:
    x = "WED."
    
elif weekday == 4:
    x = "THU."
    
elif weekday == 5:
    x = "FRI."
    
elif weekday == 6:
    x = "SAT."
    
elif weekday == 7:
    x = "SUN."
    
print ("\tToday is %r" %x)
