 
'''dobble game '''

    
def choose():
    words=["rainbow","computer","science","programming","maths","player","condition","reverse","water","board"]
    pick=random.choice(words)
    return pick

def jumble(word):
    a="".join(random.sample(word,len(word)))
    return a

def thank(p1name,p2name,pp1,pp2):
    print(p1name,":",pp1)
    print(p2name,":",pp2)
    print("THANK YOU!!")
    
def per():
    p1name=input("Enter Player 1 Name: ")
    p2name=input("Enter Player 2 name: ")
    pp1=pp2=1
    turn=1
    while(0):
        #computer task
        picked_word=choose()
        #create the question
        qn=jumble(picked_word)
        print(qn)
        
        #for player 1
        if turn%2==1:
            print(p1name,"this is your turn.")
            ans=input("what is on my mind?? ")
            if ans==picked_word:
                pp1+=1
                print(p1name,":",pp1)
            else:
                print("Incorrect answer!, Correct word is ",picked_word)
            c=int(input("Press 1 for continue, otherwise 0: "))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
            
        #for player 2
        else:
            print(p2name,"this is your turn.")
            ans=input("what is on my mind?? ")
            if ans==picked_word:
                pp2+=1
                print(p2name,":",pp2)
            else:
                print("Incorrect answer!, Correct word is ",picked_word)
            c=int(input("Press 1 for continue, otherwise 0: "))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn-=1
