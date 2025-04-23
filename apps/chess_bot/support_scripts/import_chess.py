
import chess



import chess.svg
import matplotlib.pyplot as plt
from cairosvg import svg2png
from io import BytesIO
import PIL.Image as Image


class ImportBoard(object):

    def __init__(self):
        pass

    def CreateBoard():

        board = chess.Board()


        # Define some basic checks for the chess board
        assert board.is_valid()
        assert board.turn == chess.WHITE

        # Make and Undo moves
        move = chess.Move.from_uci("e2e4")
        if move in board.legal_moves:
            board.push(move)
            # ... later:
            board.pop()


        svg = chess.svg.board(board=board, size=350)
        png = svg2png(bytestring=svg)
        img = Image.open(BytesIO(png))
        plt.imshow(img)
        plt.axis('off')
        plt.show()

        print('aqui')
        
        return board
