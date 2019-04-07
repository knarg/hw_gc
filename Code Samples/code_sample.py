def setupInitMoney():
    money = input("Insert the initial balance above 0: ")
    #TODO: Add a loop to make sure the data is corrct
    #TODO: Add user input validation
    #TODO: convert to float before return
    #TODO: ...

    return money


...

def main():
    print("Describe your app")
    initMoney = setupInitMoney()
    percent = setupPercent()
    years = setupYears()
    result = calculateTheResultMoney(initMoney, percent, years)
    ...


main()