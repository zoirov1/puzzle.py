from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QMessageBox
import random
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('mygame')
        self.start()
        
      

    def start(self):
        self.gridLay = QGridLayout()
        self.hBoxLay = QHBoxLayout()
        self.vMainLay =  QVBoxLayout()

        

        self.btn1 = QPushButton("1")
        self.btn1.clicked.connect(self.first)
        self.btn2 = QPushButton("2")
        self.btn2.clicked.connect(self.second)
        self.btn3 = QPushButton("3")
        self.btn3.clicked.connect(self.third)
        self.btn4 = QPushButton("4")
        self.btn4.clicked.connect(self.fourth)
        self.btn5 = QPushButton("5")
        self.btn5.clicked.connect(self.fifth)
        self.btn6 = QPushButton("6")
        self.btn6.clicked.connect(self.sixth)
        self.btn7 = QPushButton("7")
        self.btn7.clicked.connect(self.seventh)
        self.btn8 = QPushButton("8")
        self.btn8.clicked.connect(self.eighth)
        self.btn9 = QPushButton("9")
        self.btn9.clicked.connect(self.nineth)
        self.btn10 = QPushButton("10")
        self.btn10.clicked.connect(self.tenth)
        self.btn11 = QPushButton("11")
        self.btn11.clicked.connect(self.eleventh)
        self.btn12 = QPushButton("12")
        self.btn12.clicked.connect(self.twelfth)
        self.btn13 = QPushButton("13")
        self.btn13.clicked.connect(self.thirteenth)
        self.btn14 = QPushButton("14")
        self.btn14.clicked.connect(self.fourteenth)
        self.btn15 = QPushButton("15")
        self.btn15.clicked.connect(self.fifteenth)
        self.btn16 = QPushButton("")
        self.btn16.clicked.connect(self.sixteenth)

        self.str_style = """QPushButton {
            color:dark;
            background-color:white;
            border:1px solid black;
            border-radius:50%;
            font: bold 12pt;
            font-size:25px;
            height:70px;
            width:100px;
        }"""

        self.startbtn = QPushButton('START')
        self.startbtn.setStyleSheet('background-color:blue;color:white;font-size:25px;')
        self.startbtn.clicked.connect(self.star)


        self.closebtn = QPushButton("CLOSE")
        self.closebtn.setStyleSheet('background-color:yellow;color:dark;font-size:25px;')
        self.closebtn.clicked.connect(self.close)

        self.lst = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16]

        index = 0
        for i in range(4):
            for j in range(4):
                self.gridLay.addWidget(self.lst[index],i,j)
                self.lst[index].setStyleSheet(self.str_style)
                index+=1

        self.hBoxLay.addWidget(self.startbtn)
        self.hBoxLay.addWidget(self.closebtn)

        self.vMainLay.addLayout(self.gridLay)
        self.vMainLay.addLayout(self.hBoxLay)

        self.setLayout(self.vMainLay)
        
    def star(self):
        self.focus = list(range(1,16))
        self.focus.append("")
        for i in self.lst:
            a = random.choice(self.focus)
            self.focus.pop(self.focus.index(a))
            i.setText(str(a))

    def first(self):
            if self.btn2.text() == "":
                self.btn2.setText(self.btn1.text())
                self.btn1.setText("")
            if self.btn5.text() == "":
                self.btn5.setText(self.btn1.text())
                self.btn1.setText("")
            self.reset()

    def second(self):
            if self.btn3.text() == "":
                self.btn3.setText(self.btn2.text())
                self.btn2.setText("")
            if self.btn6.text() == "":
                self.btn6.setText(self.btn2.text())
                self.btn2.setText("")
            if self.btn1.text() == "":
                self.btn1.setText(self.btn2.text())
                self.btn2.setText("")
            self.reset()

    def third(self):
            if self.btn2.text() == "":
                self.btn2.setText(self.btn3.text())
                self.btn3.setText("")
            if self.btn7.text() == "":
                self.btn7.setText(self.btn3.text())
                self.btn3.setText("")
            if self.btn4.text() == "":
                self.btn4.setText(self.btn3.text())
                self.btn3.setText("")
            self.reset()
    
    def fourth(self):
            if self.btn3.text() == "":
                self.btn3.setText(self.btn4.text())
                self.btn4.setText("")
            if self.btn8.text() == "":
                self.btn8.setText(self.btn4.text())
                self.btn4.setText("")
            self.reset()

    def fifth(self):
            if self.btn1.text() == "":
                self.btn1.setText(self.btn5.text())
                self.btn5.setText("")
            if self.btn6.text() == "":
                self.btn6.setText(self.btn5.text())
                self.btn5.setText("")
            if self.btn9.text() == "":
                self.btn9.setText(self.btn5.text())
                self.btn5.setText("")
            self.reset()
    
    def sixth(self):
            if self.btn2.text() == "":
                self.btn2.setText(self.btn6.text())
                self.btn6.setText("")
            if self.btn5.text() == "":
                self.btn5.setText(self.btn6.text())
                self.btn6.setText("")
            if self.btn7.text() == "":
                self.btn7.setText(self.btn6.text())
                self.btn6.setText("")
            if self.btn10.text() == "":
                self.btn10.setText(self.btn6.text())
                self.btn6.setText("")
            self.reset()
    
    def seventh(self):
            if self.btn3.text() == "":
                self.btn3.setText(self.btn7.text())
                self.btn7.setText("")
            if self.btn6.text() == "":
                self.btn6.setText(self.btn7.text())
                self.btn7.setText("")
            if self.btn8.text() == "":
                self.btn8.setText(self.btn7.text())
                self.btn7.setText("")
            if self.btn11.text() == "":
                self.btn11.setText(self.btn7.text())
                self.btn7.setText("")
            self.reset()
    
    def eighth(self):
            if self.btn4.text() == "":
                self.btn4.setText(self.btn8.text())
                self.btn8.setText("")
            if self.btn7.text() == "":
                self.btn7.setText(self.btn8.text())
                self.btn8.setText("")
            if self.btn12.text() == "":
                self.btn12.setText(self.btn8.text())
                self.btn8.setText("")
            self.reset()

    def nineth(self):
            if self.btn13.text() == "":
                self.btn13.setText(self.btn9.text())
                self.btn9.setText("")
            if self.btn5.text() == "":
                self.btn5.setText(self.btn9.text())
                self.btn9.setText("")
            if self.btn10.text() == "":
                self.btn10.setText(self.btn9.text())
                self.btn9.setText("")
            self.reset()
            
    def tenth(self):
            if self.btn6.text() == "":
                self.btn6.setText(self.btn10.text())
                self.btn10.setText("")
            if self.btn9.text() == "":
                self.btn9.setText(self.btn10.text())
                self.btn10.setText("")
            if self.btn11.text() == "":
                self.btn11.setText(self.btn10.text())
                self.btn10.setText("")
            if self.btn14.text() == "":
                self.btn14.setText(self.btn10.text())
                self.btn10.setText("")
            self.reset()

    def eleventh(self):
            if self.btn7.text() == "":
                self.btn7.setText(self.btn11.text())
                self.btn11.setText("")
            if self.btn10.text() == "":
                self.btn10.setText(self.btn11.text())
                self.btn11.setText("")
            if self.btn12.text() == "":
                self.btn12.setText(self.btn11.text())
                self.btn11.setText("")
            if self.btn15.text() == "":
                self.btn15.setText(self.btn11.text())
                self.btn11.setText("")
            self.reset()
    
    def twelfth(self):
            if self.btn8.text() == "":
                self.btn8.setText(self.btn12.text())
                self.btn12.setText("")
            if self.btn11.text() == "":
                self.btn11.setText(self.btn12.text())
                self.btn12.setText("")
            if self.btn16.text() == "":
                self.btn16.setText(self.btn12.text())
                self.btn12.setText("")
            self.reset()

    def thirteenth(self):
            if self.btn9.text() == "":
                self.btn9.setText(self.btn13.text())
                self.btn13.setText("")
            if self.btn14.text() == "":
                self.btn14.setText(self.btn13.text())
                self.btn13.setText("")
            self.reset()

    def fourteenth(self):
            if self.btn13.text() == "":
                self.btn13.setText(self.btn14.text())
                self.btn14.setText("")
            if self.btn10.text() == "":
                self.btn10.setText(self.btn14.text())
                self.btn14.setText("")
            if self.btn15.text() == "":
                self.btn15.setText(self.btn14.text())
                self.btn14.setText("")
            self.reset()

    def fifteenth(self):
            if self.btn14.text() == "":
                self.btn14.setText(self.btn15.text())
                self.btn15.setText("")
            if self.btn11.text() == "":
                self.btn11.setText(self.btn15.text())
                self.btn15.setText("")
            if self.btn16.text() == "":
                self.btn16.setText(self.btn15.text())
                self.btn15.setText("")
            self.reset()

    def sixteenth(self):
            if self.btn15.text() == "":
                self.btn15.setText(self.btn16.text())
                self.btn16.setText("")
            if self.btn12.text() == "":
                self.btn12.setText(self.btn16.text())
                self.btn16.setText("")
            self.reset()
        
    def reset(self):
        if self.btn1.text() == "1" and self.btn2.text() == "2" and self.btn3.text() == "3" and self.btn4.text() == "4":
            if self.btn5.text() == '5' and self.btn6.text() == '6' and self.btn7.text() == '7' and self.btn8.text() == '8':
                if self.btn9.text() == '9' and self.btn10.text() == '10' and self.btn11.text() == '11' and self.btn12.text() == '12':
                    if self.btn13.text() == '13' and self.btn14.text() == '14' and self.btn15.text() == '15' and self.btn16.text() == "":
                        self.msg = QMessageBox()
                        self.msg.setIcon(QMessageBox.Information)
                        self.msg.setText('You Win')
                        self.msg.exec_()

if __name__ == '__main__':
    app = QApplication([])
    oyna = Window()
    oyna.show()
    app.exec_()
