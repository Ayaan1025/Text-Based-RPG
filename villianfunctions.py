import random

def villain_basic_attack(villain_name, villain_health, player):
    print(f"A wild {villain_name} appears!\n")
    while villain_health > 0 and player['health'] > 0:
        input("Press Enter to attack!")
        player_damage = random.randint(player['attack'] - 3, player['attack'] + 3)
        villain_health -= player_damage
        print(f"You attack {villain_name}, dealing {player_damage} damage.")
        
        if villain_health <= 0:
            print(f"You defeated {villain_name}! Victory!\n")
            # Reward gold for defeating the villain
            gold_reward = random.randint(20, 50)
            player['gold'] += gold_reward
            print(f"You gained {gold_reward} gold! You now have {player['gold']} gold.\n")
            break
        
        villain_damage = max(0, random.randint(5, 10) - player['defense'])
        player['health'] -= villain_damage
        print(f"{villain_name} attacks, dealing {villain_damage} damage to you.")
        print(f"Your health: {player['health']}, {villain_name}'s health: {villain_health}")
        
        if player['health'] <= 0:
            print("Game over! You have been defeated by the villain.")
            break

def villain_advanced_attack(villain_name, villain_health, player):
    print(f"A fierce {villain_name} appears!\n")
    while villain_health > 0 and player['health'] > 0:
        input("Press Enter to attack!")
        player_damage = random.randint(player['attack'] - 3, player['attack'] + 3)
        villain_health -= player_damage
        print(f"You attack {villain_name}, dealing {player_damage} damage.")
        
        if villain_health <= 0:
            print(f"You defeated {villain_name}! Victory!\n")
            # Reward gold for defeating the villain
            gold_reward = random.randint(50, 100)
            player['gold'] += gold_reward
            print(f"You gained {gold_reward} gold! You now have {player['gold']} gold.\n")
            break
        
        villain_damage = max(0, random.randint(10, 15) - player['defense'])
        player['health'] -= villain_damage
        print(f"{villain_name} attacks, dealing {villain_damage} damage to you.")
        print(f"Your health: {player['health']}, {villain_name}'s health: {villain_health}")
        
        if player['health'] <= 0:
            print("Game over! You have been defeated by the villain.")
            break

def dragon_boss_attack(villain_name, villain_health, player):
    print(f"The mighty {villain_name} appears!\n")
    while villain_health > 0 and player['health'] > 0:
        input("Press Enter to attack!")
        player_damage = random.randint(player['attack'] - 3, player['attack'] + 3)
        villain_health -= player_damage
        print(f"You attack {villain_name}, dealing {player_damage} damage.")
        
        if villain_health <= 0:
            print(f"You defeated the {villain_name}! Ultimate Victory!\n")
            # Reward gold for defeating the Dragon
            gold_reward = random.randint(100, 200)
            player['gold'] += gold_reward
            print(f"You gained {gold_reward} gold! You now have {player['gold']} gold.\n")
            break
        
        villain_damage = max(0, random.randint(15, 25) - player['defense'])
        player['health'] -= villain_damage
        print(f"{villain_name} attacks, dealing {villain_damage} damage to you.")
        print(f"Your health: {player['health']}, {villain_name}'s health: {villain_health}")
        
        if player['health'] <= 0:
            print("Game over! You have been defeated by the Dragon.")
            break
