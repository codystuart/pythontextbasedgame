"""
   Name: Cody Stuart
   Course: IT-140 - Intro to scripting
   Assignment: Text based game project
"""
def main():
    ###GLOBAL VARIABLES###
    # Game board map turned into dictionary
    global rooms_map
    global inventory
    global current_room
    global items_list

    rooms_map = {
        'refuge chamber': {'west': 'ventilation room'},
        'ventilation room': {'north': 'ore pass', 'east': 'refuge chamber', 'west': 'crusher room'},
        'crusher room': {'east': 'ventilation room'},
        'ore pass': {'north': 'storage room', 'south': 'ventilation room'},
        'storage room': {'north': 'tunnel 1', 'south': 'ore pass', 'west': 'electrical'},
        'electrical': {'east': 'storage room'},
        'tunnel 1': {'south': 'storage room', 'west': 'Entrance'},
        'entrance': {'east': 'tunnel 1'}
    }

    # items to be picked up
    items_list = {
        'ventilation room': 'lantern',
        'crusher room': 'helmet',
        'ore pass': 'pickaxe',
        'storage room': 'bear spray',
        'electrical': 'radio',
        'tunnel 1': 'sandwich'
    }

    # Initialize current room so we can track it as we move
    current_room = 'refuge chamber'
    # variable to hold the player's inventory
    inventory = []
    # Variable we use to stay in the gameplay loop
    gamePlaying = True

    gameStart()

    while (gamePlaying):

        #Some end game conditional checking
        collected_items = len(inventory)
        if (collected_items == 6):
            print('I have everything I need to get rid of that bear! but first let me eat this delicious sandwich!\n'
                  'You won!\n')
            break

        if (current_room == 'Entrance') and ((len(inventory) < 6)):
            print('Oh no I ran into the bear before I was ready!\n')
            'You lose!\n'
            break

        playerStatus()

        mainMenu()

###FUNCTIONS####
#create function for moving the player in between rooms,
def player_move_between_rooms(room):
    #set current_room as a global variable so we can set its value in the output
    global current_room
    global rooms_map

    #valid directional moves
    directions = ['north', 'south', 'east', 'west']

    #Tell the player which room they are in currently
    print('--------------------------------------------')
    print('You\'re currently in the {}\n'.format(room))

    #Setting a variable that we can use to break out of the move validation loop
    validDirection = False

    while ( validDirection == False ):
        #get the users input on which direction they would like to move
        direction_to_move_result = get_move()

        #compare the entered text to confirm it's a valid direction
        if direction_to_move_result in directions:
            if direction_to_move_result in rooms_map[room]:
                current_room = rooms_map[room][direction_to_move_result]
                print(rooms_map[room][direction_to_move_result])
                validDirection = True
            else:
                print('You can\'t move that direction from here!\n'
                      'You\'re currently in the {}\n'.format(room))
                #direction_to_move_result = get_move()

    print('--------------------------------------------')
    print('Moving {}\n'.format(direction_to_move_result.capitalize()))
    print('You\'re now in the {}\n'.format(current_room))
    return current_room



#This function we call when we want to get the users movement direction
def get_move():
    direction_to_move = input(

                              '\nWhich direction would you like to go?\n'
                              'go ').lower()
    return direction_to_move

def get_items():
    validItem = False
    while not (validItem):
        requested_item = input('--------------------------------------------\n'
              'To get an item type \'get <item name>\'\n'
              'For example \'get bear spray\'\n'
                               'get  ').lower()


        if requested_item in items_list.values():
            validItem = True
        else:
            print('The item you have asked for does not exit')

    if requested_item in inventory:
        print('I already found that\n')

    for k,v in items_list.items():
        if not requested_item in inventory:
            if (requested_item == v) and (current_room == k):
                inventory.append(v)

    input('Press enter to continue')

def gameStart():
    print('Wow!\n'
          'what a great nap! wait... ROOOARRRRRRRRRR\n'
          'Is that a bear I hear? I know just what to do.\n'
          'I\'ll collect 6 items to help me scare off the bear, and one of them better be a sandwich\n'
          'Press enter to continue')
    input()

def playerStatus():

    possible_moves = ""
    for key in rooms_map[current_room].keys():
        possible_moves = possible_moves + key + '; '
    if items_list.get(current_room) in inventory:
        print('-------------------------------------\n'
              'Current room: {}\n'
              'Possible moves: {}\n'
              'Inventory: {}\n'
              '-------------------------------------\n'.format(current_room, possible_moves, inventory))
    elif (current_room == 'refuge chamber'):
        print('-------------------------------------\n'
              'Current room: {}\n'
              'Possible moves: {}\n'
              'Inventory: {}\n'
              '-------------------------------------\n'.format(current_room, possible_moves, inventory))
    else:
    #Player stats section
        print('-------------------------------------\n'
                'Current room: {}\n'
                'Possible moves: {}\n'
                'Inventory: {}\n'
                'You see a {}\n'
                '-------------------------------------\n'.format(current_room, possible_moves, inventory, items_list.get(current_room)))

def mainMenu():
    try:
        user_input = input('Please enter the number corresponding to your choice\n'
                           '1. Move rooms\n'
                           '2. Get items\n'
                           '3. Show instructions\n'
                           'What would you like to do?\n'
                           '> ')

        if (int(user_input) == 1):
            player_move_between_rooms(current_room)
        elif (int(user_input) == 2):
            get_items()
        elif (int(user_input) == 3):
            show_instructions()
        else:
            print('Please choose a valid option')
    except:
        print('Please enter a valid option')

def show_instructions():
    print('Sleepy mine text game\n'
          'Collect 6 items before you run into the bear to win the game.\n\n'
          'Moving\n'
          '-------------------------------\n'
          'Possible moves are [North, South, East, West]\n'
          'Move rooms by typing \'go <direction>\'\n\n'
          'Inventory\n'
          '-------------------------------\n'
          'Pickup an item by typing \'get <item name>\'\n'
          'Press enter to continue\n')
    input()
main()

