class Animal():
    def saying(self):
        print("--")

class Cat(Animal):

    def saying(self):
        print("야옹")

persian = Cat()
persian.saying()