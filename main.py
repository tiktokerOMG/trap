import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.show()
        self.pushButton.clicked.connect(self.paintcircle)
        self.should_paint_circle = False
        print(self.should_paint_circle)

    def paintEvent(self, event):
        size = self.size()
        if self.should_paint_circle:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            painter.setBrush(Qt.yellow)
            for i in range(5):
                w = h = randint(10, 200)
                x = randint(1, size.width() - w)
                y = randint(1, size.height() - w)
                painter.drawEllipse(x, y, w, h)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setFixedSize(680, 520)
    ex.show()
    sys.exit(app.exec_())