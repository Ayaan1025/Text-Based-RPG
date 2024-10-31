def store(gold, player):
    while True:  # Keep the player in the store until they choose to exit
        print("\nWelcome to the store!")
        print("Items available:")
        print("1. Potion (+20 health) - 30 gold")
        print("2. Sword Upgrade (+5 attack) - 50 gold")  # Renamed to Sword Upgrade
        print("3. Shield Upgrade (+3 defense) - 40 gold")  # Renamed to Shield Upgrade
        print("Type 'exit' to leave the store.")
        
        choice = input("Enter the item number to buy, or type 'exit' to leave: ")
        
        if choice == "1" and gold >= 30:
            player['health'] += 20
            gold -= 30
            print("You bought a Potion! Health increased by 20.")
        elif choice == "2" and gold >= 50:
            player['attack'] += 5
            gold -= 50
            print("You bought a Sword Upgrade! Attack increased by 5.")
        elif choice == "3" and gold >= 40:
            player['defense'] += 3
            gold -= 40
            print("You bought a Shield Upgrade! Defense increased by 3.")
        elif choice.lower() == 'exit':
            print("Leaving the store.")
            break  # Exit the loop and leave the store
        else:
            print("Invalid choice or insufficient gold.")
        
        print(f"Current Status: Health = {player['health']}, Attack = {player['attack']}, Defense = {player['defense']}, Gold = {gold}")
    
    return gold
