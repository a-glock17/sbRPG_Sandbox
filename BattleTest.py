import time, math, random

def InitalizeBattleTestMenu():
    time.sleep(0.5)
    # Define a class for a character
    class Character:
        def __init__(self, name, hp, attack):
            self.name = name
            self.hp = hp
            self.attack = attack

        def is_alive(self):
            return self.hp > 0

        def take_damage(self, damage):
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

        def attack_enemy(self, enemy):
            enemy.take_damage(self.attack)

    # Define the player character and the enemy character
    player = Character("Player", 100, 10)
    enemy = Character("Enemy", 50, 5)

    # Define a function for the player's turn
    def player_turn():
        print("Player's turn!")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter your choice: ")
        if choice == "1":
            player.attack_enemy(enemy)
            print("You attacked the enemy for {} damage!".format(player.attack))
        elif choice == "2":
            print("You healed yourself for 10 HP!")
            player.hp += 10
        else:
            print("Invalid choice. Please try again.")

    # Define a function for the enemy's turn
    def enemy_turn():
        print("Enemy's turn!")
        enemy.attack_enemy(player)
        print("The enemy attacked you for {} damage!".format(enemy.attack))

    # Main game loop
    while player.is_alive() and enemy.is_alive():
        player_turn()
        if enemy.is_alive():
            enemy_turn()

    # Determine the winner
    if player.is_alive():
        print("You win!")
    else:
        print("You lose!")
