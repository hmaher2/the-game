tokens=int(input("enter the number of tokens:")) #the players will enter the number of tokens they want to play with
y=0 #y means the number of tokens that each player will take from the original tokens
x=1 #a counter to detect the winner
while tokens>0:
 if (tokens **.5)%1!=0: #u dont want the game to end so quickly,CMON!!!
  while tokens>0 and tokens!=0: #to prevent "negative" tokens due to a mathmatical mistake
    y=int(input("enter y:")) #y has to be a non zero square number
    if ((y**.5))%1==0: #to cheak that y is a non zero square
        tokens=tokens-y
        print("the number of current tokens:",tokens)
        x=x+1
    else :
        print("ERROR!!enter another number") #in that case the player REALLY REALLY dont know maths :D,get back to grade 5! :p
 else:
    print(" enter another no. of tokens") 
    tokens=int(input())      
if x%2==0:
    print("player 1 WINS!")
else:
    print("player 2 WINS!")
    
