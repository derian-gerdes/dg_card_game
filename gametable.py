"""
File: gametable.py
Author: Derian Gerdes
Last Date Edited 4/28/21

This program makes a game based on the card game War. The player with the
high cardin each hand gains a point, and the most points at the end wins.
Aces are played low.

"""
from cards import Card, Deck
from breezypythongui import EasyFrame
from tkinter import PhotoImage


class GameTable(EasyFrame):
    '''Displays the card game'''

    def __init__(self):
        '''Sets up the window and widgets'''
        EasyFrame.__init__(self, title = "Modified War")

        self.cardLabels = []
        self.computerPts = 0
        self.playerPts = 0

        #First five cards are the computer
        self.computerLabel = self.addLabel(text="Computer", row = 0,
                                           column = 0, sticky="NESW")
        self.cardLabels.append(self.addLabel(text="", row = 0, column = 1))

        #Second five cards are the player
        self.playerLabel = self.addLabel(text="Player", row = 1,
                                         column = 0, sticky="NESW")
        self.cardLabels.append(self.addLabel(text="", row = 1, column = 1))

        #Points Labels
        self.computerPointLabel = self.addLabel(text=str(self.computerPts)+" Points",
                                                row = 0, column = 2,
                                                sticky="NESW")
        self.playerPointLabel = self.addLabel(text=str(self.playerPts)+" Points",
                                              row = 1, column = 2,
                                              sticky="NESW")
        self.endGameLabel = self.addLabel(text="", row = 4, column = 1,
                                          sticky="NESW")

        #Beginning
        self.deck = Deck()
        self.deck.shuffle()
        self.computer = []
        self.player = []
        
        #Sets the backing image of the cards
        self.imgs = []
        self.backing = PhotoImage(file="DECK/b.gif")
        for i in range(2):
            self.imgs.append(self.backing)
            self.cardLabels[i]["image"] = self.backing

        #Creates the buttons
        self.newGameButton = self.addButton(text="New Game", row = 3,
                                            column = 0,command = self.newGame)
        self.newHandButton = self.addButton(text="New Hand", row = 3,
                                            column = 2,command = self.startHand)

    def newGame(self):
        '''Starts a new game'''
        self.deck = Deck()
        self.deck.shuffle()
        self.computer = []
        self.player = []
        self.imgs = []
        self.computerPts = 0
        self.playerPts = 0
        self.computerPointLabel["text"] = str(self.computerPts)+" Points"
        self.playerPointLabel["text"] = str(self.playerPts)+" Points"
        self.endGameLabel["text"] = ""
        self.endGameLabel = self.addLabel(text="", row = 4,
                                                   column = 1, sticky="NESW",
                                                   background = "white",
                                                   foreground = "black")

        for i in range(2):
            self.imgs.append(self.backing)
            self.cardLabels[i]["image"] = self.backing

        self.newHandButton["state"] = "normal"

    def startHand(self):
        '''Starts a new hand'''
        self.computer = []
        self.player = []
        if len(self.deck) < 2:
            self.newHandButton["state"] = "disabled"
            #Shows who won the game
            if self.playerPts > self.computerPts:
                self.endGameLabel = self.addLabel(text="Congrats!" +
                                                  " The player won!", row = 4,
                                                  column = 1, sticky="NESW",
                                                  background = "green",
                                                  foreground = "white")
            elif self.computerPts > self.playerPts:
                self.endGameLabel = self.addLabel(text="Oh no!" +
                                                  " The computer won!", row = 4,
                                                  column = 1, sticky="NESW",
                                                  background = "red",
                                                  foreground = "white")
            elif self.playerPts == self.computerPts:
                self.endGameLabel["text"] = "It's a tie!"
            return
        
        #Places the cards into the hand    
        for i in range(1):
            self.computer.append(self.deck.deal())
            self.imgs[i] = PhotoImage(file=self.computer[i].getImg())
            self.cardLabels[i]["image"] = self.imgs[i]

            self.player.append(self.deck.deal())
            self.imgs[i + 1] = PhotoImage(file=self.player[i].getImg())
            self.cardLabels[i + 1]["image"] = self.imgs[i + 1]

        #Calculates points
        if self.computer.__gt__(self.player):
            self.computerPts += 1
            self.computerPointLabel["text"] = str(self.computerPts)+" Points"
        elif self.player.__gt__(self.computer):
            self.playerPts += 1
            self.playerPointLabel["text"] = str(self.playerPts)+" Points"
        elif self.computer.__eq__(self.player):
            self.playerPts += 0
            self.computerPts +=0
            self.computerPointLabel["text"] = str(self.computerPts)+" Points"
            self.playerPointLabel["text"] = str(self.playerPts)+" Points"

def main():
    '''Instantiates and pops up the window'''
    GameTable().mainloop()

if __name__ == "__main__":
    main()
    
