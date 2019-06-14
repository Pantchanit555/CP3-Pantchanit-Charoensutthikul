def  login() :
    username1 = input ("Username : ")
    password1 = input ("Password : ")
    if username1 == "minad" and password1 == "3412":
        return showMenu()
    else :
        return False
def  showMenu() :
    print("-----  I_ToobShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def  menuSelect() :
    userSelected = int(input(">>"))
    if  userSelected == 1 :
        print("Vat =",vatCalculate(int(input("Price >>"))))
    elif  userSelected == 2 :
        print("Total Price =",priceCalculate())
def  vatCalculate(totalPrice) :
    vat = 7
    result = totalPrice + (totalPrice * vat /100)
    return result
def  priceCalculate() :
    price1 = int(input("First Product Price : "))
    price2 = int (input ("Second Product Price : "))
    return vatCalculate(price1+price2)
login()