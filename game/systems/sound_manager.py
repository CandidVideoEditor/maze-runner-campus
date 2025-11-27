# Minimal sound manager (no external files needed by default)
class SoundManager:
    def __init__(self):
        self.enabled = False

    def play(self, name):
        # placeholder — extend to play actual sound files when added
        if self.enabled:
            print("Play sound:", name)
