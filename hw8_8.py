class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)


aSong = Song(["Twinkle, twinkle, little star", "How I wonder what you are!",
             "Up above the world so high,", "Like a diamond in the sky."])
aSong.sing()
