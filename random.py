#random

class Player:
    def __init__(self, username, playerscore):
        self.username = username
        self.playerscore = playerscore
       
def question(Player):
    score = 0 
    question = input("what direction is the arrow pointing, left or right? ->")
    if question == "right":
        score += 1
    else:
        score += 0

    question2 = input("What direction is arrow pointing, up or down? ^")
    if question2 == "up":
        score += 1 
    else: 
        score += 0 
    

intro = input("Are you ready to play?")
if intro.lower() in ("yes", "go", "y"):
    user = input("What is your username? ")
    p1 = Player(user, 0)
else:
    exit()

cont = input("Player 2, are you ready to play? ")
if cont.lower() in ("yes", "go", "y"):
    user2 = input("What is your username? ")
    p2 = Player(user2, 0)
else: 
    print(p1, "wins by default.")

if p1.playerscore>p2.playerscore:
    print (p1.username, "is the winner!")
elif p1.playerscore == p2.playerscore:
    print ("No one wins. It's a tie!")
else:
    print (p2.username, "is the winner!")