import random

# Dice class to simulate rolling a dice with a number of sides we set later
class Dice:
    def __init__(self, sides=6): # initializer method to set number of sides
        self.sides = sides # setting sides variable of the Dice object

    def roll(self): # method to roll the dice
        return random.randint(1, self.sides) # returns a random integer between 1 and number of sides
    
# Example usage
# dice = Dice(6)
# for roll in range(100): # rolling the dice 100 times
#     print(dice.roll())

dice2 = Dice() # creating a dice object with default 6 sides
print(dice2.roll()) # rolling the dice and printing the result
