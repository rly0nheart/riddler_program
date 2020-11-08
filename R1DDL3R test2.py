def display_intro():
    """
    Displays the introduction text and asks user for their name.
    Returns the users' name
    """
    print("\033[1;33;40m\t\t\t???R1DDL3R???\n\t\t\tAuthor: >>RLY0NHEART<<\t\t©2020")
    print("What is your name?🙂")
    user_name = input()
    print(f"Hello {user_name}, Nice to meet you!😃\n" + "I am THE RIDDLER\nI will be asking you riddles then you should reply with\ncorrect answers, it's simple!🙂\n")
    print("Are you ready to get R1DDL3D?")
    user_input = input().lower()
    if user_input == "yes":
        print("Okay😃, Riddle me this:\n\n")
    elif user_input == "no":
        print("Hahaha😅 no way!, you just started you can't quit now\n\n \nJust try answering this simple riddle:\n\n")
    else:
        print("\033[0;37;41mINVALID INPUT!" + "\033[1;33;40m\n\nBut We Will Continue Though🙂\n\n")
    return user_name

def ask_riddles(riddles):
    """
    Loops through each question & answer in riddles
    Returns score, the number of riddles answered correctly
    """
    score = 0
    for question, answer in riddles:
        print("Riddle Me This:")
        print(f"==> {question}?...")
        user_input = input().lower()
        if answer in user_input:
            print("\033[0;30;42mTHAT IS CORRECT!😃👏\n\n")
            print("\033[1;33;40m")
            score +=1
        else:
            print("\033[0;37;41mTHAT IS INCORRECT!😐\n\n")
            print("\033[1;33;40m")
    return score


if __name__ == '__main__':
    # Riddles is a list of tuples where each tuple contains question & answer
    riddles = [
        ("What is it that no man wants, but no man wants to lose", "a lawsuit"), ('''I can be long, or I can be short. I can\nbe grown, and I can be bought. Ican be painted, or left bare. I can be round, or square. What am I''', "fingernails"), ("What flies BACK and FORTH, but NEVER takes you anywhere", "a swing"), ("I'm round at the ends and high in the middle. What am I", "ohio"), ('''A home of wood in a wooden place, but built not by hand. High abovethe earthen ground, it holds its pale blue gems. What is it''', "a nest"), ('''My sides are firmly laced about,Yet nothing is within;You'll think my head is strange indeed,Being nothing else but skin. What Am I''', "a drum"), ("One strand dangles. Two strands twist. Three or more can\nfashion this. What Is It", "braids"), ("I am green but not a tree. And I grow around the world. What am I", "grass"), ("""What word of five letters has only one left when two letters areremoved""", "stone"), ('''Take away my first letter and I remain the same. Take away my lastletter and remain unchanged. Remove all my letters and I’m still me.
What am I''', "a mailman"), ("If I have it, I don’t share it. If I share it, I don’t\nhave it. What is it", "a secret"), ("I am the RED tongue of the EARTH\nthat BURIES cities. What Am I", "lava"), ('''At the sound of me, men may dreamOr stamp their feet. At the sound of me, women may laugh
Or sometimes weep. What Am I''', "music"), ("""What has roots as nobody sees, Is taller than trees,
Up, up it goes
And yet never grows?""", "a mountain"), ("Twigs and spheres and poles and plates, join and bind to\nreason make. What Is It", "a skeleton"), ("What's made of wood but can't be sawed", "sawdust"), ("A box without hinges, key, or lid,\nYet golden treasure inside is hid. What Is It", "an egg"), ("A crime that is punishable if attempted but not punishable\nwhen it is actually committed. What Is It", "suicide"), ("""It cannot be seen, cannot be felt
Cannot be heard, cannot be smelt.
 It lies behind stars and under hills,
 And empty holes it fills.
 It comes first and follows after,
 Ends life, kills laughter. What Is It""", "darkness"), ('''More precious than gold, but cannot be bought,
Can never be sold, only earned if it’s sought,
If it is broken it can still be mended,
At birth it can’t start nor by death is it ended. What Is It''', "friendship")]
    
    user_name = display_intro()

    while True: # Main loop to run the program
        score = ask_riddles(riddles)
        print(f"You got {score} correct out of {len(riddles)}")
        print("Would you like to play again? (yes/no)")
        user_ans = input().lower()
        if user_ans == "yes":
            print(f"Very well {user_name}, let's play again...\n")
        else:
            print(f"\033[0;37;41mTHE RIDDLER WILL TERMINATE NOW, GOODBYE {user_name}...","\033[1;33;40m")
            break