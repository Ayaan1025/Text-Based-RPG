import currencysystem as currency
import villianfunctions as vf

def account_dictionary():
    accounts = {}
    with open('fightingmaniaAccounts.txt', 'r') as c:
        for account in c:
            username, password = account.strip().split('-')
            accounts[username] = {'password': password}
    return accounts

def create(accounts):
    username = input('Enter your username: ')
    if username not in accounts:
        password = input('Enter your password: ')
        accounts[username] = {'password': password}
        return True
    return False

def login(accounts):
    username = input('Enter your username: ')
    if username in accounts:
        password = input('Enter your password: ')
        if password == accounts[username]['password']:
            return True
    return False

def adventure_start(player):
    # Set initial player stats, including starting gold and health of 50
    player['gold'] = 50
    player['health'] = 50
    player['attack'] = 10
    player['defense'] = 5

    print('Welcome to "Fighting Mania"!')
    print('You must defeat villains and manage resources to survive.')
    print("Note: You start with 50 gold and 50 health, so use them wisely!\n")

    # Villain Sequence with adjusted Dragon stats
    villains = [("Goblin", vf.villain_basic_attack, 50),
                ("Skeleton", vf.villain_advanced_attack, 80),
                ("Dragon", vf.dragon_boss_attack, 80)]  # Dragon health set to 80 for balance
    
    for villain_name, villain_func, health in villains:
        print(f"\nNext Villain: {villain_name}!")
        
        while True:
            action = input("Choose action: F] Fight | S] Visit Store | L] Logout: ").upper()
            if action == 'F':
                villain_func(villain_name, health, player)
                if player['health'] > 0:
                    print(f"Current Status: Health = {player['health']}, Gold = {player['gold']}")
                    break
                else:
                    print("You have been defeated. Game over.")
                    return
            elif action == 'S':
                player['gold'] = currency.store(player['gold'], player)
            elif action == 'L':
                print('Logging out of Fighting Mania...')
                return
            else:
                print('Invalid option. Choose one of the game functions.')

    # Game End
    print("\nCongratulations! You have defeated all the villains, including the Dragon!")
    print("Thank you for playing Fighting Mania. Your journey has come to an end.")
