import living

player = living.Actor()
emeny = living.Actor()


def player_turn():
    print("It's your turn!")
    print(f"Foe's hp: {round(emeny.hp/emeny.maxhp, 4)*100}%")
    print("\n\n\n\n")
    print(f"Your HP: {player.hp}/{player.maxhp}")
    while True:
        print("1. Attack")
        print("2. Block")
        print("3. Items")
        print("4. RUN!")
        match input("action >> "):
            case 1:
                print("attack menu")
            case 2:
                print("Blocking") 
            case 3:
                print("no item")
            case 4:
                print("Can't flee this fight!")
            case _:
                print("please choose an option")    
def emeny_turn():
    pass

def start():
    print("A Foe Aproches!!!")
    while True:
        pass


