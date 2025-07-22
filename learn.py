print("I love coding")
#It's true I love coding and desire to discover more, of Html, CSS and python.
#Hashtag for notes or comments in Python.
# print("") is a print statement that prints a string into the console.
#If is a conditional statement that checks if a condition is true or false.
#Else is a conditional statement that executes if the if condition is false.
#Need to put if var then any condition then a colon: Then add what will be executed if the condition is true.
#Types of variables in Python: int, float, str, and bool. It contains a value that can be changed.
#Typecasting is the process of changing a variable data type to another.
#input
happiness = 57.2
happy = "I'm pretty happy today! And I will like to make other people;s day happy too! "
print(f"I'm {happiness} percent happy today! Which is pretty low mainly because I have not been able to learn how to code yet and had a lot of problems today.")

if happiness >=50:
	print(happy)

#It's actually true that I'm happy today and that I desire to learn how to code.

else:
	print("I'm not really happy today, but I will still learn how to code.")

print("Question: What is the data type for the variable happiness and happy?")
print(type(happiness))
print(type(happy))
print("In summary, happiness is an integer and happy is a string.")
happiness = int(happiness)
print(type(happiness))
print(happiness)

Bday = input("When is your birthday?: ")
print(f"Your birthday is on {Bday} I wish you a happy Birthday! On that day.")
