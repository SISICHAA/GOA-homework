# #1) მომხმარებელს შემოატანინე სიტყვა ანდა ტექსტი.  
# -> გაიგე ამ სიტყვის/ტექსტის სიგრძე და დაპრინტე 
# -> for ციკლით დაბეჭდე ამ სიტყვის თითოეული ასო ცალცალკე.


text = input("enter text:  ")

print(len(text))

for i in range(len(text)):
    print(text[i])




words = ["applee", "bannana", "kiwi", "orange", "grape"]

for i in words:
    text = len(i)
    print(text)

    if text % 2 == 0:
        print("luwia")
    else:
        print("kentia")
