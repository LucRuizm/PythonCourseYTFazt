#EXAMPLES:

# print ("asdfgh")

# dir(x)

# type(34)

# len("hello")


def hello():              # Creating a FUNCTION
    print ("Hello World") 

hello()  #Call the function created

def hello_name(name):              # Creating a FUNCTION with PARAMETER
    print ("Hello " + name) 

hello_name("Michael")  #Call the function with parameter created, adding a string
hello_name("Carl")
hello_name("Claire")

def hello_name2(name= "Person"):    # Creating a FUNCTION with PARAMETER
    print ("Hello " + name) 

hello_name2("Michael")  #Call the function with parameter created, adding a string
hello_name2("Carl")
hello_name2("Claire")
hello_name2() #The function called will print "Person" in defect



def add (numberOne, numberTwo):
    return numberOne + numberTwo

print(add(1, 90))
print(add(85, 190))
print(add(6, 56))



#Functions LAMBDA

add2 = lambda numberThree, numberFour: numberThree + numberFour

print(add2(1, 90))
print(add2(85, 190))
print(add2(6, 56))
