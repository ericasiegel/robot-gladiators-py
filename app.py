
def fight():
    print('Welcome to Robot Gladiators!')
    print('')
        
    player_name = input("What is your robot's name? ")
    player_health = 100
    player_attack = 10
    player_money = 10
    print('')
    
    print(f"{player_name} = Health: {player_health}, Attack: {player_attack}, $: {player_money}")
    print('')
    
    prompt_fight = input("Would you like to FIGHT or SKIP this battle? Enter 'Fight' or 'Skip' to choose. ")
    print('')

    enemy_name = "Roberto"
    enemy_health = 50
    enemy_attack = 12
    
    # if the player chooses to fight
    if 'fight' in prompt_fight.lower():
        # player attacks
        enemy_health -= player_attack
        print(f"{player_name} attacked {enemy_name}")
        print(f"{enemy_name} now has {enemy_health} health remaining.")
        print('')
        # Check player's health
        if player_health <= 0:
            print(f"{player_name} has died!")
        else:
            print(f"{player_name} still has {player_health} health left.")
        print('')
        
        # enemy attacks
        player_health -= enemy_attack
        print(f"{enemy_name} attacked {player_name}")
        print(f"{player_name} now has {player_health} health remaining.")
        print('')
        
        # Check enemy's health
        if enemy_health <= 0:
            print(f"{enemy_name} has died!")
        else:
            print(f"{enemy_name} still has {enemy_health} health left.")
        print('')
    
    elif 'skip' in prompt_fight.lower():
        confirm_skip = input("Are you sure you would like to skip the fight?")
        if 'yes' in confirm_skip.lower():
            player_money -= 2
            print(f"{player_name} skipped the fight.")
        else:
            fight()
    
    else:
        print('You need to choose a valid option. Try again!')
    
fight()
# print(f"{enemy_name} now has {enemy_health} health remaining.")
# print(f"{robot_name} now has {robot_health} health remaining.")