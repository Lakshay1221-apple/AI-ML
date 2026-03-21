"""
COMPLETE PYTHON GUIDE - FROM BASICS TO ADVANCED
================================================
This file covers all fundamental Python concepts with explanations and examples.
"""

# =============================================================================
# 1. PRINT STATEMENTS AND OUTPUT
# =============================================================================

"""
The print() function is used to display output to the console.
- Syntax: print(value1, value2, ..., sep=' ', end='\n')
- sep: separator between values (default is space)
- end: what to print at the end (default is newline)
"""

print("Hello, World!")  # Basic print
print("Hello", "Python", "Programming")  # Multiple values
print("Python", "is", "awesome", sep="-")  # Custom separator
print("Same line", end=" ")
print("continues here")  # Custom end character

# Formatted strings
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")  # f-string (Python 3.6+)
print("My name is {} and I'm {} years old".format(name, age))  # .format()
print("My name is %s and I'm %d years old" % (name, age))  # % formatting


# =============================================================================
# 2. DATA TYPES
# =============================================================================

"""
Python has several built-in data types:
1. Numeric: int, float, complex
2. Sequence: str, list, tuple, range
3. Mapping: dict
4. Set: set, frozenset
5. Boolean: bool
6. None: NoneType
"""

# --- Numeric Types ---
integer_num = 42                    # int: whole numbers
float_num = 3.14                    # float: decimal numbers
complex_num = 3 + 4j                # complex: complex numbers

print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# --- String (str) ---
"""
Strings are immutable sequences of characters.
Can be defined with single quotes, double quotes, or triple quotes
"""
string1 = 'Hello'
string2 = "World"
string3 = """Multi-line
string example"""

# String operations
print(string1 + " " + string2)      # Concatenation
print(string1 * 3)                  # Repetition
print(string1[0])                   # Indexing (0-based)
print(string1[1:4])                 # Slicing [start:end]
print(len(string1))                 # Length
print(string1.upper())              # Convert to uppercase
print(string1.lower())              # Convert to lowercase
print("Hello World".split())        # Split into list

# --- List ---
"""
Lists are mutable, ordered sequences that can contain mixed data types.
Syntax: [item1, item2, item3, ...]
"""
my_list = [1, 2, 3, "four", 5.0, True]
print(f"List: {my_list}")

# List operations
my_list.append(6)                   # Add to end
my_list.insert(0, 0)                # Insert at index
my_list.remove("four")              # Remove by value
popped = my_list.pop()              # Remove and return last item
print(f"Modified list: {my_list}")
print(f"List length: {len(my_list)}")
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")
print(f"Sliced list: {my_list[1:4]}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# --- Tuple ---
"""
Tuples are immutable, ordered sequences.
Syntax: (item1, item2, item3, ...)
"""
my_tuple = (1, 2, 3, "four", 5.0)
print(f"Tuple: {my_tuple}")
print(f"Tuple element: {my_tuple[0]}")
# my_tuple[0] = 10  # This would raise an error - tuples are immutable

# --- Dictionary (dict) ---
"""
Dictionaries are mutable, unordered collections of key-value pairs.
Syntax: {key1: value1, key2: value2, ...}
"""
my_dict = {
    "name": "Bob",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Java", "C++"]
}
print(f"Dictionary: {my_dict}")
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict.get('age')}")  # Safe access with .get()

# Dictionary operations
my_dict["email"] = "bob@example.com"  # Add new key-value
my_dict["age"] = 31                   # Update value
del my_dict["city"]                   # Delete key-value
print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items: {my_dict.items()}")

# --- Set ---
"""
Sets are mutable, unordered collections of unique elements.
Syntax: {item1, item2, item3, ...}
"""
my_set = {1, 2, 3, 4, 5}
another_set = {4, 5, 6, 7, 8}
print(f"Set: {my_set}")

