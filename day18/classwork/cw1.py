num1 = str(input("enter number please "))
num2 = str(input("enter number please "))
num3 = str(input("enter number please "))

if num1 == num3:
    print(f"{num1} = {num3}")
elif num1 == num2:
    print(f"{num1} = {num2}")
elif num2 == num3:
    print(f"{num2} = {num3}")
else:
    print("wrong input")


number = int(input("enter number though 1 - 12"))


if number ==12:
    print("zamtari")
elif number == 1:
    print("zamtari")
elif number == 2:
    print("zamtari")



elif number == 3:
    print("gazafxuli")
elif number == 4:
    print("gazafxuli")
elif number == 5:
    print("gazafxuli")    



elif number == 6:

    print("zafxuli")

elif number == 7:
    print("zafxuli")
elif number == 8:
    print("zafxuli")
elif number == 9:
    print("daprintet")
elif number == 10:
    print("daprintet")
elif number == 11:
    print("daprintet")


else:
    print("wrong input")

if input("enter your name") == "admin":
    if input("enter admins password") == "adminis paroli":
        print("salami admin")
    else:
        print("wrong input")
else:
    print("hi user")