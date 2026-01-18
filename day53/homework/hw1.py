# 2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.


names = ["saba", "nika", "LuKA", "Misho", "giorgi"]

name = []

for i in names:
    if i == i.lower() and i[0] == "g":
        name.append("Goga")
    elif i == i.upper() or i[0] == "N":
        name.append("Nika")
    else:
        name.append("ლიდერი")

print(name)












# 3)  შექმენით რიცხვებით სავსე სია, თუ რიცხვი არის ლუწი ან დგას ლუწ ინდექსზე, ჩაამატეთ მისი კვადრატი ახალ სიაში - გამოიყენეთ შესაბამისი მათემატიკური ოპერატორი, ხოლო თუ რიცხვი არის კენტი ან დგას კენტ ინდექსზე, ახალ სიაში ჩაამატეთ 2-ჯერ დიდი რიცხვი. გამოიყენეთ while ციკლი

numbers = [1, 2, 3, 4, 5, 6]

result = []

i = 0


while i < len(numbers):

    if numbers[i] % 2 == 0 or i % 2 == 0:

        result.append(numbers[i] ** 2)


    else:

        result.append(numbers[i] * 2)
    i += 1

print(result)







# 4) შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ პატარა და ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, მაგალითად თუ მოცემული იქნება სიტყვა "Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.

words = ["PYTHON", "Nika", "computer", "HELLO", "code", "PROGRAM"]

result = []

i = 0

while i < len(words):
    word = words[i]

    if len(word) > 6 or word == word.upper():

        result.append(word.lower())

    else:

        result.append(word + word)

    i += 1

print(result)




# 5) მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას ამ სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. დაწერეთ ორივე ხერხით, for ციკლით და while ციკლით.

numbers = "0123456789"
result = []

index = 0

for i in numbers:


    integer = int(i)

    if index % 2 == 0 or integer > 7:

        result.append(integer)
    index += 1

print(result)



numbers = "0123456789"

while_ = []

i = 0
while i < len(numbers):
    digit = int(numbers[i])
    if i % 2 == 0 or digit > 7:
        while_.append(digit)
    i += 1

print(while_)
