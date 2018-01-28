from Perceptron import Perceptron
from Point import Point
import random

randomPoints = []
testDataReady = False
exitProgram = False
showWeightVals = False
x = None

#Test data creation function
def makeTestData(totalPoints):
       for i in range(0, totalPoints):
              randomPoints.append(Point(random.randint(-1000, 1000), random.randint(-1000, 1000)))
              #print(randomPoints) - debug
              
 #Menu Code     
while exitProgram == False:
       print("What would you like to do:\n 1: Make New Perceptron\n2: Make New Test Data\n3: Train Current Perceptron\n4: Test a random point\n5: Options\n6: Exit Program")
       choice = int(input("Please Choose (1, 2...): "))
       if choice == 1:
              x = Perceptron()
              print("New Perceptron Created!\n")
       if choice == 2:
             randomPoints = []
             makeTestData(int(input("How many random test points would you like to create: ")))
             testDataReady = True
       if choice == 3 and x != None and testDataReady == True:
              print("Training With Random Data!")
              x.trainStage(randomPoints, showWeightVals)
              print("Finished Training!\n")
       if (choice == 3 or choice == 4) and x == None:
              print("There is no perceptron, please create one!!")
       if choice == 3 and testDataReady == False:
              print("There is no test data! Cannot Triain")      
       if choice == 4 and x != None:
               print("Ok! Please enter the X and Y values for your 2D point")
               x.testPoint([int(input("X: ")), int(input("Y: "))])
       if choice == 5:
              print("1: Show Weight values while training: %s\n2: Return to main menu\n\nEnter a number to change that option" % (showWeightVals))
              if(int(input()) == 1):
                     showWeightVals = True
                     print("Change Saved!\n\n")
       if choice == 6:
              exitProgram = True
