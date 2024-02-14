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
            case "1":
                while True:
                    print("Use which attack?")
                    print()
                    print("1. Quick attack - no ap")
                    print("2. Heavy blow")
                    print("3. Back")
                    match input("action >> "):
                        case "1":
                            attack_res = player.attack(1,emeny)
                            if attack_res[0]:
                                print("you attack!")
                                print(f"delt {attack_res[1]} damage")
                                break
                            else:
                                print("not enough ap!")
                        case "2":
                            attack_res = player.attack(1,emeny)
                            if attack_res[0]:
                                print("you attack!")
                                print(f"delt {attack_res[1]} damage")
                                break
                            else:
                                print("not enough ap!")
                        case "3":
                            break
                        case _:
                            print("not an option.")
            case "2":
                player.defend()
                print("You started blocking...")
            case "3":
                print("No items!")
            case "4":
                print("Can't flee this fight!")
            case _:
                print("please choose an option")    
def emeny_turn():
    pass

def start():
    print("A Foe Aproches!!!")
    while True:
        pass


