# Question 7
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
result = 0
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
print(f"Result: {result}")

# Question 8
char = input("Enter a character: ")
unicode_value = ord(char)
if 65 <= unicode_value <= 90:
    print(f"The character '{char}' is an Uppercase letter.")
elif 97 <= unicode_value <= 122:
    print(f"The character '{char}' is a Lowercase letter.")
elif 48 <= unicode_value <= 57:
    print(f"The character '{char}' is a Digit.")
else:
    print(f"The character '{char}' is a Special character.")


# Question 9
def calculate_y(a, b, c, x, k):
    if x > k:
        y = a * x**2 - b * x + c
    elif x == k:
        y = 0
    else:
        y = a * x**2 + b * x + c

    return y
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
x = float(input("Enter the value of x: "))
k = float(input("Enter the value of k: "))
result = calculate_y(a, b, c, x, k)
print(f"The value of y is: {result}")

# Question 10
import random
def guess_the_number():
    target_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    attempts = 0
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
            break
        elif user_guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
guess_the_number()

#Question 11
def apply_for_visa():
    rt_pcr_report = input("Do you have a negative RT-PCR report? (yes/no): ").lower()
    fully_vaccinated = input("Are you fully vaccinated? (yes/no): ").lower()
    duration_of_tour = int(input("Enter the duration of your tour in days: "))

    if (rt_pcr_report == 'yes' or fully_vaccinated == 'yes') and 1 <= duration_of_tour <= 15:
        print("Congratulations! You are eligible for a tourist visa.")
    else:
        print("Sorry, you do not meet the eligibility criteria for a tourist visa.")

apply_for_visa()


