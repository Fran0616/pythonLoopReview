single_digits = [0,1,2,3,4,5,6,7,8,9] #list listing numer 0-9
squares = []#empty list for sqaure num

for i in single_digits: #this for loop will go through single_dgits and print out each number in that list
  print(i)
for i in single_digits:#this list will sqaure each number from the single_digits
  i = i**2 #sqaure each number in single_digits list
  squares.append(i) #add the sqaured value to the sqaures list 
print (squares)#print complete list of sqaure list 

cubes = [i**3 for i in single_digits] #comprehension list to cube each number from the single_digits list 
print(cubes) # print cube list
