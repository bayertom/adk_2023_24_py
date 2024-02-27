from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pol = QPolygonF()
        self.q = QPointF(100, 100)
        self.add_vertex = True
    
    def switchDraw(self):
        self.add_vertex = not(self.add_vertex)

    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()

        #Add vertex to polygon
        if self.add_vertex == 1:
            #Create new point
            p = QPointF(x,y)

            #Add point to polygon
            self.pol.append(p)
           
        #Shift q 
        else:
            self.q.setX(x)
            self.q.setY(y)
            
        #Repaint screen
        self.repaint()

    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)

        #Set aatributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Draw polygon
        qp.drawPolygon(self.pol)
        
        #Set attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.red)

        #Draw point
        r = 10
        qp.drawEllipse
        qp.drawEllipse(int(self.q.x()-r), int(self.q.y()-r), 2*r, 2*r)

        #End drawing
        qp.end()