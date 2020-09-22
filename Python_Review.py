
'''
Lab 1 
Joe Harkins
COMP 469
8/28/2020
'''
import math
import datetime
########## Part 1 ###########

'''
   1) Create a variable, x, and set its value to 16
      Create a variable, y, and set its value to square root of x
      Divide x by three fifths of y, and store the result in x (hint: /=)

'''
# YOUR CODE GOES HERE
print("########## Part 1 ###########")
print("1)")
x = 16
print(f"x={x}")
y = math.sqrt(x)
print(f"y={y}")
x /= 3/5 * y
print(f"x={x}")
'''
    2)  A cube has the edge defined below.

    Store its space diagonal, surface area and volume in new variables.
    Print out the results and check your answers.
    Change the value of the edge and ensure the results are still correct.
'''
# YOUR CODE GOES HERE


class Cube:
    def __init__(self, edge):
        self.edge = edge
        self.space_diagonal = math.sqrt(3) * edge
        self.surface_area = 6 * edge ** 2
        self.volume = edge ** 3

    def toString(self):
        print(f"Edge={self.edge}")
        print(f"Space diagonal={self.space_diagonal}")
        print(f"Surface area={self.surface_area}")
        print(f"Volume={self.volume}")


print("2)")
cube = Cube(10)
cube.toString()
cube = Cube(20)
cube.toString()
print("\n")


######### Part 2 ###########

'''
    1)  For each of the following Python expressions, write down the output value. If it would give an error then write error.

                (a)False == 0
                    True
                (b) True != 1
                    False
                (c) 40 // 2
                    20
                (d) 41 // 2
                    20
                (e) 41 % 2
                    1
                (f) True + 1.33
                    2.33
                (g) False - `True'
                    SyntaxError: invalid syntax
                (h) False + \True"
                    SyntaxError: invalid syntax
                (i) 15/7+5*8**4
                    20482.14285714286
                (j) ('Hello' == 'Hi') or ( 12 > -6 )
                    # True
'''
# YOUR CODE GOES HERE
print("######### Part 2 ###########")
print("1)")
x = False == 0
print("x = False == 0")
print(x)
x = True != 1
print("x = True != 1")
print(x)
x = 40 // 2
print("x = 40 // 2")
print(x)
x = 41 // 2
print("x = 41 // 2")
print(x)
x = 41 % 2
print("x = 41 % 2")
print(x)
x = True + 1.33
print("x = True + 1.33")
print(x)
# x = False - `True'
# x = False + \True"
x = 15/7+5*8**4
print("x = 15/7+5*8**4")
print(x)
x = ('Hello' == 'Hi') or (12 > -6)
print("x = ('Hello' == 'Hi') or ( 12 > -6 )")
print(x)
print("\n")


######### Part 3 ###########


'''
    1) write a python code to calculate the age based on the user's birthdate (the year of birth, e.g.: age = 1989), if age is greater than 18 then outputs “adults' category” otherwise outputs “Children Category”.

'''

year = 1989
# YOUR CODE GOES HERE


def getAge(birth_year):
    curr_time = datetime.datetime.now()
    curr_year = curr_time.year
    return curr_year - birth_year


def category(birth_year):
    age = getAge(birth_year)
    category = ""
    if age >= 18:
        category = "Adult's category."
    else:
        category = "Children's category."
    print(f"Your age is {age} and you are in the {category}")


print("######### Part 3 ###########")
print("1)")
birth_year = input(
    "Please enter your birth year to calculate your age, and to find your category!\n")
birth_year = int(birth_year)
category(birth_year)


'''
	2) Repeat q1:
    If the year is not within 1910-2020 then prints an error message for the user
    Otherwise: calculates his/her age, if age is greater than 18 then outputs “adults' category” otherwise outputs “Children Category”.

'''

year1 = 1989
year2 = 1857

year = year1
# YOUR CODE GOES HERE
print("2)")
birth_year = input(
    "Please enter your birth year to calculate your age, and to find your category!\n")
birth_year = int(birth_year)
if birth_year not in range(1910, 2020):
    print("Error: Your age is invalid")
else:
    category(birth_year)
print("\n")

######### Part 4 ###########


'''
    1) Write a python code to print all the perfect square numbers less than 300.
'''
# YOUR CODE GOES HERE
print("######### Part 4 ###########")
print("1)")
print("All perfect squares less than 300:")


def perfectSquaresLessThan(upperBound):
    perfect_squares = []
    perfect_square = 1
    i = 1
    while perfect_square < upperBound:
        perfect_squares.append(perfect_square)
        i += 1
        perfect_square = i*i
    return perfect_squares


squares = perfectSquaresLessThan(300)
print(squares)
'''
    2) Write a python code to print all the perfect square numbers less than 300 and greater than 20 except for 100 and 121.
'''
# YOUR CODE GOES HERE
print("2)")
print("All the perfect square numbers less than 300 and greater than 20 except for 100 and 121:")

