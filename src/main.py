import sys
sys.path.append("..")

import board
import busio
from lib import sh1106

i2c = busio.I2C(board.SCL, board.SDA)

display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3C)

display.init_display()
