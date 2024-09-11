
print ("Hello World")


first_name = "Jim"
last_name = " Mercurio"
weight = 200
sentence = first_name + last_name + " weighs" + str(weight) + " lbs."
print (sentence)

data_type = type("nine")
print(data_type)
# ----
sentence = "Verisilimitude"

print(sentence[0:14:2])

print(sentence[5:])

sentence = "the sum of {0} + {1} is {2}".format(9, 7, 16)

print(sentence)

# ------
#new_list = [4,55,21,0,88,74,121,3,5,8]
new_list = ["butter", "cake", "dogs", "zippers", "sauce"]
#new_list.append("Caboose")
#new_list[3] = "Poop"
new_list.sort()
new_list.reverse()

print(new_list)

ist_2 =["alpha", "beta", "gamma", "zeta"]

new_list.sort()
new_list.reverse()
list_2.reverse()
final_list = new_list[:3] + list_2[:3]

print(final_list)

big_list = ["a", "b", "c", 2,4,5,["Monday", "Tuesday", "Wednesday"], 5, 7]

small_list = big_list[6][2
]
print(small_list)

# new_list = [4,55,21,0,88,74,121,3,5,8,0,0,0,0,0,0]
#
# # num_pos = new_list.index(121)
# num_pos = new_list.count(0)
# print(num_pos)


#TUPLES (Immutable strings, however nested strings can be changed)
# new_tuple = (1,2,3,4, "Oregon", "Washington", ["g", "d", "h"], 5, 55, 555)
# # new_tuple[6][1] = "x"
#
# print(new_tuple[7:10])

#DICTIONARIES
#Not position oriented. {Key : data/value}
# Call the key
#Unsortable
#.pop remove by key
#.clear

dict = {"a" : "New York" ,"b": 1000}
dict ["b"] = "Oregon"
dict ["c"] = "Washington"
print(dict)

