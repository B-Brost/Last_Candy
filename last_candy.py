"""
last_candy.py
Brianna Brost
10/28/22
This program is a two-player game where players take turns removing candy from boxes. The player who takes the last candy wins the game.
"""
#describes game, asks names
print("\n“Last Candy” which is a two-player game.  The game is played as follows. \nYou choose the number of boxes of candy you want, and each box contain however many pieces of candy you would like. \nAt each player/'s turn, the player has to remove some candy from one of the boxes. The player can choose the box and the number of pieces of candy to remove from that box. \nThe player who takes the last piece of candy wins the game.")
player1=str(input("Player 1, what is your name? "))
player2=str(input("Player 2, what is your name? "))
#starts lists
boxes=(int(input("How many boxes you would like? ")))
candy_per_box=(int(input("How many candy you would like per box? ")))
candies=[]
for number in range(boxes):
    candies.append(candy_per_box)
def display_game(boxes:int,candies:list)->None:
    #shows the boxes parameters are int and list returns nothing
    for i in range (boxes):
        print(f"|   {candies[i]}   |",end='')
turn=1
display_game(boxes,candies)
while True:
    print(f"\n \nYou are on turn {turn}")
    turn+=1
    for turns in range (2):
        if turns==0:
            #asks for box number until valid answer
            box=int(input(f"\n{player1}, Which box would you like to remove candy from? "))
            good_box=False
            while not good_box:
                if box>boxes or box<1:
                    box=int(input("That is not a valid box number, try again. "))
                elif candies[box-1]==0 and box<=boxes and box>0:
                    box=int(input("That box is empty, try again. "))
                else:
                    good_box=True
            #asks for candy number until valid answer
            remove=int(input(f"\n{player1} How many candies would you like to remove? "))
            good_num=False
            while not good_num:
                if remove>candies[box-1]:
                    remove=int(input("There are not that many candies in that box. Try again: "))
                elif remove<0:
                    remove=int(input("What are you doing, you can't subtract a negative number. Try again: "))
                elif remove==0:
                    remove=int(input("You have to take candies out, try again: "))
                else:
                    good_num=True
            add=candies[box-1]
            add-=remove
            candies.pop(box-1)
            candies.insert(box-1,add)
            display_game(boxes,candies)
        else:
            #asks for box number until valid answer
            box=int(input(f"\n{player2}, Which box would you like to remove candy from? "))
            good_box=False
            while not good_box:
                if box>boxes or box<1:
                    box=int(input("That is not a valid box number, try again. "))
                elif candies[box-1]==0 and box<=6 and box>0:
                    box=int(input("That box is empty, try again. "))
                else:
                    good_box=True
            #asks for candy number until valid answer
            remove=int(input(f"\n{player2} How many candies would you like to remove? "))
            good_num=False
            while not good_num:
                if remove>candies[box-1]:
                    remove=int(input("There are not that many candies in that box. Try again: "))
                elif remove<0:
                    remove=int(input("What are you doing, you can't subtract a negative number. Try again: "))
                elif remove==0:
                    remove=int(input("You have to take candies out, try again: "))
                else:
                    good_num=True
            add=candies[box-1]
            add-=remove
            candies.pop(box-1)
            candies.insert(box-1,add)
            display_game(boxes,candies)
        if candies.count(0)==boxes:
            if turn==0:
                print(f"\n \n \nCongradulations, {player1}, you are the winner!")
                exit()
            else:
                print(f"\n \n \nCongradulations, {player2}, you are the winner!")
                exit()