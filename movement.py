class Movement:
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
