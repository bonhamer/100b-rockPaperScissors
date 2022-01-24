#!python3
import random

from x01_player import *
from x02_computer import *
from x03_winner import *
"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""
"""
from x01_player import *
from x02_computer import *
from x03_winner import *
"""
while True:
  x = playerChoice()
  y = computerChoice()
  z = playerWins(y,x)

  if x == 0:
    if y == 0:
      print("Stalemate")
    elif y == 1:
      print("you won")
    elif y ==2:
      print("You lost")
  elif x == 1:
    if y == 0:
      print("you won")
    elif y == 1:
      print("stalemate")
    elif y == 2:
      print("you lost")
  elif x == 2:
    if y == 0:
      print("you lost")
    elif y== 1:
      print("you won")
    elif y == 2:
      print("stalemate")


