num1 = int(input("enter number please"))
num2 = int(input("enter number please"))

if num1 > num2:
    print(f"{num1} > {num2}")
elif num1 < num2:
    print(f"{num1} < {num2}")
else:
    print(f"{num1} = {num2}")

name = str(input("enter your name please :"))
admins_name = "saba"


if name == admins_name:
    print("chven sexniebi vart")
else:
    print("chven sxvadasxva saxelebi gvaqvs")


age = 4
age1 = 6
if age < 0 and age1 < 0:
    print("es orive ricxvi uaryofitia")
elif age > 0 and age1 > 0:
    print("es orive ricxvi dadebitia")
else:
    print("es ra jandabaa")


for i in range(50 , 100 , 2):
    print(i)



i = 20
while i < 40:
    print(i)
    i = i + 1