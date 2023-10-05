print("welcome to rock paper scissors simlulator")
rps = ['''_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|  ''', ''' _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.''','''               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     ''' ]
decision = input("rock paper or scissors\n")
print("you chose")
if decision == "rock":
    print(rps[2])
elif decision == "paper":
    print(rps[0])
elif decision == "scissors":
    print(rps[1])
else:
    print("wrong input")
import random
computer = random.choice(rps)
print("computer chose")
print(computer)
if decision == "rock" and computer == rps[1]:
    print("you win ")
elif decision == "rock" and computer == rps[2]:
    print("it is a draw")
elif decision == "rock" and computer == rps[0]:
    print("ah sorry bitch you lose")
elif decision =="paper" and computer == rps[2]:
    print("you win")
elif decision == "paper" and computer == rps[0]:
    print("it is a draw")
elif decision == "paper" and computer == rps[1]:
    print("you lose haaaa am d greatest")
elif decision == "scissors" and computer == rps[0]:
    print("you win")
elif decision == "scissors" and computer == rps[1]:
    print("it is a draw")
elif decision == "scissors" and computer == rps[2]:
    prints("itza drawwww")
else:
    print("you inputed wrong so i won cuz i inputed RIGHT")
