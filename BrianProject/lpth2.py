class Song(object):
    def __init__(self,lyrics):
        self.test=lyrics

    def sing_me_a_song(self):
        for line in self.test:
            print line

happy_bday=Song(["happy bday","to you","habby bda big guy"])

happy_bday.sing_me_a_song()