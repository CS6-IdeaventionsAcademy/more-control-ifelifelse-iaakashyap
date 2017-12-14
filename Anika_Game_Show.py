# Anika Kashyap
# Game Show
# 11/28/17


print ( "Please pick a door! ( A,B,C,D" )

door_a = "A Tarantula"
door_b = "A Rotten Egg"
door_c = "A Fridge"
door_d = "Cheese"
door_e = "A New Tesla" 


play_again = "Yes"

while play_again == "Yes"
    player_choice = input "Please pick a door!(A,B,C,D)"  

    if player_choice == door_a:
        print ("You won a new pet and guess what it is? It is a Tarantula!")
    elif player_choice == door_b:
        print ("You won a smelly Rotten EGG!")
    elif player_choice == door_c:
        print ("Lucky you,You won a new Fridge!")
    elif player_choice == door_d:
        print ("Hope you're hungry because you just got some cheese.")
    elif player_choice == door_e:
        print ("Congrats you opened the portal to dome. But lucky you there is a tesla") 
    play_again = input (" Would you like to play agaian?")
