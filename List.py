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
