print("Hello user!")

userNumber = int(input("Enter your number: "))
factorial = 1
userRange = range(userNumber)


for i in userRange:
    factorial *= i

print("Your factorial is ", factorial)