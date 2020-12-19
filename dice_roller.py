import random

def main():
  diceroll=2
  dice_sum=0
  for i in range(0, diceroll):
  	roll=random.randint(1,6)
  	dice_sum+=roll
  	print(f'You rolled a {roll}')
  print(f'You have rolled atotal of {dice_sum}')

if __name__== "__main__":
  main()