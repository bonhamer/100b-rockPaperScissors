#!python3
import random

'''
Create a function that takes 2 input parameters:
int: computer choice
int: player choice

the choices correspond to:
0: rock
1: paper
2: scissors

Based on the classic rules for Rock Paper Scissors, the return value should be an integer value that indicates if the player is the wins, loses or ties
Output:
-1: player loses
0: tie
1: player wins
'''

def playerWins(computer,player):
  
  list1 = ["Rock", "Paper", "Scissors"]
  x = random.choice(list1)
  if x == "Rock":
    x = 0
  if x == "Paper":
    x = -1
  if x == "Scissors":
    x = -2
    
  list1 = ["Rock", "Paper", "Scissors"]
  P = random.choice(list1)
  if P == "Rock":
    P = 0
  if P == "Paper":
    P = 1
  if P == "Scissors":
    P = 2

  y = x + P

  return y


  



if __name__ == "__main__":
  assert playerWins(1,1) == 0
  assert playerWins(1,0) == -1
  assert playerWins(1,2) == 1
  assert playerWins(2,1) == -1
  
