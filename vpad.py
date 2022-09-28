import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

while True:
    input("asd")
# press a button to wake the device up
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()