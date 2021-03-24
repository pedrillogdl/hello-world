

print ("Program for calculating the total profit on the sales of a product\r\n")
count=1
products={}
propertiesProduct={}
#products['propertiesProduct']={}
answer="yes"
while answer!="no":	
	if count<1:
		print (f"We are going to start with product {count}\r\n")
	else:
		print (f"Now, please enter the values for product {count}\r\n")
	while True:
		try:
			costPrice= float(input(f"Please Enter the cost Price of Product {count}: "))
			sellPrice= float(input(f"Please Enter the sell Price of Product {count}: "))
			inventory= int(input(f"Please Enter the inventory of Product {count}: "))
			assert costPrice > 0
			assert sellPrice > 0
			assert inventory >= 0
			assert sellPrice > costPrice
		except ValueError:
			print("Sorry, that is not a valid number could you please try again?")
		except AssertionError :
			print("Please enter a number bigger or equal(for Inventory) to 0, also sell Price should be bigger that cost Price")
		else:
			propertiesProduct["cost_price"]=costPrice
			propertiesProduct["sell_price"]=sellPrice
			propertiesProduct["inventory"]=inventory
			propertiesProduct["profit"]=round((inventory*sellPrice)-(inventory*costPrice))
			break
	copyDictionary=propertiesProduct.copy()
	finalProduct="Product_"+str(count)
	products[str(finalProduct)]=copyDictionary	
	answer=input("Do you want to add another product? yes/no: ")
	if answer=="yes":
		count=count+1


print("\r\nWe are going to show the Cost Price, Sell Price, Inventory and Profit for each Product that was introduced:\r\n ")
counter=0
listproducts=[]
for key in products.keys():
	listproducts.append(key)
while counter<count:
	print(listproducts[counter])
	print(products[listproducts[counter]])
	counter=counter+1
