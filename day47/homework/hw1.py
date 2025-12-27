
# 1) შექმენით სახელებით სავსე სია და ასევე ცარიელი სია: Upper_name = [].  სახელების სიიდან ცარიელ სიაში ჩაამატეთ ყველა ის სახელი რომელიც იწყება დიდი ასოთი, გამოიყენეთ for ციკლი და შესაფერისი სიის და სტრინგის ფუნქციები


names = ["SABA" , "lasha" , "luka" , "natro" , "NANA"]

Upper_name = []

for name in names:

    if name[0] == name[0].upper():
        Upper_name.append(name)

print(Upper_name)


# 2) შექმენით 2 სია - სახელების და გვარების. for ციკლის და ფუნქციების გამოყენებით სახელების სიაში ყველა სახელის ყველა ასო გახადეთ დიდი, ხოლო გვარების სიაში ყველა გვარის თითოეული ასო გახადეთ პატარა, სულ ბოლოს კი გააერთიანეთ სახელების სია გვარის სიასთან და დაპრინტეთ მიღებული შედეგი.

names = ["SABA", "Nika", "MATE"]

surname = ["arabuli" , "berulava" , "chikhradze"]

for i in range(len(names)):
    names[i] = names[i].upper()


for i in range(len(surname)):
    surname[i] = surname[i].lower()


full_list = names + surname


print(full_list)

print(surname)


# 3) შექმენით სტრინგებით სავსე სია და ამ სიიდან ამოშალეთ ყველა ის სიტყვა რომელიც არის ან 6-ზე ნაკლები სიგრძეში, ან რომელიც მთავრდება დიდი ასოთი.

words = ["fdggdf" , "fdgs" , "hhffggg" , "asdsada"]

for i in words:


    if len(i) < 6 or i[-1] == i[-1].upper():

        words.remove(i)

print(words)


# 4) შექმენით float მონაცემთა ტიპის ელემენტებით სავსე სია რომელშიც იქნება 10 float ელემენტი და ამ სიიდან ახალ ცარიელ სიაში ჩაამატეთ ის რიცხვები რომლებიც არიან 10-ზე მეტი და 100-ზე ნაკლები.

num = [3.27, 14.58, 0.93, 27.41, 8.06, 19.84, 6.72, 11.39, 2.15, 24.67]

new_list = []

for i in num:

    if 10 < i < 100:

        new_list.append(i)

print(new_list)


# 5) შექმენით 2 სია, პირველი სია იყოს სავსე 5 ცალი ქალაქის სახელებით, და მეორე სიაში მოთავსებული იყოს 10 ქვეყნის სახელი. თქვენი დავალებაა რომ ქვეყნის სახელებში ჩაამატოთ ყველა ქალაქის სახელები ცალ-ცალკე მენულე ინდექსიდან მეოთხე ინდექსის ჩათვლით. გამოიყენეთ for ციკლი და შესაბამისი ფუნქციები.

cites = ["Tbilisi", "Paris", "Berlin", "Rome", "Tokyo"]


countries = ["Georgia", "France", "Germany", "Italy", "Spain",
 "USA", "Canada", "Japan", "Brazil", "Australia"]



for i in range(len(countries)):

    countries[i] = countries[i] + cites[i][1:5]

print(countries)





