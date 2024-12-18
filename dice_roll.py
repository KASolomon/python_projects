# use a do while loop for the application
# ask the user whether to roll the dice
# while the response !== n || N, loop
# In the loop, if response === y or Y, generate 2 random numbers between 1 and 6 (inclusive)
# Print the numbers and repeat
# Print Thank you message after the loop and end the program


from random import randint

counter = 0
while(True):
    response = input("Roll the dice? (y/n).  ").lower()
    if response == 'y':
        diceNumber = int(input("How many dice do you want to roll? "))
        diceResults = []
        for i in range(0,diceNumber):
            random1 = randint(1,6)
            diceResults.append(str(random1))
        
        print(f"({','.join(diceResults)})")
        counter+=1
        continue
    elif response == 'n':
        break
    else :
        print("Invalid input. Only 'y' and 'n' allowed.")
        continue

print(f"You rolled {counter} times!")
print("Thanks for playing!")