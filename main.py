from art import *
from game_data import data
import random

print(logo)
print("Welcome to Higher Lower game")
print("You will have 2 celebrities to choose from")


celebA = random.randint(0, len(data))
celebB = random.randint(0, len(data))

# print(data[celebA,],)
# print(vs)
# print(data[celebB])

dataA = data[celebA]
print(dataA["name"])
print(vs)
dataB = data[celebB]
print(dataB["name"])
user = input("You have to guess which celeb has more follower A or B \n")


compare_dataA = dataA["follower_count"]
compare_dataB = dataB["follower_count"]

def game(compare_dataA, compare_dataB):
  count = 0
  if int(compare_dataA) > int(compare_dataB):
    if user == "A":
      count = count + 1
      print("You're correct")
      return count
    elif user == "B":
      print("Sorry you lost")
    else:
      print("Please choose correct option")

  elif int(compare_dataA) < int(compare_dataB):
    if user == "B": 
      count = count + 1
      print("You're correct")
      return count
    elif user == "A":
      print("Sorry you lost")
    else:
      print("Please choose correct option")
  else:
    print("Please try again")

game(compare_dataA, compare_dataB)

if game(compare_dataA, compare_dataB) > 0:
  print("You're correct")
  game(compare_dataA, compare_dataB) 
elif game(compare_dataA, compare_dataB) == 0:
  print("Please try again")
else:
  print("Sorry you lost")
  print(f"Your score is {game(compare_dataA, compare_dataB)}")


