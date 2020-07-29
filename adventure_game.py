import time
import random
weapons = []
mythical_creatures = ["dragon", "wizard", "ogre", "giant",
                      "werewolf", "bigfoot"]
creature = random.choice(mythical_creatures)


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {creature} is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print("")
    return response


def field():
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n")
    print_pause("What would you like to do?")
    decision1 = valid_input("Please enter (1 or 2)\n", '1', '2')
    if decision1 == '1':
        house()
    elif decision1 == '2':
        cave()


def fight():
    if 'sword' not in weapons:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {creature}.")
        print_pause("You have been defeated!")
    else:
        print_pause(f"As the {creature} moves to attack,"
                    " you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    " as you brace yourself for the attack.")
        print_pause(f"But the {creature} takes one look at your"
                    " shiny new toy and runs away!")
        print_pause("You have rid the town of the pirate. You are victorious!")


def cave():
    if 'sword' in weapons:
        print_pause("You peer into the cave but there is nothing new to see")
        print_pause("You walk back out to the field.")
        field()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        print_pause("You walk back out to the field.")
        weapons.append('sword')
        field()


def house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                f" opens and out steps a {creature}.")
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                " what with only having a tiny dagger.")
    decision2 = valid_input("Would you like to (1) fight or"
                            " (2) run away?\n", '1', '2')
    if decision2 == '1':
        fight()
    elif decision2 == '2':
        print_pause("You run back into the field. Luckily,"
                    " you don't seem to have been followed.")
        field()


def play_again():
    while True:
        play_again = input("Would you like to play again? (y/n)").lower()
        if play_again == 'y':
            print_pause("Excellent! Restarting the game...")
            play_game()
        elif play_again == 'n':
            print("Thanks for playing! See you next time")
            break
        else:
            print_pause("Please type 'y' or 'n'")


def play_game():
    intro()
    field()
    play_again()


play_game()
