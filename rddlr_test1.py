print("\033[1;33;40m\t\t\t???R1DDL3R!???\n\t\t\tAuthor: >>RLY0NHEART<<\t\t©2020")

def rdlr(rdle):
#riddles will be called as arguements, and a user has to enter answer to get the next riddle
    print(rdle)
rdlr("What is your name?🙂")
usnm = input()
print("Hello " + usnm + ", Nice to meet you!😃\n" + "I am THE RIDDLER\nI will be asking you riddles then you should reply with\ncorrect answers, it's simple!🙂\n")
rdlr("Are you ready to get R1DDL3D?")
usan = input()
if usan.lower() == "yes":
    print("Okay😃, Riddle me this:\n\n")
elif usan.lower() == "no":
    print("Hahaha😅 no way!, you just started you can't quit now\n\n \nJust try answering this simple riddle:\n\n")
else:
	print("\033[0;37;41m INVALID INPUT      \033[0m")
	print("\033[1;33;40m\n\nBut We Will Continue Though🙂\n\nRiddle Me This:'")

rdlr("==> What swings BACK and FORTH, but NEVER takes you anywhere?")
ua = input()
if ("swing" or "a swing") in ua.lower():
	print("\033[0;30;42mTHAT IS CORRECT!😃")
	print("\033[1;33;40m\n\nRiddle Me This:\n\n")
else:
	print("\033[0;37;41mNOPE!, THAT IS INCORRECT      \033[0m")
	print("\033[1;33;40m\n\nTry This Other Riddle:\n\n")
rdlr("==> I am the RED tongue of the EARTH\nthat BURIES cities. What Am I?...")
rdlean = input()
if ("lava" or "lava from a volcano") in rdlean.lower():
	print("\033[0;30;42mIMPRESSIVE!,  IT'S CORRECT!😃")
	print("\033[1;33;40m\n\n\nRiddle Me This:\n\n")
else:
	print("\033[0;37;41mTHAT IS NOT CORRECT!    \033[0m")
	print("\033[1;33;40m\n\nTry This Other One:\n\n")
rdlr("==> A part of a BIRD, that is NOT in the SKY\nWhich can SWIM in the OCEANS but ALWAYS stays DRY\nWhat is it?....")
rdleans = input() 
if ("shadow" or "a shadow") in rdleans.lower():
    print("\033[0;30;42mTHAT IS CORRECT!😃")
    print("\033[1;33;40m\n\n\n\nRiddle Me This:\n\n")
else:
    print("\033[0;37;41mINCORRECT!\033[0m")
    print("\033[1;33;40m\n\nRiddle Me This:\n\n")

rdlr("==> What is as LIGHT as a FEATHER\nyet NO man can HOLD it?..")
rdleans1 = input()
if ("flame" or "a flame") in rdleans1.lower():
    print("\033[0;30;42mEXCELLENT!🤓👏")
    print("\033[1;33;40m")
else:
    print("\033[0;37;41mTHAT IS INCORRECT!")
rdlr("\n Are you sure you ready for the next riddle?\033[0m\n")
anys = input()
if anys.lower() == "yes":
	print('''"\033[1;33;40m\n\nVery well then\n\nRiddle Me This:\n\n==> A box without hinges, key, or lid,
Yet golden treasure inside is hid. What Is It?''')
elif anys.lower() == "no":
	print(rdlr(print(quit)))
else:
	print("\033[0;37;41mINVALID INPUT\033[0m", rdlr(print(exit)))
rdleans5 = input()
if rdleans5.lower() == "an egg":
    print("\033[0;30;42mMAN YOU'RE GOOD!😃👏, but sadly i gotta go now...Goodbye☹️", exit) #To be continued....
else:
    print("\033[0;37;41mTHAT IS WRONG!\033[0m")
    print("\033[0;37;41m\nTHE RIDDLER WILL TERMINATE NOW,  GOODBYE.......", exit)
#riddler program ends here, for now the developer still digging for riddles :)