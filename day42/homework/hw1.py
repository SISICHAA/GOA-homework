# 1) შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend() ფუნქციით.

frut = ["banana" , "apple" , "mandarini"]

fruttt = ["vafshi" , "greifruti"]

frut.extend(fruttt)

print(frut)

# 2) შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.

num = [1, 2, 3, 4, 5, 6, 7, 8]

num1 = [40, 50]

num.extend(num1)

print(num)


# 3) შექმენი სია names და შეაბრუნე reverse()-ით.

names = ["gio" , "saba" , "lasha" , "zura"]

names.reverse()

print(names)


# 4) შექმენი სია სახელად nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.

nums = (1, 2, 3, 4, 5, 6, 5, 7)

print(nums.count(5))


# 5) შექმენი letters = ["a","b","a","c"] და დაბეჭდე რამდენი ცალი "a" არის ჩვენს სიაში.

letters = ["a","b","a","c"]

print(letters.count("a"))


# 6) შექმენი სია სახელად names და იპოვე "saba"-ს ინდექსი index()-ით.

names = ["saba" , "nugo" , "sandro" , "saba" , "gio", "saba"]

print(names.index("saba"))


# 7) შექმენი list = ["red","green","blue"] და იპოვე რომელ ინდექსზე დგას "blue". გამოიყენე შესაბამისი ფუნქცია.

list = ["red","green","blue"]

print(list.index("blue"))


# 8) შექმენი სია სახელად nums და დამატე მასში extend()-ით [7, 8, 9].

nums = [1, 2, 3, 4, 5, 6]

nums1 = [7, 8, 9]



nums.extend(nums1)
print(nums)


# 9) შექმენი სია სახელად foods და დააბრუნე შებრუნებული სია.

foods = ["shqmeruli" , "mwvadi" , "acharuli,xawapuri"]

foods.reverse()

print(foods)


# 10) შექმენი სია cities და იპოვე რომელ ინდექსზე დგას "tbilisi".

cities = [ "telavi" ,"kutaisi" , "tbilisi"]

print(cities.index("tbilisi"))


# 11) შექმენი animals = ["cat","dog","cat","cow"] და დაითვალე ამ სიაში რამდენი "cat" არის.

animals = ["cat","dog","cat","cow"]

print(animals.count("cat"))


# 12)შექმენი სია fruits = ["apple", "banana"] და append ფუნქციით დაამატე "grape". დაბეჭდე სია.

fruits = ["apple", "banana"]
fruis1 = "grape"
fruits.append(fruis1)

print(fruits)


# 13)შექმენი სია numbers = [1, 2, 3] და extend()-ით დაუმატე [4, 5]. დაბეჭდე სია.

numbers = [1, 2, 3]
numbers1 = [4, 5]

numbers.extend(numbers1)

print(numbers)

# 14)შექმენი სია names = ["goga", "saba"] და insert()-ით ჩასვი "luka" პირველ ინდექსზე. დაბეჭდე სია.

names = ["goga", "saba"]

names.insert( 1 , "luka")

print(names)


# 15)შექმენი სია items = ["pen", "pencil", "eraser"] და pop()-ით წაშალე ბოლო ელემენტი; დაბეჭდე განახლებული სია.

items = ["pen", "pencil", "eraser"]

items.pop()
print(items)

# 16)შექმენი სია colors = ["red", "green", "blue"] და remove()-ით წაშალე "green". დაბეჭდე შედეგი.

colors = ["red", "green", "blue"]

colors.remove("green")

print(colors)

# 17)შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.

foods = ["bread", "milk"]

if len(foods) == 2:
    foods.append("cheese")
else:
    foods.append("meat")
print(foods)


# 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.

nums = [10, 20, 30]

input = int(input("dawere a mteli ricxvi: "))

if input in nums:
    print("Already in list")
else:
    nums.append(40)

print(nums)


# 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). დაბეჭდე სია.

leters = ["a", "b", "c"]

input1 = int(input("dawere a ricxvi: "))

leters.insert(input1 , 3)
print(letters)


# 20)შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი. თუ ინდექსი სიის ფარგლებშია, pop()-ით ამოშალე შესაბამისი ელემენტი; თუ არა, დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.

values = [1, 2, 3, 4]

inputi2 = int(input("shemoiyvane a indexi: "))

lengg = len(values)

if inputi2 <= lengg-1:
    values.pop(inputi2)
else:
    print("Index out of range")

print(values)


# 21)შექმენი სია pets = ["cat", "dog", "hamster"].  მომხმარებელს შემოატანინე შინაური ცხოველის სახელი. თუ იგი არის სიის შიგნით, remove()-ით ამოშალე და დაბეჭდე "Removed", თუ არა — დაბეჭდე "Not found" და სია უცვლელი დატოვე; საბოლოოდ დაბეჭდე სია.

pets = ["cat", "dog", "hamster"]

input2 = input("dawere a cxovelis saxeli: ")

if input2 in pets:
    pets.remove(input2)
    print("Removed")
else:
    print("Not found")

print(pets)


# 22)შექმენი სია a = [5, 5, 7]. მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი არის სიის ელემენტი, დაბეჭდე რამდენჯერ არის სიაში - count() ფუნქციის გამოყენებით. სხვა შემთხვევაში append()-ით ჩასვი ის სიაში და დაბეჭდე სია.

a = [5, 5, 7]

input = int(input("shemoiyvane ricxvi: "))

if input in a:
    print(a.count(input))
else:
    a.append(input)
    print(a)


# 23)შექმენი სია queue = ["first", "second"].  მომხმარებელს შემოატანინე ახალი ელემენტი და insert()-ით ჩასვი სიის დასაწყისში. შემდეგ if-ით შეამოწმე სიის სიგრძე — თუ უფრო დიდია 5-ზე, pop()-ით ამოშალე ბოლო ელემენტი; ბოლოს დაბეჭდე სია, თუ არ არის 5-ზე მეტი დაბეჭდე შებრუნებული სია.

queue = ["first", "second"]

element = input("chhawere a elementi: ")   

element.insert(2 , element)

if len(queue) > 5:
    queue.pop()
    print(queue)
else:
    print(queue)


# 24)შექმენი სია nums = [2, 4, 6].  მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი დადებულია, append()-ით დაამატე; თუ 0-ია ან ნაკლებია ნულზე, დაბეჭდე "Only positive allowed". ბოლოს დაბეჭდე სია.

nums = [2, 4, 6]

input3 = int(input("airchie ricxvi: "))

if input3 > 0:
    nums.append(input3)
    print(nums)
elif input3 <= 0:                   
    print("Only positive allowed")

print(nums)


# 25) შექმენი სია mix = ["x", "y", "z"]. extend()-ით დაუმატე [1, 2, 3]. შემდეგ მომხმარებელს შემოატანინე ასო; თუ ეს ასო არის სიაში, remove()-ით წაშალე პირველად როცა შეგხვდება და დაბეჭდე "Removed", თუ არა — დაბეჭდე "No such element". ბოლოს დაბეჭდე სია.

mix = ["x", "y", "z"]

mixx = [1, 2, 3]

mix.extend(mixx)


input = input("SHEMOIYVANE aso: ")


if input in mix:
    mix.remove(input)
    print("Removed")
else:
    print("No such element")

print(mix)