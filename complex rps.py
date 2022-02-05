import random
scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
scissors
'''

rock = '''
      .-.________
  ----/ \ )_______)
      (  (/()___)
          ()__)
  ----\___()_) rock

'''
paper = '''
          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'paper
          
'''

game_pics = [rock, paper, scissors]
user = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(f"You chose: {game_pics[user]}")

comp = random.randint(0, 2)
print(f"Computer chose: {game_pics[comp]}")

if user >= 3 or user < 0:
  print("Crazy!  That was an invalid number")
elif user == 0 and comp == 2:
  print("You win!")
elif comp == 0 and user == 2:
  print("You lose!")
elif user > comp:
  print("You win!")
elif comp > user:
  print("You lose!")
elif comp == user:
  print("There was a tie between you two!")
