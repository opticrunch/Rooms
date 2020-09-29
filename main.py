# Stephen Royka
# ROOMS: FIVE COLORS is a text based puzzle adventure game

# Function to print the HUD and room map current_room value
def print_room_hud():
    print('_______________________________________________')
    print('PLAYER: ' + player_name + ' | AGE: ' + str(player_age)
          + ' | ROOM: ' + current_room + ' | HEALTH: ' + str(health))
    print('      _________')
    if current_room == "Green":
        print(' MAP |    X    |  COMPASS   N')
    else:
        print(' MAP |         |  COMPASS   N')
    print('     |___   ___|          W + E')
    print('|----|         |----|       S')
    if current_room == "Blue":
        print('|         X         |')
    elif current_room == "Yellow":
        print('| X                 |')
    elif current_room == "Red":
        print('|                 X |')
    else:
        print('|                   |')
    if have_red_key == 1:
        print('|----|___   ___|----|    RED KEY')
    else:
        print('|----|___   ___|----|')
    if have_red_key == 1:
        print('     |         |          0--m')
    elif current_room == "Purple":
        print('     |    X    |')
    else:
        print('     |         |')
    print('     |___   ___|')
    print('')


# Function to print the room info based on the current_room value
def get_room_info():
    print_room_hud()
    if current_room == "Blue":
        print('You are in a room with blue walls.')
        print('There is a blue light bulb on the wall switched to '
              + bulb_blue + '.')
        print('There is a number ' + str(code_number1)
              + ' scribbled on the wall.')
        print('There is a green door to the North, a yellow door to the West,')
        print('a red door to the East, and a purple door to the South.')
        print('______________ENTER A SELECTION______________')
        print('       1) Go North            5) Light bulb')
        print('2) Go West    3) Go East')
        print('       4) Go South')
    elif current_room == "Yellow":
        print('You are in a room with yellow walls.')
        print('There is a yellow light bulb on the wall switched to '
              + bulb_yellow + '.')
        print('There is a number ' + str(code_number2)
              + ' scribbled on the wall.')
        print('There is an electrical device on the wall that might'
              ' supply power somewhere.')
        print('There is a blue door to the East.')
        print('______________ENTER A SELECTION______________')
        print('       1)                     5) Light bulb')
        print('2)            3) Go East      6) Device')
        print('       4)')
    elif current_room == "Green":
        print('You are in a room with green walls.')
        print('There is a number ' + str(code_number3)
              + ' scribbled on the wall.')
        if have_red_key == 0 and lock_red == 0:
            print('There is a RED KEY on the ground.')
        print('There is a blue door to the South.')
        print('______________ENTER A SELECTION______________')
        if have_red_key == 0 and lock_red == 0:
            print('       1)                     5) Red key')
        else:
            print('       1)')
        print('2)            3)')
        print('       4) Go South')
    elif current_room == "Red":
        print('You are in a room with red walls.')
        print('There is a number ' + str(code_number4)
              + ' scribbled on the wall.')
        print('There is a red light bulb on the wall switched to '
              + bulb_red + '.')
        print('There is a blue door to the West.')
        print('______________ENTER A SELECTION______________')
        print('       1)                     5) Light bulb')
        print('2) Go West    3)')
        print('       4)')
    elif current_room == "Purple":
        print('You are in a room with purple walls.')
        print('There is a red light bulb on the wall switched to '
              + bulb_red + '.')
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
def get_win_screen(ending_health):
    # Win screen out of game loop
    print(' ______________________________________')
    print('     ____________  CONGRATULATIONS!')
    print('    |    ROOMS   |             YOU')
    print('    |     __     |     \o/   ESCAPED')
    print('    |    |  |    |      |    WITH ' + str(ending_health))
    print('    |    |  |    |     / \   HEALTH')
    print(' ______________________________________')
    print('Great job, ' + player_name + '!')

    # Creates a file and writes to it
    certificate = open('CertificateOfVictory.txt', 'w')
    certificate.write('This certificate is proof that\n' + player_name +
                      '\nescaped the mysterious\nROOMS: Five Colors'
                      '\n ______________________________________'
                      '\n     ____________  CONGRATULATIONS!'
                      '\n    |    ROOMS   |             YOU'
                      '\n    |     __     |     \o/   ESCAPED'
                      '\n    |    |  |    |      |    WITH '
                      + str(ending_health) +
                      '\n    |    |  |    |     / \   HEALTH'
                      '\n ______________________________________')


# Initialize global variables
current_room = 'Blue'
have_red_key = bool(0)
bulb_blue = 'OFF'
bulb_yellow = 'OFF'
bulb_red_power = bool(0)
bulb_red = 'OFF'
lock_green = bool(0)
lock_red = bool(0)
lock_purple = bool(0)
win = bool(0)
game_start = bool(0)
health = int(50)

# Title screen loop start
while game_start == 0:

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
        game_start = 1
    else:
        print('Enter a valid selection\n')

# Get player name use later
print('Enter your name:')
player_name = str(input())

# Get player age for use later and check to make sure it is an integer
print('Enter your age:')
player_age = input()
while isinstance(player_age, int) == 0:
    try:
        player_age = int(player_age)
    except ValueError:
        print('Please enter a whole number: ')
        player_age = input()

# Returns game_start to 0 for difficulty setting loop
game_start = 0

