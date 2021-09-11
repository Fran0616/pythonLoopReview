# pythonLoopReview
Loop Practice 


Task
=

1. Create a list called single_digits that consists of the numbers 0-9 (inclusive).
2. Create a for loop that goes through single_digits and prints out each one.
3. Before the loop, create a list called squares. Assign it to be an empty list to begin with.
4. Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.
5. After the for loop, print out squares.
6. Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
7. Print cubes. Good job!

[Script](https://github.com/Fran0616/pythonLoopReview/blob/main/forExample.py)
= 

```
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
```
Output 
= 
```
0
1
2
3
4
5
6
7
8
9
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```
Conclusion 
= 
In this lesson I learned about how I can use a loop to perform the process of iteration. Programming languages like python implement two types of iteration: indefinite and definite iteration. In indefinite iteration the number of times the loop is executed depends on how many times a condition is met. Indefinite iteration the number of times the loop is executed is defined in advance. In For loop the programmer knows in advance how many times the loop will need to be iterated because we work on a collection of predefined length. 
