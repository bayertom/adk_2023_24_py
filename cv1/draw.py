from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pol = QPolygonF()

    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()

        #Create new point
        p = QPointF(x,y)

        #Add point to polygon
        self.pol.append(p)

        #Repaint screen
        self.repaint()

    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)

        #Draw polygon
        qp.drawPolygon(self.pol)

        #End drawing
        qp.end()