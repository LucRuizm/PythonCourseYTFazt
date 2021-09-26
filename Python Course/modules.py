# To use modules you have options such as:

# Own modules
# Thirdy party modules (Recommendation: https://pypi.org/)
# Python modules (https://docs.python.org/3/py-modindex.html)


#PYTHON MODULES EXAMPLE (We can search in the link the documentation about it)

import datetime

print(datetime.date.today()) #With this methods print the actual datetime 

print(datetime.timedelta(minutes= 70)) #This method converts minutes to hours


#Other way to import the module
from datetime import timedelta

print(timedelta(minutes= 90))


#Other
from datetime import timedelta, date

print(timedelta(minutes= 120))
print(date.today())


#OWN MODULE

import fmath

fmath.add(5, 9) #Using method add

fmath.substract(10, 20) #Using method substract


#Other way

from fmath import add, substract

add(5, 7)
substract(1, 2)


#THIRDY PARTY MODULES (We can see on the pip website,
# the command to install the respective module in console and information about it)

from colorama import Fore, Style, init  #(In this case it will be printed on the Windows console.)

init (convert= True)
print (Fore.RED + "Hello World")


# Other modules that we can find for example are frameworks such as 
# Flask for web applications, Django for Apps and Tkinter for GUI (Graphical User Interfaces).