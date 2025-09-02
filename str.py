# String slicing
course = "Python for beginners. Welcome to Python journey"
print(course[22:39])

# Slicing with only end index
course = "Python for beginners. Welcome to Python journey"
print(course[:21])

# Slicing with only start index
course = "Python for beginners. Welcome to Python journey"
print(course[22:])

# Negative index slicing
course = "Python for beginners. Welcome to Python journey"
print(course[-15:])

# String Concatenation
title_1 = "Welcome to"
title_2 = "Python Journey"
title = title_1+title_2
print(title)

# String Concatenat ion with White-space
title_1 = "Welcome to"
title_2 = "Python Journey"
title = title_1+" "+title_2
print(title)

# String Methods

# upper()
title = "Welcome to Python Journey"
print(title.upper())

# capitalize()
title = "Welcome to Python Journey"
print(title.capitalize())

# title()
title = "Welcome to Python Journey"
print(title.title())

# lower()
title = "Welcome to Python Journey"
print(title.lower())

# count()
title = "Welcome to Python Journey"
print(title.count("o"))

# encode()
title = "Welcome to Python Journey"
print(title.encode())

# split()
title = "Welcome to Python Journey"
print(title.split(" "))

# find()
title = "Welcome to Python Journey"
print(title.find("P"))

# index()
title = "Welcome to Python Journey"
print(title.index("P"))

# strip()
title = "Welcome to Python Journey   "
title1 = title.strip()
print(len(title1))

# startswith()
title = "Welcome to Python Journey"
print(title.startswith("Welcome"))

# endswith()
title = "Welcome to Python Journey"
print(title.endswith("Journey"))

# isalnum()
title = "Welcome to Python Journey"
print(title.isalnum())

# isalpha()
title = "WelcometoPythonJourney"
print(title.isalpha())

# isascii()
title = "WelcometoPythonJourney"
print(title.isascii())

# isdecimal()
title = "WelcometoPythonJourney"
print(title.isdecimal())

# isdigit()
title = "WelcometoPythonJourney"
print(title.isdigit())

# islower()
title = "WelcometoPythonJourney"
print(title.islower())

# isnumeric()
title = "WelcometoPythonJourney"
print(title.isnumeric())

# isspace()
title = "WelcometoPythonJourney"
print(title.isspace())

# istitle()
title = "Welcome to Python Journey"
print(title.istitle())

# isupper()
title = "Welcome to Python Journey"
print(title.isupper())

print("Hello" + "World")

print("Python"[0])
