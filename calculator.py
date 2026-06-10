def add(*args):
    return sum(args)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(base, exponent):
    return base**exponent

while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            user_input = [float(x) for x in input("Enter numbers with spaces: ").split()]

        except ValueError:
            print("Enter number only")
            break
        
        print("Result:", sum(user_input))
        break

    elif choice == "2":
        input_numbers = input("Enter numbers separated by spaces: ")
        numbers = input_numbers.split()
        if len(numbers) >= 2:
            result = float(numbers[0])
            for num in numbers[1:]:
                result -= float(num)
            print("Result:", result)
        else:
            print("Please enter at least two numbers for subtraction.")
            
    
    elif choice == "3":
        num1= float(input("Enter your 1st number: "))
        num2= float(input("Enter your 2nd number: "))
        print("Result:", multiply(num1, num2))
          

    elif choice == "4":
        num1= float(input("Enter your first number: "))
        num2= float(input("Enter your second number: "))
        print("Result:", divide(num1, num2))


    elif choice == "5":
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))

        print("Result:", power(base, exponent))
    
    
    elif choice == "6":
        break