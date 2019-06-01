number = int(input("number : "))
for i in range(number) :
    text = ""
    space = ""
    for j in range((number-i),0,-1) :
        space += "  "
    for j in range(2*i+1) :
        text += "*"
    print(space,text)