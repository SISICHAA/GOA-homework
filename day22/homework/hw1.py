#indexi aris listshi shetanili moonacemis misamarti 


#2)შექმენით ცვლადი სადაც შეინახავთ ამ სიას [4,6,1,5,9,8,4] ,თქვენი დავალებაა რომ მიწვდეთ ამ სიაში ელემენტებს ინდექსინგის გამოყენებით ,შეკრიბეთ ორი რიცხვი რომ მიიღთ შემდეგი რიცხვები --> 10 , 2 , 14 , 20 , 4 , 7 , 27 , გამოიყენეთ მათემატიკური ოპერატოები

list = [4, 6, 1, 5, 9, 8, 4]

# ინდექსების გამოყენებით ვწერთ მოქმედებებს, რომ მივიღოთ მოთხოვნილი რიცხვები
a = list[0] + list[1]    # 4 + 6 = 10
b = list[2] + list[0]    # 1 + 4 = 5
c = list[3] + list[4]    # 5 + 9 = 14
d = list[1] * list[3]    # 6 * 5 = 30
e = list[2] * list[6]    # 1 * 4 = 4
f = list[0] + list[2]    # 4 + 1 = 5
g = list[4] + list[5] + list[6]  # 9 + 8 + 4 = 21

print(a, b, c, d, e, f, g)


#3)შექმენით სია სადაც შეიყვანთ ადამიანის სახელებს,უნდა გქონდეთ სულ 10 სახელი,თქვენი დავალებაა რომ გამოიტანოტ ,მე 5 , მე 9 ,მე 3 ,მე 7 და პირველ ინდექსზე მდგომი ელემენტები ცალ ცალკე,გამოიყენეთ ინდექსინგი

names = ["gia", "lasha", "makvala", "jumbera", "saba", "koclizuria", "mate", "sandro", "nita", "lamzira"]

print(names[5]) 
print(names[9])  
print(names[3])  
print(names[7])  
print(names[1])  

#4)შექმენით სია სადაც მოათავსებთ სტრინგ ტიპის მონაცემებს,თქვენი დავალებაა გომ for loop და while loop (ორივე) ს დახმარებით გამოიტანოთ თთოეული ელემენტი ცალ ცალკე







#5)შექმენით სია სადაც შეინახავთ 7 ცალ ელემენტს(მონაცემის ტიპს არ აქვს მნიშვნელობა),თქვენი დავალებაა რომ ამ სიაში შეცვალოთ მე 3 ინდექსზე დმგომი ელემენტი და ჩაანაცვლო "vashli" ით, ასევე შეცვალე მე 6 ინდექსზე მდგომი ელემენტი და ჩაანაცვლე 'msxali' ით ,ასევე შეცვალე მე 4 ინდექსზე მდგომი ელემენტი და ჩაანაცვლე ის 'atami" ით,გამოიტანე საბოლოო სია ტერმინალში,სადაც ეს სალი ელემენტი იქნება განახლებული~

my_list = [423, 234234, 5544, 34534, 699, 23424, 42333]
my_list[3] = "vashli"
my_list[6] = "msxali"
my_list[4] = "atami"
print(my_list)



#6)იპოვეთ საბოლოო პასუხი--> True and False or False and True or false and false or true ---> True


#7)შექმენით სია სადაც მოთავსებული გექნებათ ცხოველების სახელები, თქვენი დავალებაა რომ -->  თუ ამ სიაში მოთავსებული მე 3 ინდექსზე მდგომი ელემენტი არის ლომი მაშნ დაპრინტე --> "there is lion on index 3" სხვა შემთხვევაში დაუპრინტე რომ --> "there is no lion on index 3"

animal = ["dzagli", "sspilo", "lomi", "tigrovi", "knuti", "kata", "lassha"]

if animal[3] == "lomi":
    print("there is lion on index 3")
else:
    print("there is no lion on index 3")



#8)
basket = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]


print(basket[0])

print(basket[2])
basket[1] = "კივი"
print(basket[0])
print(basket[1])
print(basket[2])
print(basket[3])
print(basket[4])


#9)

letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

print(letters[2])
print(letters[4])
print(letters[5])
print(letters[6])
print(letters[9])

print(letters[6] + letters[4] + letters[5] + letters[6])

print(letters[2] + letters[4] + letters[0] + letters[3])


print(letters[2] + letters[4] + letters[6] + letters[2])



#10)
letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]


meotxe_ricxvi = letters[4]
if meotxe_ricxvi == "ლ":
    print("სწორია! ასო ლ ა")
else:
    print("არასწორია, სცადე თავიდან")


bolo_ricxvi = letters[9]
if bolo_ricxvi == "ე":
    print("საიდუმლო სიტყვა იწყება სწორად.")
else:
    print("საიდუმლო სიტყვა არასწორია.")


word = letters[6] + letters[4] + letters[5] + letters[6]

if word == "გელა":
    print("გაარტყი სახელი!")

else:
    print("შტერი ხარ! დ.")





my_list = ["nihao", "zdarova", "gamarjoba", "heloo", "muchoreq"]

index = int(input("Please enter an index (0-4): "))

print(my_list[index])