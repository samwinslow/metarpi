import board
import busio
import sh1106
from fetch import fetch_metars


i2c = busio.I2C(board.SCL, board.SDA)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3C)

STATION = 'KSMQ'
metar_string = fetch_metars(STATION)
n = 16
metar_lines = [metar_string[i:i+n] for i in range(0, len(metar_string), n)]

display.init_display()
display.poweron()

for i, line in enumerate(metar_lines):
  display.text(line, 0, i * 8)

display.show()
