import time

class MovementKeystrokes:
    def setup(self, Wizard):
        self.Wizard = Wizard

    def goUp(self, height):
        for i in range(height):
            self.Wizard.send_keystrokes("{w}")

    def goRight(self, height):
        for i in range(height):
            self.Wizard.send_keystrokes("{d}")

    def goLeft(self, height):
        for i in range(height):
            self.Wizard.send_keystrokes("{a}")

    def grab(self):
        self.Wizard.send_keystrokes("{q}")

    def shield(self, spam):
        for i in range(spam):
            self.Wizard.send_keystrokes("{r}")

    def smashUp(self):
        self.Wizard.send_keystrokes("{i}")

    def smashDown(self):
        self.Wizard.send_keystrokes("{k}")

    def smashRight(self):
        self.Wizard.send_keystrokes("{l}")

    def smashLeft(self):
        self.Wizard.send_keystrokes("{j}")

    def attackA(self):
        self.Wizard.send_keystrokes("{c}")

    def attackB(self):
        self.Wizard.send_keystrokes("{x}")

class MovementVPAD:
    def setup(self, vg):
        self.gamepad = vg.VX360Gamepad()
        self.vg = vg

    def aBtn(self):
        self.gamepad.press_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        self.gamepad.update()
        time.sleep(0.1)
        self.gamepad.release_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        self.gamepad.update()

    def bBtn(self):
        self.gamepad.press_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gamepad.update()
        time.sleep(0.1)
        self.gamepad.release_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gamepad.update()

    def xBtn(self):
        self.gamepad.press_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        self.gamepad.update()
        time.sleep(0.1)
        self.gamepad.release_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        self.gamepad.update()

    def yBtn(self):
        self.gamepad.press_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        self.gamepad.update()
        time.sleep(0.1)
        self.gamepad.release_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        self.gamepad.update()

    def lBtn(self):
        self.gamepad.press_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        self.gamepad.update()
        time.sleep(0.1)
        self.gamepad.release_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        self.gamepad.update()

    def zlBtn(self, value):
        self.gamepad.right_trigger_float(value_float=value)
        self.gamepad.update()

    def analogL(self, xf, yf):
        self.gamepad.left_joystick_float(x_value_float=xf, y_value_float=yf)
        self.gamepad.update()

    def analogR(self, xf, yf):
        self.gamepad.right_joystick_float(x_value_float=xf, y_value_float=yf)
        self.gamepad.update()