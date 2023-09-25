from datetime import datetime, date
 
year1 = int(input("Enter starting year: "))
month1 = int(input("Enter starting month: "))
day1 = int(input("Enter starting day: "))
date1 = date(year1,month1,day1)

year2 = int(input("Enter final year: "))
month2 = int(input("Enter final month: "))
day2 = int(input("Enter final day: "))
date2 = date(year2,month2,day2)

print('Time difference:', str(date2 - date1))
