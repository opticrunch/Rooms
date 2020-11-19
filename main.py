# Stephen Royka
# ROOMS: FIVE COLORS is a text based puzzle adventure game

# Define the class player
class Player:
    """Class to store all player attributes and eliminate need for
    global variables"""
    name = str()
    age = int()
    difficulty = str()
    current_room = str('Blue')
    health = int()
    have_red_key = bool(0)
    win = bool(0)
    game_start = bool(0)


# Define the room class
class Room:
    """Class to store attributes of the rooms"""
    lock = bool(0)
    bulb = 'OFF'
    bulb_power = bool(0)
    wall_code = int()


# Function to print the HUD and room map current_room value
def print_room_hud(player):
    print('_______________________________________________')
    print('PLAYER: ' + player.name + ' | AGE: ' + str(player.age)
          + ' | ROOM: ' + player.current_room + ' | HEALTH: '
          + str(player.health))
    print('      _________')
    if player.current_room == "Green":
        print(' MAP |    X    |  COMPASS   N')
    else:
        print(' MAP |         |  COMPASS   N')
    print('     |___   ___|          W + E')
    print('|----|         |----|       S')
    if player.current_room == "Blue":
        print('|         X         |')
    elif player.current_room == "Yellow":
        print('| X                 |')
    elif player.current_room == "Red":
        print('|                 X |')
    else:
        print('|                   |')
    if player.have_red_key == 1:
        print('|----|___   ___|----|    RED KEY')
        print('     |         |          0--m')
    elif player.current_room == "Purple":
        print('|----|___   ___|----|')
        print('     |    X    |')
    else:
        print('|----|___   ___|----|')
        print('     |         |')
    print('     |___   ___|')
    print('')


# Function to print the room info based on the current_room value
def get_room_info(player, blue_room, yellow_room, green_room, red_room):
    if player.current_room == "Blue":
        print('You are in a room with blue walls.')
        print('There is a blue light bulb on the wall switched to '
              + blue_room.bulb + '.')
        print('There is a number ' + str(blue_room.wall_code)
              + ' scribbled on the wall.')
        print('There is a green door to the North, a yellow door to the West,')
        print('a red door to the East, and a purple door to the South.')
        print('______________ENTER A SELECTION______________')
        print('       1) Go North            5) Light bulb')
        print('2) Go West    3) Go East')
        print('       4) Go South')
    elif player.current_room == "Yellow":
        print('You are in a room with yellow walls.')
        print('There is a yellow light bulb on the wall switched to '
              + yellow_room.bulb + '.')
        print('There is a number ' + str(yellow_room.wall_code)
              + ' scribbled on the wall.')
        print('There is an electrical device on the wall that might'
              ' supply power somewhere.')
        print('There is a blue door to the East.')
        print('______________ENTER A SELECTION______________')
        print('       1)                     5) Light bulb')
        print('2)            3) Go East      6) Device')
        print('       4)')
    elif player.current_room == "Green":
        print('You are in a room with green walls.')
        print('There is a number ' + str(green_room.wall_code)
              + ' scribbled on the wall.')
        if player.have_red_key == 0 and red_room.lock == 0:
            print('There is a RED KEY on the ground.')
        print('There is a blue door to the South.')
        print('______________ENTER A SELECTION______________')
        if player.have_red_key == 0 and red_room.lock == 0:
            print('       1)                     5) Red key')
        else:
            print('       1)')
        print('2)            3)')
        print('       4) Go South')
    elif player.current_room == "Red":
        print('You are in a room with red walls.')
        print('There is a number ' + str(red_room.wall_code)
              + ' scribbled on the wall.')
        print('There is a red light bulb on the wall switched to '
              + red_room.bulb + '.')
        print('There is a blue door to the West.')
        print('______________ENTER A SELECTION______________')
        print('       1)                     5) Light bulb')
        print('2) Go West    3)')
        print('       4)')
    elif player.current_room == "Purple":
        print('You are in a room with purple walls.')
        print('There is a red light bulb on the wall switched to '
              + red_room.bulb + '.')
        print('There is a blue door to the North and a door'
              ' labeled EXIT to the South.')
        print('______________ENTER A SELECTION______________')
        print('       1) Go North')
        print('2)            3)')
        print('       4) Exit')


# Function that gets player input and makes sure it is an integer
def get_player_input():
    player_choice = input()
    while isinstance(player_choice, int) == 0:
        try:
            player_choice = int(player_choice)
        except ValueError:
            print('Enter a valid selection')
            player_choice = input()
    return player_choice


