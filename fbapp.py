# Global variables
firstText = "Check"
secondText = "Mate"
jackpotText = "CheckMate"
firstNumberVerifier = 3
secondNumberVerifier = 5
singleAward = 1
jackpotAward = 3

# *** Access colors in Dictionary *****
def colors(color):
    colorDict = {
        "black": "\u001b[30m",
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "gray": "\u001b[37m",
        "reset": "\u001b[0m"
    }
    return colorDict.get(color)

# # *** Access colors in a static class
# class Colors:
#     black = "\u001b[30m"
#     red = "\u001b[31m"
#     green = "\u001b[32m"
#     yellow = "\u001b[33m"
#     blue = "\u001b[34m"
#     magenta = "\u001b[35m"
#     cyan = "\u001b[36m"
#     gray = "\u001b[37m"
#     reset = "\u001b[0m"

#--- checking for integer and boundaries -------------- #
def isValidInput(num, limit):
    try:
        intNum = int(num)
        if intNum >= limit:
            return intNum
    except ValueError:
        return None

def settings(num, limit):
    response = isValidInput(num, limit)
    while response == None:
        print(f"{colors('red')} Number should be integer not less than {limit}! {colors('reset')}")
        response = isValidInput(input(f"Enter a number again (integer not less than {limit}): "), limit)
    return response

def fizzBuzz(num, list):
    if num not in list:
        if (num % 3 == 0) and (num % 5 == 0):
            print(f"{colors('yellow')} {jackpotText} {colors('reset')}")
            return 2
        elif (num % 3 == 0):
            print(f"{colors('yellow')} {firstText} {colors('reset')}")
            return 1
        elif (num % 5 == 0):
            print(f"{colors('yellow')} {secondText} {colors('reset')}")
            return 1
        else:
            print(f"{colors('red')}TIME's UP! {num} is not a multiple of {firstNumberVerifier} or {secondNumberVerifier} {colors('reset')}")
            return None
    else:
        print(f"{colors('red')} TIME's UP! You already played {num} {colors('reset')}")
        return None

def playGame():
    print(f"""{colors('gray')} 
    RULES OF THE GAME:
    IF INPUT IS A MULTIPLE OF {firstNumberVerifier}, PLAYER SCORES {singleAward} POINT & PROGRAM DISPLAYS {firstText}.
    IF INPUT IS A MULTIPLE OF {secondNumberVerifier}, PLAYER SCORES {singleAward} POINT & PROGRAM DISPLAYS {secondText}
    IF INPUT IS A MULTIPLE {firstNumberVerifier} AND {secondNumberVerifier}, PLAYER SCORES {jackpotAward} POINTS & PROGRAM DISPLAYS {jackpotText}
    BUT IF INPUT IS NOT A MULTIPLE, THE PLAYER LOSES SESSION TO PLAY
    AND IF THE INPUT IS A REPEAT, THE PLAYER LOSES SESSION TO PLAY
       {colors('reset')} """)

    playerList = []
    scoreList = []
    playedNumList = []
    startNum = settings(input(f"Enter start of range  to {jackpotText} (integer above 0): "), 1)
    numPlayers = settings(input("Enter number of Players (integer above 0): "), 1)

    def get_surfix(num):
        surfix = "st" if (num != 11 and num % 10 == 1) \
            else ("nd" if (num != 12 and num % 10 == 2)
                  else ("rd" if (num != 13 and num % 10 == 3)
                        else "th"))
        return surfix()

    count = 1
    while count <= numPlayers:
        # Ternary expression (setting surfix Ex. 1st, 2nd, 3rd, 4th, .... 21st 22nd )
        surfix = get_surfix(count)

        text = f"{count}{surfix}" if numPlayers > 1 else ""

        player = input(f"Enter name of {text} player: ")
        playerList.append(player)
        scoreList.append(0)
        playedNumList.append([])
        count += 1
    for i in range(len(playerList)):
        print(f"\n{colors('cyan')}{playerList[i]} IS PLAYING NOW {colors('reset')}")
        num = settings(input(f"Enter a number to {jackpotText} (integer not less than {startNum}): "), startNum)
        res = fizzBuzz(num, playedNumList[i])
        if res is not None:
            scoreList[i] += res
            playedNumList[i].append(num)

        while res is not None:
            num = settings(input(f"Enter a number to {jackpotText} (integer not less than {startNum}): "), startNum)
            res = fizzBuzz(num, playedNumList[i])
            if res is not None:
                scoreList[i] += res
                playedNumList[i].append(num)

    print("-" * 60)
    print(F"\n{colors('cyan')}*** SCRORE BOARD ***{colors('reset')}")
    winnerList = []
    maxScore = max(scoreList)
    for i in range(len(scoreList)):
        if scoreList[i] == maxScore:
            winnerList.append(playerList[i])

    if numPlayers > 1:
        if len(winnerList) > 1:
            print(f"\n{colors('blue')} DRAW GAME FOR THE FOLLOWING:{colors('reset')}")
            for i in range(len(winnerList)):
                print(winnerList[i])
        else:
            print(f"\n{colors('magenta')}The Winner is {winnerList[0]} {colors('reset')}")

        for i in range(len(playerList)):
            print(f"\n{playerList[i]}: {scoreList[i]} Points")
            print(f"Played: {playedNumList[i]}")
    else:
        print(f"\n{colors('magenta')}{winnerList[0]}, You scored {scoreList[0]} Points {colors('reset')}")
        print(f"Played: {playedNumList[0]}")

playGame()
