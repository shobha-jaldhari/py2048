# py2048
Note: The project was done on WINDOWS

welcome to the game 2048
This is basically a python project for a terminal based 2048 game
version of python uses : Python 3.8

Libraries used:

1.copy

2.os

3.msvcrt

4.random

5.time
 

on running the file on windows command prompt or git CMD(windows)
the user is asked to enter the following:

1.VALUE OF N(for e.g. input 3 gives a board of 3*3)

2.THE VALUE FOR WINNING THE GAME(i.e. the value until which the game should go on)


Press enter after entering the value of n and also after entering the win value


The game starts now with a board of desired number of grids(as per the user)
the user is now expected to play game by entering suitable keys

w  for up 

a for left 

s for down

d for right

THE USER IS NOT REQUIRED TO PRESS ENTER AFTER EVERY INPUT

the game board initially has a randomly located 2..in case of any valid move a random unoccupied grid is occupied by 2. 

if two tiles with same number are merged the number adds up (i.e. becomes double).

If the user enters any key except w,a,s,d, the game displays "enter valid key"  which means add a key among w,a,s and d.

If the board does not change on giving input ....The game displays "invalid move".


User wins the game when tile of winning value is achieved
if no more moves are available then user loses the game(i.e the game displays game over)

In a board of 1*1 :
if the winning value is 2 ..on pressing any of the valid keys the game displays you won
in case of any other value ..on pressing any of the valid keys it displays game over


taking an example of a board where the value of n is 4 and the win value is 16 ....The board is displayed as follows


![WhatsApp Image 2020-05-18 at 22 26 37](https://user-images.githubusercontent.com/64811911/82239958-37776f00-9957-11ea-843e-be7a863a651b.jpeg)

Since the win value is 16..on reaching the tile 16 message displayed is ..."you won"

![WhatsApp Image 2020-05-18 at 22 26 36](https://user-images.githubusercontent.com/64811911/82240237-b076c680-9957-11ea-86b7-ed65d3797c00.jpeg)

lets conider another example where n=2 and win value=64...since all tile are occupied and no move is available the "game over" message is displayed

![WhatsApp Image 2020-05-18 at 22 26 33](https://user-images.githubusercontent.com/64811911/82240344-e9af3680-9957-11ea-946b-dfc16f957751.jpeg)


