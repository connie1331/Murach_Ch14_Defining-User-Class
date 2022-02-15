#******************************************************************************
# Author:           Joel Murach
# Lab:              Murach's example - Define a user class
# Date:             02.15.2022
# Description:      Define Product class
# Sources:          Murach's Python Programming: Beginner - Chapter 14 - How to define and use your own classes
#                   Create Product class in the module named objects
#******************************************************************************

class Product:
    # a constructor that initializes 3 attributes to perform a calculation
    def __init__(self, name, price, discountPercent):
        self.name = name                            # attribute 1
        self.price = price                          # attribute 2
        self.discountPercent = discountPercent      # attribute 3

    # a method that use two attributes to perform a calculation
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    # a method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

