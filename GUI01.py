from PyQt5 import QtWidgets


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title='Main Window'
        self.left=600
        self.top=450
        self.width=640
        self.height=480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeoMetry(self.left, self.top, self.width, self.height)
        self.show()

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    window=QtWidgets.QWidget()
    window.setWindowTitle('Main Window')
    window.show()
    app.exec_()