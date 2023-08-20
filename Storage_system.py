print('Beginning of program. Lets start \n')
account = float(0)
command_list = ['balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'overview', 'commands', 'example list', 'exit']
#Pozycja w liscie:  0        1          2          3        4          5           6           7            8            9
warehouse_list = []
quantity_of_items = []
prices = []
print(f'Your account balance at the beginning of the program: {account}')
print(f'The state of your warehouse at the beginning of the program: {warehouse_list}')
print(f'List of commands: {command_list}')

while True:
    command = input('What command do you want to use? \n')

    if command == 'balance':
        command_balance = input('Do you want to add or subtract an amount? You can use only add or subtract here: \n')
        if command_balance == 'add':
            value = float(input('Specify the value you want to add: \n'))
            account += value
            print(account)
        elif command_balance == 'subtract':
            value = float(input('Specify the value you want to add: \n'))
            account -= value
            print(account)
        else:
            print('You must provide the value in numbers, try again. \n')
            continue

    elif command == 'sale':
        pass
    elif command == 'purchase':
        item = input('What do You want to buy?: \n')
        if item not in warehouse_list:
            quantity = int(input('How many pieces do You want to buy?: \n'))
            piece_price = float(input('How much for piece?: \n'))
            price_of_all = float(quantity*piece_price)
            if price_of_all <= account:
                print(f'You have just bought: {item}, {quantity} pieces, for {price_of_all}. \n')
                account -= price_of_all
                warehouse_list.append(item)
                quantity_of_items.append(quantity)
                prices.append(piece_price)
                continue
            else:
                price_of_all > account
                print(f'You dont have enough money on account. You have {account}. Try again. \n')
                continue

    elif command == 'account':
        print(f'Your account balance is: {account}')
        continue

    elif command == 'list':
        pass
    elif command == 'warehouse':
        pass
    elif command == 'overview':
        pass
    elif command == 'example list':
        pass

    elif command == 'commands':
        print(f'Command list: {command_list} \n')

    elif command == 'exit':
        print('Here the program ends. Goodbye. \n')
        break

    else:
        print('There is no such command, try again. \n')
        continue
