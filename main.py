import game_class
import game_solo
import modele


def start_game_solo():
    jeux = game_solo.start_game() 
    while True:
        data_input = (next(jeux))
    
def start_game_AI():
    i=0
    while True:
        instance = game_class.SnakeGame(1000)
        game = instance.stat_game()
    
        while not instance.done:
            data_input = instance.stat_game()   
            print(i, data_input)
            i+=1
    


    # data_input = (next(game))
    # print(data_input)
    
    

def transit_data():
    pass

def transit_instruction():
    pass

def monitoring():
    pass



User_choice = int(input("""Voulez-vous : 
1 : jouer 
2 : lancer l'IA 
"""))

if User_choice == 1:
    start_game_solo()

elif User_choice == 2:

    start_game_AI()
    pass