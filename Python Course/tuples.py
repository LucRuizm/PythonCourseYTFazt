#Tuples is another way to create lists, but it is immutable.
x= (1, 2, 3)
print (x)
print (type(x))

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
print (months)

y = tuple((1, 2, 3)) #In function of the type of application this is useful or not
print (y)

#print(dir(tuple))

z= (1,)
print (z)

print(x[0])
print(x[1])
print(x[2])

#del x     To delete the variable
#print (x) Verification

locations = {
    (35.689722, 139.692222) : 'Tokyo',
    (40.712728, -74.006015) : 'New York',
    (-34.599722, -58.381944) : 'Buenos Aires'
}
print (locations)

