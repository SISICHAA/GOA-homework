num1 = int(input("enter random number: "))


if num1 > 0:
    print("ეს რიცხვი დადებითია")
elif num1 < 0:
    print("ეს რიცხვი უარყოფითია")
elif num1 == 0:
    print("ეს რიცხვი ნულის ტოლია")
else:
    print("false input")



age = int(input("enter your age please: "))


if 0 <= age <= 12:
    print("you are child")
elif 13 <= age <= 19:
    print("you are teenager")
elif 20 <= age <= 64:
    print("you are adult")
elif 65 <= age <= 120:
    print("you are beberi")
elif age > 120:
    print("you are guru or witch")
else:
    print("false input")
    
password = "saba123"
tries = 0
while True:
        password_guesser = str(input("enter password in sabas password guesser"))
        tries += 1
        if password_guesser == password:
            print(f"you guesed it right in, {tries} tries.")
            break
        else:
            print("nahhh much stronger password")

num = int(input("enter number: "))
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))

print("highest number is,", max(num, num1, num2))


week = int(input("enter number between 1-7"))
choice = week

if choice == 1:
    print("today is orshabati")
elif choice == 2:
    print("today is samshabati")
elif choice == 3:
    print("today is otxshabati")
elif choice == 4:
    print("today is xuthsbati")
elif choice == 5:
    print("today is paraskevi")
elif choice == 6:
    print("today is shabati")
elif choice == 7:
    print("today is kvira")
else:
    print("i dont know that day")