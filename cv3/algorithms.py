from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *

class Algorithms:
    
    def __init__(self):
        pass
    
    def getPointPolPosition(self, q:QPointF, pol:QPolygonF):
        #Point and polygon position, ray crossing algorithm
        k = 0
        n = len(pol)
        
        #Process all vertices of the polygon
        for i in range(n):
            #Reduce coordinates
            x_ir = pol[i].x() - q.x()
            y_ir = pol[i].y() - q.y()
            
            x_i1r = pol[(i+1)%n].x() - q.x()
            y_i1r = pol[(i+1)%n].y() - q.y()
            
            #Appropriate segment intersection the ray
            if (((y_i1r > 0) and (y_ir <= 0)) or ((y_ir > 0) and (y_i1r <= 0))):
                
                #Compute intersection coordinate
                xm = (x_i1r*y_ir - x_ir*y_i1r)/(y_i1r-y_ir)
                
                # Appropriate intersection, increment k
                if xm > 0:
                    k = k + 1
        
        #Inside          
        if k%2 == 1:
            return 1
        
        #Outside
        return 0
    
    
    def get2VectorsAngle(self, p1:QPointF, p2:QPointF, p3:QPointF, p4:QPointF):
        #Angle between two vectors
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()    
        
        #Dot product
        dot = ux*vx + uy*vy
        
        #Norms
        nu = (ux**2 + uy**2)**0.5
        nv = (vx**2 + vy**2)**0.5
        
        return acos(dot/(nu*nv))
    
    
    def createCH(self, pol:QPolygonF):
        #Create Convex Hull using Jarvis Scan
        ch = QPolygonF()
        
        #Find pivot q (minimize y)
        q = min(pol, key = lambda k: k.y())

        #Find left-most point (minimize x)
        s = min(pol, key = lambda k: k.x())
        
        #Initial segment
        pj = q
        pj1 = QPointF(s.x(), q.y())
        
        # Add to CH
        ch.append(pj)
        
        # Find all points of CH
        while True:
            #Maximum and its index
            omega_max = 0
            index_max = -1
            
            #Browse all points
            for i in range(len(pol)):
                #Compute omega
                omega = self.get2VectorsAngle(pj, pj1, pj, pol[i])
        
                #Actualize maximum
                if(omega>omega_max):
                    omega_max = omega
                    index_max = i
                    
            #Add point to the convex hull
            ch.append(pol[index_max])
            
            #Reasign points
            pj1 = pj
            pj = pol[index_max]
            
            # Stopping condition
            if pj == q:
                break
            
        return ch
    
    
    def createMMB(self, pol:QPolygonF):
        # Create min max box and compute its area

        #Points with extreme coordinates        
        p_xmin = min(pol, key = lambda k: k.x())
        p_xmax = max(pol, key = lambda k: k.x())
        p_ymin = min(pol, key = lambda k: k.y())
        p_ymax = max(pol, key = lambda k: k.y())
        
        #Create vertices
        v1 = QPointF(p_xmin.x(), p_ymin.y())
        v2 = QPointF(p_xmax.x(), p_ymin.y())
        v3 = QPointF(p_xmax.x(), p_ymax.y())
        v4 = QPointF(p_xmin.x(), p_ymax.y())
        
        #Create new polygon
        mmb = QPolygonF([v1, v2, v3, v4])
        
        #Area of MMB
        area = (v2.x() - v1.x()) * (v3.y() - v2.y())
        
        return mmb, area
    
    
    def LH(self, pol:QPolygonF):
        #Compute polygon area using LH formula
        area = 0
        n = len(pol)
        
        #Compute area
        for i in range(n):
            area = area + pol[i].x() * (pol[(i + 1)%n].y() - pol[(i - 1 + n)%n].y())
            
        return abs(area)/2