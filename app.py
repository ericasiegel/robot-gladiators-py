import random

class Player:
    def __init__(self, player_name):
        self.name = player_name.upper()
        self.health = 100
        self.attack = 10
        self.money = 10

class Enemy:
    def __init__(self, enemy_name):
        self.name = enemy_name
        self.health = random.randint(19, 51)
        self.attack = random.randint(9, 21)

class Game:
    # def fight(self, **args):
    #     new_enemy_health = enemy_health - player_attack
    #     new_player_health = player_health - enemy_attack
        
    # def player_attack(self, enemy_health, player_attack):
    #     return enemy_health - player_attack
    # def enemy_attack(self, player_health, enemy_attack):
    #     return player_health - enemy_attack
    def skip(self, player_money):
        return player_money - 2
    def store(self):
        pass

def fight(**kwargs):
    # game = Game()
    print(kwargs['enemy'])
    print(kwargs['player'])
    current_enemy = kwargs['enemy']
    current_player = kwargs['player']
    
    # enemy attack
    player_health = current_player['health'] - current_enemy['attack']
    # print(player_health)
    # player attack
    enemy_health = current_enemy['health'] - current_player['attack']
    # print(enemy_health)
    
    return player_health, enemy_health


def play():
    print('Welcome to Robot Gladiators!')
    print('')
    
    player_name = input("What is your robot's name? ")
    print('')
    player = Player(player_name)
    print(f"PLAYER : {player.name} = Health: {player.health}, Attack: {player.attack}, $: {player.money}")

    enemy_robots = ['Roborto', 'Amy Android', 'Robo Trumble']
    enemy_name = enemy_robots[0]
    enemy = Enemy(enemy_name)
    print(f"ENEMY : {enemy.name} = Health: {enemy.health}, Attack: {enemy.attack}")
    print('')
    
    while player.health > 0 or enemy.health > 0:
        prompt_fight = input("Would you like to FIGHT or SKIP this battle? Enter 'Fight' or 'Skip' to choose. ")
        print('')
        if 'fight' in prompt_fight.lower():
            print()
            player.health, enemy.health = fight(enemy=vars(enemy), player=vars(player))
            # print(player.health)
            # print(enemy.health)
            print(f"{enemy.name} gets attacked by {player.name}")
            print(f"{enemy.name} has {enemy.health} health remaining")
            print('')
            print(f"{player.name} gets attacked by {enemy.name}")
            print(f"{player.name} has {player.health} health remaining")
            
        elif 'skip' in prompt_fight.lower():
            print('fight skipped')
            
        else:
            print('fight ended')
    else:
        print('game ended')     
            



play()
   
