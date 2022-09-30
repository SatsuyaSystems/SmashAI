import PIL.ImageGrab
import win32gui
import time

class Image:
    def getImage(self):
        hwnd = win32gui.FindWindow(None, "yuzu 1184 | Super Smash Bros. Ultimate (64-Bit) | 13.0.0 | NVIDIA")
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1/1000000.0)
        rect = win32gui.GetWindowRect(hwnd)
        screenshot = PIL.ImageGrab.grab(rect)
        s = screenshot.resize((288,178))
        return s
