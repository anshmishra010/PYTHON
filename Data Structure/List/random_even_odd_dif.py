#in this we have to generate random num and have to diff even n odd num from random list
import random
x=[]
for i in range(10):
    val = random.randint(1,20)
    x.append(val)
print("Original list ",x)
e=[]
o=[]
for i in range(len(x)):
    if(x[i]%2==0):
        e.append(x[i])
    else:o.append(x[i])
print("Even list ",e)
print("Odd list ",o)
