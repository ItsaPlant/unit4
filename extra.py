import csv


items = [
    {
        'name' : "Eliz",
        'quantity' : '5',
        'unit' : "PLN",
        'unit_price' : '4000'
    },
    {
        'name' : 'Yamaha',
        'quantity' : '6',
        'unit' : "USD",
        'unit_price' : '1500'
    },
    {
        'name' : "MBL",
        'quantity' : '2',
        'unit' : "Rupees",
        'unit_price' : '20000'
    },
    {
        'name' : "B&W",
        'quantity' : '8',
        'unit' : "EUR",
        'unit_price' : '10000'
    }

    
    ]

sold_items = []



if __name__ == "__main__": #AUTO CSV LOAD
    load_items_from_csv()



def get_items():
    count = len(items)
    print("Name \t\tquant \t\tUnit \t\tUnit price")
    
    for i in range(count):
        item = items[i]
        info = []
        for key, to_print in item.items():
            info.append(to_print)
        name, quantity, unit, unit_price = info
        print(f"{name} \t\t{quantity} \t\t{unit} \t\t{unit_price}")
    starting()



def add_item():
    raw_input = input("name, quantity, unit_name, unit_price: ")
    new_item = raw_input.split(", ")

    new_item_dict = {}
    new_item_dict['name'] = new_item[0]
    new_item_dict['quantity'] = new_item[1]
    new_item_dict['unit'] = new_item[2]
    new_item_dict['unit_price'] = new_item[3]

    items.append(new_item_dict)
    starting()



def sell_item():
    sell_name = input("name: ")
    sell_quant = input("quantity: ")

    for item in items:
        if item['name'] == sell_name:
            quant = item['quantity']

            quant = int(quant)
            input_quant = int(sell_quant)

            quantity_new = quant - input_quant
            
            item["quantity"] = quantity_new

            price = input_quant * int(item["unit_price"])

            x = item["name"]
            y = item["unit"]

            print(f"\nSOLD {input_quant} {x} for {price} {y}\n")

            #SOLD_ITEMS
            new_item_dict = {}
            new_item_dict['name'] = item['name']
            new_item_dict['quantity'] = sell_quant
            new_item_dict['unit'] = item["unit"]
            new_item_dict['unit_price'] = item["unit_price"]
            new_item_dict['total sum'] = price

            sold_items.append(new_item_dict)

    starting()



def get_costs():

    price = []
    for item in items:
        price.append(int(item['quantity']) * int(item["unit_price"]))
    total = sum(price)

    print(total)

    starting()



def get_income():

    price = []
    for item in sold_items:
        price.append(int(item['quantity']) * int(item["unit_price"]))
    total = sum(price)

    print(total)

    starting()



def export_items_to_csv():
    with open('items.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in items:
            writer.writerow(item)
    
    starting()



def load_items_from_csv():

    items.clear()

    with open('items.csv', newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            new_item_dict = {}
            new_item_dict['name'] = row['name']
            new_item_dict['quantity'] = row['quantity']
            new_item_dict['unit'] = row['unit']
            new_item_dict['unit_price'] = row['unit_price']

            items.append(new_item_dict)
    starting()




def starting():
    print( "\nyour options: \nexit \tto quit \nshow \tto show items \nadd \tto add items \nsell \tto sell items")
    print("total \tto check store value \nincome \tto check the income \nexport \tto export items \nload \tto load items")
    start = input('\nWhat to do? ')
    
    if start == "exit" : #exit
        print("\nOk, bye!") + exit(1) 
    elif start == "show" : #show items
        print("\ncurrently avilable items: ") 
        get_items()
    elif start == "add" : #add items
        print("\ntype: ")
        add_item()
    elif start == "sell" : #sell item
        print("\nwhat to sell?")
        sell_item()
    elif start == "total": #check store value
        print("\nitems in store are worth: ")
        get_costs()
    elif start == "income" : #check income
        print("\nincome equals: ")
        get_income()
    elif start == "export" : #export to csv
        print("\nexporting...")
        export_items_to_csv()
    elif start == "load" : #load csv
        print('loading...')
        load_items_from_csv()
    else:
        start = None
        starting()



starting()
