import board
import busio
import sh1106
from fetch import fetch_metars
from utils import chunk


i2c = busio.I2C(board.SCL, board.SDA)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3C)

STATION = 'KSMQ'
metar_string = fetch_metars(STATION)
metar_lines = chunk(metar_string, 16)

display.init_display()
display.poweron()

display.text("Now: ", 0, 0)

for i, line in enumerate(metar_lines):
  y = (i * 8) + 1
  display.text(line, 0, y)

display.show()
