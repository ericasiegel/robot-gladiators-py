import random

class Player:
    def __init__(self, player_name):
        self.name = player_name.upper()
    health = 100
    attack = 10
    money = 10

class Enemy:
    def __init__(self, enemy_name):
        self.name = enemy_name
        self.health = random.randint(19, 51)
        self.attack = random.randint(9, 21)
        
class Game:
    def player_attack(self, enemy_health, player_attack):
        return enemy_health - player_attack
    def enemy_attack(self, player_health, enemy_attack):
        return player_health - enemy_attack
    def skip(self, player_money):
        return player_money - 2
    def store(self):
        pass

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
    
    game = Game()
    # first attack
    player.health = game.enemy_attack(player.health, enemy.attack)
    enemy.health = game.enemy_attack(enemy.health, player.attack)
    print(f"{enemy.name} gets attacked by {player.name}")
    print(f"{enemy.name} has {enemy.health} health remaining")
    print('')
    print(f"{player.name} gets attacked by {enemy.name}")
    print(f"{player.name} has {player.health} health remaining")
    
    # prompt_fight = input("Would you like to FIGHT or SKIP this battle? Enter 'Fight' or 'Skip' to choose. ")
    # print('')


play()
   
