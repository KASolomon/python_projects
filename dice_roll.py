# use a do while loop for the application
# ask the user whether to roll the dice
# while the response !== n || N, loop
# In the loop, if response === y or Y, generate 2 random numbers between 1 and 6 (inclusive)
# Print the numbers and repeat
# Print Thank you message after the loop and end the program


from random import randint


while(True):
    response = input("Roll the dice? (y/n).  ").lower()
    if response == 'y':
        random1 = randint(1,6)
        random2 = randint(1,6)
        print(f'({random1}, {random2})') 
        continue
    elif response == 'n':
        break
    else :
        print("Invalid input. Only 'y' and 'n' allowed.")
        continue

print("Thanks for playing!")