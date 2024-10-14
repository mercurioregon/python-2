
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

#Booleans and comparison operators

print (11==11)
print( ("beef" == "BEEF") or (4 == 4) and True)
print(8 ==8.00)
print(7 > 8)
print( 9 >= 9)
print( 9 != 5)


cond = ( not 9==7)
print(cond)


my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
print(my_list [0]["Bill"])

In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
# """

# my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]

# my_list[2] [0] [3]= "x"
# my_list[-2] = "television"

# $ # def friday( ):
# #     print("The last day of the work week")
# #
# # friday()

# def  badge(nickname =  "bro"):
#     print("Hello there " + nickname + ", what's up?")

# badge("Dude")

# # def  remainder (num1, num2):
# #     return num1 % num2
# #
# # remainder_value = remainder(55,4)
# # print(remainder_value)


# def new_sum(*args):
#     return sum(args)
# solution = new_sum(1,2,3,4,5,3,6,3,)
# print(solution)

# #KWARGS

# # def key_values(**kwargs):
# #         print(kwargs)
# #         print(kwargs.keys())
# #         print(kwargs.values())
# #         print(kwargs.get("party"))
# #
# # key_values(state = "Oregon", party= "Democrat")

# #MORE SCOPE EXAMPLES

# def  new_age():
#         age = 52
#         #the above is an example of data outside the scope. running this will only resolve the func below

#         def add_4_to_age(age):

#                 age = age +4
#                 #Ths defines the function.  The below line runs it. The print is converted into a string for the answer.
#                 print("ADDING METHOD: " + str(age))
#                 #Below is  data passed thru from second line in outer func
#         add_4_to_age(age)
#     #below it is run
# new_age()


def merge_lists(list1, list2):
    return list1+ list2

new_list = merge_lists(["monday", "tuesday"], ["thursday", "friday"])

print(new_list)
# list function list() -  turns whatever passes thru into a list(invidiual chars)
#  .split -  splits the elements into a new string, not the characters

# def separate (str):
#         return list(str)
#
# print (separate("this was a difficult one "))

# -------

# def multi_merge (list1, string1):
#         return list1 + string1.split() + list(string1)
#
# print (multi_merge(["Mon", "Tues", "Wed"], "The days of the week;"))

# def last_list (*args):
#         return args[-1 ]
#
# print (last_list([1,2,3,4,5], ["a", "b","c"], ["hi", "hello"]))

#CANNOT CONCATENATE STRINGS AND NUMBERS.  USE STR


# IF ELSE ELIF
# animal = "orangutan"
# if animal == "cow":
#     print("eats grass")
# elif animal == "bird":
#     print("eats worms")
# elif animal == "monkey" or animal == "orangutan":
#     print("throws poo")
# else:
#     print("unsure what animal does")

#LOOPS

# space_movies = ["star_wars", "star_trek", "serenity", "2001", "ice_pirates"]
# counter = 0
#
# for movie in  space_movies:
#     counter = counter + 1
#     sentence = str(counter) +  ") " + movie + "  is my fave sci-fi movie."
#     print(sentence)

space_movies = "This is just a string of characters in sentence form."
counter = 0

for char in space_movies:
    if char == "c":
       # break
       # continue
    counter = counter + 1
    letters = str(counter) + " " + char
    print(letters)



pass #does nothing but prevent error in code.  Used as a placeholder.


x = 2
while x < 10:
        print(x)
        x = x + 1.7 # x += 1 (SAME THING)
else:
        print("big ol' number")

#loop thru DICTIONARIES
#DEFAULT print just prints keys. /// .items prints the pair /// .values prints the value only

# employees = {"jon" : 65000, "sandy" : 67000, "marvin": 80000, "tom" : 82000}
#
# for key, value in employees.items():
#     print(key)
#     print(value)

#LOOP THRU TUPLES

employees = [("jon" , 65000), ("sandy" , 67000), ("marvin" , 80000), ("tom" ,  82000)]

