word_1 = str(input("Enter the 1st word : "))
word_2 = str(input("Enter the 2nd word : "))

l1 = list(word_1)
l2 = list(word_2)

origin = []

for x in l1:
    if x not in l2:
        origin.append(x)

for x in l2:
    if x not in l1:
        origin.append(x)
        
if len(origin) == 0:
    print("-1")
else:
    print(origin)