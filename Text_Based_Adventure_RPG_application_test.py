import Text_Based_Adventure_RPG_utility_test as u

def main():
    accounts = u.account_dictionary()
    main_menu = 'Welcome to Fighting Mania!\n1] Create an account.\n2] Login into account.\n3] Exit Fighting Mania.'
    main_menu_input = ''
    while main_menu_input != '3':
        print(main_menu)
        main_menu_input = input('Enter your option: ')
        if main_menu_input == '1':
            if u.create(accounts):
                print('Account has been created. You have successfully logged in.\n')
                player = {'health': 100, 'attack': 10, 'defense': 5, 'gold': 100}  # Initial player stats
                u.adventure_start(player)
            else:
                print('Account already exists.')
        elif main_menu_input == '2': 
            if u.login(accounts):
                print('You have successfully logged in.')
                player = {'health': 100, 'attack': 10, 'defense': 5, 'gold': 100}  # Initial player stats
                u.adventure_start(player)
            else:
                print('Login information incorrect. Check for any errors.')
        elif main_menu_input == '3':
            print('Exiting Fighting Mania. Thank you for playing!')
        else:
            print('Invalid choice. Returning to main menu.')

main()