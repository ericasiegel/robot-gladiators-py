import random

player = {
    'name': '',
    'health': 100,
    'attack': 10,
    'money':10,
}

enemy_names = ['E Robot 1', 'E Robot 2', 'E Robot 3']
enemy = {
    'name': '',
    'health': 0,
    'attack': random.randint(9, 21),
}
        
def fight(index):
    print(f"ROUND {index + 1}")
    print(f"PLAYER: {player['name']}, health = {player['health']}, money = ${player['money']}")
    print(f"ENEMY: {enemy['name']}, health = {enemy['health']}")
    print('')
    while enemy['health'] > 0 and player['health'] > 0:
        prompt_fight = input('Would you like to FIGHT or SKIP? ')
        print('')
        if 'fight' in prompt_fight.lower():
            enemy['health'] -= player['attack']
            if enemy['health'] <= 0:
                print(f"{player['name']} attacks {enemy['name']}.")
                print(f"{enemy['name']} has died!")
                print('')
                break
            else:
                print(f"{player['name']} attacks {enemy['name']}. {enemy['name']} has {enemy['health']} health remaining")

            player['health'] -= enemy['attack']
            if player['health'] <= 0:
                print(f"{enemy['name']} attacks {player['name']}.")
                print(f"{player['name']} has died!")
                print('')
                break
            else:
                print(f"{enemy['name']} attacks {player['name']}. {player['name']} has {player['health']} health remaining")
                print('')
        
        elif 'skip' in prompt_fight.lower():
            confirm_skip = input('Are you sure you want to quit? (YES or NO) ')
            print('')
            if 'yes' in confirm_skip.lower():
                player['money'] -= 2
                print(f"{player['name']} skipped the fight. {player['name']} has lost $2 and now has ${player['money']}")
                print('')
                break
            elif 'no' in confirm_skip.lower():
                fight(index)
            else:
                print('Please choose YES or NO')
                print('')
        else:
            print('Please choose FIGHT or SKIP')
            print('')
            
def shop():
    print('Entered Shop')
    print(f"You currently have $player['money']")
    print('')     
    store_choice = input("Would you like to REFILL your health, UPGRADE your attack, or LEAVE the store? Please enter one: 'REFILL', 'UPGRADE', or 'LEAVE' to make a choice. ") 
    print('')
    match store_choice.upper():
        case 'REFILL':
            if player['money'] >= 6:
                print(f"Refilling {player['name']}'s health by 20 for $6")
                print('')
                player['health'] += 20
                player['money'] -= 6
            else:
                print("You don't have enough money!")
                shop()
        case 'UPGRADE':
            if player['money'] >= 7:
                print(f"Upgrading {player['name']}'s attack by 6 for $7")
                print('')
                player['health'] += 20
                player['money'] -= 7
            else:
                print("You don't have enough money!")
                shop()
        case 'LEAVE':
            print('Leaving Store')
            print('')
        case _:
            print('please choose a valid option')
            print('')
            shop()
        

def endgame():
    print("The game has ended. Let's see how you did:")
    print('')
    # if player is still alive
    if player['health'] > 0:
        print(f"Congratulations, you survived!")
        print(f"Your remaining health is {player['health']} and you have ${player['money']}")
        print('')
        print('GAME OVER')
        print('')
    else:
    # if player has died
        print(f"Your robot {player['name']} has died in battle.")
        print('')
        print('GAME OVER')
        print('')
    
    play_again = input('Would you like to play again? YES or NO ')
    if 'yes' in play_again.lower():
        player['attack'] = 10
        player['health'] = 100
        player['money'] = 10
        play()
    else:
        print('')
        print('Thank you for playing Robot Gladiators!')

def play():
    print(f"Welcome to Robot Gladiators!")
    print('')
    
    player_name = input("What is your robot's name? ")
    print('')
    player['name'] = player_name.upper()
    print(f"Lets start {player_name.upper()}!")
    print('')
    
    for index, name in enumerate(enemy_names):
        # reset enemy stats
        enemy['name'] = name
        enemy['health'] = random.randint(19, 51)
        
        if player['health'] > 0:
            fight(index)
            if player['health'] > 0 and index < (len(enemy_names) - 1):
                go_shop = input('The fight is over. visit the store before the next round? YES or NO ')
                if 'yes' in go_shop.lower():
                    shop()
            
        else:
            print('You have lost your robot in battle! GAME OVER!')
    
    endgame()

play()