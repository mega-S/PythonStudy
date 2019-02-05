print("hello world")

usd = 28
euro = 32


money = int(input("Usd(11) or euro(12)?"))
value = int(input("How much?"))

if (money == 11):
    sum = round(value / usd, 2)
    nom = "usd"
elif (money == 12):
    sum = round(value / euro, 2)
    nom = "euro"
else:
    sum = 0
    print("Unknown error!")

print("Your money: ", sum, nom )