# Function that prints the win screen (takes an argument)
def get_win_screen(player):
    # Win screen out of game loop
    print(' ______________________________________')
    print('     ____________  CONGRATULATIONS!')
    print('    |    ROOMS   |             YOU')
    print('    |     __     |     \o/   ESCAPED')
    print('    |    |  |    |      |    WITH ' + str(player.health))
    print('    |    |  |    |     / \   HEALTH')
    print(' ______________________________________')
    print('Great job, ' + player.name + '!')

    # Creates a file and writes to it
    certificate = open('CertificateOfVictory.txt', 'w')
    certificate.write('This certificate is proof that\n' + player.name +
                      '\nescaped the mysterious\nROOMS: Five Colors'
                      '\non ' + player.difficulty + ' difficulty.'
                      '\n ______________________________________'
                      '\n     ____________  CONGRATULATIONS!'
                      '\n    |    ROOMS   |             YOU'
                      '\n    |     __     |     \o/   ESCAPED'
                      '\n    |    |  |    |      |    WITH '
                      + str(player.health) +
                      '\n    |    |  |    |     / \   HEALTH'
                      '\n ______________________________________')


# Define the play game function
def play_game():

    # Initialize the player and room classes
    player = Player()
    blue_room = Room()
    yellow_room = Room()
    green_room = Room()
    red_room = Room()
    purple_room = Room()

    # Title screen loop start
    while player.game_start == 0:

        # Print the title screen utilizing the * and + string operators
        print('-' * 19)
        print('|  R  O  O  M  S  |')
        print('|   Five Colors   |')
        print('-' * 19 + '\n')
        print('Enter a number to select an option:')
        print('1) Start     2) Help')
        home_screen_selection = get_player_input()
        if home_screen_selection == 2:
            print('In ROOMS you will navigate five rooms')
            print('with the goal of reaching the exit.')
            print('You must escape before your health runs out.')
            print('Health is displayed at the top of the HUD.')
            print('Enter a number and press ENTER to select')
            print('an option. Good luck!\n')
            input('Press ENTER to continue')
        elif home_screen_selection == 1:
            player.game_start = 1
        else:
            print('Enter a valid selection\n')

    # Get player name use later
    print('Enter your name:')
    player.name = str(input())

    # Get player age for use later and check to make sure it is an integer
    print('Enter your age:')
    player.age = input()
    while isinstance(player.age, int) == 0:
        try:
            player.age = int(player.age)
        except ValueError:
            print('Please enter a whole number: ')
            player.age = input()

    # Returns game_start to 0 for difficulty setting loop
    player.game_start = 0

    # Prompts for difficulty setting (determines starting health)
    while player.game_start == 0:
        print('Choose a difficulty setting:')
        print('1) Easy    2) Medium  3) Hard')
        difficulty_choice = get_player_input()
        if difficulty_choice == 1:
            player.health = 50
            player.game_start = 1
            player.difficulty = 'EASY'
            print('You got this!\n')
            input('Press ENTER to continue')
        elif difficulty_choice == 2:
            player.health = 35
            player.game_start = 1
            player.difficulty = 'MEDIUM'
            print('Good luck!\n')
            input('Press ENTER to continue')
        elif difficulty_choice == 3:
            player.health = 20
            player.game_start = 1
            player.difficulty = 'HARD'
            print('Uh oh... I hope you make it!\n')
            input('Press ENTER to continue')
        # Secret to get the max starting health
        elif difficulty_choice == 42:
            player.health = 100
            player.game_start = 1
            player.difficulty = 'CHEATER'
            print('Wait... How did you know that? MAX HEALTH!!\n')
            input('Press ENTER to continue')
        else:
            print('Enter a valid selection\n')

    # Generate code numbers that will be on walls using player age
    # Utilizes ** (exponent), / (division), // (floor division), % (modulus)
    blue_room.wall_code = int((player.age ** 3 / 2) // 1000 % 10)
    yellow_room.wall_code = int((player.age ** 3 / 2) // 100 % 10)
    green_room.wall_code = int((player.age ** 3 / 2) // 10 % 10)
    red_room.wall_code = int((player.age ** 3 / 2) % 10)

    # Start of the game loop that checks for win condition and health
    while player.win == 0 and player.health > 0:

        # Door lock checks
        if blue_room.bulb and yellow_room.bulb == 'ON'\
                and red_room.bulb == 'OFF':
            green_room.lock = 1
        else:
            green_room.lock = 0
        if blue_room.bulb and red_room.bulb == 'ON'\
                and yellow_room.bulb == 'OFF':
            purple_room.lock = 1
        else:
            purple_room.lock = 0

        # Print the HUD
        print_room_hud(player)
        get_room_info(player, blue_room, yellow_room, green_room, red_room)

        # Blue room events
        if player.current_room == "Blue":
            player_input = get_player_input()
            if player_input == 1:
                if green_room.lock == 1:
                    player.current_room = "Green"
                    print('You go through the green door')
                else:
                    print('The door is locked')
            elif player_input == 2:
                player.current_room = "Yellow"
                print('You go through the yellow door')
            elif player_input == 3:
                if player.have_red_key == 0 and red_room.lock == 0:
                    print('The door is locked')
                elif player.have_red_key == 1 and red_room.lock == 0:
                    player.have_red_key = 0
                    red_room.lock = 1
                    player.current_room = "Red"
                    print('You used the red key to unlock the red door')
                else:
                    player.current_room = "Red"
                    print('You go through the red door')
            elif player_input == 4:
                if purple_room.lock == 0:
                    print('The door is locked')
                else:
                    player.current_room = "Purple"
                    print('You go through the purple door')
            elif player_input == 5:
                if blue_room.bulb == "OFF":
                    blue_room.bulb = "ON"
                    print('You flipped the switch ' + blue_room.bulb)
                else:
                    blue_room.bulb = "OFF"
                    print('You flipped the switch ' + blue_room.bulb)
            elif player_input == 0:
                print('There is a faded orange panel on the floor.')
                if yellow_room.bulb == 'ON' and red_room.bulb == 'ON' and \
                        blue_room.bulb == 'OFF':
                    print('You open it.')
                    print('A creepy man looks up at you disapprovingly.')
                    print('Better not go in here...')
                else:
                    print('It appears to be locked tight.')
            else:
                print('Enter a valid selection')

        # Yellow room events
        elif player.current_room == "Yellow":
            player_input = get_player_input()
            if player_input == 3:
                player.current_room = "Blue"
                print('You go through the blue door')
            elif player_input == 5:
                if yellow_room.bulb == "OFF":
                    yellow_room.bulb = "ON"
                    print('You flipped the switch ' + yellow_room.bulb)
                else:
                    yellow_room.bulb = "OFF"
                    print('You flipped the switch ' + yellow_room.bulb)
            elif player_input == 6:
                if red_room.bulb_power == 0:
                    print('The device has a keypad that requires a code')
                    print('A message above it reads THE SUM OF THE FOUR')
                    print('Enter a code:')
                    code_entered = input()
                    while isinstance(code_entered, int) == 0:
                        try:
                            code_entered = int(code_entered)
                        except ValueError:
                            print('Enter a valid numerical code')
                            code_entered = input()
                    if code_entered == blue_room.wall_code\
                            + yellow_room.wall_code + green_room.wall_code\
                            + red_room.wall_code * 1:
                        red_room.bulb_power = 1
                        print('Power has been supplied somewhere')
                    else:
                        print('Nothing happened')
                else:
                    print('The device is already powered on')
            else:
                print('Enter a valid selection')

        # Green room events
        elif player.current_room == "Green":
            player_input = get_player_input()
            if player_input == 4:
                player.current_room = "Blue"
                print('You go through the blue door')
            elif player_input == 5 and player.have_red_key == 0 and\
                    red_room.lock == 0:
                player.have_red_key = 1
                print('You picked up the red key')
            else:
                print('Enter a valid selection')

        # Red room events
        elif player.current_room == "Red":
            player_input = get_player_input()
            if player_input == 2:
                player.current_room = "Blue"
                print('You go through the blue door')
            elif player_input == 5:
                if red_room.bulb_power == 0:
                    print('The light bulb has no power')
                else:
                    if red_room.bulb == "OFF":
                        red_room.bulb = "ON"
                        print('You flipped the switch ' + red_room.bulb)
                    else:
                        red_room.bulb = "OFF"
                        print('You flipped the switch ' + red_room.bulb)
            else:
                print('Enter a valid selection')

        # Purple room events
        elif player.current_room == "Purple":
            player_input = get_player_input()
            if player_input == 1:
                player.current_room = "Blue"
                print('You go through the blue door')
            elif player_input == 4:
                print('There is device locking the EXIT that'
                      ' seems to be voice activated.')
                print('A message is scribbled above it:')
                print('SPEAK THE NAME OF THE WISE ONE TO BE FREE')
                print('Type your answer:')
                answer = str(input())
                if answer == player.name:
                    print('The door unlocks and you swing it open.')
                    player.win = 1
                else:
                    print('Nothing happened')
            else:
                print('Enter a valid selection')

        # Prompts the player to press enter to continue
        input('\nPress ENTER to continue')

        # Decrements health variable with a shortcut operator
        player.health -= 1

    # Calls win screen function if player has met win condition
    if player.win == 1:
        get_win_screen(player)

    # Death text if player win condition is not met
    else:
        print('\nYou have died from exhaustion.')
        print("Better luck next time!")
        # Code to satisfy for in range requirements
        for x in range(5):
            print("Xx______________________xX")


# Calls the play game function to play the game
play_game()