for (key,value) in employees:
    print(key)

#LIST

# word  = "oregon"
# newWord  = list(word)
# print (newWord)

# for num in range(12):
#     print(num)

# for num in range(2, 10, 2):
#     print(num)

#ZIP

# mynum = [1,2,3,4,5,6]
# words = ["there", "are", "other", "words", "derp"]
#
# for items in zip(mynum, words):
#     print(items)

#EMUMERATE

words = ["there", "are", "other", "words", "derp"]
for item in enumerate(words):
    print(item)

list_a = ["mon", "tues", "wed", "thurs", "fri"]
list_b = [7,8,9,10,11,12,13]
# list_c = [1814, 1911, 1941, 1972, 2002, 2024]
#
# newlist = list(zip(list_a, list_b, list_c))
# print(newlist)
#
# #UNPACKING THE ZIPPED LIST
# for a,b,c in newlist:
#     print(a)
#     print(b)
#     print(c)

#LIST CHECKS MIN AND MAX

# print("sat" in list_a)

# answer = max(list_b)
# print(answer)

#RANDINT PROVIDES RAND NUMBER BUT :

#IMPORT FROM LIBRARY!!!


#from random import randint
# randomnum = randint(0,1000)
# print(randomnum)


# print(mylist)
#
# shuffle(mylist)
#
# mylist = [1,2,3,4,5,6,7,8,9,10]
#
# from random import shuffle
#

from random import shuffle
mylist = list (range(101))
shuffle(mylist)
print(mylist)


#INPUT


last_name = input("Please enter your last name.")
print(last_name +" is a very cool name.")

#.STRIP REMOVES ANY UNWANTED WHITESPACE

#INT() TO CONVERT STRING BACK TO NUMBER


# BAD CODE -- FROM EXERCISES
#
# def twelver (a,b):
# (a == 12 or b == 12 or a+b == 12):
#
#
# twelver(12,6)
#
# print(twelver())

# def sequence(num_list):
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1]  == 2 and num_list [i +2] == 3:
#             return True
#     return False
# print(sequence((1,5,2,4,7,2,1,5,1,2,3,4)))
# 
# def grow_string(str):
#     result = ""
#     for i in range(len(str)):
#         result = result + str[:i+1]
#     return result
# 
# print (grow_string("Seahawks"))

#  .POP etc, = method
#  max()   = function


#BELOW
# SELF IS AN INSTANCE OF VEHICLE
class Vehicle:

    color = "red"
    engine = "v6"
    vehicle_counter = 0
    #this is a class attribute that is applied to the vehicles below

    def __init__(self, body_type, make):
        self.vehicle_body = body_type
        self. vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        return Vehicle.vehicle_counter

car1 = Vehicle("coupe", "Toyota")

car2= Vehicle("truck", "ford")

print(car2.vehicle_counter)

#importing. FROM FOLDER.FILE import CLASS

from machines.machine_stuff import Vehicle

car1 = Vehicle()

from Machine_Folder.machine_stuff import Vehicle
#
# #after importing, create a subclass. CLASS NEW CLASS(ORIGINAL CLASS)
#
class Truck(Vehicle)

#creating new Trucks means they have to have the same characteristics as the original
#Vehicle class


truck1 = Truck("pickup", "ford")
truck2 = Truck("semi", "mack")
truck3 = Truck("cube", "mistubishi")
print(truck3.get_vehicle_count)


#CLASSES AND SUBCLASSES

class Animal:
    def __init__(self, name):
        self.animal_name = name
    def eat(self):
        raise NotImplementedError("Child class should be implementing this")

class Monkey(Animal):
    def eat(self):
        print("Monkey eats bananas")

class Bird(Animal):
    def eat(self):
        print("Eats worms")

    def fly(self):
        print("Way up there")


myMonkey = Monkey("mr scoops")
myMonkey.eat()

mybird = Bird("sparky")
mybird.eat()
mybird.fly()
