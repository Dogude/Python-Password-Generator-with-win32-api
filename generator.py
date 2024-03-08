import random
import string
import win32gui
import win32con

characters = string.ascii_letters + string.digits + string.punctuation
password = []
for _ in range(8):
    f = random.choice(characters)
    password.append(f)

final = ''.join(password)

win32gui.MessageBox(0, final, "hello there!", 0)


