# ### Question 10: Simple Input and Variables ⭐

# **⏱️ Time Estimate:** 5 minutes  
# **🎯 Category:** User Input  
# **📝 Skills Tested:** Getting user input

# **Task:** Get input from the user and store it in variables.

# **What to do:**

# - Ask the user for their name using `input()`
# - Store the input in a variable
# - Ask the user for their age
# - Convert the age to an integer
# - Print a greeting with their information


# **Think about:**

# - What type does `input()` return?
# - Why do you need to convert the age to an integer?

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Welcome, {user_name}! You are {user_age} years old.")
