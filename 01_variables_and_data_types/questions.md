# 🐍 Variables and Data Types - Questions

> **Master Python's fundamental building blocks!** 🧱

---

## 🏷️ **Question Categories**

- 🟢 **🟢 Basic** - Foundational concepts
- 🟡 **🟡 Intermediate** - Practical applications
- 🟠 **🟠 Advanced** - Complex scenarios
- 🔴 **🔴 Expert** - Real-world challenges

---

## 🟢 **Basic Level Questions** (1-10)

### Question 1: Creating Your First Variables ⭐

**⏱️ Time Estimate:** 3 minutes  
**🎯 Category:** Basic Types  
**📝 Skills Tested:** Variable creation, assignment

**Task:** Create simple variables to store basic information.

**What to do:**

- Create a variable called `name` and store your name in it
- Create a variable called `age` and store your age as a number
- Create a variable called `is_student` and store `True` or `False`

**Example:**

```python
name = "Alice"
age = 25
is_student = True
```

**Think about:**

- What types of data are you storing?
- How do you choose good variable names?

**💡 Tip:** Use descriptive names that explain what the variable contains!

---

### Question 2: Understanding Different Data Types ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Data Types  
**📝 Skills Tested:** String, integer, float, boolean

**Task:** Create variables of different data types and check their types.

**What to do:**

- Create a string variable (text in quotes)
- Create an integer variable (whole number)
- Create a float variable (decimal number)
- Create a boolean variable (True or False)
- Use `type()` to check what type each variable is

**Example:**

```python
text = "Hello World"
number = 42
decimal = 3.14
is_true = True

print(type(text))    # Should show: <class 'str'>
print(type(number))  # Should show: <class 'int'>
```

**Think about:**

- What's the difference between `42` and `"42"`?
- When would you use each data type?

---

### Question 3: Basic Math with Variables ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Numbers  
**📝 Skills Tested:** Arithmetic operations

**Task:** Use variables to perform simple calculations.

**What to do:**

- Create two number variables (like `a = 10` and `b = 5`)
- Add them together and store the result in a new variable
- Subtract them and store the result
- Multiply them and store the result
- Print all results

**Example:**

```python
a = 10
b = 5

sum_result = a + b
difference = a - b
product = a * b

print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
```

**Think about:**

- Can you use the same variable name for different results?
- What happens if you change the values of `a` and `b`?

---

### Question 4: Working with Strings ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Strings  
**📝 Skills Tested:** String operations

**Task:** Create and combine strings using variables.

**What to do:**

- Create a variable with your first name
- Create a variable with your last name
- Combine them to create your full name
- Print your full name

**Example:**

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Should print: John Doe
```

**Think about:**

- What happens if you try to add a string and a number?
- How can you add a space between the names?

---

### Question 5: Converting Between Types ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Type Conversion  
**📝 Skills Tested:** Basic type conversion

**Task:** Convert between different data types.

**What to do:**

- Create a string variable with a number (like `"123"`)
- Convert it to an integer using `int()`
- Create a float variable (like `3.14`)
- Convert it to an integer using `int()`
- Print the results

**Example:**

```python
number_string = "123"
number_int = int(number_string)
print(number_int)  # Should print: 123

decimal_number = 3.14
whole_number = int(decimal_number)
print(whole_number)  # Should print: 3
```

**Think about:**

- What happens when you convert `3.14` to an integer?
- Can you convert any string to a number?

---

### Question 6: Using Variables in Calculations ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Practical Application  
**📝 Skills Tested:** Real-world variable usage

**Task:** Calculate the area of a rectangle using variables.

**What to do:**

- Create variables for length and width of a rectangle
- Calculate the area (length × width)
- Store the result in a variable
- Print the result

**Example:**

```python
length = 10
width = 5
area = length * width
print(f"The area is: {area}")
```

**Think about:**

- What if you want to calculate the area of a different rectangle?
- How can you make this calculation reusable?

---

### Question 7: Boolean Variables ⭐

**⏱️ Time Estimate:** 3 minutes  
**🎯 Category:** Booleans  
**📝 Skills Tested:** True/False values

**Task:** Work with boolean variables.

**What to do:**

- Create a variable `is_sunny` and set it to `True` or `False`
- Create a variable `is_raining` and set it to the opposite
- Print both variables

**Example:**

```python
is_sunny = True
is_raining = False
print(f"Sunny: {is_sunny}")
print(f"Raining: {is_raining}")
```

**Think about:**

- When would you use `True` vs `False`?
- Can you think of other yes/no situations?

---

### Question 8: Updating Variables ⭐

**⏱️ Time Estimate:** 3 minutes  
**🎯 Category:** Variable Assignment  
**📝 Skills Tested:** Changing variable values

**Task:** Update the value of a variable.

**What to do:**

- Create a variable called `score` and set it to 0
- Print the score
- Update the score to 100
- Print the score again

**Example:**

```python
score = 0
print(f"Score: {score}")

