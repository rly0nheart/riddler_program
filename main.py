# r1ddler program version-0.1.3
# Author: rlyonheart
# Twitter: rly0nheart
# Github: rlyonheart
# ©2021


# for loop,for a triangle pattern
rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("❓", end=" ")
    print(" ")

print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("❔", end=' ')
    print(" ")





# import time
import time

import sys

# import color module (termcolor)
import termcolor
from termcolor import colored,cprint


def display_intro():
    """
    Displays the introduction text and asks user for their names.
    Returns the users' firstname and lastname
    """
    print(colored("\t\t  ❔❓❓R1DDL3R❔❓❓  ",'red',attrs=['underline','bold']),colored("\n\t\t   Author: rly0nheart  ",'white',attrs=['underline','bold']),colored("\t"+"©2020",'grey',attrs=['underline','bold']))
    print(colored("\n\n\t\tENTER YOUR FULL NAMES TO BEGIN🔻 ",'red',attrs=['bold','underline']))
    print("\033[1;33;40m")
    print(colored("\n\nEnter First-name:",attrs=['underline']))
    fnme = input().capitalize()
    print(colored("\033[1;33;40m\n\nEnter Last-name:",attrs=['underline']))
    lnme = input().capitalize()
    time.sleep(1)
    print(colored(f"\n\nGreetings {fnme} {lnme}!, it is a pleasure meeting you!\n",'white','on_green',attrs=['bold']) + colored("I am The R1DDLER!'\nAnd I am about to take you on a journey filled with mystery, to a land where only a few return victorious!, a land right in front of your eyes👁️👁️. ",'white','on_red',attrs=['bold']))
    print("\n\nAre you ready❓ ")
    user_input = input().lower()
    if user_input == "yes":
        time.sleep(1)
        cprint("Very Well..",'white','on_green',attrs=['bold'])
    elif user_input == "no":
        cprint("Thinking.....\n",'blue',attrs=['bold'])
        time.sleep(1)
        sys.exit(colored(f'Alright then, come back when you are ready.','red',attrs=['bold']))
    else:
        print(colored("\033[0;37;41m⚠️INVALID INPUT⚠️   ",'white','on_red',attrs=['bold']),"\033[1;33;40m\n\nBut We Shall Proceed🙂\n\n")
    return fnme, lnme

def ask_riddles(riddles):
    """
    Loops through each question & answer in riddles
    Returns score, the number of riddles answered correctly
    """
    score = 0
    for question, answer in riddles:
        cprint("Riddle Me This:",'white',attrs=['bold','underline'])
        print(f"\033[1;33;40m==> {question}❓... ")
        user_input = input().lower()
        if answer in user_input:
            cprint("\nchecking your answer.....",'blue')
            time.sleep(1)
            print(colored("THAT IS CORRECT!☑️ \n\n",'white','on_green',attrs=['bold']))
            print("\033[1;33;40m")
        elif "quit" in user_input:
            sys.exit(colored(f"\nProgram terminated by {fnme}",'red',attrs=['bold']))
            score +=1
        else:
            cprint("\nchecking your answer.....",'blue',attrs=['bold'])
            time.sleep(2)
            cprint("THAT IS INCORRECT!❎ \n\n",'white','on_red',attrs=['bold'])
    return score


