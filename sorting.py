numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Sorted list:", sorted_numbers)

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("Sorted list:", numbers)

# Using sorted()
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Descending sorted list:", sorted_numbers_desc)

# Using sort() method
numbers.sort(reverse=True)
print("Descending sorted list:", numbers)
