import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = MatrixScanner(
            # required arguments:
            column_pins = self.col_pins,
            row_pins = self.row_pins,
            # optional arguments with defaults:
            columns_to_anodes=DiodeOrientation.COL2ROW,
            interval=0.02,
            max_events=64
        )

    col_pins = (
        board.GP27,
        board.GP26,
        board.GP22,
        board.GP20,
        board.GP23,
        board.GP21,
    )
    row_pins = (
        board.GP05,
        board.GP06,
        board.GP07,
        board.GP08,
        board.GP09,
    )
    diode_orientation = DiodeOrientation.COLUMNS
    i2c = board.I2C
    data_pin = board.RX
    coord_mapping = [
     0,  1,  2,  3,  4,  5,         37, 36, 35, 34, 33, 32,
     6,  7,  8,  9, 10, 11,         43, 42, 41, 40, 39, 38,
    12, 13, 14, 15, 16, 17,         49, 48, 47, 46, 45, 44,
    18, 19, 20, 21, 22, 23, 29, 61, 55, 54, 53, 52, 51, 50,
             25,26, 27, 28,         60, 59, 58, 57,
    ]
