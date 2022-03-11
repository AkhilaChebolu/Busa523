#!/usr/bin/env python
# coding: utf-8

# 1. Write a program for flipping a coin 10,000 times and store the results in a list.
# After which, identify the number of streaks. (streak - a series of 5 or more
# heads or tails.
# 

# In[1]:


import random

coinList = [random.choice(["Head", "Tail"]) for toss in range(10000)]
print(coinList)

coinHeadStreak = 0
total_Head_Streak = 0

for i in coinList:
    if i == 'Head':
        coinHeadStreak += 1
        if coinHeadStreak >= 5:
            total_Head_Streak += 1
    else :
        coinHeadStreak = 0
print('The streak of >=5 heads in a list is : ', total_Head_Streak)
coinTailStreak = 0
total_Tail_Streak = 0
for j in coinList:
    if j == 'Tail':
        coinTailStreak += 1
        if coinTailStreak >= 5:
            total_Tail_Streak += 1
    else :
        coinTailStreak = 0
print('The Streak of >=5 tails in a list is : ', total_Tail_Streak)


# 2. Write a program to take user inputs (number of swords, diamonds, gold coins,
# ropes and potions) for a video game and store them in a dictionary. After
# which print the following output.
# 
# Inventory:
#     5 swords
#     10 diamonds
#     6 gold coins
#     3 rope
#     2 potions

# In[1]:


n = 5
user = dict()
for i in range(n):
    data = input('Enter key & value separated by ":" ')
    temp = data.split(':')
    user[temp[0]] = int(temp[1])
print("Inventory:")
for k in user:
    print(user[k], k)


# 3. Repeat question 1 using arrays.

# In[8]:


import random
import numpy as np

coinList = [random.choice(["Head", "Tail"]) for toss in range(10000)]
print(coinList)

# converting list to array, can use array = np.ravel(List) also
coinArray = np.asarray(coinList)
# printing my_array
print(coinArray)

coinHeadStreak = 0
total_Head_Streak = 0

for i in coinArray:
    if i == 'Head':
        coinHeadStreak += 1
        if coinHeadStreak >= 5:
            total_Head_Streak += 1
    else :
        coinHeadStreak = 0
print('The streak of >=5 heads in a array is : ', total_Head_Streak)
coinTailStreak = 0
total_Tail_Streak = 0
for j in coinArray:
    if j == 'Tail':
        coinTailStreak += 1
        if coinTailStreak >= 5:
            total_Tail_Streak += 1
    else :
        coinTailStreak = 0
print('The Streak of >=5 tails in a array is : ', total_Tail_Streak)


# 4. Create a game with the following instructions: 
#     a. There are 3 players and 10 iterations.
#     b. In each iteration, every player rolls a die.
#     c. The winner of the game is the one who has the highest score when rolls from all the iterations are added.

# In[8]:


import random

# Initialise player scores to 0
player1 = 0
player2 = 0
player3 = 0

# Repeat everything in this block 10 times
for i in range(10):
    # Generate random numbers between 1 and 6 for each player.
    player1_value = random.randint(1, 6)
    player2_value = random.randint(1, 6)
    player3_value = random.randint(1, 6)

    # Display the player1 values
    print("Player1:", player1_value)
    player1 = player1 + player1_value

    # Display the player2 values
    print("Player2:", player2_value)
    player2 = player2 + player2_value

    # Display the player3 values
    print("Player3:", player3_value)
    player3 = player3 + player3_value

print("player1_score is:", player1)
print("player2_score is:", player2)
print("player3_score is:", player3)

if player1 > player2 and player1 > player3:
    print("Player1 wins and his score is:", player1)
elif player2 > player1 and player2 > player3:
    print("Player2 wins and his score is:", player2)
elif p3 > player1 and player3 > player2:
    print("Player3 wins and his score is:", player3)
elif player1 == player2 == player3:
    print("Draw")
elif player1 == player2:
    print("player1,player2 wins")
elif player2 == player3:
    print("player2,player3 wins")
else:
    print("player1,player3 wins")

