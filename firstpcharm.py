list = []

Greeting = input("Hello! Please enter your name: ")
print("Hello " + Greeting + " I hope you have a good day!")
num1 = input('Please enter the first number you would like to add: ')
# list.append(num1)
num2 = input('Please enter another number you would like to add: ')
# list.append(num2)

total = float(num1) + float(num2)
# total = sum(list)
split = total/4

print("The total is " + str(total))
print("Each person is responsible for" + str(split))