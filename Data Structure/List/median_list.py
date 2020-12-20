#have to find median of list and also print sorted list
a=[]
n=int(input())
for i in range(n):
    ele = int(input())
    a.append(ele)
print("Original ",a)
s=sorted(a)
print("sorted list ",a)
i=len(a)-1
if n%2!=0:
    print("MEdian ",a[i//2])
else:print("Median ",a[i//2]+a[i+1//2]/2)