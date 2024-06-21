#SWERTRES
from random import randint                                              # from random module import the randint function

number = [int(input(f"ENTER NUMBER {i+1}: ")) for i in range(3)]        # the user input the three enter numbers to store them in a list
gens = [randint(0, 9) for _ in range(3)]                                # To generate the 3 random numbers  in 0 and 9 to stoe them in a list 

print(f"BET: {number}")                                                 # Print list of the result of the user entered the three number
print(f"RESULT: {gens}")                                                # Print the list of the three random numbers generated

if number == gens:                                                      # checking the users number if exactly the match the generated the numbers
    print("You Win!")                                                   # Print "you win" if the number are exactly to match the generated numbers
elif sorted(number) == sorted(gens):                                    # Checking if the sorted list number of the user  are matches the sorted list of generated numbers
    print("You partially win!")                                         # Print "You Partially Win" if the two numbers are the same matches in generated numbers
else:
    print("You lose!")                                                  # Print the result ("You Lose") if the three number are not exaclty matches in generated numbers