def calculate_g_mean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if (a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
a = 9
b = 8
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculate_g_mean(a, b)
isgreater(a, b)
c = 9
d = 10
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculate_g_mean(c, d)
isgreater(c, d)

def my_function(f_name):
    print(f_name , "Magar")

my_function("Bijay"),
my_function("Sanjeev"),

def my_name(fname, lname):
    print(fname + " " + lname)
my_name("Sanjeev", "Magar")


def my_class(classno, name):
    print(classno + " "+ name)
my_class("Class-6", "sanjeev")


def home_address(address):
    print(address)
home_address("baluwatar")


def my_function(*kids):
    print("The youngest child is " + kids[0])
my_function("Bijay", "Roshan", "Ayush")


def my_kids(child3, child2, child1):
    print("The youngest child is "+ child3)
my_kids(child1 = "Sanjeev", child2 = "Roshan", child3 = "Bijay")


def first_last_name(**kid):
    print("His first name is " + kid["fname"] + "His last name is " + kid["lname"])
first_last_name(fname = "sanjeev", lname = "Magar")


def my_country(country="Norway"):
    print("I am from " + country)
my_country("Sweden")
my_country("Nepal")
my_country("America")
my_country()

def return_function(x):
    return 5 * x
print(return_function(5))
print(return_function(6))