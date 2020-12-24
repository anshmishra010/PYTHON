#program that generate set of prime num & another set of odd num , show union,intersection,diff,symetric
odd = set()
for i in range(2,20):
    if i%2!=0:
        odd.add(i)
print(odd)
# prime = set()
prime = {x for x in range(2, 20) if not any(x % y == 0 for y in range(2, x))}
print(prime)
print("union = ", odd.union(prime))
print("intersection ",odd.intersection(prime))
print("symmetric ",odd.symmetric_difference(prime))
print("Diff ",odd.difference(prime))



