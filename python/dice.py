#! /usr/bin/python
# A Python script to make sure the dice we're playing with are fair.
# A fair die should be random: that is, it should have a random 1/6
# chance of landing on each side with each roll. 
#
# You will need to define two functions: one to produce dice rolls
# and one to analyze those dice rolls for fairness. If the dice are
# fair, maybe you want to gamble; if the dice are rigged, maybe the
# dealer is trying to cheat you, and you should let your pistol
# do the talking.

# Module for dealing with random numbers.
import random


# Define a RollTheDice() function here. This function should take
# one argument (the number of times to roll the dice) and return
# a list of integers, one through six, representing rolls of the
# dice. The length of the list should be equal to the number of
# requested dice rolls.

def RollTheDice(num_rolls):
	rolls = []
	for i in range(num_rolls):
		rolls.

# Define an IsFair() function here. This function should take
# the list of dice rolls returned by RollTheDice and analyze
# them to see if the dice are fair. Return True if the dice
# are fair, and return False if the dice are rigged.  



def main():
  num_rolls = 10000  # Ten thousand dice rolls.
  rolls = RollTheDice(num_rolls)
  if IsFair(rolls):
    print 'The dice are fair. Show me the money.'
  else:
    print 'Hey! You are trying to cheat me!'


if __name__ == '__main__':
  main()