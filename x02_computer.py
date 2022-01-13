#!python3
import random
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""

def computerChoice():
  
  list1 = ["Rock", "Paper", "Scissors"]
  x = random.choice(list1)
  if x == "Rock":
    x = 0
  if x == "Paper":
    x = 1
  if x == "Scissors":
    x = 2

  return x
  
  
  return value


if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
