#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("What is your name? ")
age = int(input("How old are you? "))
age2 = age + 1
print(f"Hello, {name}! You are {age} years old. Next year, you will be {age2}!")
