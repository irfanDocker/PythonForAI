
# In this adventure game, the player takes on the role of an explorer searching
# for a legendary treasure hidden in an ancient land.
#
# The player must:
# - Navigate various challenges
# - Make strategic decisions
# - Overcome obstacles
#
# Each choice influences the storyline outcome:
# - Some bring the player closer to victory
# - Others lead to failure or restarts
#
# The game world includes multiple paths — such as a dense forest and a mysterious cave —
# each presenting unique, decision-based scenarios.

print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------Welcome to Adventure game-----------------------------------")
print("--------------------------------------------------------------------------------------------------")
print("\n")
print("\n")


# Task 2: Create a function to start the game
# Actions:
# • Define the function start_game() to display the game introduction
# • Ask the player for their name and store it in a variable
# • Provide the player with an initial choice (explore a forest or enter a cave)
# • Use GitHub Copilot to generate the function body
def start_game():
    print("You are an explorer on a quest to find the legendary treasure hidden in an ancient land.")
    player_name = input("What is your name, brave explorer? ")
    print(f"Welcome, {player_name}! Your adventure begins now.")
    print("You stand at a crossroads. Do you want to:")
    print("1. Explore the dense forest")
    print("2. Enter the mysterious cave")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        explore_forest()
    elif choice == '2':
        enter_cave()
    else:
        print("Invalid choice. Please try again.")
        start_game()

# Task 3: Create the forest path
# Actions:
# • Define the function forest_path() that describes the forest scenario
# • Provide the player with choices (follow a river or climb a tree)
# • Use an if-else structure to handle player choices

def forest_path():
    print("You venture into the dense forest. The trees are tall and the canopy is thick.")
    print("As you walk, you come across a fork in the path. Do you want to:")
    print("1. Follow the river")
    print("2. Climb a tree to get a better view")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        print("You follow the river and find a hidden waterfall with a cave behind it.")
        print("Inside the cave, you discover the legendary treasure! Congratulations!")
    elif choice == '2':
        print("You climb the tree but lose your footing and fall.")
        print("You are injured and must return home to recover. Game over.")
    else:
        print("Invalid choice. Please try again.")
        forest_path()



# Task 4: Create the cave path
# Actions:
# • Define the function cave_path() that describes the cave scenario
# • Provide the player with choices (light a torch or proceed in the dark)
# • Use conditionals to determine the outcome

def cave_path():
    print("You enter the mysterious cave. It's dark and eerie.")
    print("As you proceed, you must decide how to navigate. Do you want to:")
    print("1. Light a torch")
    print("2. Proceed in the dark")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        print("With the torch lit, you see a path leading deeper into the cave.")
        print("You find the legendary treasure hidden in a chamber! Congratulations!")
    elif choice == '2':
        print("You stumble in the dark and fall into a pit.")
        print("You are trapped and must call for help. Game over.")
    else:
        print("Invalid choice. Please try again.")
        cave_path()

# Task 5: Run the adventure game
# Actions:
# • Call start_game() to begin the adventure
# • Ensure the program runs in a loop until the player completes their journey
# • Provide an option to restart the game after completion

def start_game():
    print("You are an explorer on a quest to find the legendary treasure hidden in an ancient land.")
    player_name = input("What is your name, brave explorer? ")
    print(f"Welcome, {player_name}! Your adventure begins now.")
    print("You stand at a crossroads. Do you want to:")
    print("1. Explore the dense forest")
    print("2. Enter the mysterious cave")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        forest_path()
    elif choice == '2':
        cave_path()
    else:
        print("Invalid choice. Please try again.")
        start_game()


# Result
# The result will be an adventure_game.py script that runs a fully functional text-based
# adventure game. The final project (script and report) should be submitted on the LMS.
while True:
    start_game()
    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() != 'yes':
        print("Thank you for playing! Goodbye!")
        break
def explore_forest():
    forest_path()