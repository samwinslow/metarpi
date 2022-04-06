import board
import busio
from Adafruit_SSD1306 import SSD1306_128_64

disp = SSD1306_128_64(None, i2c_address=0x3D)

disp.begin()
disp.clear()
disp.display()
