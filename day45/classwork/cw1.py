names = ["saba", "giorgi", "luka", "tekla", "andria"]

for i in names[:]:   
    if len(i) > 5:
        names.remove(i)

print(names)
