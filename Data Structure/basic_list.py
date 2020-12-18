#list is versatile data type ,key feature of the list is that it can have element of different data type.
a=[5,2,8,5,9,1]
b=[4,'T','w',"tuv",[3,4,5]]
c=[43,56,12,3,89,23]
d=["python"]

#access the value
print("First element from list a ", a[0])
print("element from the sublist")
print(b[4],[2])

#updating the list value
a[1] = 99
print("List after updation ", a)
a.append(100)
print("List after append ",a)
del a[1]
print("after deleting one element ",a)
del a[2:4]
print("after deleting multiple element ")
print("Deleting whole list ")
del a[:]
print(a) # it w# ill print empty list.

#Various operations
print("length ",len(c))
print(56 in c)
print(56 not in c)
print("maximum element ",max(c))
print("minimum ",min(c))
print("Sum ",c)
print("List ",list(d))
print("Sorted list ",sorted(c))

