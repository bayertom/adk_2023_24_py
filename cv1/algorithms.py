from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class Algorithms:
    
    def __init__(self):
        pass
    
    def getPointPolPosition(self, q:QPointF, pol:QPolygonF):
        #Point and polygon position, ray crossing algorithm
        
        k = 0
        n = len(pol)
        
        #Process all vertices
        for i in range(n):
            #Reduce coordinates
            x_ir = pol[i].x() - q.x()
            y_ir = pol[i].y() - q.y()
            
            x_i1r = pol[(i+1)%n].x() - q.x()
            y_i1r = pol[(i+1)%n].y() - q.y()
            
            #Appropriate segment
            if (((y_i1r > 0) and (y_ir <= 0)) or ((y_ir > 0) and (y_i1r <= 0))):
                
                #Compute intersection
                xm = (x_i1r*y_ir - x_ir*y_i1r)/(y_i1r-y_ir)
                
                # Correct intersection, increment intersections
                if xm > 0:
                    k = k+1
        
        #Inside          
        if k%2 == 1:
            return 1
        
        #Outside
        return 0
    
    
                
                
        