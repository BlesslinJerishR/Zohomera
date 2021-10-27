n = int(input("Enter the number of N : "))
i = 1
s = n * n
sp = " "
num = list(x for x in range(1,n))
for x in range(n):
    m = int(s/2)
    print((sp * m) , i , (sp * m))
    i += 1