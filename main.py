import random

guessesTaken = 0
minNumber = 1
maxNumber = 20

number = random.randint(minNumber, maxNumber)
print("Hello! What is your name?:  ")
username = input("Enter your username: ")
print("Well, " + username + ' . I am thinking in a number between ' + str(minNumber)  +  ' and '  +  str(maxNumber))


while guessesTaken < 6:
  print("Take a guess: ")
  guess = input()
  guess = int(guess)

  guessesTaken = guessesTaken + 1

  if guess < number:
    print("Your guess is too Low.")
  if guess > number:
    print("Your guess is too High")
  if guess == number:
    break;

if guess == number:
  guessesTaken = str(guessesTaken)
  print("Good Job. " + username + ' ! you guesses my number in ' + guessesTaken + ' guesses')
if guess != number:
  number = str(number)
  print("No the number I was thinking of was " + number)