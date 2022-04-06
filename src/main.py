import board
import busio
import Adafruit_SSD1306

i2c = busio.I2C(board.SCL, board.SDA)
oled = Adafruit_SSD1306.SSD1306_I2C(128, 64, i2c)

oled.fill(1)
oled.show()
