Name: Sophia Cheng, Christian Garcia, Hanae Sugiura
Course: CS 5 Gold 

Our game utilizes the menu option that we used for one of the homework assignments on stock market prices.
The menu presents four options to the user for playing Connect Four: human against human, human against AI, AI against AI, and grutor against AI.
The user will be able to choose the ply that the AI plays with and the checker that they would like to play with. 
We chose the first option for the extension part of the final project and implemented Connect Four in VPython. 
We encountered some troubles getting the VPython to work: the board (code below) works alone in VPython and the board and player class code for Connect Four 
work in python perfectly. However, they don't work together in VPython - we keep getting an error message. We spent more than 6 hours on trying to debug it, but we don't know
what exactly is causing the bug in VPython. 

We built the board as follows:
for row in range(0,8):
    mybox = box(  pos=vec(0,0,-(row/2)*5 + row *5 ),  axis=vec(1,0,0),  size=vec(20,5, 1) )
myhbox = box(  pos=vec(-10,0,8.75 ),  axis=vec(0,0,1),  size=vec(18.5,5, 1))
for row in range(7):
    for col in range(6):
        myX = sphere(  pos=vec(-8 + 2.5*col,0,1.2+ row*2.5 ),  axis=vec(0,0,1),  size=vec(1.5,1.5,1.5), color=vec(150,0,0 ))

We then put in the code for the game (the one in final.py) in VPython.
We inserted the the following for loop in the playGame method so that each time player chooses a column, a sphere would be added to the board on VPython:
 for row in range(7): 
                for col in range(6):
                    if D[row][col] == 'X':
                        myX = sphere(  pos=vec(-8 + 2.5*col,0,1.2+ row*2.5 ),  axis=vec(0,0,1),  size=vec(1.5,1.5,1.5), color=vec(150,0,0 ))
                    elif D[row][col] == 'O':
                        myX = sphere(  pos=vec(-8 + 2.5*col,0,1.2+ row*2.5 ),  axis=vec(0,0,1),  size=vec(1.5,1.5,1.5), color=vec(0,0,0 ))
                    