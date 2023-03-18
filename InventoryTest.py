import time, math

def InitalizeGenericInventory():
    time.sleep(0.5)

    # initalizes item 'blueprint' for later use
    class InventoryItem:
        def __init__(self, quantity, rarity, is_quest_item, is_magic_item, use_value, sell_value, item_id):
            self.quantity = quantity
            self.rarity = rarity
            self.is_quest_item = is_quest_item
            self.is_magic_item = is_magic_item
            self.use_value = use_value
            self.sell_value = sell_value
            self.item_id = item_id

    class Inventory:
        def __init__(self):
            self.items = {}

        def add_item(self, item_name, quantity, rarity, is_quest_item, is_magic_item, use_value, sell_value, item_id):
            self.items[item_name] = InventoryItem(quantity, rarity, is_quest_item, is_magic_item, use_value, sell_value, item_id)

        def remove_item(self, item_name):
            del self.items[item_name]

        def get_item(self, item_name):
            return self.items[item_name]

        def get_all_items(self):
            return self.items
        

    # Create an inventory object
    game_inventory = Inventory()

    # Add example items to the inventory
    game_inventory.add_item("Potion", 5, 2, False, False, 20, 50, 21)
    game_inventory.add_item("Sword", 1, 4, False, True, 50, 1000, 71)
    game_inventory.add_item("Key", 3, 0, True, False, 0, 10, 8)

    # Get an item from the inventory and print its details
    sword = game_inventory.get_item("Sword")
    print("Item: Sword, Quantity: {}, Rarity: {}, Quest Item: {}, Magic Item: {}, Use Value: {}, Sell Value: {}, Item ID: {}".format(sword.quantity, sword.rarity, sword.is_quest_item, sword.is_magic_item, sword.use_value, sword.sell_value, sword.item_id))

    #Remove an item from the inventory
    game_inventory.remove_item("Key")

    # Get all items from the inventory and print their details
    all_items = game_inventory.get_all_items()
    for item_name, item in all_items.items():
        print("Item: {}, Quantity: {}, Rarity: {}, Quest Item: {}, Magic Item: {}, Use Value: {}, Sell Value: {}, Item ID: {}".format(item_name, item.quantity, item.rarity, item.is_quest_item, item.is_magic_item, item.use_value, item.sell_value, item.item_id))


