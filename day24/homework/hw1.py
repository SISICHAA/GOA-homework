

numbers = [1, 230, 23, 22, 1121, 69, 111]


print(numbers[-3])
print(numbers[-4])




fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]

print(fruits[2])
print(fruits[3])

print(fruits[-3])
print(fruits[-4])



numbers = [3,4,5,6,7,1,2,9,8,11]

input = int(input("Enter an index (0-9): "))

if 0 < input < 10:
    print(numbers[input])
else:
    print("you entered negative or more than 10  number ")




list = ["dog" ," most" ,"is" ,"angry" ,"running", "the" , "forest", "fast", "in" , "cat" ,"human", "very"]


print(list[-12])


print(list[-10])

print(list[-8])
print(list[-4])

print(list[-7])
print(list[-6])

print(list[-1])
print(list[-5])


print(list[5])

print(list[9])
print(list[2])

print(list[11])

print(list[3])



animal = ["dog", "cat", "horse", "cow", "sheep", "goat"]

number = int(input("Enter an index (0-5): "))

if animal[number] == "cat":
    print("შენ აირჩიე კატა.")
elif animal[number] == "goat":
    print("შენ აირჩიე თხა.")
else:
    print("სხვა ცხოველი აირჩიე.")


city = ["Tbilisi", "Batumi", "Zugdidi", "Kutaisi", "Rustavi", "Zestafoni"]

ind = int(input("Enter the first index (0-5): "))
ind2 = int(input("Enter the second index (0-5): "))

if ind < ind2:
    print(city[ind])
    print(city[ind2])
elif ind > ind2:
    print("შეცვალე ინდექსები ადგილებით")
    print(city[ind2])
    print(city[ind])
else:
    print("ორივე ერთია")
    print(city[ind])



index = int(input("enter a symbol: "))

word1 = ("a")

word2 = ("z")


if index == word1:
    print("სიტყვა იწყება a-თი")

elif index == word2:
    print("სიტყვა მთავრდება z-თი ")

else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")




first_word = input("enter a word: ")

second_word = input("enter a second word: ")

if first_word == second_word:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")

GOA = "agivorsbgitr"

print(GOA[1])
print(GOA[4])
print(GOA[1])
print(GOA[0])


print(GOA[6])
print(GOA[0])
print(GOA[7])
print(GOA[0])


print(GOA[7])
print(GOA[0])
print(GOA[10])
print(GOA[2])
print(GOA[3])
print(GOA[0])
print(GOA[5])


