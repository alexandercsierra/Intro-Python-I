"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# print(calendar.month(20, 5)) 

def calFunc():
  ans = input('Which calendar would you like to see?').split()
  y = "20"
  m = "05"    
  if len(ans) == 1:
    m = ans[0]
  elif len(ans) == 2:
    m = ans[0]
    y = ans[1]
  if m.isdigit() == False or y.isdigit() == False:
    return print('please enter numbers')
  
  year = int(y)
  month = int(m)
  if month > 12 or month < 1:
    return print('please enter a valid month')
  print(calendar.month(year, month))
  print(f'month is {m}')
  print(f'year is {y}')

calFunc()
