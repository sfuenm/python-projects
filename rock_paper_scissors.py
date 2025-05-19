from idlelib.debugobj import myrepr

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]
choice_names = ["Rock", "Paper", "Scissors"]
import random
print("Welcome to Rock, Paper, Scissors!")
your_choice = int(input("Pick 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

# if your_choice == 0:
#     print("You chose: Rock\n")
#     print(rock)
# elif your_choice ==1:
#     print("You chose: Paper\n")
#     print(paper)
# elif your_choice ==2:
#     print("You chose: Scissors\n")
#     print(scissors)
# else:
#     print("You didn't choose a number between the range.")
#     exit()

if your_choice not in [0, 1, 2]:
    print("You didn't choose a number between the range.")
    exit()

print(f"You chose: {choice_names[your_choice]}\n")
print(choice_list[your_choice])

# if computer_choice == 0:
#     print(f"Computer chose: Rock\n")
#     print(rock)
# elif computer_choice ==1:
#     print("Computer chose: Paper\n")
#     print(paper)
# elif computer_choice ==2:
#     print("Computer chose: Scissors\n")
#     print(scissors)
# else:
#     print()

computer_choice = random.randint(0,2)
print(f"Computer Chose: {choice_names[computer_choice]}")
print(choice_list[computer_choice])


if your_choice == computer_choice:
    print("Tie")
elif your_choice == 0 and computer_choice ==1:
    print("Computer Wins")
elif your_choice == 1 and computer_choice == 2:
    print("Computer Wins")
elif your_choice == 2 and computer_choice ==0:
    print("Computer Wins")
else:
    print("You win")



