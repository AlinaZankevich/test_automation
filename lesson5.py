#
class BasePlant:
    biology_class = 'Plants'

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def watering(self):
        return 'I need to be watered'

    def photosynthesis(self):
        return 'I need light'

    def get_info(self):
        return f"I am a {self.name}, color - {self.color}"


class Flower(BasePlant):
    biology_class = 'Flowers'

    def __init__(self, name, color, height):
        super().__init__(name, height)  # super() returns a link to the parent class, это определили атрибуты (которые есть в родительском

        self.color = color # так мы определяем атрибут, который не входит в родитльский атрибут


    def bloom(self):
        return 'I can bloom'

    # def print_info(self): # get - это всегда return, a print always print
    #     print(f"I am a {self.name}, color - {self.color}, height: {self.height}")
    #     print(f"Watering: {self.watering()}")

    def get_info(self):
        return f"I am a {self.name}, color - {self.color}, " \
               f"height - {self.height}, Watering - {self.watering()}" # return печатается только первый


class Cactus(BasePlant): # наследник, наследует методы от Plants

    def watering(self):
        return "I don't need to be watered"


class Tree(BasePlant):
    def __init__(self, name, height, branches):
        super().__init__(name, height)
        self.branches = branches

flower1 = Flower('rose', 'white', 30)
print(flower1.height)
flower1.color
flower1.name

flower2 = Flower('tulip', 'red', 20)
plant1 = Plants('palm', 'green', 400)
plant2 = Cactus('Baloon', 'green', 20)
plant3 = Cactus('Chin', 'green', 10)

# print(plant3.get_info())

# # I am a Chin, color - green, height - 10, Watering - I don't need to be watered
# # относится к наследнику и наследует метод класса Plant
#
#
# print(flower1.biology_class)
# # print(flower1.color)
# # print(flower1.watering())
# # print(plant2.watering())
# # print(plant2.name)
# # print(plant2.photosynthesis())
#
# # #хоть этого метода нет в классе Cactus, он унаследован от класса Plant
# # plant2.get_info()
#
# # print(flower2.get_info())

# Color Ghost
# Create a class Ghost
#
# Ghost objects are instantiated without any arguments.
#
# Ghost objects are given a random color attribute of
# "white" or "yellow" or "purple" or "red" when instantiated



          # *** Везде ошибка ***
# Task 1

# Color Ghost
# Create a class Ghost
#
# Ghost objects are instantiated without any arguments.
#
# Ghost objects are given a random color attribute of
# "white" or "yellow" or "purple" or "red" when instantiated



# не получилось

# import random
#
#
# class Ghost(object):
#
#     def _init_(self):
#         self.color = choice(['white', 'yellow', 'purple', 'red'])
#
#
# ghost = Ghost()
# print(ghost.color)


# Ahoy matey!
#
# You are a leader of a small pirate crew. And you have a plan.
# With the help of OOP you wish to make a pretty efficient system to identify
# ships with heavy booty on board!
#
# Unfortunately for you, people weigh a lot these days, so how do you know
# if a ship is full of gold and not people?
#
# You begin with writing a generic Ship class / struct:

# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#
#     def is_worth_it(self):
#         return self.draft > self.crew * 1.5 > 20
#
#
# The following code was thought to be working properly, however
# when the code tries to access the age of the person instance it fails.

# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)
#
# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = f'{self.first_name} {self.last_name}'


# Write a class Block that creates a block (Duh..)
#
# Requirements
# The constructor should take an array as an argument,
# this will contain 3 integers of the form [width, length, height] from which the Block should be created.
#
# Define these methods:
#
# `get_width()` return the width of the `Block`
#
# `get_length()` return the length of the `Block`
#
# `get_height()` return the height of the `Block`
#
# `get_volume()` return the volume of the `Block`
#
# `get_surface_area()` return the surface area of the `Block`

#  b = Block([2,4,6]) -> create a `Block` object with a width of `2`
#  a length of `4` and a height of `6`
#
#     b.get_width() -> return 2
#
#     b.get_length() -> return 4
#
#     b.get_height() -> return 6
#
#     b.get_volume() -> return 48
#
#     b.get_surface_area() -> return 88

# class Block:
#     def __init__(self, lst):
#         self.width = lst[0]
#         self.length = lst[1]
#         self.height = lst[2]
#
#     def get_width(self):
#         return self.width
#
#     def get_length(self):
#         return self.length
#
#     def get_height(self):
#         return self.height
#
#     def get_volume(self):
#         return self.width * self.length * self.height
#
#     def get_surface_area(self):
#         return 2 * (self.width * self.length + self.height * self.width + self.height * self.length)
#
#
# b1 = Block([1, 2, 3])
# b1.height
#
# b2 = Block([1, 2, 3])
#




# This kata is about static method that should return different values.
#
# On the first call it must be 1, on the second and others - it must be a double
# from previous value.
#
# Look tests for more examples, good luck :)

# class Class:
#     counter = 0
#
#     @staticmethod
#     def get_number():
#         rez = 2 ** Class.counter
#         Class.counter += 1
#         return rez

