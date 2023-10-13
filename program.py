# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""
for i in range(32):
  result = ""
  if (i+1)%3 == 0:
    result = "Fizz"
  if (i+1)%5 == 0:
    result = result + "Buzz"
  if result == "":
    result = str(i+1)

print(result + "\n")
