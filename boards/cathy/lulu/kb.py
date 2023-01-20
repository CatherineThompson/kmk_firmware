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

    # [
    #     '__class__', '__name__',
    #     'GP02', 'GP03', 'GP04', 'GP05', 'GP06', 'GP07', 'GP08', 'GP09', 'GP10',
    #     'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP20',
    #     'GP21', 'GP22', 'GP23', 'GP24', 'GP25', 'GP26', 'GP27', 'GP28', 'GP29',
    #     'I2C', 'MISO', 'MOSI', 'NEOPIXEL', 'RX', 'SCK', 'SCL', 'SDA', 'SPI', 'TX', 'board_id'
    # ]

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
         0,  1,  2,  3,  4,  5,         35, 34, 33, 32, 31, 30,
         6,  7,  8,  9, 10, 11,         41, 40, 39, 38, 37, 36,
        12, 13, 14, 15, 16, 17,         47, 46, 45, 44, 43, 42,
        18, 19, 20, 21, 22, 23, 29, 59, 53, 52, 51, 50, 49, 48,
                    25, 26, 27, 28, 58, 57, 56, 55, 
    ]

