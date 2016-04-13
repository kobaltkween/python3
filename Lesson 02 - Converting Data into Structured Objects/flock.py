from birdApi import Bird

class Flock(object):
    birds = []
    def addBird(self, bird):
        self.birds.append(bird)
        
    def race(self):
        """
        Show how far the brids of the flock can go in one hour carrying their respective loads.
        """
        print("Distance flown in one hour by the flock")
        for bird in self.birds:
            distance = "-" * (bird.calculate() // 10)
            notice = "{0}: {1} carrying {2} items".format(distance, bird.name, len(bird.__dict__))
            print(notice)
            
if __name__ == "__main__":
    swallow = Bird(coconut = 1, name = "Swallow")
    african = Bird(coconut = 1, piece = "of string", visited = False, name = "African Swallow")
    european = Bird(coconut = 1, lotteryNumbers = (23, 12, 34), piece = "of string", visited = True, name = "European Swallow")
    birds = (
        ("Swallows are a group of birds in the family Hirundinidae.", swallow),
        ("African swallows are said to be abel to carry coconuts.", african),
        ("European swallows are said to have trouble carrying coconuts.", european)
    )
    
    flock = Flock()
    for stmt, bird in birds:
        print(stmt)
        flock.addBird(bird)
    print("*" * 40)
    flock.race()