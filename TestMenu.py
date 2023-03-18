import BattleTest, ShopTest, InventoryTest, TravelTest, time

def main():
    time.sleep(0.25)
    print("----TEST MENU----\n1. Inventory\n2. Battle\n3. Shop\n4. World\n")

    MainMenuChoice = int(input("select a menu: "))

    # error
    if MainMenuChoice < 0:
        print("\nError in MenuChoice; invalid selection.")
        quit(-1)

    # inventory test
    if MainMenuChoice == 1:
        time.sleep(0.15)
        InventoryTest.InitalizeGenericInventory()

    # battle test
    if MainMenuChoice == 2:
        time.sleep(0.15)
        BattleTest.InitalizeBattleTestMenu()

    # shop test
    if MainMenuChoice == 3:
        time.sleep(0.15)
        ShopTest.OpenTestShop()

    # travel test
    if MainMenuChoice == 4:
        time.sleep(0.15)
        TravelTest.InitTestWorldMap()
if  __name__ == "__main__":
    main()