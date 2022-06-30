import random

player = {
    'name': '',
    'health': 100,
    'attack': 10,
    'money':10
}

enemy = {
    'name': '',
    'health': random.randint(19, 51),
    'attack': random.randint(9, 21),
}
        
def fight():
    prompt_fight = input('Would you like to FIGHT or SKIP? ')
    print('')
    if 'fight' in prompt_fight.lower():
        player['health'] = player['health'] - enemy['attack']
        if player['health'] <= 0:
            print(f"{enemy['name']} attacks {player['name']}. {player['name']} has died!")
        else:
            print(f"{enemy['name']} attacks {player['name']}. {player['name']} has {player['health']} health remaining")
        
        enemy['health'] = enemy['health'] - player['attack']
        if enemy['health'] <= 0:
            print(f"{player['name']} attacks {enemy['name']}. {enemy['name']} has died!")
        else:
            print(f"{player['name']} attacks {enemy['name']}. {enemy['name']} has {enemy['health']} health remaining")
        print('')
    
    elif 'skip' in prompt_fight.lower():
        skip()
    
    else:
        print('Please choose FIGHT or SKIP')
        print('')

def skip():
    confirm_skip = input('Are you sure you want to quit? (YES or NO) ')
    print('')
    if 'yes' in confirm_skip.lower():
        player['money'] = player['money'] - 2
        print(f"{player['name']} skipped the fight. {player['name']} has lost $2 and now has ${player['money']}")
        print('')
    elif 'no' in confirm_skip.lower():
        fight()
    else:
        print('Please choose YES or NO')
        print('')
    
    
def play():
    enemy_names = ['E Robot 1', 'E Robot 2', 'E Robot 3',]
    player_name = input("What is your robot's name? ")
    print('')
    player['name'] = player_name.upper()
    print(f"Welcome to Robot Gladiators {player_name.upper()}!")
    
    for name in enemy_names:
        enemy['name'] = name
        fight()
        
    # while player['health'] > 0:
    #     fight(enemy)
        
        
play()