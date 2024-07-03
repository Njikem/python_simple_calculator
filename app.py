
#This function add two numbers

def add(numbone, numbtwo):
    numberOne = numbone + numbtwo
    print(numberOne)
    return


# This function subtract two numbers

def subtract(numbone, numbtwo):
    numberOne = numbone - numbtwo
    print(numberOne)
    return



# This function multiply two numbers

def multiply(numbone, numbtwo):
    numberOne = numbone * numbtwo
    print(numberOne)
    return



# This function divide two numbers

def divide(numbone, numbtwo):
    numberOne = numbone / numbtwo
    print(numberOne)
    return


print("Select operation")
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')


# User Choice

choice = input("Enter choice(1,2,3,4):")

if choice in('1', '2', '3', '4'):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Invalid input. Please enter a number.")

if choice == '1':
    print(f"The result is: {add(num1, num2)}")

elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")

elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")

elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")  