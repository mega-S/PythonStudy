def main():
    sayHello()
    exchange()
    
    pass

def sayHello():
    name = input("What is your name? ")
    print("Hello ", name)

def exchange():
    usdCode = 21
    euroCode = 22
    usd = 28
    euro = 32

    value = int(input("Enter your value(Usd(21) Euro(22): "))
    cash = int(input("Enter your cash: "))
    if value == usdCode:
        sum = (cash / usd)
        print("Your money: ", sum, " usd")
    elif value == euroCode:
        sum = (cash / euro)
        print("Your money: ", sum, " euro")
    else:
        print("Undefined value!!!")

main()