#The datetime module supplies classes for manipulating dates and times.
#While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
import datetime

print(datetime.date.today())

#arithmetic operation on datetime
#date, time, microseconds
print(datetime.datetime.today()- datetime.datetime(1994, 10, 10, 3, 59))