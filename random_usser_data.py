# First, we need to import the 'random' module
# This helps us to generate random numbers and randomly select items from a list
import random

# Step 1: Create a list of names
names = ["Alice", "Bob", "Lisa", "Diana", "Eve", "Frank"]

# Step 2: Define a function that generates a random user
def generate_user():
    # Pick a random name from the names list
    random_name = random.choice(names)
    
    # Generate a random age between 18 and 60
    random_age = random.randint(18, 60)
    
    # Return the name and age as a dictionary
    return {"name": random_name, "age": random_age}

# Step 3: Generate and print random user data
# You can change the range (5) to generate more or fewer users
for i in range(5):
    user = generate_user()
    print(f"User {i+1}: Name = {user['name']}, Age = {user['age']}")
