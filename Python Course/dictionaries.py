
product = {
    "name" : "book",
    "quantity" : 3,
    "price" : 5.99
} 

person = {
    "first_name" : "Ryan",
    "last_name" : "Rey",
    "age" : 45
}

print (product)
print (type(product))

print (person)
print (type(person))

#print(dir(person))

print(product.keys())
print(person.keys())

print(product.items()) #ITEMS OR VALUES 
print(person.values()) #ITEMS OR VALUES

#del person 
#print (person)

#person.clear()
#print(person) 

products = [
    {"name" : "book2", "quantity" : 3, "price" : 8.99},
    {"name" : "book3", "quantity" : 1, "price" : 10.99}
] # This is another way with tuples

print(products)