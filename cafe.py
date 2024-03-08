#Create a list called menu with at least 4 items
#Create stock dictionary which contains value for each item on the menu
#Create price dictionary which contains prices for each item on the menu

menu = ['coffee','donuts','omelette','bagel','croissant']      #list of menu

#dictionary for the value of stock
stock = {'coffee':80,        
                'donuts':50,
                'omelette':20,
                'bagel':25,
                'croissant':10}

#dictionary for the price of the items
price = {'coffee':5.5,        
                'donuts':2.5,
                'omelette':4.5,
                'bagel':4.5,
                'croissant':3.5}

#using a loop to set items as keys to access corresponding stock and price
total_stock =0
for item in menu:
    item_value = stock[item] * price[item]      #calculate stock worth
    total_stock += item_value               #adding up all item value

print(f"The total stock worth in the cafe is: {total_stock}")
