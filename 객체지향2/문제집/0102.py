class findNumber():
    num = 0

    def find(self, num_list):
        if self.num in num_list:
            return True
        else:
            return False
    
    def setNum(self, n):
        self.num = n