# pip install pyqt5
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QApplication, QWidget, \
    QLabel, QTextEdit, QPushButton, QMainWindow, QLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QBoxLayout
import sys

app = QApplication(sys.argv)


class MainMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.a = None
        self.b = None
        self.amal = None
        self.setWindowTitle("Kalkulyator")
        self.setFixedSize(475, 550)
        self.lab = QLabel("0")
        self.lab.setStyleSheet("border : 3px solid red")
        __font = QFont()
        __font.setBold(True)
        self.lab.setFont(__font)
        self.lab.setFont(QFont('Arial', 25))
        self.lab.setAlignment(Qt.AlignRight)
        self.b0 = QPushButton("0")
        self.b0.clicked.connect(self.bosish)
        self.b1 = QPushButton("1")
        self.b1.clicked.connect(self.bosish1)
        self.b2 = QPushButton("2")
        self.b2.clicked.connect(self.bosish2)
        self.b3 = QPushButton("3")
        self.b3.clicked.connect(self.bosish3)
        self.b4 = QPushButton("4")
        self.b4.clicked.connect(self.bosish4)
        self.b5 = QPushButton("5")
        self.b5.clicked.connect(self.bosish5)
        self.b6 = QPushButton("6")
        self.b6.clicked.connect(self.bosish6)
        self.b7 = QPushButton("7")
        self.b7.clicked.connect(self.bosish7)
        self.b8 = QPushButton("8")
        self.b8.clicked.connect(self.bosish8)
        self.b9 = QPushButton("9")
        self.b9.clicked.connect(self.bosish9)
        self.b10 = QPushButton("*")
        self.b10.clicked.connect(self.kopaytirish)
        self.b11 = QPushButton("/")
        self.b11.clicked.connect(self.bolish)
        self.b12 = QPushButton("-")
        self.b12.clicked.connect(self.ayrish)
        self.b13 = QPushButton("+")
        self.b13.clicked.connect(self.qoshish)
        self.b14 = QPushButton("+-")
        self.b14.clicked.connect(self.p_m)
        self.b15 = QPushButton(".")
        self.b15.clicked.connect(self.nuqta)
        self.b16 = QPushButton("=")
        self.b16.setFont(QFont("Arial", 25))
        self.b16.setStyleSheet("Border :2px solid blue")
        self.b16.clicked.connect(self.natija)
        self.b16.setFixedHeight(100)
        self.lab.setFixedHeight(75)
        self.buttons = (
            self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self.b10,
            self.b11,
            self.b12, self.b13, self.b14, self.b15)
        for b in self.buttons:
            b.setFixedSize(100, 75)
            b.setFont(QFont("Arial", 25))
            b.setStyleSheet("Border :2px solid black")
        self.b13.setStyleSheet("Border :2px solid green")

        layloud = QVBoxLayout()
        layloud.addWidget(self.lab)
        layloud1 = QHBoxLayout()
        layloud2 = QHBoxLayout()
        layloud3 = QHBoxLayout()
        layloud4 = QHBoxLayout()
        layloud5 = QHBoxLayout()
        layloud5.addWidget(self.b16)
        layloud4.addWidget(self.b14)
        layloud4.addWidget(self.b0)
        layloud4.addWidget(self.b15)
        layloud4.addWidget(self.b13)
        layloud1.addWidget(self.b1)
        layloud1.addWidget(self.b2)
        layloud1.addWidget(self.b3)
        layloud1.addWidget(self.b10)
        layloud2.addWidget(self.b4)
        layloud2.addWidget(self.b5)
        layloud2.addWidget(self.b6)
        layloud2.addWidget(self.b11)
        layloud3.addWidget(self.b7)
        layloud3.addWidget(self.b8)
        layloud3.addWidget(self.b9)
        layloud3.addWidget(self.b12)
        layloud.addLayout(layloud1)
        layloud.addLayout(layloud2)
        layloud.addLayout(layloud3)
        layloud.addLayout(layloud4)
        layloud.addLayout(layloud5)
        container = QWidget()

        container.setLayout(layloud)
        self.setCentralWidget(container)

    def natija(self):
        self.b = int(self.lab.text())
        if self.amal == 0:
            pass
        elif self.amal == 1:
            self.lab.setText(f"{self.a + self.b}")
            self.amal = 0
        elif self.amal == 2:
            self.lab.setText(f"{self.a * self.b}")
            self.amal = 0
        elif self.amal == 3:
            self.lab.setText(f"{self.a - self.b}")
            self.amal = 0
        elif self.amal == 4:
            natija = self.a / self.b
            if natija == int(natija):
                natija = int(natija)
            self.lab.setText(f"{natija}")
            self.amal = 0

    def kopaytirish(self):
        self.amal = 2
        try:
            self.a = int(self.lab.text())
        except:
            self.a = float(self.lab.text())
        self.lab.setText("0")

    def bolish(self):
        self.amal = 4
        try:
            self.a = int(self.lab.text())
        except:
            self.a = float(self.lab.text())
        self.lab.setText("0")

    def p_m(self):
        try:
            self.lab.setText(f"{-1 * int(self.lab.text())}")
        except:
            self.lab.setText(f"{-1 * float(self.lab.text())}")

    def qoshish(self):
        try:
            self.a = int(self.lab.text())
        except:
            self.a = float(self.lab.text())
        self.amal = 1
        self.lab.setText("0")

    def ayrish(self):
        try:
            self.a = int(self.lab.text())
        except:
            self.a = float(self.lab.text())
        self.amal = 3
        self.lab.setText("0")

    def nuqta(self):
        if "." in self.lab.text():
            pass
        else:
            self.lab.setText(f"{self.lab.text()}.")

    def bosish(self):
        if float(self.lab.text()) > 0:
            strin = str(self.lab.text()) + self.b0.text()
            self.lab.setText(str(strin))
        else:
            pass

    def bosish1(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b1.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b1.text()))

    def bosish2(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b2.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b2.text()))

    def bosish3(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b3.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b3.text()))

    def bosish4(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b4.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b4.text()))

    def bosish5(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b5.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b5.text()))

    def bosish6(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b6.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b6.text()))

    def bosish7(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b7.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b7.text()))

    def bosish8(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b8.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b8.text()))

    def bosish9(self):
        if self.lab.text() == "0":
            self.lab.setText(str(self.b9.text()))
        else:
            self.lab.setText(str(str(self.lab.text()) + self.b9.text()))


w = MainMenu()
w.show()

app.exec()
