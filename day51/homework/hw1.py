#1) შექმენით რიცხვებით სავსე სია და ახალ სიაში ჩააგდეთ ყველა რიცხვი გამრავლებული 2-ზე. დაპრინტეთ ახალი სია.
numbers = [1, 3, 5, 7, 9]

new_numbers = []

for i in numbers:
    new_numbers.append(i * 2)


print(new_numbers)


#2) შექმენით სახელებით სავსე სია, მომხმარებელს შემოატანინეთ რაიმე რიცხვი, და ამ რიცხვის ინდექსზე ჩაამატეთ სახელი "ნიკა" თქვენს სიაში.


names = ["საბა", "გიორგი", "ნინო", "ანა"]


index = int(input("შეიყვანე რიცხვი: "))


names.insert(index, "ნიკა")

print(names)

#3) შექმენით string წინადადების ცვლადი, ამ წინადადებიდან დაპრინტეთ მხოლოდ ხმოვანი ასოები.


sentence = "Python is very easy"


vowels = "aeiouAEIOU"


for i in sentence:
    if i in vowels:
        print(i)



#4) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 4-ზე მეტი სიგრძეში ან დგანან კენტ ინდექსზე. გამოიყენეთ remove() ფუნქცია.

words = ["cat", "house", "sun", "tree", "sky", "flower"]

w_remove = []

for i in range(len(words)):
    if len(words[i]) > 4 or i % 2 == 1:
        w_remove.append(words[i])

for word in w_remove:
    words.remove(word)

print(words)


#5) შექმენით რიცხვებით სავსე სია, გამოითვალეთ რიცხვების საშუალო არითმეტიკული - რიცხვების ჯამი გაყოფილი რიცხვების რაოდენობაზე.
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num


count = len(numbers)


average = total / count

print("საშუალო არითმეტიკული:", average)
