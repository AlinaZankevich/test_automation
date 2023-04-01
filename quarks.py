# Your Quark class should allow you to create quarks of any valid color
# ("red", "blue", and "green") and any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').
#
# Every quark has the same baryon_number (BaryonNumber in C#): 1/3.
#
# Every quark should have an .interact() (.Interact() in C#)
# # method that allows any quark to interact with another quark via the strong force.
# # When two quarks interact they exchange colors.
#
# Example
# >>> q1 = Quark("red", "up")
# >>> q1.color
# "red"
# >>> q1.flavor
# "up"
# >>> q2 = Quark("blue", "strange")
# >>> q2.color
# "blue"
# >>> q2.baryon_number
# 0.3333333333333333
# >>> q1.interact(q2)
# >>> q1.color
# "blue"
# >>> q2.color
# "red"

class Quark:
    baryon_number = 1/3
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def interact(self, quark):
        my_color = self.color
        their_color = quark.color

        self.color = their_color
        quark.color = my_color


red_quark = Quark('red', 'up')
blue_quark = Quark('blue', 'down')

red_quark.interact(blue_quark)

print(red_quark.color)
print(blue_quark.color)