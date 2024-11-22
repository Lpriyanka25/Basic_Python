#example 1
def find_min_max(numbers):
    if not numbers:
        return "The list is empty!"
    
    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num

# Taking input from the user
try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    if numbers:  # Check if the list is not empty
        min_num, max_num = find_min_max(numbers)
        print(f"Minimum number: {min_num}")
        print(f"Maximum number: {max_num}")
    else:
        print("You did not enter any numbers.")
except ValueError:
    print("Invalid input! Please enter only numbers separated by spaces.")

#example 2
def find_min_max(numbers):
    if not numbers:
        return "The list is empty!"
    
    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num

# Example usage
numbers = [10, 20, 5, 35, 50, -10]
min_num, max_num = find_min_max(numbers)

print(f"Minimum number: {min_num}")
print(f"Maximum number: {max_num}")
