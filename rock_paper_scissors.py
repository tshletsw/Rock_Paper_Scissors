#import getpass as input ensures that the user's input is not visible in the console
from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")

#keep score for each win
player1Score = 0
player2Score = 0

#this loop will ensure that the game will continue until one
#player reaches 3 wins
while player1Score < 3 or player2Score < 3:
  #get player1's input and capitalize it if it is lowercase
  player1 = input("Player 1, select your move (R, P or S): ").capitalize()

  #we use a counter and a while loop to ensure that our user input is either R, P or S
  n = 0
  while n == 0:
    if player1 == "R" or player1 == "P" or player1 == "S":
      n = 1
    else:
      player1 = input(
          "Player 1: invalid move, please reselect your move (R, P or S): "
      ).capitalize()

  player2 = input("Player 2, select your move (R, P or S): ").capitalize()
  n = 0
  while n == 0:
    if player2 == "R" or player2 == "P" or player2 == "S":
      n = 1
    else:
      player2 = input(
          "Player 2: invalid move, please reselect your move (R, P or S): "
      ).capitalize()

  #game logic: checks if player2's input is the same as player1's input or not, and uses
  #comparison operators to determine the winner
  if player1 == "R":
    if player2 == "R":
      print("It's a tie!")
    elif player2 == "P":
      print("Player 2 wins!")
      player2Score += 1
    elif player2 == "S":
      print("Player 1 wins!")
      player1Score += 1
    else:
      print("Invalid move Player 2!")

  if player1 == "P":
    if player2 == "R":
      print("Player 1 wins!")
      player1Score += 1
    elif player2 == "P":
      print("It's a tie!")
    elif player2 == "S":
      print("Player 2 wins!")
      player2Score += 1
    else:
      print("Invalid move Player 2!")

  if player1 == "S":
    if player2 == "R":
      print("Player 2 wins!")
      player2Score += 1
    elif player2 == "P":
      print("Player 1 wins!")
      player2Score += 1
    elif player2 == "S":
      print("It's a tie!")
    else:
      print("Invalid move Player 2!")
  
  #if one of the players reaches 3 wins, the loop will break  
  if player1Score == 3:
    print("Player 1 wins the game!")
    break
  elif player2Score == 3:
    print("Player 2 wins the game!")
    break
  #if not, the loop will ocntinue  
  else:
    continue
#once the loop breaks, the game will exit
exit()
