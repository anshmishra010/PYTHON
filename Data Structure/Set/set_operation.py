#SET built-in operations
#note= do not this whole code in one go as result may varry due to previous results

s = set([1,2,3,4,5,10,11])
t = set([1,2,3,4,5,6,7,8,9])

print(len(s))
print(s)
print(t)


print(6 in s) #check wether element is in the set or not

print(s.issubset(t)) #return true if every element in set s is present in set t or not

print(s.issuperset(t)) #return true if every element in t is present in set s

print(s.union(t)) #return a set s that has elements from both set s and t and eliminate same element

print(s.intersection(t)) #return a new set which are common in both

s.intersection_update(t)
print(s)

i=s.difference(t)
print(i) #returns a new set that has elements in set s but not in t

s.difference_update(t)
print(s) #removes all the elements of another from this set

z=s.symmetric_difference(t) #returns a new set with elements either in s or in t but not both
print(z)

print(s.isdisjoint(t)) #returns true if two set have a null intersection