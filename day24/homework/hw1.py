

numbers = [1, 230, 23, 22, 1121, 69, 111]


print(numbers[-1] * numbers[-7])
print(numbers[-3] * numbers[-5])





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

 
print(list[-12], list[-10],  list[-8],  list[-4], list[-7], list[-6], list[-1], list[-5])
print(list[5], list[9], list[2],list[11], list[3])




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



index = input("enter a word: ")

word1 = ("a")

word2 = ("z")


if index[0] == word1:
    print("სიტყვა იწყება a-თი")

elif index[-1] == word2:
    print("სიტყვა მთავრდება z-თი ")

else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")




first_word = input("enter a word: ")


if first_word[-1] == first_word[0]:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")

GOA = "agivorsbgitr"

print(GOA[1] +  GOA[4] + GOA[1] + GOA[0])


print(GOA[6] +  GOA[0] +  GOA[7] + GOA[0])


print(GOA[7] + GOA[0] + GOA[10] + GOA[2] + GOA[3] + GOA[0] + GOA[5])




string = "giorgi"


for i in string:
    print(i)


i = 0

while i < 6:
    print(string[i])
    i += 1