import time

def slowprint(s):
    print(s)
    time.sleep(0.5)
def point_buy():
    totalpoints = 27

    strength = 8
    dexterity = 8
    constitution = 8
    intelligence = 8
    wisdom = 8
    charisma = 8


    print("Total Points: " + str(totalpoints) + "\n" + "Strength: " + str(strength) + "\n" + "Dexterity: " + str(dexterity) + "\n" + "Constitution: " + str(constitution)
    +"\n" + "Intelligence: " + str(intelligence) + "\n" + "Wisdom: " + str(wisdom) + "\n" + "Charisma: " + str(charisma) + "\n")
    x = True
    while totalpoints > 0 or x == True:
        statchoice = input("Which stat would you like to increase?(If you want to subtract points simply put in a negative "
        "number or quit if you want to quit)\n").lower()

        if statchoice == "strength":
            points = input("How many points would you like to put in strength?\n")
            strength += int(points)
            totalpoints -= int(points)
            print("Total points: " + str(totalpoints) + "/27")

        elif statchoice == "dexterity":
            points = input("How many points would you like to put in dexterity?\n")
            dexterity += int(points)
            totalpoints -= int(points)
            print("Total points: " + str(totalpoints) + "/27")
            print("Dexterity: " + str(dexterity))

        elif statchoice == "constitution":
            points = input("How many points would you like to put in constitution?\n")
            constitution += int(points)
            totalpoints -= int(points)
            print("Total points: " + str(totalpoints) + "/27")
            print("Constitution: " + str(constitution))

        elif statchoice == "intelligence":
            points = input("How many points would you like to put in intelligence?\n")
            intelligence += int(points)
            totalpoints -= int(points)
            print("Total points: " + str(totalpoints) + "/27")
            print("Intelligence: " + str(intelligence))

        elif statchoice == "wisdom":
            points = input("How many points would you like to put in wisdom?\n")
            wisdom += int(points)
            totalpoints -= int(points)
            print("Total points: " + str(totalpoints) + "/27")
            print("Wisdom: " + str(wisdom))

        elif statchoice == "charisma":
            points = input("How many points would you like to put in charisma?\n")
            charisma += int(points)
            totalpoints -= int(points)
            print("Total points: " + str(totalpoints) + "/27")
            print("Charisma: " + str(charisma))

        elif statchoice == "quit":
            slowprint("You quit")
            break

        else:
            slowprint("That is not a valid input")
            continue



        finished = input("Are you finished?\n").lower()

        if finished == "yes":
            totalpoints = -1
            x = False
            print("Done")
        else:
            x = True
            print("Continue")

    slowprint("\nStrength: " + str(strength) + "\n" + "Dexterity: " + str(dexterity) + "\n" + "Constitution: " + str(constitution)
    + "\n" + "Intelligence: " + str(intelligence) + "\n" + "Wisdom: " + str(wisdom) + "\n" + "Charisma: " + str(charisma) + "\n")

    charismamodifier = int(charisma / 2 - 5)
    wisdommodifier = int(wisdom / 2 - 5)
    intelligencemodifier = int(intelligence / 2 - 5)
    constitutionmodifier = int(constitution / 2 - 5)
    dexteritymodifier = int(dexterity / 2 - 5)
    strengthmodifier = int(strength / 2 - 5)

    if strengthmodifier < 0:
        slowprint("Strength Modifier: " + str(strengthmodifier))
    else:
        slowprint("Strength Modifier: +" + str(strengthmodifier))

    if dexteritymodifier < 0:
        slowprint("Dexterity Modifier: " + str(dexteritymodifier))
    else:
        slowprint("Dexterity Modifier: +" + str(dexteritymodifier))

    if constitutionmodifier < 0:
        slowprint("Constitution Modifier: " + str(constitutionmodifier))
    else:
        slowprint("Constitution Modifier: +" + str(constitutionmodifier))

    if intelligencemodifier < 0:
        slowprint("Intelligence Modifier: " + str(intelligencemodifier))
    else:
        slowprint("Intelligence Modifier: +" + str(intelligencemodifier))

    if wisdommodifier < 0:
        slowprint("Wisdom Modifier: " + str(wisdommodifier))
    else:
        wisdommodifier = "+" + str(wisdommodifier)
        slowprint("Wisdom Modifier: " + str(wisdommodifier))

    if charismamodifier < 0:
        slowprint("Charisma Modifier: " + str(charismamodifier))
    else:
        charismamodifier = "+" + str(charismamodifier)
        slowprint("Charisma Modifier: " + str(charismamodifier))

point_buy()