score = 100
print(f"Score: {score}")
```

**Think about:**

- What happens to the old value when you update a variable?
- Can you update a variable multiple times?

---

### Question 9: Combining Different Data Types ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Mixed Types  
**📝 Skills Tested:** Working with different types

**Task:** Create a simple profile using different data types.

**What to do:**

- Create variables for: name (string), age (integer), height (float), is_student (boolean)
- Print all the information in a nice format

**Example:**

```python
name = "Alice"
age = 20
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")
```

**Think about:**

- How can you make the output look better?
- What other information could you add?

---

### Question 10: Simple Input and Variables ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** User Input  
**📝 Skills Tested:** Getting user input

**Task:** Get input from the user and store it in variables.

**What to do:**

- Ask the user for their name using `input()`
- Store the input in a variable
- Ask the user for their age
- Convert the age to an integer
- Print a greeting with their information

**Example:**

```python
name = input("What is your name? ")
age_string = input("What is your age? ")
age = int(age_string)

print(f"Hello {name}, you are {age} years old!")
```

**Think about:**

- What type does `input()` return?
- Why do you need to convert the age to an integer?

---

## 🟡 **Intermediate Level Questions** (11-15)

### Question 11: Multiple Variables in One Line ⭐⭐

**⏱️ Time Estimate:** 3 minutes  
**🎯 Category:** Assignment  
**📝 Skills Tested:** Multiple assignment

**Task:** Assign multiple variables at once.

**What to do:**

- Assign three different values to three variables in one line
- Print all three variables

**Example:**

```python
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")
```

**Think about:**

- How many values do you need for three variables?
- What happens if you have more variables than values?

---

### Question 12: Swapping Variables ⭐⭐

**⏱️ Time Estimate:** 3 minutes  
**🎯 Category:** Variable Manipulation  
**📝 Skills Tested:** Variable swapping

**Task:** Swap the values of two variables.

**What to do:**

- Create two variables with different values
- Swap their values
- Print both variables before and after

**Example:**

```python
a = 10
b = 20
print(f"Before: a = {a}, b = {b}")

a, b = b, a
print(f"After: a = {a}, b = {b}")
```

**Think about:**

- How many lines of code do you need to swap variables?
- What happens to the original values?

---

### Question 13: String Formatting with Variables ⭐⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** String Formatting  
**📝 Skills Tested:** f-strings

**Task:** Use f-strings to format output with variables.

**What to do:**

- Create variables for a product name and price
- Use f-strings to create a nice product description
- Print the formatted string

**Example:**

```python
product = "Laptop"
price = 999.99
description = f"The {product} costs ${price}"
print(description)
```

**Think about:**

- How do f-strings make output formatting easier?
- Can you use expressions inside f-strings?

---

### Question 14: Simple Calculator with Variables ⭐⭐

**⏱️ Time Estimate:** 8 minutes  
**🎯 Category:** Practical Application  
**📝 Skills Tested:** Variables in calculations

**Task:** Create a simple calculator using variables.

**What to do:**

- Create variables for two numbers
- Calculate and store: sum, difference, product, quotient
- Print all results

**Example:**

```python
num1 = 15
num2 = 3

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
```

**Think about:**

- What happens if you divide by zero?
- How can you make the output more readable?

---

### Question 15: Temperature Conversion ⭐⭐

**⏱️ Time Estimate:** 8 minutes  
**🎯 Category:** Real-world Application  
**📝 Skills Tested:** Formula implementation

**Task:** Convert temperature from Celsius to Fahrenheit.

**What to do:**

- Create a variable for temperature in Celsius
- Use the formula: Fahrenheit = (Celsius × 9/5) + 32
- Store the result in a variable
- Print both temperatures

**Example:**

```python
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
```

**Think about:**

- What happens if you change the Celsius temperature?
- How can you make this conversion reusable?

---

## 🟠 **Advanced Level Questions** (16-20)

### Question 16: Working with Constants ⭐⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Constants  
**📝 Skills Tested:** Constant naming

**Task:** Create constants for mathematical values.

**What to do:**

- Create constants for PI (3.14159) and GRAVITY (9.81)
- Use them in a calculation (like area of a circle)
- Print the result

**Example:**

```python
PI = 3.14159
GRAVITY = 9.81