# Set operations
my_set.add(6)                       # Add element
my_set.remove(1)                    # Remove element
print(f"Union: {my_set | another_set}")
print(f"Intersection: {my_set & another_set}")
print(f"Difference: {my_set - another_set}")

# --- Boolean ---
"""
Boolean values: True or False (note the capitalization)
"""
is_valid = True
is_complete = False
print(f"Boolean: {is_valid}, Type: {type(is_valid)}")

# --- None Type ---
"""
None represents the absence of a value
"""
empty_value = None
print(f"None value: {empty_value}, Type: {type(empty_value)}")


# =============================================================================
# 3. OPERATORS
# =============================================================================

"""
Python supports various types of operators:
1. Arithmetic operators
2. Comparison (Relational) operators
3. Logical operators
4. Assignment operators
5. Bitwise operators
6. Membership operators
7. Identity operators
"""

# --- Arithmetic Operators ---
a, b = 10, 3
print("\nArithmetic Operators:")
print(f"{a} + {b} = {a + b}")       # Addition
print(f"{a} - {b} = {a - b}")       # Subtraction
print(f"{a} * {b} = {a * b}")       # Multiplication
print(f"{a} / {b} = {a / b}")       # Division (float)
print(f"{a} // {b} = {a // b}")     # Floor division (integer)
print(f"{a} % {b} = {a % b}")       # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}")     # Exponentiation (power)

# --- Comparison Operators ---
print("\nComparison Operators:")
print(f"10 == 10: {10 == 10}")      # Equal to
print(f"10 != 5: {10 != 5}")        # Not equal to
print(f"10 > 5: {10 > 5}")          # Greater than
print(f"10 < 5: {10 < 5}")          # Less than
print(f"10 >= 10: {10 >= 10}")      # Greater than or equal to
print(f"10 <= 5: {10 <= 5}")        # Less than or equal to

# --- Logical Operators ---
print("\nLogical Operators:")
x, y = True, False
print(f"True and False: {x and y}")  # Logical AND
print(f"True or False: {x or y}")    # Logical OR
print(f"not True: {not x}")          # Logical NOT

# --- Assignment Operators ---
print("\nAssignment Operators:")
num = 10
print(f"Initial value: {num}")
num += 5    # num = num + 5
print(f"After += 5: {num}")
num -= 3    # num = num - 3
print(f"After -= 3: {num}")
num *= 2    # num = num * 2
print(f"After *= 2: {num}")
num /= 4    # num = num / 4
print(f"After /= 4: {num}")

# --- Bitwise Operators ---
print("\nBitwise Operators:")
p, q = 5, 3  # 5 = 0101, 3 = 0011 in binary
print(f"{p} & {q} = {p & q}")       # Bitwise AND
print(f"{p} | {q} = {p | q}")       # Bitwise OR
print(f"{p} ^ {q} = {p ^ q}")       # Bitwise XOR
print(f"~{p} = {~p}")               # Bitwise NOT
print(f"{p} << 1 = {p << 1}")       # Left shift
print(f"{p} >> 1 = {p >> 1}")       # Right shift

# --- Membership Operators ---
print("\nMembership Operators:")
fruits = ["apple", "banana", "cherry"]
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# --- Identity Operators ---
print("\nIdentity Operators:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list3: {list1 is list3}")      # Same object
print(f"list1 is list2: {list1 is list2}")      # Different objects
print(f"list1 == list2: {list1 == list2}")      # Same values
print(f"list1 is not list2: {list1 is not list2}")


# =============================================================================
# 4. CONDITIONAL STATEMENTS (if, elif, else)
# =============================================================================

"""
Conditional statements allow you to execute code based on conditions.
Syntax:
    if condition:
        # code block
    elif another_condition:
        # code block
    else:
        # code block
        
Note: Python uses indentation (typically 4 spaces) to define code blocks
"""

print("\n" + "="*50)
print("CONDITIONAL STATEMENTS")
print("="*50)

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("The temperature is comfortable")

