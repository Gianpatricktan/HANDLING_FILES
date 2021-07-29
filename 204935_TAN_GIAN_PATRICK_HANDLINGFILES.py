# Products Dictionary
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# Problem 1 (Product Information Lookup): get_product function
def get_product(code):
    get_product_output = products[code]
    return get_product_output

# Problem 2 (Product Property Lookup): get_property function
def get_property(code,property):
    get_property_output = products[code][property]
    return get_property_output

# Problem 3 (The Point-of-Sale Terminal): main function
def main():
    total_price = 0 # Define a new variable total_price and set it to nil
    product_orders_set = {} # Create a new set product_orders_set
    product_quantity_list = [] # Create a new list product_quantity_list
    product_subtotal = 0 # Define a new variable product_subtotal and set it to nil
    receipt_product_data = '' # Define a new variable receipt_product_data
    
    while True: # Infinite loop for inputting customer order data
        customer_order = input('{product_code},{quantity}: ') # Input of customer order
        try: # In cases where the inputs of customer_order is invalid
            if customer_order == '/': # No more customer orders
                break # Terminates the program

            product_code,product_quantity = customer_order.split(',') # .split() to separate product_code from product_quantity
            product_name = get_product(product_code)['name'] # Product property name
            product_quantity = int(product_quantity) # Convert the string to an integer
            product_price = get_product(product_code)['price'] # Product property price
            product_subtotal = ((product_price) * (product_quantity)) # Formula in calculating for the product_subtotal

            if product_quantity > 0: # Logical inputs
                if product_code in product_orders_set.keys(): # If the product also already been ordered
                    product_orders_set[product_code]['product_quantity'] += product_quantity # Add the new product_quantity to the existing value of product_quantity
                    product_orders_set[product_code]['product_subtotal'] += product_subtotal # Add the new product_subtotal to the existing value of product_subtotal
                else: # If the product has not been ordered by the customer
                    product_orders_set[product_code] = {'product_quantity' : product_quantity, 'product_subtotal' : product_subtotal} # Add the key-value pairs of product_code and product_subtotal under the product_code

                total_price += product_subtotal # Summation of all product_subtotal equals total_price

            else: # Illogical or invalid inputs from customer_order
                print('Please enter a valid quantity and/or an available product.') # Display error message
                continue # Goes back to the beginning of the while loop (ignore the error as if nothing occurred)
        except: # If the execution of the codes encounter an error, then...
            print('Please enter a valid quantity and/or an available product.') # Display error message
            continue

    product_orders_set = dict(sorted(product_orders_set.items())) # Alphabetise all items in product_orders_set

    # Receipt Header
    receipt_header = '==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n' # First part of the receipt

    # Receipt Body
    receipt_body = ''
    for product_code,customer_order in product_orders_set.items(): # Middle part of the receipt
        product_name = get_property(product_code,'name') # Product property name
        product_quantity = customer_order['product_quantity'] # Quantity of the product ordered by the customer
        product_subtotal = customer_order['product_subtotal'] # Subtotal cost of the product ordered by the customer
        if len(product_code) < 8:
            receipt_per_product_data = f'{product_code}\t\t\t{product_name}\t\t\t{product_quantity}\t\t\t\t{product_subtotal}\n' # Format of the receipt body
        else:
            receipt_per_product_data = f'{product_code}\t\t{product_name}\t\t{product_quantity}\t\t\t\t{product_subtotal}\n' # Format of the receipt body
        receipt_body += receipt_per_product_data # All the receipt_per_product_data will be appended in the variable receipt_product_data (will be used in writing the receipt)

    # Receipt Conclusion
    receipt_grand_total = f'\nTotal:\t\t\t\t\t\t\t\t\t\t{total_price}\n==' # Last part of the receipt

    # receipt.txt text file
    with open('receipt.txt','w') as receipt_file:
        receipt_file.write(receipt_header) # Writes the receipt_header into receipt.txt
        receipt_file.write(str(receipt_body)) # Writes the receipt_body into receipt.txt
        receipt_file.write(receipt_grand_total) # Writes the receipt_grand_total into receipt.txt
        # receipt_header, receipt_per_product_data and receipt_grand_total must appear on the text editor. 
    
main()
