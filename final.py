import random


def fun():
    fgh = input("Where do you want to go? (A:Gym, B:Arcade) ")
    print()
    if fgh.upper() == "A":
        print("You head to the gym to get a workout in")
        print("While you are working out, you need to use the bathroom.")
        print()
        cxn = input("Do you go to the bathroom? (A:yes, B:no) ")
        if cxn.upper() == "A":
            print("You go to the bathroom and after, get back to your workout.")
            print("You finish your workout and go home")
            print()
            print("You got the good ending!")
            # ending
        elif cxn.upper() == "B":
            print("While doing the rest of your workout, a tiktoker comes up to you and asks")
            print()
            print("'Hey if you can beat me at any lift of your choice, ill give you 500 dollars'")
            print()
            print("He shows you the 500 in cash he has")
            cnm = input("What will you do? (A:Do the tiktok challenge, B:Grab the cash and run) ")
            print()
            if cnm.upper() == "A":
                print("You accept the tiktok challenge, and he asks what exercise you want to do")
                nv = input("What will you do? (A:Calf raises, B:Bench press")
                if nv.upper() == "A":
                    print("You guys do the challenge and you end up winning")
                    print("'Wow, I can't believe you won'")
                    print("' I guess Im not as strong as I thought '")
                    print("He walks away disappointed after giving you the cash")
                    print()
                    print("You got the ego crusher ending!")
                    quit()
                    # ending
                elif nv.upper() == "B":
                    print("You guys do the challenge and you lose")
                    print("'Damn you are really weak bro'")
                    print("You get sad and go home without finishing your workout")
                    print()
                    print("You got the ego crushed ending!")
                    quit()
                    # ending
            elif cnm.upper() == "B":
                print("You grab the cash and dash away from him")
                print("'HEY COME BACK HERE'")
                print()
                ns = input("What will you do? (A:Keep running, B:Go and return the money) ")
                if ns.upper() == "A":
                    print(" You keep running from the guy and run out of the gym")
                    print("You see him walk back into the gym and you leave")
                    print()
                    print("You got the scammer ending!")
                    quit()
                    # ending
                elif ns.upper() == "B":
                    print("You turn around and give the money back to the tiktoker")
                    print("He snatches the money from your hand and walks away")
                    print("A gym employee walks up to you and asks you to leave.")
                    print()
                    print("You got the Kicked out ending!")
                    quit()

    elif fgh.upper() == "B":
        print()


def rps():
    user = 0
    comp = 0
    choices = ["rock", "paper", "scissors"]

    while True:
        user_throw = input("If you want to play, type Rock, Paper, or Scissors. If you want to quit or check score type Q ").lower()
        if user_throw == "q":
            break
        if user_throw not in choices:
            print("Please type rock, paper or scissors")
            continue
        rt = random.randint(0, 2)
        comp_throw = choices[rt]
        print("Computer threw " + str(comp_throw))

        if user_throw == "rock" and comp_throw == "scissors":
            print("You won!")
            user += 1
        if user_throw == "paper" and comp_throw == "rock":
            print("You won!")
            user += 1
        if user_throw == "scissors" and comp_throw == "paper":
            print("You won!")
            user += 1
        if user_throw == "rock" and comp_throw == "paper":
            print("You lost!")
            comp += 1
        if user_throw == "scissors" and comp_throw == "rock":
            print("You lost!")
            comp += 1
        if user_throw == "paper" and comp_throw == "scissors":
            print("You lost!")
            comp += 1
        if user_throw == "scissors" and comp_throw == "scissors":
            print("It's a tie!")
        if user_throw == "paper" and comp_throw == "paper":
            print("It's a tie!")
        if user_throw == "rock" and comp_throw == "rock":
            print("It's a tie!")
        again = input("Want to play again? ")
        if again.lower() == "yes":
            continue
        else:
            return user, comp


def work():
    print("You make it to the McDonalds and clock in.")
    print("Your shift is pretty normal except for one customer")
    print()
    print(f"'I can't believe you got my order wrong! {name}, you do not know how to do your job! Let me speak to your manager")
    print()
    dsa = input("What will you do? (A:Ignore them, B:Get your manager, C:Fight them) ")
    print()
    if dsa.upper() == "A":
        print("You ignore the annoying customer and they get angry")
        print()
        print(f"'STOP IGNORING ME {name}'")
        print()
        print("They come up to you and punch you. People start filming")
        print()
        cx = input("What will you do? (A: Hit them back, B: Stand there and get beat ")
        if cx.upper() == "A":
            print("You beat the customer so bad that they start bleeding and they die.")
            print("The people filming have called the police and they are on the way")
            print()
            jk = input("What will you do? (A:Run, B:Accept your fate and wait for the police)")
            if jk.upper == "A":
                print("You dash out of the McDonalds and see the police coming.")
                print("You run away and go into a life of hiding")
                print()
                print("You got the criminal ending!")
                quit()
                # ending
            elif jk.upper() == "B":
                print("You stand over the customers dead body while waiting for the police.")
                print("They arrive and you are taken away, but not before a cop shoots a customer for some reason.")
                print()
                print("You got the arrested ending!")
                quit()
                # ending
        elif cx.upper() == "B":
            print("You stand there as the customer beats you until a bystander comes up and pulls them off of you.")
            print("The police come and take the customer away.")
            print("You black out from the customers beating.")
            print()
            print()
            print()
            print("You wake up in the hospital and see on social media that the video of you getting beat has gone viral.")
            print("Everyone is on your side and they even started a gofund me for you")
            print("You collect the donations from the gofund me and use them to make sure the customer never gets out of prison!")
            print()
            print("You got the sympathy ending!")
            quit()
            # ending
    elif dsa.upper() == "B":
        print("You go get your manager and walk away from the customer")
        print("After they finish speaking, your manager comes up to you")
        print()
        print("'Get your stuff, you're fired'")
        print()
        ds = input("What will you do? (A:Go home, B:Get on demon time 😈")
        if ds.upper() == "A":
            print("You walk outside of the McDonalds and you think to yourself")
            eu = input("What will you do? (A:Go home, B:Go to the gym)")
            if eu.upper() == "A":
                print("You get back to your house and relax for the day")
                print()
                print("You got the fired ending!")
                quit()
            else:
                fun()
        elif ds.upper() == "B":
            print("You go into the kitchen, but instead of going to the break room and grabbing your things, you get a knife.")
            print("You walk back out and stab your manager")
            print("Everyone starts screaming")
            kl = input("What will you do? (A:Run away, B:Cant leave witnesses)")
            if kl.upper() == "A":
                print("You run out of the Mcdonalds and go into hiding to escape the police.")
                print()
                print("You got the into hiding ending!")
                quit()
            # ending
    else:
        print("You beat the customer so bad that they start bleeding and they die.")
        print("The people filming have called the police and they are on the way")
        print()
        jk = input("What will you do? (A:Run, B:Accept your fate and wait for the police) ")
        print()
        if jk.upper() == "B":
            print("You stand over the customers dead body while waiting for the police.")
            print("They arrive and you are taken away, but not before a cop shoots a customer for some reason.")
            print()
            print("You got the arrested ending!")
            quit()
            # ending

        else:
            print("You dash out of the McDonalds and see the police coming.")
            print("You run away and go into a life of hiding")
            print()
            print("You got the criminal ending!")
            quit()
            # ending


