print("Hello user!")

userNumber = int(input("Enter your number: "))
i = 1
factorial = 1

while i <= userNumber:
    factorial *= i
    i += 1
    pass

print("Your factorial is: ", factorial)