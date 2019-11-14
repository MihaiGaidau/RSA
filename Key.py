class Key:
    def __init__(self):
        self.exponent = 0
        self.modul = 0

    def __repr__(self):
        return "Key("+str(self.exponent) + "," + str(self.modul)+")"

    def __str__(self):
        return "Key("+str(self.exponent) + "," + str(self.modul)+")"