radius = 5
area = PI * radius * radius
print(f"Area of circle: {area}")
```

**Think about:**

- Why use uppercase for constants?
- What makes a value a "constant"?

---

### Question 17: String Operations with Variables ⭐⭐

**⏱️ Time Estimate:** 8 minutes  
**🎯 Category:** String Methods  
**📝 Skills Tested:** String manipulation

**Task:** Manipulate strings using variables.

**What to do:**

- Create a variable with a sentence
- Create variables for the length, uppercase version, and lowercase version
- Print all the information

**Example:**

```python
sentence = "Hello World"
length = len(sentence)
upper_case = sentence.upper()
lower_case = sentence.lower()

print(f"Original: {sentence}")
print(f"Length: {length}")
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")
```

**Think about:**

- What does `len()` tell you about a string?
- How do string methods work?

---

### Question 18: Simple Data Validation ⭐⭐

**⏱️ Time Estimate:** 8 minutes  
**🎯 Category:** Input Validation  
**📝 Skills Tested:** Type checking

**Task:** Validate user input and convert it safely.

**What to do:**

- Get a number from the user
- Check if it can be converted to an integer
- If yes, convert it; if no, use a default value
- Print the result

**Example:**

```python
user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
else:
    number = 0

print(f"The number is: {number}")
```

**Think about:**

- What happens if the user enters "abc"?
- How can you handle different types of invalid input?

---

### Question 19: Working with Multiple Data Types ⭐⭐

**⏱️ Time Estimate:** 10 minutes  
**🎯 Category:** Mixed Operations  
**📝 Skills Tested:** Type handling

**Task:** Create a simple inventory system.

**What to do:**

- Create variables for: item name (string), quantity (integer), price (float), in_stock (boolean)
- Calculate total value (quantity × price)
- Print a formatted inventory report

**Example:**

```python
item_name = "Laptop"
quantity = 5
price = 999.99
in_stock = True

total_value = quantity * price

print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Price: ${price}")
print(f"In Stock: {in_stock}")
print(f"Total Value: ${total_value}")
```

**Think about:**

- How can you format the price to show only 2 decimal places?
- What if the item is out of stock?

---

### Question 20: Simple Game Score System ⭐⭐

**⏱️ Time Estimate:** 10 minutes  
**🎯 Category:** Game Logic  
**📝 Skills Tested:** Variable updates

**Task:** Create a simple scoring system.

**What to do:**

- Start with a score of 0
- Add points for different actions (like +10 for correct answer, +5 for bonus)
- Keep track of total questions answered
- Print the final score and average

**Example:**

```python
score = 0
questions_answered = 0

# Simulate some game actions
score += 10  # Correct answer
questions_answered += 1

score += 5   # Bonus
questions_answered += 1

score += 10  # Another correct answer
questions_answered += 1

average = score / questions_answered

print(f"Final Score: {score}")
print(f"Questions Answered: {questions_answered}")
print(f"Average Score: {average}")
```

**Think about:**

- How can you make this more interactive?
- What happens if no questions are answered?

---

## 🔴 **Expert Level Questions** (21-25)

### Question 21: Advanced String Formatting ⭐⭐⭐

**⏱️ Time Estimate:** 12 minutes  
**🎯 Category:** Advanced Formatting  
**📝 Skills Tested:** Complex string formatting

**Task:** Create a formatted receipt using variables.

**What to do:**

- Create variables for item details, prices, and quantities
- Calculate subtotal, tax, and total
- Format everything as a professional receipt

**Example:**

```python
item1_name = "Coffee"
item1_price = 3.50
item1_qty = 2

item2_name = "Sandwich"
item2_price = 8.99
item2_qty = 1

subtotal = (item1_price * item1_qty) + (item2_price * item2_qty)
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax

