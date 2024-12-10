import random

def generate_random_name(length_first=5, length_last=7):
    """
    Generate a random name with specified lengths for first and last names.
    
    Args:
    - length_first (int): Length of the first name. Default is 5.
    - length_last (int): Length of the last name. Default is 7.
    
    Returns:
    - str: A string in the format 'First Last'.
    """
    # Define the pool of characters or syllables to use
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    # Helper function to create a name
    def random_name(length):
        name = ""
        for i in range(length):
            if i % 2 == 0:  # Alternate between consonants and vowels
                name += random.choice(consonants)
            else:
                name += random.choice(vowels)
        return name.capitalize()

    # Generate first and last names
    first_name = random_name(length_first)
    last_name = random_name(length_last)
    
    return f"{first_name} {last_name}"

# Example usage
print(generate_random_name())
