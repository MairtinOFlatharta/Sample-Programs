alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("Hello, Time to play In and Out! This game requires 3 players")
print("It requires a host and two other players")


#Here, the host sets the secret phrase
winning_phrase = (input("The host must now choose the secret phrase. Make sure the other players aren't peeking!\n")).upper()
guesses = ""
guess = ''
player = 1 #Keeps track of player
game_phase = 0 #Keeps track of whether rhe player must enter a char in (0) or not in (1) the phrase

while (True):
    phrase_string = ""
    i = 0
    already_guessed = 0#Bool variable to check if user input was already guessed
    too_long = 0#Bool variable to check if user input is more than one letter

    # for every character in winning_phrase    
    for char in winning_phrase:

        #Builds up string of letters that were guessed and are in winning_phrase
        if char in guesses:
            phrase_string += char
        elif (char == ' '):
            phrase_string += char
        else:
            phrase_string += '_'  

    print(phrase_string)
    print(alphabet)
    
    # ask the user to guess a character
    print("Player", player,":-")
    
    if game_phase == 0:
        guess = (input("-Guess a character in the phrase or input 'guess' if you think you know the phrase:\nEnter only one letter!\n")).upper()
        
    elif game_phase == 1:
        guess = (input("-Guess a character that isn't in the phrase or input 'guess' if you think you know the phrase:\nEnter only one letter!\n")).upper()
        
    if (guess.lower() == 'guess'):
        if(winning_phrase == (input("What is the phrase?\n")).upper()):
            print("Player", player,"wins!")
            break
        else:
            print("Incorret Guess")
            
    elif len(guess)>1:
        too_long = 1
        
    elif guess in guesses:
        already_guessed = 1
    
    else:
        while alphabet[i] != guess.upper():
                if i > (len(alphabet)-2):#Check if input is valid
                    print("This character is not a valid input!")
                    break
                else:
                    i+=1
                    
        del alphabet[i]
    
    if too_long:
        print("Too many letters entered!")
        player = (player%2)+1#Switching to next player
        print ("Next player is player", player)
        game_phase = 0#Resetting game phase to default
        
    elif already_guessed:
        print("Letter", guess,"was already entered")
        player = (player%2)+1
        print ("Next player is player", player)
        game_phase = 0

    elif guess not in winning_phrase and game_phase == 0:        
        print ("You guessed wrong")
        player = (player%2)+1
        print ("Next player is player", player)
        game_phase = 0
        guesses += guess
        
    elif guess in winning_phrase and game_phase == 1:
        print ("You guessed wrong")
        player = (player%2)+1
        print("Next player is player", player)
        game_phase = 0
        guesses += guess

    else:
        guesses += guess
        game_phase = (game_phase+1)%2#Switching to next game phase
