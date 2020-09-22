import random
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

app = QApplication([])
window = uic.loadUi("CrazyNotStupid.ui")
window.stackedWidget.hide()

class MainWindow():
    window.setGeometry(0,0,568,426)

    oImage = QImage("Unknown.jpeg")
    sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    window.setPalette(palette)

    window.label = QLabel('What Are You', window)  # test, if it's really backgroundimage
    window.label.setGeometry(100, -110, 400, 400)

    window.label2 = QLabel('NOT', window)
    window.label2.setGeometry(180, 10, 300, 300)
    window.label.setStyleSheet("font-weight: bold; font-size: 50pt")
    window.label2.setStyleSheet("font-weight: bold; font-size: 100pt")

    window.show()




def CrazyQuotes():
    window.stackedWidget.show()
    randomQuoteList = ['Albert Einstein: "Only those who attempt the absurd can achieve the impossible."','Nathaniel Lee: "They called me mad, and I called them mad, and damn them, they outvoted me."','Megan Chance: "Calling it lunacy makes it easier to explain away the things we do not understand."']
    randomNumber = randint(0,len(randomQuoteList)-1)
    window.lblQuote.setText(randomQuoteList[randomNumber])
    window.label.hide()
    window.label2.hide()

def StupidQuotes():
    window.stackedWidget.show()
    randomQuoteList = ['Albert Einstein: "Two things are infinite: the universe and human stupidity; and Im not sure about the universe."','George Carlin: "Never underestimate the power of stupid people in large groups."','"Sometimes I wonder whether the world is being run by smart people who are putting us on or by imbeciles who really mean it."']
    randomNumber = randint(0,len(randomQuoteList)-1)
    window.lblQuote.setText(randomQuoteList[randomNumber])
    window.label.hide()
    window.label2.hide()


def rePlay():
    window.label.show()
    window.label2.show()
    window.stackedWidget.hide()

window.btnCrazy.clicked.connect(CrazyQuotes)
window.btnStupid.clicked.connect(StupidQuotes)
window.btnChange.clicked.connect(rePlay)


MainWindow()

window.show()
app.exec()