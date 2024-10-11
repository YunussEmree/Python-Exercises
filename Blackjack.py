import random
import tkinter as tk
from tkinter import messagebox

cash = 1000
print(f"You cash is : {cash}")
bet = 300

cash -= bet


root = tk.Tk()
root.title("BlackJack")

frame = tk.Frame(root)
frame.pack()

player_deck = []
croupier_deck = []

player_deck_label = tk.Label(root, text=f"Player's deck: {', '.join(player_deck)}")
player_deck_label.pack()

croupier_deck_label = tk.Label(root, text=f"Croupier's deck: {', '.join(croupier_deck)}")
croupier_deck_label.pack()

space = tk.Label(root, text=f" ")
space.pack()


spaceforresult = tk.Label(root, text=f"Game Lose!")

new_game_button = tk.Button(frame, 
                   text="NEW GAME", 
                   fg="red")

hit_button = tk.Button(frame, 
                   text="NEW GAME", 
                   fg="red")



def hit() :
    global decklist
    global player_score
    global player_deck
    
    card = random.choice(decklist)
    player_deck.append(card)
    decklist.remove(card)
    print(f"Hitted : {card}")
    print(f"Now your deck: {player_deck}")
    
    if card != 'A' and card != 'J' and card != 'K' and card != 'Q' and card != 'J' :
        player_score += int(card)
        update_decks()
        choicewithoutdouble()
    elif card == 'A' :
        player_score += 11 # 1 lik mekanik de eklenecek
        update_decks()
    else :
        player_score += 10 
        update_decks()
        
        
    update_decks()
    
    if player_score > 21 : 
        print("Game Lose!")
        spaceforresult = tk.Label(root, text=f"Game Lose!")
        hit_button.destroy()
        stand_button.destroy()
        spaceforresult.pack()
        return
    else : choicewithoutdouble()
    
def double() :
    global cash
    global bet 
    global player_score
    global decklist
    global player_deck
    
    if cash >= bet : 
    
        card = random.choice(decklist)
        player_deck.append(card)
        decklist.remove(card)
        print(f"Doubled with : {card}")
        print(f"Now your deck: {player_deck}")
        
        bet *= 2

        if card != 'A' and card != 'J' and card != 'K' and card != 'Q' and card != 'J' :
            player_score += int(card)
        elif card == 'A' :
            player_score += 11 # 1 lik mekanik de eklenecek
        else :
            player_score += 10 
            
            update_decks()

        if player_score > 21 : 
            print("Game Lose!")
            
            spaceforresult = tk.Label(root, text=f"Game Lose!")
            hit_button.destroy()
            stand_button.destroy()
            spaceforresult.pack()
        else : 
            stand()
            update_decks()
    else : 
        print("No money")
        choice()
        update_decks()

def stand():
    global croupier_score
    global player_score
    global decklist
    
    
    while croupier_score < 21 and croupier_score < player_score :
        randomcard = random.choice(decklist)
        print(f"Croupier new card : {randomcard}")
        update_decks()
        if randomcard != 'A' and randomcard != 'J' and randomcard != 'K' and randomcard != 'Q' and randomcard != 'J' :
            croupier_score += int(randomcard)
        elif randomcard == 'A' :
            croupier_score += 11 # 1 lik mekanik de eklenecek
        else :
            croupier_score += 10 
            
        update_decks()
            
    if croupier_score > 21 : 
        print("Game Win!")
        spaceforresult = tk.Label(root, text=f"Game Win!")
        hit_button.destroy()
        stand_button.destroy()
        spaceforresult.pack()
        
    elif croupier_score >= player_score :
        print("Game Lose!")
        spaceforresult = tk.Label(root, text=f"Game Lose!")
        hit_button.destroy()
        stand_button.destroy()
        spaceforresult.pack()

def choice() :
    choice = input("What do you want? (h for Hit, s for Stand, d for Double) : ").lower()
    if choice == "h" : 
        hit()
    elif choice == "s" :
        print("Stand")
        stand()
    elif choice == "d" :
        double()
    else : 
        print("Wrong argument.")
        choice()

def choicewithoutdouble() :
    choice = input("What do you want? (h for Hit, s for Stand) : ").lower()

    if choice == "h" : 
        hit()
    elif choice == "s" :
        print("Stand")
        stand()
    else : 
        print("Wrong argument.")
        choice()


def buttons():
    global hit_button
    global stand_button
    
    hit_button = tk.Button(frame,
                       text="HIT",
                       command=hit)
    hit_button.pack(side=tk.LEFT)
    
    stand_button = tk.Button(frame,
                       text="STAND",
                       command=stand)
    stand_button.pack(side=tk.LEFT)


def newgame() :
    global player_deck
    global croupier_deck
    global decklist
    global player_score
    global croupier_score
    
    
    spaceforresult.destroy()
    buttons()
    
    
    player_score = 0
    croupier_score = 0
    
    decklist = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'] * 4
    
    player_deck = random.choices(decklist, k=2)
    
    for card in player_deck :
        decklist.remove(card)
        if card != 'A' and card != 'J' and card != 'K' and card != 'Q' and card != 'J' :
            player_score += int(card)
        elif card == 'A' :
            player_score += 11
        else :
            player_score += 10
        
    croupier_deck = random.choices(decklist, k=1)
    
    for card in croupier_deck :
        if card != 'A' and card != 'J' and card != 'K' and card != 'Q' and card != 'J' :
            croupier_score += int(card)
        elif card == 'A' :
            croupier_score += 11
        else :
            croupier_score += 10
    
    for card in player_deck :
        decklist.remove(card)
        
    update_decks()

    
def update_decks():
    player_deck_label['text'] = f"Player's deck: {', '.join(player_deck)}"
    croupier_deck_label['text'] = f"Croupier's deck: {', '.join(croupier_deck)}"



newgame()



new_game_button = tk.Button(frame, 
                   text="NEW GAME", 
                   fg="red",
                   command=newgame)
new_game_button.pack(side=tk.LEFT)


root.mainloop()


choice()