import random

player = {
    'name': '',
    'health': 100,
    'attack': 10,
    'money':10
}

enemy = {
    'name': 'Test Robot',
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
    print('fight skipped')
    
    
def play():
    player_name = input("What is your robot's name? ")
    print('')
    player['name'] = player_name.upper()
    print(f"Welcome to Robot Gladiators {player_name.upper()}!")
        
    while player['health'] > 0:
        fight()
        
        
play()