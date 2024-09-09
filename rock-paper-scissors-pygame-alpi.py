import random

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
#kullanicidan alinan input degeri string oldugu icin hata aliyordum, bu yuzden input degerini int yaptim.
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if users_choice == 0:
    print(f"You chose: {rock}")
elif users_choice == 1:
    print(f"You chose: {paper}")
elif users_choice == 2:
    print(f"You chose: {scissors}")
else:
    print("Invalid choice! Please enter 0, 1, or 2.")
    exit()

print("------------------------------------")

computer_chose = random.randint(0,2)
if computer_chose == 0:
    print(f"Computer chose : {rock}")
elif computer_chose == 1:
    print(f"Computer chose : {paper}")
elif computer_chose == 2:
    print(f"Computer chose : {scissors}")

print("------------------------------------")

if computer_chose == users_choice:
    print("it looks like a draw :)")
elif (users_choice == 0 and computer_chose == 2) or (users_choice == 1 and computer_chose == 0) or (users_choice == 2 and computer_chose == 1):
    print("You win!")
else:
    print("Computer wins.")