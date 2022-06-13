#BLINK182 is a dice game where the player rolls the dice and contiously adds up their score until 
# a '1'' is rolled, in which case the player restarts at 0. The point of this application is to simulate 
# the game and see how often a player can expect to get 182 exactly (no more or less)
import random

TARGET_NUMBER = 182
NUMBER_OF_SIMULATIONS = 100000
DICE = [1, 2, 3, 4, 5, 6]
numberOfSuccesses = 0

for round in range(NUMBER_OF_SIMULATIONS):
  currentScore = 0
  while(1):
    rollValue = random.choice(DICE)
    if(rollValue == 1):
      break
    currentScore += rollValue
    if(currentScore == TARGET_NUMBER):
      numberOfSuccesses += 1
      break

print("Out of %d simulations, %d was reached %d times" %(NUMBER_OF_SIMULATIONS, TARGET_NUMBER, numberOfSuccesses))