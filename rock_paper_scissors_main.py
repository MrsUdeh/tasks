import random

print("Let's play Rock, Paper, Scissors \n"
"R for rock \n"
"P for paper \n"
"S for scissors")
game_options = ["R", "P", "S"]
Player = input("Enter a choice (R, P, S): ")
CPU = random.choice(game_options)
print(f"\nYou choose{Player}, computer chose {CPU}.\n")

while Player not in game_options:
    print("Please enter a valid option")
    continue 
    
if Player == CPU:
    print("It is a tie")
elif Player == "R":
    if CPU == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif Player == "P":
    if CPU == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif Player == "S":
    if CPU == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
