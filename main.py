# practicing dictionary and tuples

my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)

print(type(t))


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)


print()

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(9)
print(duplicates)
duplicates = tup.count(2)
print(duplicates) 

pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }
item_1 = pol_eng_dictionary["woda"]

print(item_1)
print(pol_eng_dictionary)

pol_eng_dictionary["woda"] = "kiki"
item2 = pol_eng_dictionary["woda"]
print(item2)
print(pol_eng_dictionary)

pol_eng_dictionary.update({"Sandy": "Wexler"})

print(pol_eng_dictionary, end="")

print("Join meee")
print()
print(pol_eng_dictionary.get("Sandy"))
print()
print()
for key, val in pol_eng_dictionary.items():
  print(key,val)
print()
print()


n= input("Enter: ")
while True:
  if n in pol_eng_dictionary:
    item3= pol_eng_dictionary[n]
    print(item3 in pol_eng_dictionary)
  else:
    print("Give  a valid")
    break
second_dict= pol_eng_dictionary.copy()


if "Sandy" in second_dict:
    print("Yes")
else:
    print("No")

  
print()
print()
# Tuples
tuple_ = 1, 2, 3

for n in tuple_:
    print(n, end="")
print()
for n in tuple_:
    print(n)
print(3 in tuple_)
print(4 not in tuple_)

# del tuple_
# print(tuple_)

tuple_ = 1, 2, 3