# if-elif-else statement
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# Nested if statements
num = 15
if num > 0:
    if num % 2 == 0:
        print(f"{num} is positive and even")
    else:
        print(f"{num} is positive and odd")
else:
    print(f"{num} is negative or zero")

# Ternary operator (conditional expression)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Multiple conditions
username = "admin"
password = "12345"
if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Login failed")


# =============================================================================
# 5. LOOPS (for, while)
# =============================================================================

"""
Loops allow you to execute a block of code repeatedly.
Two main types:
1. for loop: iterate over a sequence
2. while loop: execute while a condition is true
"""

print("\n" + "="*50)
print("LOOPS")
print("="*50)

# --- For Loop ---
print("\nFor Loop Examples:")

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterate over a range
print("\nNumbers 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

# Range with start and stop
print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Range with start, stop, and step
print("\nEven numbers 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# Iterate over string
for char in "Python":
    print(char, end="-")
print()

# Enumerate (get index and value)
print("\nEnumerate example:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Iterate over dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}
print("\nIterating over dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# --- While Loop ---
print("\nWhile Loop Examples:")

# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with condition
number = 1
print("\nPowers of 2 less than 100:")
while number < 100:
    print(number, end=" ")
    number *= 2
print()

# --- Loop Control Statements ---
print("\nLoop Control Statements:")

# break: exit the loop
print("Break example (stop at 3):")
for i in range(10):
    if i == 3:
        break
    print(i, end=" ")
print()

# continue: skip to next iteration
print("Continue example (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# else with loops: executes when loop completes normally (without break)
print("\nLoop else clause:")
for i in range(3):
    print(i, end=" ")
else:
    print("Loop completed normally")

# Nested loops
print("\nNested loop (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end=" ")
    print()

# List comprehension (alternative to for loop)
print("\nList comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")


# =============================================================================
# 6. FUNCTIONS
# =============================================================================

"""
Functions are reusable blocks of code that perform a specific task.
Syntax:
    def function_name(parameters):
        '''docstring'''
        # function body
        return value
"""

print("\n" + "="*50)
print("FUNCTIONS")
print("="*50)

# --- Basic Function ---
def greet():
    """Simple function with no parameters"""
    print("Hello, World!")

greet()  # Call the function

# --- Function with Parameters ---
def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_person("Alice")

# --- Function with Multiple Parameters ---
def add_numbers(a, b):
    """Function that adds two numbers"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# --- Function with Default Parameters ---
def greet_with_title(name, title="Mr."):
    """Function with default parameter value"""
    print(f"Hello, {title} {name}")

greet_with_title("Smith")           # Uses default title
greet_with_title("Jones", "Dr.")    # Custom title

# --- Function with Keyword Arguments ---
def describe_person(name, age, city):
    """Function demonstrating keyword arguments"""
    print(f"{name} is {age} years old and lives in {city}")

describe_person(name="Bob", age=30, city="NYC")
describe_person(age=25, city="LA", name="Alice")  # Order doesn't matter

# --- Function with Variable Arguments (*args) ---
def sum_all(*numbers):
    """Function that accepts variable number of arguments"""
    total = sum(numbers)
    return total

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# --- Function with Keyword Variable Arguments (**kwargs) ---
def print_info(**info):
    """Function that accepts variable keyword arguments"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Charlie", age=28, profession="Engineer")

# --- Lambda Functions (Anonymous Functions) ---
"""
Lambda functions are small anonymous functions.
Syntax: lambda arguments: expression
"""
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

add = lambda x, y: x + y
print(f"3 + 7 = {add(3, 7)}")

# Lambda with map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# --- Recursive Functions ---
def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# --- Function Annotations ---
def multiply(a: int, b: int) -> int:
    """Function with type hints"""
    return a * b

print(f"3 * 4 = {multiply(3, 4)}")

# --- Docstrings ---
def complex_function(param1, param2):
    """
    This is a docstring explaining what the function does.
    
    Parameters:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
    """
    return param1 + param2

print(f"Function docstring: {complex_function.__doc__}")


# =============================================================================
# 7. OBJECT-ORIENTED PROGRAMMING (OOP)
# =============================================================================

"""
OOP is a programming paradigm based on the concept of "objects".
Key concepts:
1. Class: Blueprint for creating objects
2. Object: Instance of a class
3. Encapsulation: Bundling data and methods
4. Inheritance: Creating new classes from existing ones
5. Polymorphism: Same method name, different implementations
6. Abstraction: Hiding complex implementation details
"""

print("\n" + "="*50)
print("OBJECT-ORIENTED PROGRAMMING")
print("="*50)

# --- Basic Class ---
class Person:
    """A simple Person class"""
    
    def __init__(self, name, age):
        """Constructor method - called when object is created"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """Instance method"""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
    
    def have_birthday(self):
        """Method that modifies instance variable"""
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age}")

# Create objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.introduce()
person2.introduce()
person1.have_birthday()

# --- Class Variables and Instance Variables ---
class Dog:
    """Class demonstrating class and instance variables"""
    
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
    
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

buddy = Dog("Buddy", 3)
miles = Dog("Miles", 5)

print(f"Buddy's species: {buddy.species}")
print(f"Miles' species: {miles.species}")
print(buddy.description())
print(miles.speak("Woof!"))

# --- Inheritance ---
"""
Inheritance allows a class to inherit attributes and methods from another class.
"""

class Animal:
    """Parent/Base class"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # To be implemented by subclasses
    
    def info(self):
        print(f"This is {self.name}")

class Cat(Animal):
    """Child/Derived class"""
    
    def speak(self):
        return "Meow!"

class Bird(Animal):
    """Another child class"""
    
    def __init__(self, name, can_fly=True):
        super().__init__(name)  # Call parent constructor
        self.can_fly = can_fly
    
    def speak(self):
        return "Chirp!"

cat = Cat("Whiskers")
bird = Bird("Tweety")

cat.info()
print(f"{cat.name} says: {cat.speak()}")
bird.info()
print(f"{bird.name} says: {bird.speak()}")

# --- Encapsulation (Private and Protected Members) ---
"""
Encapsulation is hiding internal details and restricting access.
- Public: accessible from anywhere
- Protected (_variable): should not be accessed outside class (convention)
- Private (__variable): name mangled, harder to access
"""

class BankAccount:
    """Class demonstrating encapsulation"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner              # Public
        self._balance = balance         # Protected (convention)
        self.__account_number = "123"   # Private (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid amount")
    
    def get_balance(self):
        """Getter method for private data"""
        return self._balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")

# --- Polymorphism ---
"""
Polymorphism allows objects of different classes to be treated similarly.
"""

class Shape:
    """Base class for shapes"""
    
    def area(self):
        pass

class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 4), Circle(3), Rectangle(10, 2)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# --- Special/Magic Methods ---
"""
Special methods (dunder methods) allow you to define behavior for built-in operations.
"""

class Book:
    """Class demonstrating special methods"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation (for print())"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Official string representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of the book (number of pages)"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison"""
        return self.title == other.title and self.author == other.author

book1 = Book("Python Basics", "John Doe", 200)
book2 = Book("Python Basics", "John Doe", 200)

print(book1)                    # Uses __str__
print(repr(book1))              # Uses __repr__
print(f"Pages: {len(book1)}")   # Uses __len__
print(f"Books equal: {book1 == book2}")  # Uses __eq__

# --- Class Methods and Static Methods ---
class MyClass:
    """Class demonstrating class and static methods"""
    
    class_variable = 0
    
    def __init__(self, value):
        self.value = value
    
    def instance_method(self):
        """Regular instance method"""
        return f"Instance method called, value = {self.value}"
    
    @classmethod
    def class_method(cls):
        """Class method - has access to class, not instance"""
        return f"Class method called, class_variable = {cls.class_variable}"
    
    @staticmethod
    def static_method():
        """Static method - no access to class or instance"""
        return "Static method called"

obj = MyClass(10)
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())

# --- Property Decorators ---
class Temperature:
    """Class demonstrating property decorators"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")
temp.celsius = 30
print(f"Updated: {temp.celsius}°C = {temp.fahrenheit}°F")


# =============================================================================
# 8. FILE HANDLING
# =============================================================================

"""
File handling allows you to work with files on your system.
Operations: create, read, write, append, delete
File modes:
- 'r': Read (default)
- 'w': Write (overwrites existing file)
- 'a': Append
- 'x': Create (fails if exists)
- 'b': Binary mode
- 't': Text mode (default)
- '+': Read and write
"""

print("\n" + "="*50)
print("FILE HANDLING")
print("="*50)

# --- Writing to a File ---
print("\nWriting to file...")

# Method 1: Using with statement (recommended - automatically closes file)
with open("example.txt", "w") as file:
    file.write("Hello, this is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

print("File 'example.txt' created and written")

# Writing multiple lines
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("multiline.txt", "w") as file:
    file.writelines(lines)

print("File 'multiline.txt' created")

# --- Reading from a File ---
print("\nReading from file...")

# Read entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("Full content:")
    print(content)

# Read line by line
with open("example.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"\nLines list: {lines}")

# Read specific number of characters
with open("example.txt", "r") as file:
    first_10_chars = file.read(10)
    print(f"\nFirst 10 characters: {first_10_chars}")

# --- Appending to a File ---
print("\nAppending to file...")
with open("example.txt", "a") as file:
    file.write("This is an appended line\n")

print("Line appended to 'example.txt'")

# --- File Methods and Properties ---
# Check if file exists and get info
import os

if os.path.exists("example.txt"):
    print(f"\nFile exists: example.txt")
    print(f"File size: {os.path.getsize('example.txt')} bytes")
    print(f"Is file: {os.path.isfile('example.txt')}")
    print(f"Is directory: {os.path.isdir('example.txt')}")

# --- Working with File Paths ---
# Get current directory
current_dir = os.getcwd()
print(f"\nCurrent directory: {current_dir}")

# Join paths
file_path = os.path.join(current_dir, "example.txt")
print(f"Full file path: {file_path}")

# --- Binary File Operations ---
# Writing binary data
binary_data = b'\x00\x01\x02\x03\x04'
with open("binary_file.bin", "wb") as file:
    file.write(binary_data)

# Reading binary data
with open("binary_file.bin", "rb") as file:
    data = file.read()
    print(f"\nBinary data: {data}")

# --- Working with CSV Files ---
import csv

# Writing CSV
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"],
    ["Charlie", 35, "Chicago"]
]

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("\nCSV file 'data.csv' created")

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    print("\nReading CSV:")
    for row in reader:
        print(row)

# Using DictWriter and DictReader
with open("dict_data.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 25, "city": "NYC"})
    writer.writerow({"name": "Bob", "age": 30, "city": "LA"})

# --- Working with JSON Files ---
import json

# Writing JSON
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Java", "C++"],
    "address": {
        "city": "NYC",
        "zip": "10001"
    }
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nJSON file 'data.json' created")

# Reading JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("\nLoaded JSON data:")
    print(loaded_data)

# JSON to/from string
json_string = json.dumps(data, indent=2)
print("\nJSON string:")
print(json_string)

parsed_data = json.loads(json_string)
print(f"\nParsed data: {parsed_data}")

# --- File Exception Handling ---
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\nError: File not found!")
except PermissionError:
    print("\nError: Permission denied!")
except Exception as e:
    print(f"\nAn error occurred: {e}")

# --- Deleting Files ---
# Uncomment to actually delete files
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("File deleted")

# --- Directory Operations ---
# Create directory
if not os.path.exists("test_directory"):
    os.mkdir("test_directory")
    print("\nDirectory 'test_directory' created")

# List directory contents
print(f"\nCurrent directory contents: {os.listdir('.')}")

# Remove directory
# os.rmdir("test_directory")  # Only works if directory is empty

# --- Context Manager (with statement) ---
"""
The 'with' statement is used for resource management.
It ensures proper acquisition and release of resources.
Files are automatically closed even if an exception occurs.
"""

# Without with statement (not recommended)
file = open("temp.txt", "w")
try:
    file.write("Some content")
finally:
    file.close()

# With 'with' statement (recommended)
with open("temp.txt", "w") as file:
    file.write("Some content")
# File is automatically closed here


# =============================================================================
# 9. EXCEPTION HANDLING
# =============================================================================

"""
Exception handling allows you to handle errors gracefully.
Syntax:
    try:
        # code that might raise an exception
    except ExceptionType:
        # handle the exception
    else:
        # executes if no exception
    finally:
        # always executes
"""

print("\n" + "="*50)
print("EXCEPTION HANDLING")
print("="*50)

# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Multiple except blocks
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid value!")

# Catching multiple exceptions
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# else and finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result: {result}")
finally:
    print("This always executes")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# Custom exceptions
class CustomError(Exception):
    """Custom exception class"""
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught custom error: {e}")


# =============================================================================
# 10. MODULES AND PACKAGES
# =============================================================================

"""
Modules are Python files containing functions, classes, and variables.
Packages are directories containing modules.

Importing:
- import module_name
- from module_name import function_name
- from module_name import *
- import module_name as alias
"""

print("\n" + "="*50)
print("MODULES AND PACKAGES")
print("="*50)

# Standard library modules
import math
import random
import datetime

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number: {random.randint(1, 10)}")
print(f"Current date: {datetime.datetime.now()}")

# Importing specific functions
from math import factorial, pow
print(f"Factorial of 5: {factorial(5)}")
print(f"2^3: {pow(2, 3)}")

# Using aliases
import datetime as dt
now = dt.datetime.now()
print(f"Time: {now.strftime('%H:%M:%S')}")


# =============================================================================
# 11. LIST COMPREHENSIONS AND GENERATORS
# =============================================================================

print("\n" + "="*50)
print("LIST COMPREHENSIONS AND GENERATORS")
print("="*50)

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dict: {square_dict}")

# Set comprehension
unique_squares = {x**2 for x in [1, -1, 2, -2, 3]}
print(f"Unique squares: {unique_squares}")

# Generator expression (memory efficient)
gen = (x**2 for x in range(1, 6))
print(f"Generator: {gen}")
print(f"Generator values: {list(gen)}")

# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num, end=" ")
print()


# =============================================================================
# 12. DECORATORS
# =============================================================================

"""
Decorators are functions that modify the behavior of other functions.
They allow you to wrap another function to extend its behavior.
"""

print("\n" + "="*50)
print("DECORATORS")
print("="*50)

# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# =============================================================================
# CONCLUSION
# =============================================================================

print("\n" + "="*50)
print("This file covers all fundamental Python concepts!")
print("Topics covered:")
print("1. Print statements and output")
print("2. Data types (int, float, str, list, tuple, dict, set, bool)")
print("3. Operators (arithmetic, comparison, logical, etc.)")
print("4. Conditional statements (if, elif, else)")
print("5. Loops (for, while)")
print("6. Functions (regular, lambda, recursive)")
print("7. Object-Oriented Programming (classes, inheritance, polymorphism)")
print("8. File handling (read, write, CSV, JSON)")
print("9. Exception handling (try, except, finally)")
print("10. Modules and packages")
print("11. List comprehensions and generators")
print("12. Decorators")
print("="*50)

