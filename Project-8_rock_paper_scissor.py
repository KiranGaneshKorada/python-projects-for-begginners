# it is a simple rock , paper and scissor game

import random


def rps():
    your_score=0
    bot_score=0
    option=["rock","paper","scissor"]

    while your_score<3 and bot_score<3:

        user=input("select rock , paper or scissor")

        random.shuffle(option)

        bot=random.choice(option)

        user=user.lower()
        bot=bot.lower()

        if user==bot:
            print("no change both chose same option {}\n\n".format(user))
        elif user=="rock" and bot=="scissor":
            print("you hit the scissor and scissor broke")
            your_score=your_score+1
        elif user=="paper" and bot=="rock":
            print("you rolled stone with your paper")
            your_score=your_score+1
        elif user=="scissor" and bot=="paper":
            print("you cut the paper into pieces")
            your_score=your_score+1
        else:
            print("oh no!! your {} got hit with {}".format(user,bot))
            bot_score=bot_score+1

        print("current scores are YOU={}  \t  BOT={}\n\n".format(your_score,bot_score))

    if  your_score==3:
        print("CONGOOO YOU WON!!\n\n\n")
    else:
        print("Oh shit computer wont the game BETTER LUCK NEXT TIME DEAR\n\n")


print("welcome to rock , paper and scissors game \n\n")

print("you versus computer\n\n")

rps()



