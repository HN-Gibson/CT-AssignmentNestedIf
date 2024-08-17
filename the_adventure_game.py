#Task 1: Code Correction 
    #You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

place = input("Choose a place: forest or cave? ")

#there are 4 spots where I added a second "=" to correct the comparison statement
    # Line 10, 12, 14 & 20
#also, line 14, the "else" should be an "elif"

if place == "forest": #added second "="
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree": #added second "="
        print("You found a bird's nest!")
    elif action == "cross a river": #added second "=" & and changed "else" to "elif"
        print("You found a boat!")

# Task 2: Setting the Scene
    # Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

elif place == "cave": #added second "="
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch": #made lighting a torch the conition for finding the treasure
        print("You find a hidden treasure!")
    if action == "proceed in the dark": #assigned proceeding in the dark an outcome
        print("You stumble into a deep hole and injure yourself!")

# Task 3: Default Path
    # If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?

else:
    pass # "pass" used in the else statement to provide a default path through the if statement and indicate the intention to return and add some other outcome options

print ("Your adventure continues!")