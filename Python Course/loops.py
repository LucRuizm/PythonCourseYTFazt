
#FOR

foods = ['apple', 'bananas', 'bread', 'cheese', 'milk', 'grapes']

for food in foods:
    if food == "cheese":
        break              # break the loop when the word cheese appears
    print (food)


for food in foods:
    if food == "cheese":
        continue           # the word cheese is omitted
    print (food)

for number in range (1, 9):  #the variable (number) is being declared here
    print (number)


for letter in "Hello There":
    print (letter)

#WHILE

count = 4

while count <= 10:
    print(count)
    count = count + 1
