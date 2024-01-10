#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"
import random
print("Welcome to Rock, Paper, Scissors!")
print("Choose rock(1), peper(2) or Scissors(3)")
my_choose = int(input("Your choose:"))
computer_choose = (random.randint(1, 3))
print ("My choose:" + str(computer_choose))
if my_choose == 1 and computer_choose == 2:
    print(" you win, you have rock, but me - scissors.")
elif my_choose == 1 and computer_choose == 3:
    print(" you lose, you have rock, but me - papar.")
elif my_choose == 1 and computer_choose == 1:
    print(" This is draw.")

elif my_choose == 2 and computer_choose == 3:
    print(" you win, you have scissors, but me - papar.")
elif my_choose == 2 and computer_choose == 1:
    print(" you lose, you have scissors, but me - rock.")
elif my_choose == 2 and computer_choose == 2:
    print(" This is draw.")

elif my_choose == 3 and computer_choose == 1:
    print(" you win, you have papar, but me - rock.")
elif my_choose == 3 and computer_choose == 2:
    print(" you lose, you have papar, but me - scissors.")
elif my_choose == 3 and computer_choose == 3:
    print(" This is draw.")
print("Thunk you for game:)")



