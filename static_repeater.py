from zython import pali

word = str(input("Enter the word to analyse repeater : ")) 
garage_0 = [x for x in word ]
garage_1 = set()
unix, l_uniq = [], []
l_uniq = [x for x in garage_0 if x not in unix or garage_1.add(x) ]
print("I am first repeater in my family : ",l_uniq[0])

def repeater(word):
    garage_0 = [x for x in word]
    garage_1 = set()
    unix = []
    l_uniq = [x for x in garage_0 if x not in unix or garage_1.add(x) ]
    print("I am first repeater in my family : ",l_uniq[0])