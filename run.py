from tictactoe.board import BoardCalculator

if __name__ == '__main__':
    # Run main program
    # Get stdin
    entries =[]
    for i in range(0,3):
        msg = "Enter Line %s of TicTacToe eg X,O,X: " % str(i + 1)
        entry = input(msg)
        entries.append(tuple(entry.split(',')))

    board = BoardCalculator()
    print(entries)
    try:
        board.loadBoardValues(entries)
        status = board.checkBoard()
        print("\n*** ",status," ***\n")
    except Exception as e:
        print('Error:', e.args[0])