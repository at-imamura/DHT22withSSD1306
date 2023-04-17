from machine import Pin
from lib.dht22.PicoDHT22 import PicoDHT22
import time
import ssd1306

dht22 = PicoDHT22(Pin(16,Pin.IN,Pin.PULL_UP))
sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0,sda=sda, scl=scl, freq=400000)

oled = ssd1306.SSD1306_I2C(128, 32, i2c)

while True:
    T, H = dht22.read()
    now = time.localtime()
    
    print(now)
    if T is None:
        print("T=----\xdfC H=----}%")
    else:
        print("T={:3.1f}, H={:3.1f}%".format(T,H))
        oled.fill(0)
        oled.text("Temp: {:3.1f}C".format(T), 0, 0)
        oled.text("Humi: {:3.1f}%".format(H), 0, 10)
        oled.show()
    time.sleep_ms(500)
