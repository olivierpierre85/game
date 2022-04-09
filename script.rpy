# The script of the game goes in this file.

# Declare All characters used by this game.

define system = Character("")
define soldier = Character("soldier")
define host = Character("The host")

# The game starts here.
label start:
    # TODO Menu Image
    scene great_hall

    # These display lines of dialogue.
    jump character_selection
    

    return
