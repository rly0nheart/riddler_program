print("\t\t\t???R1DDL3R!???\n\t\t\tAuthor: >>RLY0NHEART<<\t\t©2020")

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
	print("!!!!!INVALID INPUT!!!!!!😐\n\nBut We Will Continue Though🙂\n\nRiddle Me This:'")

rdlr("==> What swings BACK and FORTH, but NEVER takes you anywhere?")
ua = input()
if ("swing" or "a swing") in ua.lower():
	print("THAT IS CORRECT!😃👏\n\nRiddle Me This:\n\n")
else:
	print("NOPE!      😑THAT IS INCORRECT\n\nTry This Other Riddle:\n\n")
rdlr("==> I am the RED tongue of the EARTH\nthat BURIES cities. What Am I?...")
rdlean = input()
if ("lava" or "lava from a volcano") in rdlean.lower():
	print("IMPRESSIVE! 👏, IT'S CORRECT!\n\nRiddle Me This:\n\n")
else:
	print("THAT IS NOT CORRECT!\n\nTry This Other One:\n\n")
rdlr("==> A part of a BIRD, that is NOT in the SKY\nWhich can SWIM in the OCEANS but ALWAYS stays DRY\nWhat is it?....")
rdleans = input() 
if ("shadow" or "a shadow") in rdleans.lower():
    print("THAT IS CORRECT! 🤓\n\nRiddle Me This:\n\n")
else:
    print("That is INCORRECT!☹️\n\nRiddle Me This:\n\n")

rdlr("==> What is as LIGHT as a FEATHER\nyet NO man can HOLD it?..")
rdleans1 = input()
if rdleans1.lower() == "flame":
    print("EXCELLENT!🤓👏")
else:
    print("THAT IS INCORRECT!😑\n\n Are you sure you want to continue doing this?🤔")
anys = input("Yes/No")
if anys.lower() == "yes":
	print('''\n\nVery well then\n\nRiddle Me This:\n\n==> A box without hinges, key, or lid,
Yet golden treasure inside is hid. What Is It?''')
elif anys.lower() == "no":
	print(rdlr(print(exit)))
else:
	print("!!!!!!INVALID INPUT!!!!!!", rdlr(print(exit)))
rdleans5 = input()
if ("egg" or "an egg") in rdleans5.lower():
    print("MAN YOU'RE GOOD!😃👏, but sadly i gotta go now...Goodbye☹️", exit) #To be continued....
else:
    print("INCORRECT!😐\nTHE RIDDLER WILL TERMINATE NOW,  GOODBYE.......", exit)
#riddler program ends here, for now the developer still digging for riddles :)