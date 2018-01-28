import random
from Point import Point
               
#test seporator is x = y (Can be changed in Point.py)

class Perceptron:
       inputs = []
       weights = []
       LR = 0.001

       #Edits the weights using error difference from answer and guess
       def changeWeights(self, guess, answer, showWeightVals):
              error = answer - guess
              newWeights = []
              weightChange = []
              if error != 0:
                     for i in range(0, 2):
                            self.weights[i] += (float(error) * float(self.inputs[i]) * self.LR)
              print("Result of Training: Guess = %i  |  Answer = %i  |  Error = %i" % (guess, answer, error))
              if showWeightVals:
                     print(self.weights)

      #Gets the out using current weights               
       def calcOutput(self):
              print("Output calculaiting")
              #Multiplying by weights and adding together
              output = float(0)
              for i in range(0, 2):
                     output += float(self.inputs[i]) * float(self.weights[i])
              #Sign activation func
              if output >= 0:
                     output = 1
              else:
                     output = -1
              return output
                     
       #Test a single point
       def testPoint(self, inputs):
              self.inputs = inputs
              print(self.calcOutput())

       #Train using data given as Array
       def trainStage(self, trainData, showWeightVals):
              print("Training...")
              for p in trainData:
                     self.inputs = [p.x0, p.x1]
                     self.changeWeights(self.calcOutput(), p.label, showWeightVals)

       def __init__(self):
              self.inputs = [2]
              self.weights = []
              for _ in range(0, 2):
                      self.weights.append(random.random())
                      
#Man holds 1000 random point training session for debbuging
def main():
       x = Perceptron()
       randomPoints = []
       for i in range(0, 1000):
              randomPoints.append(Point(random.randint(-1000, 1000), random.randint(-1000, 1000)))
       x.trainStage(randomPoints, True)
        
        
if __name__ == "__main__":
        main()
      

       
