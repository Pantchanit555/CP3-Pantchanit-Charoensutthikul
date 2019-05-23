username1 = input("Username : ")
password1 = input("Password : ")
if username1 == "store1" and password1 == "2436" :
    print("--------------------WELCOME--------------------")
    print("1. Orange Juice          - 35 THB")
    print("2. Lemonade              - 30 THB")
    print("3. Apple Juice            - 35 THB")
    print("4. Tomato Juice         - 25 THB")
    print("5. RoselleJuice          - 20 THB")
    print("6. Grape Juice            - 40 THB")
    select1 = int(input(">> "))
    if  select1 == 1:
             q = int(input("Quantity : "))
             sumselect = q*35
             print("Total : ",sumselect)
             print("--------------------THANK YOU--------------------")
    elif select1 == 2:
            q = int(input("Quantity : "))
            sumselect = q *30
            print("Total : ", sumselect)
            print("--------------------THANK YOU--------------------")
    elif select1 == 3:
            q = int(input("Quantity : "))
            sumselect = q*35
            print("Total : ", sumselect)
            print("--------------------THANK YOU--------------------")
    elif select1 == 4:
            q = int(input("Quantity : "))
            sumselect = q*25
            print("Total : ", sumselect)
            print("--------------------THANK YOU--------------------")
    elif select1 == 5:
            q = int(input("Quantity : "))
            sumselect = q*20
            print("Total : ", sumselect)
            print("--------------------THANK YOU--------------------")
    elif select1 == 6:
            q = int(input("Quantity : "))
            sumselect = q*40
            print("Total : ", sumselect)
            print("--------------------THANK YOU--------------------")
else :
    print("!!!!!!!!!!!!!!!!!!!!!!WRONG!!!!!!!!!!!!!!!!!!!!!!!")
    print("--------------------TRY AGAIN--------------------")


