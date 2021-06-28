a = "yufanphombolimbu"

print("Indexing in python3")
print(a[1:7])
print(a[1:])
print(a[:5])

print("negative Indexing in python3")

print(a[:-1])
print(a[-1:])
print(a[:-5])

print("Data structure in a python3")
# list - a collection of a data which is mutable
# tuple - a collection of a data which is immutable
# set - collection of unique data
# dictionary - collection of key-pair value

a = {"address":"kathmandu","age":19,"phone_number":9812345678}
for i in a.items():
    for j in i:
         print(j)


list = [str(1),str(2),str(3),str(4),"yufan","limbu"]
print(list[0])
# adding items in a list.
list.append("yufan limbu")
print(list)
print("print a u character from a list in a python3")
print(list[4][1])

print("print a m character that you have recent add items in a list")
print(list[6][8])

# sorting a list in a python

list.sort()
print(list)

print("An example of set in a python3")

s = set()
list = ["yufan","yufan","limbu","phombo","john"]
for i in list:
    s.add(i)
print(s)

print("How much elements does set ")
print(len(s))