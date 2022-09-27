import time
import pywinauto
yuzuVersion = 'yuzu 1182 | Super Smash Bros. Ultimate (64-Bit) | 13.0.0 | NVIDIA'

import psutil
process_name = "yuzu"
pid = None
for proc in psutil.process_iter():
    if process_name in proc.name():
        pid = proc.pid
        print("Found pid: " + str(pid))
if pid == None:
    print("Cant find pid!")
    exit()

app = pywinauto.Application(backend="win32").connect(process=pid)
Wizard = app[yuzuVersion]
from movement import Movement
m = Movement()
m.setup(Wizard)
while True:
    m.shield(30)
    time.sleep(1)

