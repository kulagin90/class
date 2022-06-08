import random
def gg(a,b):
    return random.randint(a,b)
a=1
b=10
c=5
list1=[]
for i in range(c):
    list1.append(gg(a,b))
print(list1)
