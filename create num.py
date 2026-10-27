numbers=[10,5,100,30]
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers+[40,50])
numbers.append(70)
print(numbers)
numbers.extend([67,90,57,65])
print(numbers)

numbers.insert(5,11)
print(numbers)

print(numbers.index(5))
print(numbers.count(100))

