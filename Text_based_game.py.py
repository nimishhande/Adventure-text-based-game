
import sys
class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 500
        self.inventory = []
        self.location = 'Harry Potter World'

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"{item} is not in your inventory.")

    def show_inventory(self):
        print(f"Inventory: {', '.join(self.inventory)}")

    def move_to(self, new_location):
        self.location = new_location

def create_character():                                #CREATING A CHARACTER NAME AND ITS CLASS
    name = input("Enter your character's name: ")
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Thief")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        character_class = 'Warrior'
    elif choice == '2':
        character_class = 'Mage'
    elif choice == '3':
        character_class = 'Thief'
    else:
        print("Invalid choice, defaulting to Warrior.")
        character_class = 'Warrior'
    return Player(name, character_class)

def main():                                           #MAIN FUNCTION TO PLAY
    player = create_character()
    print(f"Welcome, {player.name} the {player.character_class}!")
    print("Your adventure begins in your world.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Explore the world")
        print("2. Check inventory")
        print("3. Go on a quest")
        print("4. Exit game")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            explore_village(player)
        elif choice == '2':
            player.show_inventory()
        elif choice == '3':
            start_quest(player)
        elif choice == '4':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def explore_village(player):                         #MODULE OF EXPLORING VILLAGE
    print("You wander through the village and find a market stall selling potions.")
    print("Do you want to buy a potion for 10 gold?")
    choice = input("Enter 'yes' or 'no': ").lower()
    if choice == 'yes':
        player.add_to_inventory('Potion')
        print("You bought a potion and added it to your inventory.")
    else:
        print("You decide not to buy anything.")

def start_quest(player):                           #MOODULE OF STARTING QUEST
    print("You decide to embark on a quest!")
    if player.character_class == 'Warrior':
        print("As a Warrior, you head to the forest to hunt monsters.")
        forest_quest(player)
    elif player.character_class == 'Mage':
        print("As a Mage, you travel to the ancient ruins to find a lost spell.")
        ruins_quest(player)
    elif player.character_class == 'Thief':
        print("As a Thief, you sneak into the castle to steal treasures.")
        castle_quest(player)

def forest_quest(player):                          #ANOTHER MODULE FOR QUESTS FOR WARRIOR
    print("You encounter a wild boar in the forest.")
    print("Do you want to fight or flee?")
    choice = input("Enter 'fight' or 'flee': ").lower()
    if choice == 'fight':
        print("You bravely fight the boar and win! You find a treasure chest.")
        player.add_to_inventory('Treasure Chest')
    else:
        print("You flee back to the village safely.")

def ruins_quest(player):                           #ANOTHER MODULE FOR QUESTS FOR MAGE
    print("You discover an ancient spell book in the ruins.")
    print("Do you want to take it?")
    choice = input("Enter 'yes' or 'no': ").lower()
    if choice == 'yes':
        player.add_to_inventory('Ancient Spell book')
        print("You take the spell book and return to the village.")
    else:
        print("You leave the spell book and return to the village.")

def castle_quest(player):                          #ANOTHER MODULE FOR QUESTS FOR THIEF
    print("You sneak into the castle and find a golden crown.")
    print("Do you want to steal it?")
    choice = input("Enter 'yes' or 'no': ").lower()
    if choice == 'yes':
        player.add_to_inventory('Golden Crown')
        print("You steal the crown and return to the village.")
    else:
        print("You leave the crown and return to the village.")

if __name__ == "__main__":
    main()





