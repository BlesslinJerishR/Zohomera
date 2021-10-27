def leader(times):
    gang = []
    print(f"Enter the {times} team members names : ")
    # Gang
    id = 1
    for i in range(times):
        thug = int(input(f"Enter the power of Thug id {id} : "))
        id += 1
        gang.append(thug)   
        
    power = 1
    leaders = []
    for pow in gang:
        if pow > gang[power:power+1]:
            power += 1
            leaders.append(pow)
            print("I am the leader")
            print(pow)
        
        elif pow < sum(gang[power:]):
            power += 1
    leaders.append(gang[-1])
    print("We are the leaders " ,set(leaders))
# Diver Class
leader(5)