from objects import Product
# create two product objects
product1 = Product("Stanley 24 OUnce Wood Hammer", 12.99, 62)
product2 = Product("National Hardware 3/4", 5.06, 0)

# print data for product1 and product2
print("Name: {:s}".format(product1.name))
print("Price: {:.2f}".format(product1.price))
print("Discount percent: {:d}%".format(product1.discountPercent))
print("Discount amount: {:.2f}".format(product1.getDiscountAmount()))
print("Discount price: {:.2f}".format(product1.getDiscountPrice()))