print("=== RECEIPT ===")
print(f"{item1_name} x{item1_qty}: ${item1_price * item1_qty:.2f}")
print(f"{item2_name} x{item2_qty}: ${item2_price * item2_qty:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
```

---

### Question 22: Data Type Conversion Challenge ⭐⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Type Conversion  
**📝 Skills Tested:** Complex conversions

**Task:** Handle various data type conversions safely.

**What to do:**

- Create a function that safely converts different inputs
- Handle strings, integers, floats, and booleans
- Provide meaningful error messages

**Example:**

```python
def safe_convert(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        elif target_type == "bool":
            return bool(value)
    except ValueError:
        return f"Error: Cannot convert '{value}' to {target_type}"

# Test the function
print(safe_convert("123", "int"))
print(safe_convert("3.14", "float"))
print(safe_convert("abc", "int"))
```

---

### Question 23: Variable Scope Understanding ⭐⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Scope  
**📝 Skills Tested:** Variable scope rules

**Task:** Understand how variables work in different scopes.

**What to do:**

- Create global variables
- Create a function that uses and modifies variables
- Demonstrate scope rules

**Example:**

```python
global_score = 100

def update_score(points):
    global global_score
    local_score = 50
    global_score += points
    print(f"Local score: {local_score}")
    print(f"Global score: {global_score}")

print(f"Initial global score: {global_score}")
update_score(25)
print(f"Final global score: {global_score}")
```

---

### Question 24: Complex Data Structure Basics ⭐⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Data Structures  
**📝 Skills Tested:** Lists and dictionaries

**Task:** Work with basic data structures.

**What to do:**

- Create a list of numbers
- Create a dictionary with person information
- Access and modify the data

**Example:**

```python
# List of scores
scores = [85, 92, 78, 96, 88]
average_score = sum(scores) / len(scores)

# Dictionary of person
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(f"Scores: {scores}")
print(f"Average: {average_score}")
print(f"Person: {person['name']} is {person['age']} years old")
```

---

### Question 25: Real-world Application Project ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Project  
**📝 Skills Tested:** All concepts combined

**Task:** Create a simple student grade calculator.

**What to do:**

- Store student information (name, grades for different subjects)
- Calculate average grade
- Determine letter grade
- Print a formatted report

**Example:**

```python
student_name = "John Doe"
math_grade = 85
science_grade = 92
english_grade = 78

average_grade = (math_grade + science_grade + english_grade) / 3

if average_grade >= 90:
    letter_grade = "A"
elif average_grade >= 80:
    letter_grade = "B"
elif average_grade >= 70:
    letter_grade = "C"
else:
    letter_grade = "F"

print("=== GRADE REPORT ===")
print(f"Student: {student_name}")
print(f"Math: {math_grade}")
print(f"Science: {science_grade}")
print(f"English: {english_grade}")
print(f"Average: {average_grade:.1f}")
print(f"Letter Grade: {letter_grade}")
```

---

## 🎯 **Learning Path**

**Start Here:** Questions 1-5 (Absolute basics)
**Build Confidence:** Questions 6-10 (Simple applications)
**Practice More:** Questions 11-15 (Intermediate concepts)
**Challenge Yourself:** Questions 16-20 (Advanced topics)
**Master Level:** Questions 21-25 (Expert applications)

---

## 💡 **Tips for Success**

1. **Start Simple:** Don't skip the basic questions - they build your foundation
2. **Practice Regularly:** Work on a few questions each day
3. **Experiment:** Try changing values and see what happens
4. **Use Print:** Always print your variables to see what's happening
5. **Ask Questions:** If something doesn't make sense, investigate it

---

## 🔧 **Common Mistakes to Avoid**

- ❌ Using `=` instead of `==` for comparisons
- ❌ Forgetting quotes around strings
- ❌ Not converting input() to the right type
- ❌ Using unclear variable names
- ❌ Forgetting to print your results

---

## 🆕 **Additional Practice Questions** (26-30)

### Question 26: Memory Management and Garbage Collection ⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Memory Management  
**📝 Skills Tested:** Memory optimization, garbage collection, reference counting

**Task:** Understand Python's memory management and optimize memory usage in applications.

**Real-life Scenario:** You're building a data processing application that handles large datasets:
- Monitor memory usage of different data types
- Understand reference counting and garbage collection
- Optimize memory usage for large data structures
- Handle memory leaks and circular references

**Think about:**
- How does Python manage memory automatically?
- What happens when objects are no longer referenced?
- How can you optimize memory usage in your applications?

**Challenge yourself:**
- Can you create a memory-efficient data structure for large datasets?
- What if you need to handle memory constraints in embedded systems?

**If you can't solve this, review:** Memory management, garbage collection, reference counting, memory optimization

**💾 Memory Tip:** Understanding memory management helps build efficient applications!

---

### Question 27: Deep Copy vs Shallow Copy ⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Object Copying  
**📝 Skills Tested:** copy module, nested objects, reference vs value

**Task:** Master different copying techniques for complex data structures.

**Real-life Scenario:** You're building a configuration management system:
- Copy configuration objects without affecting originals
- Handle nested dictionaries and lists
- Understand when to use shallow vs deep copy
- Prevent unintended modifications to shared data

**Think about:**
- What's the difference between copying references and copying values?
- When do you need to copy nested structures completely?
- How do you prevent accidental data modification?

**Challenge yourself:**
- Can you implement a custom copying mechanism for complex objects?
- What if you need to handle circular references in your data?

**If you can't solve this, review:** copy module, shallow copy, deep copy, nested objects

**📋 Copy Logic:** Choose the right copying method to prevent data corruption!

---

### Question 28: Magic Methods and Dunder Methods ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Special Methods  
**📝 Skills Tested:** dunder methods, operator overloading, object behavior

**Task:** Use Python's magic methods to customize object behavior.

**Real-life Scenario:** You're building a custom data structure library:
- Implement custom comparison operators
- Override string representation methods
- Create objects that behave like built-in types
- Implement custom iteration and indexing

**Think about:**
- How do you make your objects work with built-in functions?
- What happens when you need custom behavior for operators?
- How do you make objects more intuitive to use?

**Challenge yourself:**
- Can you create a custom list-like class with special behavior?
- What if you need to implement complex mathematical operations?

**If you can't solve this, review:** Magic methods, dunder methods, operator overloading, object customization

**🎭 Magic Methods:** Use dunder methods to make your objects behave like built-in types!

---

### Question 29: Dependency Management and Virtual Environments ⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Project Management  
**📝 Skills Tested:** virtual environments, dependency management, project isolation

**Task:** Manage Python dependencies and create isolated project environments.

**Real-life Scenario:** You're working on multiple Python projects with different requirements:
- Create isolated environments for different projects
- Manage package versions and conflicts
- Handle project dependencies and requirements
- Ensure reproducible development environments

**Think about:**
- How do you prevent package conflicts between projects?
- What happens when different projects need different package versions?
- How do you ensure your project works on other machines?

**Challenge yourself:**
- Can you create a project template with proper dependency management?
- What if you need to handle complex dependency trees?

**If you can't solve this, review:** Virtual environments, pip, requirements.txt, dependency management

**🌍 Environment Management:** Isolate projects to prevent dependency conflicts!

---

### Question 30: Built-in Functions for File Handling ⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** File Operations  
**📝 Skills Tested:** built-in functions, file handling, I/O operations

**Task:** Use Python's built-in functions for efficient file operations.

**Real-life Scenario:** You're building a file processing utility:
- Use built-in functions for file operations
- Handle different file types and encodings
- Implement efficient file reading and writing
- Process large files without memory issues

**Think about:**
- Which built-in functions are most efficient for file operations?
- How do you handle different file encodings and formats?
- What's the best way to process large files?

**Challenge yourself:**
- Can you create a file processing pipeline using only built-in functions?
- What if you need to handle binary files and different encodings?

**If you can't solve this, review:** Built-in functions, file I/O, encoding handling, memory efficiency

**📁 File Functions:** Use built-in functions for efficient and reliable file operations!

---

## 🎯 **Updated Study Progress Summary**

### 📈 **Completion Status:**

- 🟢 **Basic Level:** 0/10 completed
- 🟡 **Intermediate Level:** 0/10 completed
- 🟠 **Advanced Level:** 0/5 completed
- 🔴 **Expert Level:** 0/5 completed
- 🆕 **Additional Practice:** 0/5 completed

### ⏱️ **Total Estimated Time:** 12 hours 30 minutes

### 🎓 **Next Steps:**

1. Start with Basic Level questions (1-10)
2. Move to Intermediate when comfortable
3. Challenge yourself with Advanced concepts
4. Master Expert level for real-world scenarios
5. Practice with Additional Questions (26-30) featuring modern Python features

---

> **💡 Pro Tip:** Modern Python features like enhanced memory management and improved built-in functions make data handling more efficient and reliable!

---

_Remember: Every expert was once a beginner. Take your time, practice regularly, and don't be afraid to make mistakes!_ 🚀
