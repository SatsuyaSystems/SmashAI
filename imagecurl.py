import PIL.ImageGrab
import win32gui
import time
hwnd = win32gui.FindWindow(None, "yuzu 1182 | Super Smash Bros. Ultimate (64-Bit) | 13.0.0 | NVIDIA")
win32gui.SetForegroundWindow(hwnd)
time.sleep(1/1000000.0)
rect = win32gui.GetWindowRect(hwnd)

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("start")
array = []
for i in range(1000):
    screenshot = PIL.ImageGrab.grab(rect)
    a = screenshot.resize((288,178))
    array.append(a)
print("done")

counter = 1
for i in array:
    i.save(f"screenshot/file"+ str(counter)+ ".png", "PNG")
    counter = counter +1