import random
from data import Data

class Rhythm:

    def getMinRhythm(measure):
        return Data.rhythm_atomic[-1] / measure[1] * measure[0]


    def calcSpaceWhenString(item):
        number = ""
        for v in item:
            if v.isdigit():
                number += v
        result = (Data.rhythm_atomic[-1] / int(number)) + Data.rhythm_atomic[-1] / (int(number)*2)
        return result

    def calcSpace(r, space):
        
        tam = 0.0
        fits = False
       
        if isinstance(r, list):
            for item in r:
                if isinstance(item, str):
                    tam += int(Rhythm.calcSpaceWhenString(item))
                else:
                    tam += Data.rhythm_atomic[-1] / item
        else:
            tam += Data.rhythm_atomic[-1] / r
        
        if (space - tam) >= 0.0:
            fits = True

        return fits, tam

    def getRhythm(space: float):
        correct = False
        
        while(correct!= True):
            selection = random.random()

            if selection>0.4:
                r = Data.rhythm_cells[random.randint(0, len(Data.rhythm_cells)-1)]
            else:
                r = Data.rhythm_atomic[random.randint(0, len(Data.rhythm_atomic)-1)]

            correct, tam = Rhythm.calcSpace(r, space)
        return r, tam