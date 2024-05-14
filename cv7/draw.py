from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from Edge import *
from QPoint3DF import *
from random import *
from Triangle import *
from math import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = [] 
        self.dt = []
        self.contours = []
        self.triangles = []
        
        self.view_dt = True
        self.view_contours = True
        self.view_slope = True
        self.view_aspect = True
    
    
    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()
        z = random()*500 + 100

        #Create new point
        p = QPoint3DF(x, y , z)

        #Add point to point cloud
        self.points.append(p)
            
        #Repaint screen
        self.repaint()


    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)
        
        #Draw slope
        if self.view_slope:
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.gray)
            
            #Draw triangles: slope
            for t in self.triangles:
                
                #Get vertices and slope
                vertices = t.getVertices()
                slope = t.getSlope()
                
                #Compute color
                RGB = int(255 - slope * 2*255/pi)
                col = QColor(RGB, RGB, RGB)
                
                qp.setBrush(col)
                
                #Draw trinagle
                qp.drawPolygon(vertices)

        #Draw DT
        if self.view_dt:
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.green)
            qp.setBrush(Qt.GlobalColor.transparent)

            #Draw Delaunay triangulation
            for e in self.dt:
                qp.drawLine(int(e.getStart().x()), int(e.getStart().y()),int(e.getEnd().x()), int(e.getEnd().y()))
        
        #Draw contours
        if self.view_contours:
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.lightGray)
            qp.setBrush(Qt.GlobalColor.transparent)

            #Draw contour lines
            for e in self.contours:
                qp.drawLine(int(e.getStart().x()), int(e.getStart().y()),int(e.getEnd().x()), int(e.getEnd().y()))
        
        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Draw points
        r = 10
        for p in self.points:
            qp.drawEllipse(int(p.x()-r), int(p.y()-r), 2*r, 2*r)
       
        qp.end()
        
        
    def getPoints(self):
        #Return points
        return self.points
    
      
    def clearAll(self):
        #Clear points
        self.points.clear()
        
        #Clear triangles
        self.dt.clear()
                
        #Repaint screen
        self.repaint()
        
    
    def setDT(self, dt:list[Edge]):
        #Set DT
        
        self.dt = dt
    
    
    def getDT(self):
        #Get DT
        return self.dt
    
    
    def setContours(self, contours:list[Edge]):
        #Set contour lines
        self.contours = contours
        
        
    def setTriangles(self, triangles:list[Triangle]):
        #Set triangles
        self.triangles = triangles
        
        
    def setViewDT(self, view_dt):
        self.view_dt = view_dt
        
        
    def setViewContourLines(self, view_contours):
        self.view_contours = view_contours
        
        
    def setViewSlope(self, view_slope):
        self.view_slope = view_slope
        
        
    def setViewAspect(self, view_aspect):
        self.view_aspect = view_aspect