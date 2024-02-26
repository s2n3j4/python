# set1 = {1, 2, 3, 4}
# set2 = {2, 4, 6, 5}
# print(set1 | set2)   #union dont repeat dublicate
# print(set1 & set2)    #intersection only matched values
# print(set1 - set2)    #diff between 1 & 2 (Only shows 1 diff)
# print(set1 ^ set2)    # unmatched values

# set3 = {9, 8, 7, 6}
# set3.add(10)

# set3.remove(9)
# print(set3)

# age_dict = {
#     "name Sanjeev", "Class = 13,", "Age = 19"}
# print(age_dict)

# age = (int(input("Enter your age")))
# if age >= 18:
#      print("You can Participate")
# else:
#      print("You cannot Participate")


# a = 4
# b = 6.5
# c = 4j
# print(a, b, c)
# print(a + b)
# print(a + b + c)
# print(type(c))

# x = " Hello World"
# y = x.strip() 
# print(y)
# z = x.upper()
# print(z)

# age = 20
# name = "Sanjeev"

# print("My name is {} and my age is {}".format(name, age))

# price = 19.99
# print("The price is ${:.2f}".format(price))


# fruits = {"Banana", "Apple", "Grapes"}
# morefruits = {"orange", "mango"}
# # if "Apple" in fruits:
# #     print("Apple is a fruit")
# # fruits.insert(1, "lemon")
# # print(fruits)
# # print(len(fruits))
# fruits.update(morefruits)
# print(fruits)

# # Creating a dictionary
# student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 75}

# # Retrieving values using get()
# print("Alice's grade:", student_grades.get('Alice'))  # Output: 85
# print("David's grade:", student_grades.get('David'))   # Output: None

# # Providing a default value
# print("David's grade (if not found):", student_grades.get('David', 'Not available'))  # Output: Not available


ecs = {"Tirtha": 20000, "dil": 24000, "Nabin": 1500,}
print("Tirtha's salary", ecs.get("Tirtha") )
print("Dil's salary", ecs.get("dil"))
print("not found in record", ecs.get("not found"))


dict = {
    "Name": "Sanjeev",
    "Age": 18
}
print(dict)
dict['Age'] = 19
print(dict)
dict['address'] = "Baluwatar"
print(dict)