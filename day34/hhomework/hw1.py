# 1) შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
#    for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.



cities = ["Tbilissi", "Batumi", "Kuttaisi", "Rustavi", "Telavi", "Gori", "Marneuli"]

for i in range(len(cities)): 

    if len(cities[i]) > 6:    

        print(cities[i])      



# 2) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.


words = ["ggufta", "chaxoxbili", "lassshatalaxadzeeee", "voleyball", "lashavarrrrrrrrrrr"]



for i in range(len(words)):


    if len(words[i]) % 15 == 0:


        print(words(i))




# 3) შექმენით სია რიცხვებით.  
# -> გამოიყენეთ for loop რათა დათვალოთ რამდენი რიცხვია სიაში.  
# -> არ გამოიყენოთ len() — დაითვალეთ ხელით.


num = [123, 132312, 4235235, 534, 44, 645656, 1345234]

start = 0

for i in num:
    start += 1
print(start)







# 4) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.

liss = ["lasha", "meraba", "salamaleikum", "kebab"]


for i in range(len(liss)):
    if len(liss[i]) == 5:
        print(liss[i])


# 5) მომხმარებელს შემოატანინე წინადადება.  
# -> გაიგე რამდენი სიმბოლოა წინადადებაში.  
# -> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.

sentence = input("enter sentence: ")
a_A = 0
lenght = 0
for i in sentence:
    lenght += 1
    if i == "a" or i == "A":
        a_A += 1
print(lenght, a_A)
        










# 6) <= Boss Level =>
# შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
# --> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი

string = ["GIO", "zviko", "eduarda", "lashiko"]

grdzeli = ""


for i in range(len(string)):
    if len(string[i]) > len(grdzeli):

        grdzeli = string[i]

print(grdzeli)
