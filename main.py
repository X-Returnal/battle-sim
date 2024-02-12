from os import system as sys
import battle
while True:
    print("welc")
    print("1. star gam")
    print("2. lod gmea")
    print("3. quit drugs")
    match input(">> "):
        case "1":
            battle.start()
        case "2":
            print("make a gome to opla")
        case "3":
            print("no more .")
            exit(0)
        case _:
            sys("cls")
            print("make a correct dicison")
