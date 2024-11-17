import random

def generate_username():
    # Lists of adjectives and nouns
    adjectives = ["Fast", "Silly", "Brave", "Happy", "Clever", "Mighty", "Cool", "Lazy", "Sneaky", "Quirky"]
    nouns = ["Panda", "Tiger", "Dragon", "Unicorn", "Cheetah", "Falcon", "Wolf", "Phoenix", "Dolphin", "Penguin"]
    
    # Randomly select an adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Generate a random number to append
    number = random.randint(1, 9999)
    
    # Combine parts to create the username
    username = f"{adjective}{noun}{number}"
    return username

# Generate and print 10 random usernames
for _ in range(10):
    print(generate_username())
