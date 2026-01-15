# 1)შექმენით სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიის ბოლოში დაამატე სიტყვა --> "ianvari" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

sia = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

sia.append("ianvari")
print(sia)



# 2)შექმენი სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიაში მეორე ინდექსზე დაამატე სიტყვა ---> "bati" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა


list = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

list.insert( 2 , "bati" )

print(list)

# 3)შექმენი სია ---->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე მე 5 ინდექსზე მდგომი ელემენტი და დაპრინტე საბოლოო სია ნახე ამოიშალა თუ არა


liss = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

liss.pop(5)
print(liss)

# 4)შექმენი სია --->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე True და ასევე ამოშალე "kote" და დაპრინტე საბოლოო სია და ნახე ამოიშალა თუ არა


lisss = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

lisss.remove("kote")
lisss.remove(True)

print(lisss)