import board
import busio
from Adafruit_SSD1306 import SSD1306_128_64

i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_128_64(None, i2c=i2c)

oled.fill(1)
oled.show()
