
def fight():
    print('Welcome to Robot Gladiators!')
    print('')
    
    robot_name = input("What is your robot's name? ")
    robot_health = 100
    robot_attack = 10
    print('')
    
    print(f"{robot_name} = Health: {robot_health}, Attack: {robot_attack}")
    print('')
    
    enemy_name = "Roberto"
    enemy_health = 50
    enemy_attack = 12

    # player attacks
    enemy_health -= robot_attack
    print(f"{robot_name} attacked {enemy_name}")
    print(f"{enemy_name} now has {enemy_health} health remaining.")
    print('')
    # Check player's health
    if robot_health <= 0:
        print(f"{robot_name} has died!")
    else:
        print(f"{robot_name} still has {robot_health} health left.")
    print('')
    
    # enemy attacks
    robot_health -= enemy_attack
    print(f"{enemy_name} attacked {robot_name}")
    print(f"{robot_name} now has {robot_health} health remaining.")
    print('')
    
    # Check enemy's health
    if enemy_health <= 0:
        print(f"{enemy_name} has died!")
    else:
        print(f"{enemy_name} still has {enemy_health} health left.")
    print('')
    
    
fight()
# print(f"{enemy_name} now has {enemy_health} health remaining.")
# print(f"{robot_name} now has {robot_health} health remaining.")