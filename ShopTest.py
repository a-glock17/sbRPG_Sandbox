import time, math

def OpenTestShop():
    time.sleep(0.5)
    # Define a dictionary to store the items in the shop
    shop_items = {
        "Potion": 50,
        "Elixir": 100,
        "Ether": 200,
        "Phoenix Down": 500
    }

    # Define the exchange rate for the in-game currency
    currency_exchange_rate = 10

    # Define the starting amount of in-game currency for the player
    player_currency = 1000

    # Function to display the shop menu
    def show_shop_menu():
        print("Welcome to the shop! What would you like to do?")
        print("1. Buy an item")
        print("2. Sell an item")
        print("3. Check your currency balance")
        print("4. Exit the shop")

    # Function to buy an item from the shop
    def buy_item():
        global player_currency
        print("Here are the items available in the shop:")

        for item, price in shop_items.items():
            print("{} - {} gold".format(item, price))

        item_to_buy = input("Which item would you like to buy? ")
        if item_to_buy in shop_items:
            item_price = shop_items[item_to_buy]
            if player_currency >= item_price:
                player_currency -= item_price
                print("You have purchased {} for {} gold!".format(item_to_buy, item_price))
            else:
                print("Sorry, you don't have enough gold to buy this item.")
        else:
            print("Sorry, we don't have that item in stock.")

    # Function to sell an item to the shop
    def sell_item():
        global player_currency
        print("Here are the items you have in your inventory:")
        # Assume the player's inventory is a list of dictionaries with 'name' and 'sell_value' keys
        player_inventory = [
            {"name": "Potion", "sell_value": 25},
            {"name": "Antidote", "sell_value": 10},
            {"name": "Phoenix Down", "sell_value": 250}
        ]
        for item in player_inventory:
            print("{} - {} gold".format(item['name'], item['sell_value']))

        item_to_sell = input("Which item would you like to sell? ")
        for item in player_inventory:
            if item['name'] == item_to_sell:
                sell_price = item['sell_value']
                player_currency += sell_price
                player_inventory.remove(item)
                print("You have sold {} for {} gold!".format(item_to_sell, sell_price))
                return
            
        print("Sorry, you don't have that item in your inventory.")

    # Function to check the player's currency balance
    def check_currency_balance():
        global player_currency, currency_exchange_rate
        print("You have {} gold and {} in-game currency.".format(player_currency, player_currency // currency_exchange_rate))

    # Main game loop
    while True:
        show_shop_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            buy_item()
        elif choice == "2":
            sell_item()
        elif choice == "3":
            check_currency_balance()
        elif choice == "4":
            print("Thanks for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")
