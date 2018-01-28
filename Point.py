'''
Each point has two co-ords (X0, X1) and a label (-1  or 1) depending on if its below the
seporator or above. Default seporator function is X < Y
'''
class Point:
       x0 = 0
       x1 = 0
       label = 0

       def getX0():
              return float(X0)
       def getX1():
              return float(X1)
       def getLabel():
              return int(self.label)
       def __init__(self, x0in, x1in):
               self.x0 = x0in
               self.x1 = x1in
               if self.x1 >= self.x0:
                      self.label = +1
               else:
                     self.label = -1       
