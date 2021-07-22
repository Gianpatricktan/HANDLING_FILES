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
def get_property(code, property):
    get_property_output = products[code][property]
    return get_property_output

# Problem 3 (The Point-of-Sale Terminal): main function
def main():
    total_cost = 0 # Define a new variable total_cost
    product_code_list = [] # Create a new list product_code_list
    product_name_list = [] # Create a new list product_name_list
    product_quantity_list = [] # Create a new list product_quantity_list
    product_subtotal_list = [] # Create a new list product_subtotal_list
    grand_total = 0 # Define a new variable grand_total
    receipt_product_data = '' # Define a new variable receipt_product_data
    
    while True: # Infinite loop for inputting customer order data
        product_code_input = str(input('Enter the product code: ')).lower() # Input product code
        try:
            if product_code_input != '/': # Terminate the 
                product_name = get_product(product_code_input)['name'] # Product property name
                product_quantity_input = int(input('Enter the quantity: ')) # Input product quantity
                if product_quantity_input > 0: # Solely logical quantities considered
                    if product_code_input not in product_code_list: # product_code_input has not been ordered yet
                        product_code_list.append(product_code_input) # Add product_code_input to product_code_list
                        product_name_list.append(product_name) # Add product_name to product_name_list
                        product_quantity_list.append(product_quantity_input) # Add product_quantity_input to product_quantity_list
                        product_subtotal = get_product(product_code_input)['price'] # Product property price
                        product_subtotal_list.append(product_subtotal * product_quantity_input) # Add product_subtotal to product_subtotal_list
                        grand_total += (product_subtotal * product_quantity_input) # Summation of (product_subtotal * product_quantity_input)
                    else: # product_code_input has been ordered
                        product_code_input_additional = product_quantity_list[product_code_list.index(product_code_input)] + product_quantity_input # Assign a new variable product_code_input_additional that will get the index
                        product_quantity_list[product_code_list.index(product_code_input)] = product_code_input_additional # Index will be the same as the first time that product_code_input was mentioned
                        product_subtotal = get_product(product_code_input)['price'] # Product property price
                        product_subtotal_list[product_code_list.index(product_code_input)] = ((product_subtotal) * (product_code_input_additional))
                        grand_total += ((product_subtotal) * (product_quantity_input)) # Summation of (product_subtotal * product_quantity_input)
                else: # Illogical inputs
                    print('Please enter a valid product and/or quantity.')
                    continue # Goes back to the first if conditional
            else:
                break # Terminates the entire while loop
        except:
            print('Please enter a valid product and/or quantity.')
            continue
            
    product_code_list.sort() # Alphabetise all product_code_input in product_code_list.
    product_name_list.sort() # Alphabetise all product_name_input in product_name_list.
    
    # Receipt Header           
    receipt_header = '==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n'
    # Receipt Body
    for product_code_list, product_name_list, product_quantity_list, product_subtotal_list in zip(product_code_list, product_name_list, product_quantity_list, product_subtotal_list):
        if len(product_code_list) < 8: # Fix alignment of product_code_list, product_name_list, product_quantity_list, product_subtotal_list
            receipt_per_product_data = f'{product_code_list}\t\t\t{product_name_list}\t\t\t{product_quantity_list}\t\t\t\t{product_subtotal_list}\n'
        elif len(product_code_list) >= 8: # Fix alignment of product_code_list, product_name_list, product_quantity_list, product_subtotal_list
            receipt_per_product_data = f'{product_code_list}\t\t{product_name_list}\t\t{product_quantity_list}\t\t\t\t{product_subtotal_list}\n'
        receipt_product_data += receipt_per_product_data
    
    # Receipt Conclusion
    receipt_grand_total = f'\nTotal:\t\t\t\t\t\t\t\t\t\t{grand_total}\n=='
        
    # receipt.txt text file
    with open('receipt.txt','w') as receipt_file:
        receipt_file.write(receipt_header) # Writes the receipt_header into receipt.txt
        receipt_file.write(receipt_product_data) # Writes the receipt_product_data into receipt.txt
        receipt_file.write(receipt_grand_total) # Writes the receipt_grand_total into receipt.txt
        # receipt_header, receipt_per_product_data and receipt_grand_total must appear on the text editor (Atom). 
        
main()
