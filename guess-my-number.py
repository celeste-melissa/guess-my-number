print("Can you guess my number?")
my_number = 18
guess = 0
max_guess = 3
while guess < max_guess:
  number = int(input("Guess my number:"))
  guess += 1
  if number == my_number:
    print("Wow! You must be a mind reader!")
    break
  else:
      print("Nope! Good guess but that's not it.")
else:
      print("Sorry! Your out of chances.")