# Prompts for difficulty setting (determines starting health)
while game_start == 0:
    print('Choose a difficulty setting:')
    print('1) Easy    2) Medium  3) Hard')
    difficulty_choice = get_player_input()
    if difficulty_choice == 1:
        health = 50
        game_start = 1
        print('You got this!\n')
        input('Press ENTER to continue')
    elif difficulty_choice == 2:
        health = 35
        game_start = 1
        print('Good luck!\n')
        input('Press ENTER to continue')
    elif difficulty_choice == 3:
        health = 20
        game_start = 1
        print('Uh oh... I hope you make it!\n')
        input('Press ENTER to continue')
    # Secret to get the max starting health
    elif difficulty_choice == 42:
        health = 100
        game_start = 1
        print('Wait... How did you know that? MAX HEALTH!!\n')
        input('Press ENTER to continue')
    else:
        print('Enter a valid selection\n')

# Generate code numbers that will be on walls using player age
# Utilizes ** (exponent), / (division), // (floor division), % (modulus)
code_number1 = int((player_age ** 3 / 2) // 1000 % 10)
code_number2 = int((player_age ** 3 / 2) // 100 % 10)
code_number3 = int((player_age ** 3 / 2) // 10 % 10)
code_number4 = int((player_age ** 3 / 2) % 10)

# Generates the device code and multiplies it by 1 so I can use the * operator
device_code = code_number1 + code_number2 + code_number3 + code_number4 * 1

# Start of the game loop that checks for win condition and health
while win == 0 and health > 0:

    # Door lock checks
    if bulb_blue and bulb_yellow == 'ON' and bulb_red == 'OFF':
        lock_green = 1
    else:
        lock_green = 0
    if bulb_blue and bulb_red == 'ON' and bulb_yellow == 'OFF':
        lock_purple = 1
    else:
        lock_purple = 0

    # Blue room events
    if current_room == "Blue":
        get_room_info()
        player_input = get_player_input()
        if player_input == 1:
            if lock_green == 1:
                current_room = "Green"
                print('You go through the green door')
            elif lock_green == 0:
                print('The door is locked')
        elif player_input == 2:
            current_room = "Yellow"
            print('You go through the yellow door')
        elif player_input == 3:
            if have_red_key == 0 and lock_red == 0:
                print('The door is locked')
            elif have_red_key == 1 and lock_red == 0:
                have_red_key = 0
                lock_red = 1
                current_room = "Red"
                print('You used the red key to unlock the red door')
            else:
                current_room = "Red"
                print('You go through the red door')
        elif player_input == 4:
            if lock_purple == 0:
                print('The door is locked')
            else:
                current_room = "Purple"
                print('You go through the purple door')
        elif player_input == 5:
            if bulb_blue == "OFF":
                bulb_blue = "ON"
                print('You flipped the switch ' + bulb_blue)
            else:
                bulb_blue = "OFF"
                print('You flipped the switch ' + bulb_blue)
        else:
            print('Enter a valid selection')

    # Yellow room events
    elif current_room == "Yellow":
        get_room_info()
        player_input = get_player_input()
        if player_input == 3:
            current_room = "Blue"
            print('You go through the blue door')
        elif player_input == 5:
            if bulb_yellow == "OFF":
                bulb_yellow = "ON"
                print('You flipped the switch ' + bulb_yellow)
            else:
                bulb_yellow = "OFF"
                print('You flipped the switch ' + bulb_yellow)
        elif player_input == 6:
            if bulb_red_power == 0:
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
                if code_entered == device_code:
                    bulb_red_power = 1
                    print('Power has been supplied somewhere')
                else:
                    print('Nothing happened')
            else:
                print('The device is already powered on')
        else:
            print('Enter a valid selection')

    # Green room events
    elif current_room == "Green":
        get_room_info()
        player_input = get_player_input()
        if player_input == 4:
            current_room = "Blue"
            print('You go through the blue door')
        elif player_input == 5 and have_red_key == 0 and lock_red == 0:
            have_red_key = 1
            print('You picked up the red key')
        else:
            print('Enter a valid selection')

    # Red room events
    elif current_room == "Red":
        get_room_info()
        player_input = get_player_input()
        if player_input == 2:
            current_room = "Blue"
            print('You go through the blue door')
        elif player_input == 5:
            if bulb_red_power == 0:
                print('The light bulb has no power')
            else:
                if bulb_red == "OFF":
                    bulb_red = "ON"
                    print('You flipped the switch ' + bulb_red)
                else:
                    bulb_red = "OFF"
                    print('You flipped the switch ' + bulb_red)
        else:
            print('Enter a valid selection')

    # Purple room events
    elif current_room == "Purple":
        get_room_info()
        player_input = get_player_input()
        if player_input == 1:
            current_room = "Blue"
            print('You go through the blue door')
        elif player_input == 4:
            print('There is device locking the EXIT that'
                  ' seems to be voice activated.')
            print('A message is scribbled above it:')
            print('SPEAK THE NAME OF THE WISE ONE TO BE FREE')
            print('Type your answer:')
            player_answer = str(input())
            if player_answer == player_name:
                print('The door unlocks and you swing it open.')
                win = 1
            else:
                print('Nothing happened')
        else:
            print('Enter a valid selection')

    # Prompts the player to press enter to continue
    input('\nPress ENTER to continue')

    # Decrements health variable with a shortcut operator
    health -= 1

if win == 1:
    get_win_screen(health)

else:
    print('\nYou have died from exhaustion.')
    print('Better luck next time, scrub.')