def game():
    print()
    print()
    print()
    print("You wake up at 7:00 AM, like always. You have work in a few hours, and you really don't feel like going")
    first_choice = input("What will you do? (A: Go to work, B: Don't go to work) ")
    if first_choice.upper() == "A":
        print("You get ready and go to work")
        a = input("How do you get to work? (A: Drive, B: Public transport/walk) ")
        print()
        if a.upper() == "A":
            print("You get into your 2004 Toyota corolla.")
            print()
            asd = [1, 2, 3, 4, 5, 6]
            bruh = random.choice(asd)
            if bruh == 1:
                print("You got into a car crash and died :(")
                print()
                print("You got the car crash ending!")
                quit()
                # ending
            else:
                work()

        elif a.upper() == "B":
            print("You hop on the bus and see there are seats in the front and back.")
            b = input("Where do you want to sit? (A:Front, B:Back) ")
            print()
            if b.upper() == "A":
                print("You take seat at the very front of the bus.")
                print("After a while, the bus fills up, and an old lady comes and asks for your seat.")
                print()
                c = input("What will you do? (A: Give up your seat, B: Stand on bidness) ")
                print()
                if c.upper() == "A":
                    print("You give your seat up and she thanks you.")
                    print("A stop before you get off, a man walks in with a gun and yells 'THIS IS A HIJACKING' and shoots you")
                    print()
                    print("You got the hijacking ending!")
                    quit()
                    # ending
                elif c.upper() == "B":
                    print("The people on the bus look at you weird and the grandma gets angry.")
                    d = input("What will you do? (A: ignore her, B: stand up and fight")
                    print()
                    if d.upper() == "A":
                        print("She walks away and asks someone else for their seat.")
                        print("You make it to the McDonalds and clock in.")
                        work()
                    elif d.upper() == "B":
                        print("You stand up and roll your sleeves up")
                        print("The grandma gets so afraid that she has a heart attack and dies.")
                        print()
                        print()
                        print("You make it to the McDonalds and clock in.")
                        work()
            elif b.upper() == "B":
                print("You take a seat at the back of the bus")
                print("While on the way to work, a guy next to you starts asking to play rock paper scissors")
                print()
                kl = input("What will you do? (A:Play, B: Dont")
                print()
                if kl.upper() == "A":
                    rps()
                    print("'That was fun!'")
                    print("The rest of your bus ride is normal and you get off at your stop")
                    print()
                    work()
                elif b.upper() == "B":
                    print("Well, if you don't want to play, I have an offer for you")
                    print("Have you ever heard of herbalife?")
                    print()
                    foe = input("Do you listen to his yapping? (A:Yes, B:No) ")
                    print()
                    if foe.upper() == "A":
                        print("*He proceeds to yap*")
                        print("'And to start you off, here is 10k'")
                        print()
                        er = input("Do you take it? (A:yes, B:no) ")
                        print()
                        if er == "A":
                            print("You take the 10k and go to work")
                            work()
                        elif er == "B":
                            print("'Oh, I guess you dont wanna join herbalife'")
                            print("He gets off the bus right before you and you go to work")
                            work()

                    elif foe.upper() == "B":
                        print("He gets mad that you won't listen to him")
                        print("'Why won't you listen to me about herbalife'")
                        print("He punches you and starts to beat you")
                        print("After beating you till you bleed he yells,")
                        print("'WHY DID YOU MAKE ME DO THIS, YOU COULD HAVE JUST LISTENED'")
                        print()
                        print("You bleed out and die")
                        print()
                        print("You got the dead ending!")
                        quit()
                        # ending

    elif first_choice.upper() == "B":
        print("You decide to go to the gym instead of work")
        fun()


x = input("Hello! Welcome to my story game! Would you like to play? ")
if x.lower() == "yes":
    print("Okay! Let us begin")
    y = input("What is your name? ")
    name = y
    print(f"Alright {name}, let's go!")
    game()
else:
    quit()
