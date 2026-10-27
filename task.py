fruits=["Apple","Orange","Apple","Banana","Mango"]
print(fruits[1])
print(fruits[3])
print(fruits[2:5])

fruits=["Apple","Orange","Apple","Banana","Mango"]
print(fruits[-4])

fruits.append("Cherry")
print(fruits)

fruits.extend(["Banana","Kiwi"])
print(fruits)

fruits.insert(3,"Strawberry")
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits.pop(3)
print(fruits)

del fruits[4]
print(fruits)

print(fruits)
print(fruits.index("Kiwi"))

print(fruits)
print(fruits.count("Apple"))

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

copy_list=fruits.copy()
print(copy_list)

print(len(fruits))
