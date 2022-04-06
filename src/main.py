from time import sleep
import board
import busio
import sh1106
from fetch import fetch_metars
from utils import chunk, time_now
from gpiozero import Button

STATION = 'KEWR'

wake_button = Button(4)
i2c = busio.I2C(board.SCL, board.SDA)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3C)

display.init_display()

while True:
  wake_button.wait_for_press()

  display.poweron()
  display.text("...", 0, 0)
  display.show()

  metar_string = fetch_metars(STATION)
  metar_lines = chunk(metar_string, 16)

  display.fill(0)
  display.text(f"Now: {time_now()}", 0, 0)

  for i, line in enumerate(metar_lines):
    y = (i + 1) * 8
    display.text(line, 0, y)

  display.show()
  sleep(10)
  display.fill(0)
  display.poweroff()
