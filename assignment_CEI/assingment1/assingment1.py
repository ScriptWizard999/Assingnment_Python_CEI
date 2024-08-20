#Q1
print("Hello World!")

#Q2
Name = 'Souvik Sen'
age = 21
hobby = 'Watching Movies'
print(f"My name is {Name}.\nMy age is {age}.\nMy favorite hobby is {hobby}")

# Q3
# in the above code i create 3 variables and print those variables by using f-string.

# Q4
x = int(input("Write a number "))
if x>0:
    print("The number is Positive number")
elif x<0:
    print("The number is Negative.")
else:
    print("The number is Zero")

# Q5
Year = int(input("Write a Year "))
if Year%4==0:
    print("The Year is a leap year")
elif Year%400==0:
    print("The Year is a Leap year.")
else:
    print("The Year is not a leap year")

# Q6
for number in range(0,10):
    print(number)

# Q7
number = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# Q8
for nmbr in range(0,10):
    if nmbr%3==0:
        continue
    print(nmbr)
        
# Q9
for i in range(0,10):
    if i>5:
        break
    print(i)

# Q10
def greetings(greet):
    greet = input("Enter your Name ")
    print(f"Hello {greet}")

greetings(greet=input)

# Q11
def Sum_of_two_nmbr(x,y):
    x = int(input("Enter a number "))
    y = int(input("Enter another Number "))
    print(f"The sum of{x} and {y} is {x+y}")

Sum_of_two_nmbr(x=input,y=input)