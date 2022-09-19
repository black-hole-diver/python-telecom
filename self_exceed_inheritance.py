class Ember:
    def __init__(self, csaladnev, vezeteknev):
        self.csaladnev = csaladnev
        self.vezeteknev = vezeteknev

    def intro(self):
        print(self.csaladnev, self.vezeteknev)

y = Ember("Olsen", "Thor")
y.intro()

class Diak(Ember):
    def __init__(self, csaladnev, vezeteknev, year):
        super().__init__(csaladnev, vezeteknev)
        self.vege = year
    def intro(self):
        print(self.vezeteknev, self.csaladnev, " will graduate ", self.vege)

x = Diak("Olsen", "Mike", 2018)
x.intro()
