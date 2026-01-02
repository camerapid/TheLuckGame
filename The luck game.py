import random
import time
from playsound import playsound

def level1(passlist) :
    players=passlist.copy()
    temp=passlist.copy()
    
    while temp:
        
        num=random.randint(0,5)
        chance=5
        ch=random.choice(temp)
        
        while chance>0:
            guess=(input("PLAYER {} pls guess the number  between0-5 :".format(ch)))
            if guess==str(num):
                print("Congratulations!\n\tYou Passed this level\n ")
                playsound("Youlose.mpeg")
                
                #improve
                break
            else:
                print('\nGuessed wrong ... try again !!! ',chance-1," chances left \n")
                if not guess.isnumeric():
                    print("\n\nYou must choose a whole number!!!\n")
            chance-=1
        else:
            print("Sorry {} You are out , You couldnt beat your luck this time.\n Try again later\n".format(ch))
            print("The number is ",num,"\n\n")
            passlist.remove(ch)
            playsound("Youwin.mpeg")
            #if break is used outer loop  is breaked. if not, inner loop continues
        
        temp.remove(ch)#the inner loop is being executed again
    print("Among players - ",players)
    if passlist==[]:
        print("Nobody passed the level")
        print("Give a try Later")
        return
    elif passlist==players:
        print("Everybody Passed The Level\n\\\\\\Cheers///\n")#The Escape sequence for \ is \\ 
    else :   
        print ("players ",passlist,"  Passed Level 1 and entered the next level ")
    level2(passlist)

    
def level2(passlist) :
    
    players=passlist.copy()
    temp=passlist.copy()
    
    while temp:
        
        num=random.randrange(10)
        chance=6
        ch=random.choice(temp)
        
        while chance>0:
            guess=(input("PLAYER {} pls guess the number between 0-10 : ".format(ch)))
            if guess==str(num):
                print("Congratulations!\n\tYou Passed this level\n ")
                playsound("Youlose.mpeg")
                #improve
                break
            else:
                print('Guessed wrong ... try again !!! ',chance-1," chances left \n")
                if not guess.isnumeric():
                    print("\n\nYou must choose a whole number!!!\n")
            chance-=1
        else:
            print("Sorry {} You are out , You couldnt beat your luck this time.\n Try again later\n".format(ch))
            print("The number is ",num,"\n")
            passlist.remove(ch)
            playsound("Youwin.mpeg")
            #if break is used outer loop  is breaked. if not, inner loop continues
        
        temp.remove(ch)#the inner loop is being executed again
    print("\nAmong players - ",players)
    if passlist==[]:
        print("Nobody passed the level")
        ranks(players_list)
        return
    elif passlist==players:
        print("Everybody Passed The Level\n\\\\\\Cheers///\n")#The Escape sequence for \ is \\
    else :   
        print ("players ",passlist,"  Passed Level 2 and entered the next level ")
    level3(passlist)
    
    
def level3(passlist) :
    players=passlist.copy()
    temp=passlist.copy()
    
    while temp:
        
        num=random.randint(1,30)
        chance=8
        ch=random.choice(temp)
        
        while chance>0:
            guess=(input("PLAYER {} pls guess the number between 0-30 : ".format(ch)))
            if guess==str(num):
                print("Congratulations!\n\tYou Passed this level\n ")
                playsound("Youlose.mpeg")
                #improve
                break
            else:
                print('Guessed wrong ... try again !!! ',chance-1," chances left \n")
                if not guess.isnumeric():
                    print("\n\nYou must choose a whole number!!!\n")
            chance-=1
            
        else:
            print("Sorry {} You are out , You couldnt beat your luck this time.\n Try again later\n".format(ch))
            print("The number is ",num,"\n")
            passlist.remove(ch)
            playsound("Youlose.mpeg")
        
        temp.remove(ch)#the inner loop is being executed again
    print("\nAmong players - ",players)
    if passlist==[]:
        print("Nobody passed the level") 
    elif passlist==players:
        print("Everybody Passed The Level\n\\\\\\Cheers///\n")#The Escape sequence for \ is \\
    else :   
        print ("players ",passlist,"  Passed Level 3 and entered the next level ")
        #level3(passlist)
    ranks(players_list)

def ranks(players_list) :
    pass

       
def initiate():
    global players_list
    players_list=[]
    try:
        users_no=int(input("How many users : "))
        for i in range(users_no):
            players_list.append(input("Enter the username {} : ".format(i+1)).title())

        passlist=players_list.copy()
        level1(passlist)

    except:
        print("ERROR ! ! ! \n ---\n\n")
        if not users_no.isnumeric():
            print("Please Enter A whole number for no of users ...\n")
            

if __name__=="__main__":
    initiate()
