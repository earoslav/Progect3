from PyQt5.QtWidgets import (QWidget, QLabel,
    QRadioButton, QVBoxLayout,QHBoxLayout,QApplication,QMessageBox)
from PyQt5.QtCore import Qt

SIZE_WIN = (400, 300)
title = "Test"
qw = "Яка тварина безсмертна"
answ = ["Лев", "Медуза", "Дельфін", "Макака"]

app = QApplication([])
win = QWidget()
win.resize(SIZE_WIN[0], SIZE_WIN[1])
win.move(460, 170)
win.setWindowTitle(title)

qw2 = QLabel(qw)
rbn_list = list()
for i in range(4):
    rbn = QRadioButton(answ[i])
    rbn_list.append(rbn)

lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()
mainLine = QVBoxLayout()

lineH1.addWidget(qw2, alignment=Qt.AlignCenter)
lineH2.addWidget(rbn_list[0], alignment=Qt.AlignCenter)
lineH2.addWidget(rbn_list[1], alignment=Qt.AlignCenter)
lineH3.addWidget(rbn_list[2], alignment=Qt.AlignCenter)
lineH3.addWidget(rbn_list[3], alignment=Qt.AlignCenter)
mainLine.addLayout(lineH1)
mainLine.addLayout(lineH2)
mainLine.addLayout(lineH3)

win.setLayout(mainLine)

def showWin():
    mess = QMessageBox()
    mess.setWindowTitle("Winner")
    mess.setText("You won")
    mess.show()
    mess.exec()
def showLose():
    mess = QMessageBox()
    mess.setWindowTitle("Looser")
    mess.setText("You lost")
    mess.show()
    mess.exec()


rbn_list[1].clicked.connect(showWin)    
rbn_list[0].clicked.connect(showLose)
rbn_list[2].clicked.connect(showLose)
rbn_list[3].clicked.connect(showLose)

win.show()
app.exec()

