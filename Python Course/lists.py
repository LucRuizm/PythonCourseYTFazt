demo_list = [5, "Hello", 5.56, True, [1, 2, 3]]
colors= ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
#print (numbers_list)
#print (type(numbers_list))

#r = list(range(1, 11))
#print (r)

#print(dir(colors))
print(len(colors))

print(len(demo_list))

print (colors[1])
print (colors[-2])

print ('green' in colors) #True or False
print ('yellow' in colors)

colors.append('yellow')
print(colors)

#colors.append('violet, brown')
#print(colors)

#colors.extend(['pink, black, white'])
#print(colors)

#colors.insert(1, 'violet')
#print(colors)

#colors.insert(len(colors), 'black')
#print(colors)

#colors.pop() #Delete last position
#print (colors)

#colors.pop() #Delete last position
#colors.pop() #Delete last position
#print (colors)

#colors.remove('violet') #Delete the selected position
#print (colors)

#colors.pop(1) #Delete index
#print (colors)

#colors.clear() #Clear everything
#print (colors)

colors.sort()
print (colors)

colors.sort(reverse=True)
print (colors)

print(colors.index('red'))

print(colors.count('red'))



