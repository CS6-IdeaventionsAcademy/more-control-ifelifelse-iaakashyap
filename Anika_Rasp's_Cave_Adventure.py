# Anika Kashyap
# 12/5/17
# Raspi's Cave Adventure
# A text based adventure game 

def left_cave(): 
    print ("You walk into the left cave.It is cold and dark!")
    print ("The cave opens up into to a underground river.")
    # River choice
    print ("You see an underground river with a boat next to it.")
    print ("Do you want to swim, take boat, or walk around the river?")
    choice = input ("Pleas enter S ( swim ), B (boat), or W (walk): "). upper() 
    return choice

def right_cave(): 
    print ("You walk into the right cave.It is cold and dark!")
    print ("The cave stats slooping downwards.")
    # Rope and Torch Choice
    print ("You see a hole with a rope going down and a torch of in the distance.")
    print ("Do you want to walk to the torch or climb down the rope?")
    choice = input ("Enter T (torch) or R (rope): "). upper() 
    return choice

def wrong_answer():
    # Wrong answer
    print ("You make bad desions, don't you?")
    print ("A rabid squirel bites you!You die.")
    print ("GAME OVER")

def torch_death():
    '''This is the players death when they walk to the torch'''
    print: (" You reach for the torch and die!")

def dragon_lair():
    ''' This is the players choice of wether to fight the dragon or not.'''
    print("You see the dragon sleeping and a dark off to the side.")
    input ("Do you want to slay the dragon or go to the dark room.") 
        
# Tittle 
print ( "<00>" * 100)
print (" Welcome to Raspi's Cave Adventure!!!!")
print ('''

 /$$$$$$$                                /$$ /$$                                                                                              
| $$__  $$                              |__/| $/                                                                                              
| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$|_//$$$$$$$                                                                                       
| $$$$$$$/ |____  $$ /$$_____/ /$$__  $$| $$  /$$_____/                                                                                       
| $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$| $$ |  $$$$$$                                                                                        
| $$  \ $$ /$$__  $$ \____  $$| $$  | $$| $$  \____  $$                                                                                       
| $$  | $$|  $$$$$$$ /$$$$$$$/| $$$$$$$/| $$  /$$$$$$$/                                                                                       
|__/  |__/ \_______/|_______/ | $$____/ |__/ |_______/                                                                                        
                              | $$                                                                                                            
                              | $$                                                                                                            
                              |__/                                                                                                            
  /$$$$$$                                       /$$$$$$        /$$                                 /$$                                        
 /$$__  $$                                     /$$__  $$      | $$                                | $$                                        
| $$  \__/  /$$$$$$  /$$    /$$ /$$$$$$       | $$  \ $$  /$$$$$$$ /$$    /$$ /$$$$$$  /$$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$   /$$$$$$       
| $$       |____  $$|  $$  /$$//$$__  $$      | $$$$$$$$ /$$__  $$|  $$  /$$//$$__  $$| $$__  $$|_  $$_/  | $$  | $$ /$$__  $$ /$$__  $$      
| $$        /$$$$$$$ \  $$/$$/| $$$$$$$$      | $$__  $$| $$  | $$ \  $$/$$/| $$$$$$$$| $$  \ $$  | $$    | $$  | $$| $$  \__/| $$$$$$$$      
| $$    $$ /$$__  $$  \  $$$/ | $$_____/      | $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$  | $$  | $$ /$$| $$  | $$| $$      | $$_____/      
|  $$$$$$/|  $$$$$$$   \  $/  |  $$$$$$$      | $$  | $$|  $$$$$$$   \  $/  |  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$/| $$      |  $$$$$$$      
 \______/  \_______/    \_/    \_______/      |__/  |__/ \_______/    \_/    \_______/|__/  |__/   \___/   \______/ |__/       \_______/      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
''')
print ("<00>" * 100)

# 1st choice Left or right
print ("You see a cave spilt to a left and right tunnel.")
print ("Do you choose to go left or right?")
cave_choice = input ("Enter R for right or L for left: ").upper()
if cave_choice == "L" or cave_choice == "LEFT":
    # Left cave
    choice = left_cave()
    if choice == "B" or choice == "Boat":
        #Boat choice
        print ("You climb into the wooden boat and push of.")
        # Death Sence
    elif choice == "S" or choice == "SIWM":
        # Swim option
        print("You take a deep breath and dive into the cold river.")
        print ("You just realize that you skipped your medieval swim lessons.")
        print ("But you find out you are a natural...")
        # Get treasure
    elif choice == "W" or choice == "WAlK":
        print("You start walking along the narrow edge of the river.")
        # Death Secne
    else:
        # Wrong answer
        wrong_answer()

elif cave_choice == "R" or cave_choice == "RIGHT":
    # Right cave
    print ("You walk into the right cave.")
    print ("The cave starts slooping downwards...")
    choice = right_cave()
    if choice == "T" or choice == "TORCH":
        print ("You walk towards the torch slowly.")
        # TODO Add death function
    elif choice == "R" or choice == "ROPE":
    print ("You go down the rope and live yeah.")
    print ("You hear a drogon breathing in the dark room")=
    choice = dragons_lair()
    if choice == "S" or choice "SLAY":
        print("You die")'
    elif choice == "R" or choice "ROOM":
        print ("You Win")
    else:
        wrong_answer()
else:
    # Wrong answer
    wrong_answer()

  
