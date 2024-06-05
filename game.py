#-> Modules
import random as rd

#<<---Rock, Paper or Scissor Game--->>#

#-> Options
options = ['Rock', 'Paper', 'Scissor']

#-> Functions
def result(pcopt, usopt, pwins, uswins):
    botwins = pwins
    playerwins = uswins

    if usopt == pcopt:
        print(f"Draw! -> {usopt} vs {pcopt}")
        print(f"User: {playerwins}, PC: {botwins}\n")
        return botwins, playerwins
    elif usopt == 'Rock' and pcopt == 'Scissor':
        print(f"User wins! -> {usopt} vs {pcopt}")
        playerwins += 1
        print(f"User: {playerwins}, PC: {botwins}\n")
        return botwins, playerwins
    elif usopt == 'Paper' and pcopt == 'Rock':
        print(f"User wins! -> {usopt} vs {pcopt}")
        playerwins += 1
        print(f"User: {playerwins}, PC: {botwins}\n")
        return botwins, playerwins
    elif usopt == 'Scissors' and pcopt == 'Paper':
        print(f"User wins! -> {usopt} vs {pcopt}")
        playerwins += 1
        print(f"User: {playerwins}, PC: {botwins}\n")
        return botwins, playerwins
    else:
        print(f"PC wins! -> {usopt} vs {pcopt}")
        botwins += 1
        print(f"User: {playerwins}, PC: {botwins}\n")
        return botwins, playerwins

def run():
    #-> Title
    print(f"\n{'*'*20}Rock, Paper or Scissor Game{'*'*20}")
    print(f"#<-Wins the one with 3 victories->#\n")

    #-> Wins
    pc_wins = 0
    user_wins = 0

    #-> Round
    round = 0

    #-> Result
    while True:
        pc = rd.choice(options)

        if pc_wins == 3:
            print(f"PC wins! -> {pc_wins} - {user_wins}")
            break
        elif user_wins == 3:
            print(f"User wins! -> {user_wins} - {pc_wins}")
            break

        round += 1
        print(f"\n******Round {round}******")
        user = input("Rock, Paper or Scissor? -> ").title()

        if user == options[0] or user == options[1] or user == options[2]:
            pc_wins, user_wins = result(pc, user, pc_wins, user_wins)
        else:
            print("Choose a correct option please")

#Run main
if __name__ == '__main__':
    run()