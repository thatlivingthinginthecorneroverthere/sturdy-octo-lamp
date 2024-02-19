# aminal.py
# by nate
# created today

class Aminal:
    has_brain = True
    alive = True
    age = 0
    name = None

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def move(speed, direction, distance):
        pass

class Burd(Aminal):
    def chirp(self):
        print("                           ______________")
        print("                          /__CHRIP_CHIP__\\")
        print("     _\|      __     |/_ /\n\
   _-  \_   _/\"->   _/  -_\n\
   -_    `-'(   )`-'    _-\n\
    `=.__.=-(   )-=.__.='\n\
            |/-\|\n\
            Y   Y")

beilly = Burd("Beilly", 68 + 1)
print(f"This is {beilly.name}, he is very chipry and happens to be {beilly.age} años")
print(f"Ain't e just butifil? iLLEGAL to fire upon his gorgenouous")
beilly.chirp()