squares = perfectSquaresLessThan(300)
new_squares = []
for square in squares:
    if square > 20 and square != 100 and square != 121:
        new_squares.append(square)
print(new_squares)

'''
    3) Write a python code to calculate 100*101*102...*200
'''
# YOUR CODE GOES HERE
print("3)")
product = math.prod(range(100, 200))
print(f"100*101*102...*200 = {product}")
print("\n")
######### Part 5 ###########

'''
    1) Given a list of values: x = [1,'ok',3, 17.01, True]
    Write a code to print the last element of it
'''
# YOUR CODE GOES HERE
print("######### Part 5 ###########")
print("1)")
x = [1, 'ok', 3, 17.01, True]
print("last element of x = [1,'ok',3, 17.01, True] is:")
print(x[-1])

'''   2) Given a list of integers: e.g.: [1,2,3,2,0]
        (a) return the average
        (b) return the list resulted from adding up each number with its index. e.g.: output:[1,3,5,5,4]
        (c) given another list, return their common elements. e.g.: SecondList = [1, 1, 2, 2, 2, 2, 4, 6, 7, 88, 8], output :[1,2]
      
        
'''
# YOUR CODE GOES HERE
print("2)")
int_list = [1, 2, 3, 2, 0]
print(f"list = {int_list}")
average = sum(int_list) / len(int_list)
print("(a)")
print(f"Average = {average}")
print("(b)")
plus_index = [i + int_list[i] for i in range(len(int_list))]
print("The list resulting from adding up each number with its index:")
print(plus_index)
print("(c)")
SecondList = [1, 1, 2, 2, 2, 2, 4, 6, 7, 88, 8]
intersect_list = list(set(int_list).intersection(SecondList))
print(f"Common elements of {int_list} and {SecondList}")
print(intersect_list)
print("\n")

######### Part 6 ###########

'''
    1)  Write a function to find the even numbers in the list and return a list of those numbers:
        e.g.: list1 = [9,-6, 0, 7, 1, 5, 6, 8]-->[-6, 0, 6, 8]
'''

# YOUR CODE GOES HERE
print("######### Part 6 ###########")
print("1)")
list1 = [9,-6, 0, 7, 1, 5, 6, 8]
print(f"Even numbers of {list1}:")
def getEven(list1):
    return [num for num in list1 if num % 2 == 0]
even_nums = getEven(list1)
print(even_nums)
'''
    2)  Write a function to find the odd numbers in the list and return a list of their indices: e.g.: list1 = [9,-6, 0, 7, 1, 5, 6, 8] --> [0,3,4,5]
'''
# YOUR CODE GOES HERE
print("2)")
print(f"Odd numbers of {list1}:")
def getOdd(list1):
    return [i for i in range(len(list1)) if list1[i] % 2 == 1]
odd_nums = getOdd(list1)
print(odd_nums)
print("\n")

######### Part 7 ###########

'''
    1) Write a function to get a message as an input and to replace all instances of ‘o’ with ’a’ and to return the updated message.
'''

# YOUR CODE GOES HERE
print("######### Part 7 ###########")
def messageReplace():
    message = input("Type a message for me to play with.\n")
    return message.replace("o", "a")
print(messageReplace())
print("\n")
######### Part 8 ###########
'''
    1) Write a function to drop the duplications in a list of numbers.
    (Hint: use dictionary)  e.g.: 
    Input_list = [11,2,3,8,0,11,4,2,2,7,0]-->[11,2,3,8,0,4,7]

'''
# YOUR CODE GOES HERE
print("######### Part 8 ###########")
def dropDuplicates(num_list):
    return list(dict.fromkeys(num_list))
Input_list = [11,2,3,8,0,11,4,2,2,7,0]
print(f"{Input_list} without duplicates:")
print(dropDuplicates(Input_list))
print("\n")
######### Part 9 ###########
'''
    1) Write a function to get the radius of a circle and to return its area. (import pi and exponentiation from math module)
    
'''
# YOUR CODE GOES HERE
print("######### Part 9 ###########")
def areaOfCircle(radius):
    return math.pi * radius ** 2
print(f"Area of circle with radius 100cm = {areaOfCircle(100)}cm squared")
print("\n")
######### Part 10 ###########
'''
   1) Write a python function to find the frequency of the characters in a sentence.
(Hint : Use a dictionary)

e.g.:  ‘Hhellloo’      {‘H’:1 , ‘h’: 1, ‘e’:1, ‘l’:3 , ‘o’:2}
    
'''
# YOUR CODE GOES HERE
print("######### Part 10 ###########")
def frequencyOfChars():
    sentence = input("Enter a sentence to find the frequency of characters within it.\n")
    characters = dict.fromkeys(sentence)
    for key in characters.keys():
        characters[key] = sentence.count(key)
    print(characters)
frequencyOfChars()
