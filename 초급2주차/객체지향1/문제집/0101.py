class Animal():
    name = ''
    say = ''
    
    def saying(self):
        print(self.say)
    

dog = Animal()
dog.name = "강아지"
dog.say = "멍멍!"
dog.saying()
