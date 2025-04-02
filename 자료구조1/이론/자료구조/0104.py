class maxMachine :
   
    def __init__(self) :
        self.myData = []

    def addNumber(self, n) :
        self.myData.append(n)

    def removeNumber(self, n) :
        self.myData.remove(n)

    def getMax(self) :
        return max(self.myData)

def sorting(myList) :
    
    myMachine = maxMachine()

    result = []

    for element in myList:
        myMachine.addNumber(element)
    for i in range(len(myList)):
        myMax = myMachine.getMax()

        result.append(myMax)

        myMachine.removeNumber(myMax)

    return result