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

#app = pywinauto.Application(backend="win32").connect(process=pid)
#Wizard = app[yuzuVersion]

from movement import MovementVPAD
import vgamepad as vg
m = MovementVPAD()
m.setup(vg)

def test():
    input("Press")
    m.analogL(xf=1.0, yf=0.0)
    input("2")
    m.analogL(xf=-1.0, yf=0.0)
    input("3")
    m.analogL(xf=-0.0, yf=0.0)
    input("4")
    m.analogL(xf=1.0, yf=0.0)
    m.bBtn()
    time.sleep(0.2)
    m.analogL(xf=0.0, yf=0.0)
    input("p")
    m.lBtn()
    time.sleep(1)
    m.zlBtn(value=1.0)
    time.sleep(2)
    m.zlBtn(value=0.0)

while True:
    test()