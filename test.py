gang = []
times = int(input("Enter the number of times : "))
print(f"Enter the {times} team members names : ")
# Gang
id = 1
for i in range(times):
    thug = int(input(f"Enter the power of Thug id {id} : "))
    id += 1
    gang.append(thug)   
leaders = []
gangx = gang[1:]
for i in gang:
    for j in gangx:
        if i > j:
            leaders.append(i)
        else:
            continue
        
print(list(set(leaders)))