##signal&slot

from PyQt5 import Qt, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()

        lcd=QLCDNumber(self)
        sld=QSlider(Qt.Horizontal,self)

        vbox=QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Signal&slot')
        self.show()


if __name__ =='--main--':
    app=QtWidget.QApplication([])
    window=QWidget()
    window.setWindowTitle('Signal&slot')
    window.show()
    ex=Example()
    app.exec_()