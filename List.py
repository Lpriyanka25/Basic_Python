#EXAMPLE 1
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements by index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1]) # Output: cherry (negative index starts from the end)

# Adding an element
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Inserting at a specific position
fruits.insert(1, "mango")
print(fruits)  # Output: ['apple', 'mango', 'banana', 'cherry', 'orange']

# Removing an element
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'orange']

# Removing the last element
fruits.pop()
print(fruits)  # Output: ['apple', 'mango', 'cherry']

#EXAMPLE 2
# Creating a new list with squares of numbers
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

numbers = [4, 2, 8, 6, 7]

# Sorting
numbers.sort()
print(numbers)  # Output: [2, 4, 6, 7, 8]

# Reversing
numbers.reverse()
print(numbers)  # Output: [8, 7, 6, 4, 2]

# Counting occurrences
print(numbers.count(8))  # Output: 1
