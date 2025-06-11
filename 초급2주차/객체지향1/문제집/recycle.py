class Recycle():
    trash = ''
    isRecycle = False
    
    def canRecycle(self):
        self.isRecycle = True
    
    def whatTrash(self, tr):
        if self.isRecycle:
            self.trash = tr
        else:
            self.trash = '일반 쓰레기'
            
    def throwTrash(self):
        if self.isRecycle:
            print(self.trash + '을(를) 분리수거 했어요!')
        else:
            print(self.trash + '는 분리수거가 안 돼요!')