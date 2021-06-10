guess= None
value=10
live= 5
print("WELCOME TO OUR GAME")


while live > 0:
    print('Your life is {} '.format(live))
    guess = int(input("enter a number: "))
    
    if guess == value:
        print('you win')
        break
    else:
        live-=1

    







