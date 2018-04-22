#!/usr/bin/python

### board.py - contains the calculator class for assessing board input
import pandas as pd
import numpy as np


class BoardCalculator():
    def __init__(self):
        self.board = None

    def responses(self):
        '''
        Return dict with different statuses of game
        :param val:
        :return:
        '''
        return {3: 'X Wins!', 0: 'O Wins!', 1: 'Draw', 4: 'Game Incomplete', 5: 'Invalid Game'}

    def loadBoardValues(self, listarray):
        '''
        Pass in board values 'X','O' or ''
        :param listarray: ARRAY OF row tuples
        :return:
        '''

        if not self.validInput(listarray):
            raise ValueError('Invalid input')
        self.board = pd.DataFrame(data=listarray)
        self.board.replace('X', 1, inplace=True)
        self.board.replace('O', 0, inplace=True)
        self.board.replace('', np.nan, inplace=True)


    def validInput(self, listarray):
        '''
        Checks entries are valid input 'X','O' or ''
        :return:
        '''
        # check all values are valid
        rtn = True
        for t in listarray:
            for v in t:
                if v not in ['X','O', '']:
                    rtn = False
                    break
        return rtn

    def validData(self):
        '''
        Checks data is valid, incomplete or invalid game
        :param listarray:
        :return: 0 if valid, 4 if incomplete and 5 if invalid game
        '''
        # check complete
        rtn = 0
        if self.board is not None:
            # all blanks is incomplete or sum less than 3
            if self.board.isnull().values.all() or int(sum(self.board.sum(numeric_only=True))) < 3:
                rtn = 4
            # 'X' goes first so has 3 min and 5 max for valid game
            elif not int(sum(self.board.sum(numeric_only=True))) in range(3,6):
                rtn = 5
        return rtn

    def checkBoard(self):
        '''
        Check status of game
        :return: Status (string)
        '''
        rtn = None
        if self.board is not None:
            valid = self.validData()
            if valid > 0:
                rtn = self.responses()[valid]
            else:
                # sum rows and columns
                df_rows = self.board.sum(axis=1, skipna=True)
                df_cols = self.board.sum(axis=0, skipna=True)
                for df in [df_rows,df_cols]:
                    for i in [0, 3]:
                        if len(df[df == i]) > 0:
                            rtn = self.responses()[i]
                # sum diagonals
                if rtn is None:
                    df_diag = pd.DataFrame([(self.board.loc[0, 0], self.board.loc[1, 1], self.board.loc[2, 2]),
                                          (self.board.loc[0, 2], self.board.loc[1, 1], self.board.loc[2, 0]) ])
                    for diag in df_diag.sum(axis=1,skipna=False,numeric_only=False):
                        if np.isnan(diag):
                            continue
                        elif int(diag) == 3 or int(diag) == 0:
                            rtn = self.responses()[int(diag)]
                # draw
                if rtn is None and int(sum(self.board.sum(numeric_only=False))) == 5:
                    rtn = self.responses()[1]


        else:
            print('ERROR: Board entries not loaded')
        return rtn

######################################################################################################################
if __name__ == '__main__':

    entries = {'xwinr':[('X','X','X'),('O','',''),('O','','')],
               'owinr':[('X','X',''),('O','O','O'),('','X','')],
               'xwinc':[('X','X','O'),('O','X','X'),('O','X','O')],
               'owinc': [('X', 'X', 'O'), ('', 'X', 'O'), ('', '', 'O')],
               'xwind': [('X', '', 'O'), ('O', 'X', 'X'), ('O', '', 'X')],
               'owind': [('X', 'X', 'O'), ('', 'O', 'X'), ('O', 'X', 'O')],
               'draw': [('X', 'X', 'O'), ('O', 'O', 'X'), ('X', 'X', 'O')],
               'incomplete': [('X', 'X', 'O'), ('', '', ''), ('', '', '')],
               'incomplete0': [('', '', ''), ('', '', ''), ('', '', '')],
               'incomplete1': [('X', '', ''), ('', '', ''), ('', '', '')],
               'invalidgame': [('X', 'X', 'X'), ('O', 'X', 'X'), ('O', 'X', 'O')],
               'invalidinputA': [('a', 'X', 'O'), ('O', 'X', 'X'), ('O', 'X', 'O')],
               'invalidinputX0': [('XO', 'X', 'O'), ('O', 'X', 'X'), ('O', 'X', 'O')]
               }
    board = BoardCalculator()
    for test in entries.keys():
        print(test)
        print(entries[test])
        try:
            board.loadBoardValues(entries[test])
            status = board.checkBoard()
            print("\n*** ",status," ***\n")
        except Exception as e:
            print('Error:', e.args[0])