if __name__ == '__main__':
    # Riddles is a list of tuples where each tuple contains question & answer
    riddles = [
        ("What has 6 wheels and flies", "a garbage truck"),("What is it that no man wants, but no man wants to lose", "a lawsuit"),('''It\'s got twists and turns, but has no curves. Twist it to fix it, turn it to
ruin it. What is it''', "a rubiks cube"),('''What has everything inside it? Everything you can imagine\neven god,
wind, world, sky, heaven, earth and everything that comes to your
mind''', "the alphabet"),('''What is it that makes tears without sorrow and takes it\'s \njourney to
heaven''', "smoke"),("""Downward grows the root. Outward grows the skin.
Upward grows the shoot. What way blows the wind""", "wayward"),("What's always coming, but never arrives", "tomorrow"),("What is everyone in the world doing at the same time", "growing old"),('''On my way to St. Ives,

I met a man with seven wives.

Each wife had seven sacks,

Each sack had seven cats,

Each cat had seven kits.

Kits, cats, sacks, wives,

How many were going to St. Ives''', "one"), ('''Above all things have I been placed

Thus have I, a man disgraced.

I describe sunlight or lock.
But after all, I'm just a rock. 
What Am I''', "the moon"),('''Two bodies have I, though both joined in one.

The more still I stand, the quicker I run.

What am I''', "an hourglass"),("""Two children are born on the same day, from the same mother,\nbut they
are not twins. How is that possible""", "they are triplets"),('''I can be long, or I can be short. I can\nbe grown, and I can be bought. I
can be painted, or left bare. I can be round, or square.\nWhat am I''', "fingernails"), ("What stays where it is when it goes off", "an alarm"),("What flies BACK and FORTH, but NEVER takes you anywhere", "a swing"),("I'm round at the ends and high in the middle. What am I", "ohio"),("What loses its head every morning\nonly to get it back every night", "a pillow"),('''A home of wood in a wooden place, but built not by hand. High above
the earthen ground, it holds its pale blue gems. What is it''', "a nest"),("I have four legs, a back, but no head. What am I", "a chair"),('''My sides are firmly laced about,
Yet nothing is within;
You'll think my head is strange indeed,
Being nothing else but skin. What Am I''', "a drum"),("One strand dangles. Two strands twist. Three or more can\nfashion this. What Is It", "braids"),('''The one who makes it sells it.
The one who buys it doesn't use it.
The one who's using it doesn't know he's using it.
What is it''',"a coffin"),("I am green but not a tree. And I grow around the world. What am I", "grass"), ("""I have a tongue, but cannot speak.\nI have a bed but cannot sleep.\nI have
four legs but cannot walk. Yet I move as you do. What am I""", "a wagon"),("""You may always chase me but you are always about 3 miles away.
What am I""", "the horizon"),("""What word of five letters has only one left when two letters are
removed""", "stone"),('''Take away my first letter and I remain the same. Take away my last
letter and remain unchanged. Remove all my letters and I’m still me.

What am I''', "a mailman"),("If I have it, I don’t share it. If I share it, I don’t\nhave it. What is it", "a secret"),("I am the RED tongue of the EARTH\nthat BURIES cities. What Am I", "lava"),("Why can't the Tyrannosaurus rex clap", "it is extinct"),("I am something all men have but all men deny. Man created me but no man can hold me.\nWhat Am I", "fear"), ("""My thunder comes before my lightning.\nMy lightning comes before my rain.\nAnd my rain dries all the ground it touches.\nWhat am I""", "a volcano"),("""I have a hundred legs but cannot stand, a long neck but no\nhead; I eat
the maid's life. What am I""", "a broom"), ("I bind it and it walks. I loose it and it stops. What Is It", "a sandal"),("""The word CANDY can be spelled using just 2 letters. Can you\nfigure
out how""", "c and y"),('''At the sound of me, men may dream
Or stamp their feet. At the sound of me, women may laugh
Or sometimes weep. What Am I''', "music"), ("""What has roots as nobody sees, Is taller than trees,
Up, up it goes
And yet never grows?""", "a mountain"),('''My first is in FLOWER and in ROSE

My second is in FORK and well as HOSE

My third is in CROCUS but not in GNOME

My fourth is in RAKE never in HOME

My fifth is in HOE and also in WEEDS

My sixth is in SHEARS though not in SEEDS

My seventh is in LADYBIRD not in CREATURE

What am I''', "rockery"),("Twigs and spheres and poles and plates, join and bind to\nreason make. What Is It", "a skeleton"),("What's made of wood but can't be sawed", "sawdust"),("A box without hinges, key, or lid,\nYet golden treasure inside is hid. What Is It", "an egg"),("A crime that is punishable if attempted but not punishable\nwhen it is actually committed. What Is It", "suicide"),("What gets bigger as you take out of it", "a hole"),("Pedro hides but his head is still exposed", "a nail"), ("""I fly, yet I have no wings.\nI cry, yet I have no eyes.\nDarkness follows
me; lower light I never see. What am I""", "a cloud"),("""It cannot be seen, cannot be felt
Cannot be heard, cannot be smelt.
 It lies behind stars and under hills,
 And empty holes it fills.
 It comes first and follows after,
 Ends life, kills laughter. What Is It""", "darkness"),('''More precious than gold, but cannot be bought,
Can never be sold, only earned if it’s sought,
If it is broken it can still be mended,
At birth it can’t start nor by death is it ended. What Is It''', "friendship")]
    
    fnme, lnme = display_intro()

    while True: # Main loop to run the program
        score = ask_riddles(riddles)
        cprint(f"You got {score} correct out of {len(riddles)}",'green',attrs=['bold'])
        print(colored("Would you like to play again❔",'green',attrs=['bold'])+colored("(yes/no) ",'cyan'))
        user_ans = input().lower()
        if user_ans == "yes":
            time.sleep(1)
            print(f"Very well {fnme} {lnme}, let's play again...\n")
        else:
            print(f"THE RIDDLER WILL TERMINATE NOW, GOOD-BYE {fnme}...",'white','on_red',attrs=['bold'])
            break
