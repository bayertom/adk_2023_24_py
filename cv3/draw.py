from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.building = QPolygonF()
       
    
    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()
              
        #Create new point
        p = QPointF(x,y)

        #Add point to polygon
        self.building.append(p)
           
        #Repaint screen
        self.repaint()

    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)

        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Draw building
        qp.drawPolygon(self.building)
        
        #End drawing
        qp.end()
        
    
    def getPolygon(self):
        # Return polygon
        return self.building
    
    
    def clearAll(self):
        #Clear polygon
        self.building.clear()
        
        #Repaint screen
        self.repaint()
        
    