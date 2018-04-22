import unittest2 as unittest
from tictactoe.board import BoardCalculator

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.entries = {'xwinr': [('X', 'X', 'X'), ('O', '', ''), ('O', '', '')],
                   'owinr': [('X', 'X', ''), ('O', 'O', 'O'), ('', 'X', '')],
                   'xwinc': [('X', 'X', 'O'), ('O', 'X', 'X'), ('O', 'X', 'O')],
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
        self.board = BoardCalculator()

    def test_Xwins(self):
        tests = ['xwinr', 'xwinc','xwind']
        expected = 'X Wins!'
        for test in tests:
            print(self.entries[test])
            self.board.loadBoardValues(self.entries[test])
            status = self.board.checkBoard()
            self.assertEqual(status,expected)

    def test_Owins(self):
        tests = ['owinr', 'owinc','owind']
        expected = 'O Wins!'
        for test in tests:
            print(self.entries[test])
            self.board.loadBoardValues(self.entries[test])
            status = self.board.checkBoard()
            self.assertEqual(status, expected)

    def test_Draw(self):
        tests = ['draw']
        expected = 'Draw'
        for test in tests:
            print(self.entries[test])
            self.board.loadBoardValues(self.entries[test])
            status = self.board.checkBoard()
            self.assertEqual(status, expected)

    def test_Incomplete(self):
        tests = ['incomplete','incomplete0','incomplete1']
        expected = 'Game Incomplete'
        for test in tests:
            print(self.entries[test])
            self.board.loadBoardValues(self.entries[test])
            status = self.board.checkBoard()
            self.assertEqual(status, expected)

    def test_InvalidGame(self):
        tests = ['invalidgame']
        expected = 'Invalid Game'
        for test in tests:
            print(self.entries[test])
            self.board.loadBoardValues(self.entries[test])
            status = self.board.checkBoard()
            self.assertEqual(status, expected)

    def test_InvalidInput(self):
        tests = ['invalidinputA','invalidinputX0']
        for test in tests:
            print(self.entries[test])
            self.assertRaises(ValueError, self.board.loadBoardValues,self.entries[test])

