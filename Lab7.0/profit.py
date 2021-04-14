

print("Program for calculating the total profit on the sales of a product\r\n")
count = 1
products = {}
propertiesproduct = {}
answer = "yes"
while answer != "no":
    if count < 1:
        print(f"We are going to start with product {count}\r\n")
    else:
        print(f"Now, please enter the values for product {count}\r\n")
    while True:
        try:
            costprice = float(input(f"Enter cost Price of Product {count}: "))
            sellprice = float(input(f"Enter sell Price of Product {count}: "))
            inventory = int(input(f"Enter inventory of Product {count}: "))
            assert costprice > 0
            assert sellprice > 0
            assert inventory >= 0
            assert sellprice > costprice
        except ValueError:
            print("Sorry, that is an invalid number, please try again?")
        except AssertionError:
            print("Please enter a number bigger or equal(for Inventory) to 0, also sell Price should be bigger that cost Price")
        else:
            propertiesproduct["cost_price"] = costprice
            propertiesproduct["sell_price"] = sellprice
            propertiesproduct["inventory"] = inventory
            propertiesproduct["profit"] = round((inventory * sellprice) - (inventory * costprice))
            break
    copydictionary = propertiesproduct.copy()
    finalproduct = "Product_" + str(count)
    products[str(finalproduct)] = copydictionary
    answer = input("Do you want to add another product? yes/no: ")
    if answer == "yes":
        count = count + 1


print("\r\nCost and Sell Price, Inventory and Profit introduced:\r\n ")
counter = 0
listproducts = []
for key in products.keys():
    listproducts.append(key)
while counter < count:
    print(listproducts[counter])
    print(products[listproducts[counter]])
    counter = counter + 1
