def classify_number(number):
    if number < 0:
        return "The number is negative"
    elif number == 0:
        return "The number is zero"
    else:
        return "The number is positive"


try:
    user_input = float(input("Enter a number: "))
    result = classify_number(user_input)
    print(f"The number {user_input} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
