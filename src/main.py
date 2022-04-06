import board
import busio
from Adafruit_SSD1306 import SSD1306_128_64

# i2c = busio.I2C(board.SCL, board.SDA)
disp = SSD1306_128_64(None)

disp.begin()
disp.clear()
disp.display()
