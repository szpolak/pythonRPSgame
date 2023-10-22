import sys, random

win = 0
lose = 0
tie = 0
while True:
    print('%s Win, %s Lose, %s Tie' %(win, lose, tie))
    while True:
        print('enter you move: p(aper), (r)ock, (s)cissors pr (q)uit')
        move = input()

        if move == 'q':
            sys.exit()
        else:
            print(move)
        if move == 'p' or move =='r' or move =='s':
            break

    if move == 'p':
        print('PAPER VERSUS..')
    elif move == 'r':
        print('ROCK VERSUS...')
    elif move == 's':
        print('SCISSORS VERSUS...')

    computerChoice = random.randint(0 ,2)

    if computerChoice == 0:
        computerChoice = "PAPER"
    elif computerChoice == 1:
        computerChoice = "ROCK"
    elif computerChoice == 2:
        computerChoice = "SCISSORS"

    print(computerChoice)


    
    if move == 'p' and computerChoice == "PAPER":
        print("It's a tie!")
        tie += 1
    elif move == 'p' and computerChoice == "ROCK":
        print("You win")
        win += 1
    elif move == 'p' and computerChoice == "SCISSORS":
        print("You lose")
        lose += 1

    elif move == 'r' and computerChoice == "ROCK":
        print("It's a tie!")
        tie += 1
    elif move == 'r' and computerChoice == "SCISSORS":
        print("You win")
        win += 1
    elif move == 'r' and computerChoice == "PAPER":
        print("You lose")
        lose += 1

    elif move == 's' and computerChoice == "SCISSORS":
        print("It's a tie!")
        tie += 1
    elif move == 's' and computerChoice == "PAPER":
        print("You win")
        win += 1
    elif move == 's' and computerChoice == "ROCK":
        print("You lose")
        lose += 1
