import random

def toss():
    print("its Toss time")
    n=random.randint(0,1)
    toss_process(n) 
    
def toss_process(n):
    t=int(input("enter 1 to selelct HEAD ,0 to select TAIL"))
    if(t==n):
        print("congo!! u won the toss")
        select()
    elif t<0 or t>1 :
        print("Invalid responce enter again")
        toss_process(n)
    elif n==0:
        print(" oh no computer won the toss and choose to bat first")
        ch=0
        comp_bat(ch)
    elif n==1:
        print(" oh no computer won the toss and choose to bowl first")
        ch=1
        comp_bowl(ch)

def select():
    ch=int(input("enter 1 to BAT or 0 to BOWL"))
    if( ch<0 or ch>1):
        print("Invalid responce enter again")
        select()
    elif ch==0:
        user_bowl(ch)
    else:
        user_bat(ch)

def user_bowl(ch):
    print("are u ready to bowl")
    print("game is on")
    target=0
    score=0
    bowling(target,ch,score)
    

def user_bat(ch):
    print("are u ready to bat")
    print("game is on")
    target=0
    score=0
    batting(target,ch,score)

def comp_bat(ch):
    print("are u ready to bowl")
    print("game is on")
    score=0
    target=0
    bowling(target,ch,score)

def comp_bowl(ch):
    print("are u ready to bat")
    print("game is on")
    target=0
    score=0
    batting(target,ch,score)

def batting(target,ch,score):
    if (ch==0) and score>=target:
        print("congo!! u chased the target and u WON")
        return
    comp_num=random.randint(1,10)
    num=int(input("enter any number ranging 1-10"))
    if(num<1 or num>10):
        print("Invalid responce enter again")
        batting(target,ch,score)
    elif (comp_num==num) and (ch==1):
        print("oh no u got out")
        target=score+1
        score=0
        print("the target is"+str(target))
        print("get ready to bowl")
        bowling(target,ch,score)
    elif ch==0 and comp_num==num:
        print("oops!! u got bowled")
        print("computer won the game better luck nxt time")
    else:
        score=score+num
        print("the current score is= "+str(score))
        batting(target,ch,score)

def bowling(target,ch,score):
    comp_num=random.randint(1,10)
    num=int(input("bowl any number ranging 1-10"))
    if(num<1 or num>10):
        print("Invalid responce enter again")
        bowling(target,ch,score)
    elif (score>=target) and ch==1:
        print("oh no you lost the match")
        print("Better luck next time")
    elif comp_num==num and (ch==1):
         print("computer got bowled \nCongratulations you won the match")
    elif comp_num==num and ch==0:
         print("ayy!! u took a wicket") 
         target=score+1
         score=0
         print("u need to score "+str(target)+" runs to win")    
         batting(target,ch,score)   
    else:
        score=score+comp_num
        print("still"+str(target-score)+"runs need to be chased")
        bowling(target,ch,score)

print("Welcome to handcricket game")
toss()
    