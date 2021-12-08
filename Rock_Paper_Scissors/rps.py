import random

#get player's choice
def play():
    player = input("Choose your weapon (r = rock, p = paper, s = scissors): ")
    npc = random.choice(['r', 'p', 's'])
    print ("NPC picked: " + npc)

#if same choice, game is tied
    if player == npc:
        return ("Tied")

#demetermine winner
    if winner(player, npc):
        return ("You win!")
    else:
        return ("You lose :(")        

#play the game
def winner(player, npc):
    if player == 's' and npc == 'p' or player == 'p' and npc == 'r' or player == 'r' and npc == 's':
        return True 
    
    else:
        return False

print (play())