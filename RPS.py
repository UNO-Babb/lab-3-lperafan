#RPS.py
#Name:
#Date:
#Assignment: Rock Paper Scissors (RPS.py)
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain =="Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.
    computer = random.choice( ["R", "P", "S"] )
    player = input("Pick your weapon (R, P, S): ")
    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection

  #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")


    if player == "R":
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    else:
      print("Player chose Scissors")

    if player == computer:
      print("Tie")
      ties += 1
    elif (player == "R" and computer == "S") or \
         (player == "S" and computer == "P") or \
         (player == "P" and computer == "R"): 
      print("You Win!") 
      wins += 1
    else:
      print("Computer wins.") 
      losses += 1

    #Ask the user if they would like to play again.
    playAgain = input("Do you want to play again? (Y/N): ")


  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
