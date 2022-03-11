#!/usr/bin/env python
# coding: utf-8

# # Question 1
# - Write a program which randomly selects a number between 1 and 20. The user is then given 5 chances to guess the number correctly to win.

# In[1]:


import random

guessesTaken = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 5:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)


# # Question 2
# - Make the following changes to the above program.
#         - After each guess, print if the next guess should be lower or higher. 
#         - For example, if the computer selection is 10 and the user input is 6, print guess is a higher value.

# In[8]:


import random

guessesTaken = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 5:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print('Your guess is too low.') 

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)


# # Question 3
# - Write a program for “Rock-Paper-Scissors-Lizard-Spock”.

# In[10]:


import random

print("Enter your move: Rock, Paper, Scissors, Lizard or Spock")
user = input()

number = random.randint(1,5)

if number == 1:
    computer = "Rock"
elif number == 2:
    computer = "Paper"
elif number == 3:
    computer = "Scissors"
elif number == 4:
    computer = "Lizard"
elif number == 5:
    computer = "Spock"
    
if user == computer:
    print("It's a Tie!")
elif user == "Rock" and computer == "Spock":
    print("You Win!")
elif user == "Paper" and computer == "Rock":
    print("You Win!")
elif user == "Scissors" and computer == "Paper":
    print("You Win!")
elif user == "Lizard" and computer == "Scissors":
    print("You Win!")
elif user == "Spock" and computer == "Lizard":
    print("You Win!")
    
elif user == "Rock" and computer == "Lizard":
    print("You Lose!")
elif user == "Paper" and computer == "Spock":
    print("You Lose!")
elif user == "Scissors" and computer == "Rock":
    print("You Lose!")
elif user == "Lizard" and computer == "Paper":
    print("You Lose!")
elif user == "Spock" and computer == "Scissors":
    print("You Lose!")

else:
    print("Invalid Entry")

