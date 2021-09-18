myStr= "Hello World"
#print (dir(myStr)) Print in screen what you can do with different methods
#For example using .upper, the string will be like this: HELLO WORLD
#String Methods:
print (myStr.upper())
print (myStr.lower())
print (myStr.title())
print (myStr.encode())
print (myStr.capitalize())
print (myStr.swapcase())

print (myStr.replace("Hello", "Bye"))
print (myStr.replace("Hello", "Bye").upper())
print (myStr.count("l")) #How many times the "l" is used
print (myStr.count(" ")) #How many times empty character is used

print (myStr.startswith("Hola"))
print (myStr.startswith("Hello"))
print (myStr.startswith("He"))
print (myStr.endswith("Mundo"))
print (myStr.endswith("World"))
print (myStr.endswith("ld"))


print (myStr.split())
print (myStr.split("o"))
print (myStr.split("l"))

myStr2= "Lemon, Pies"
print (myStr2.split(","))

print (myStr2.find("o")) #Find the position [0, 1, 2, 3 ("O" is in the third position)]
print (myStr2.find(" ")) #6
print (myStr2.find("s")) #10
print (len(myStr2)) #9 
print (myStr2.index("m")) #Search the index

print (myStr2.isnumeric())
print (myStr2.isalpha())

print (myStr2[4]) #Print the character of the fourth position "n"

myStr3= "Ryan"
print ("My name is " + myStr3)
print (f"My name is: {myStr3}")
print ("My name is: {0}".format(myStr3))

