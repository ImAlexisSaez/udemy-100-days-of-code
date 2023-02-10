class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water.")

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")


nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()
