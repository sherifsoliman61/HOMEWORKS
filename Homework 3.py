combination = "SSNWES"
stepCounter = 0
lifeCounter = 3

game = True


class LostLife:
    if stepCounter == 10:
        lifeCounter - 1
        stepCounter = 0


class LifeCheck:
    if lifeCounter == 0:
        game = False
        print("Game Over, try again")


while game:
    print("You have entered the Maze, where would you like to go? (N,S,E,W)")
    if input() == "S":
        print("CORRECT")
        if input() == "S":
            print("CORRECT")
            if input() == "N":
                print("CORRECT")
                if input() == "W":
                    print("CORRECT")
                    if input() == "E":
                        print("CORRECT")
                        if input() == "S":
                            print("YOU HAVE ESCAPED THE MAZE")
                            game = False

                        else:
                            print("INCORRECT")
                    else:
                        print("INCORRECT")
                else:
                    print("INCORRECT")
            else:
                print("INCORRECT")
        else:
            print("INCORRECT")

    else :
        print("INCORRECT")