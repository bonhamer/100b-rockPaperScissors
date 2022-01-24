#!python3
import random


"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""
"""
from x01_player import *
from x02_computer import *
from x03_winner import *
"""
def main():
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
  main()
  main1 = main
  print(main1)

