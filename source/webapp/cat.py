from random import randint

class Cat:
    AVATAR_HAPPY = 'images/happy.jpg'
    AVATAR_SAD = 'images/sad.jpg'
    AVATAR_ANGRY = 'images/angry.jpg'
    AVATAR_SLEEPING = 'images/sleeping.jpg'

    def __init__(self, name=None):
        self.name = name
        self.age = 1
        self.happiness = 10
        self.fullness = 40
        self.avatar = self.AVATAR_HAPPY
        self.is_sleeping = False

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness -= 5
            self.avatar = self.AVATAR_SAD
        else:
            if randint(1, 3) == 1:
                self.happiness = 0
                self.avatar = self.AVATAR_ANGRY
            else:
                self.happiness += 15
                self.fullness -= 10
                self.avatar = self.AVATAR_HAPPY

        self._check_limit()


    def feed(self):
        if not self.is_sleeping:

            self.fullness += 15
            self.happiness += 5
            self.avatar = self.AVATAR_HAPPY

            self._check_limit()

            if self.fullness == 100:
                self.happiness -= 30
                self.avatar = self.AVATAR_SAD
                self._check_limit()
        else:
            self.avatar = self.AVATAR_SLEEPING


    def sleep(self):
        self.is_sleeping = True
        self.avatar = self.AVATAR_SLEEPING

    def _check_limit(self):
        if self.happiness > 100:
            self.happiness = 100
        elif self.happiness < 0:
            self.happiness = 0

        if self.fullness > 100:
            self.fullness = 100
        elif self.fullness < 0:
            self.fullness = 0

