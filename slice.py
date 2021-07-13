fruits = ["apple", "banana", "cherry", "banana", "watermelon", "blueberry"]


slice1 = fruits[1:5]
show_slice1 = print(slice1)

apple1 = fruits[0]
slice_of_apple = print(apple1[:3])
#to concatenate, you only want to add two elements of the same type

print(fruits.count("banana"))
print(slice1.count("banana"))
#we can see that even if slice1 is supposed to slice the fruits, it still has all the elements of fruits stored

#index and count both look for elements in the string that start with the requested format
#split will seperate the string following whatever rule you apply