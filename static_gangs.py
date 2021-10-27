# Gang
gang = []
times = int(input("Enter the team size : "))
id = 1
for i in range(times):
    thug = int(input(f"Enter the power of Thug id {id} : "))
    id += 1
    gang.append(thug)   
print(f"We are the leaders {max(gang)} , {str(gang[-1])}")