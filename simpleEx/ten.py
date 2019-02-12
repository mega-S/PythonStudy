userName = str(input("Enter your name: "))
print("Hello ", userName)

userChoise = str(input("Would you like to write something about yourself? (y - definitely yes, n - no thanks): "))
if userChoise.lower() == "y":
    with open("files/about.txt", "w") as file:
        userText = input()
        file.write(userText)
elif userChoise.lower() == "y":
    print("Thank you ^-^")
else:
    print("Something gone wrong!")

print("Here what you did sad: ")
with open("files/about.txt", "r") as readFile:
    print(readFile.read())