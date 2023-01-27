# -------- Using ChatGPT to help :) ----------

import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QGridLayout, QWidget, QHBoxLayout, QFrame, QVBoxLayout, QCheckBox, QComboBox
import os
import random

app = QApplication(sys.argv)

answer = "A"
directories = []
showing_answer = False
Test_mode = False
reviewmode = False

TestQIndex = 0
Questions = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

class Question:
    def __init__(self, directory, answerdirectory, answer):
        self.directory = directory
        self.answerdirectory = answerdirectory
        self.user_answer = None
        self.answer = answer
    def SetUserAnswer(answer1):
        self.user_answer = answer1
    def GetDirectory():
        return "a"
    
def UpdateTestView():
    global pixmap, label, Questions, directories, button_a, reviewmode
    pixmap = QPixmap(Questions[TestQIndex].directory)
    label.setPixmap(pixmap)
    ans = Questions[TestQIndex].user_answer
    ansa = Questions[TestQIndex].answer
    
    button_a.setStyleSheet("QPushButton")
    button_b.setStyleSheet("QPushButton")
    button_c.setStyleSheet("QPushButton")
    button_d.setStyleSheet("QPushButton")
    button_e.setStyleSheet("QPushButton")
    button_f.setStyleSheet("QPushButton")
    button_g.setStyleSheet("QPushButton")
    if ans == "A":
        button_a.setStyleSheet("background-color : blue;")
    elif ans == "B":
        button_b.setStyleSheet("background-color : blue;")
    elif ans == "C":
        button_c.setStyleSheet("background-color : blue;")
    elif ans == "D":
        button_d.setStyleSheet("background-color : blue;")
    elif ans == "E":
        button_e.setStyleSheet("background-color : blue;")
    elif ans == "F":
        button_f.setStyleSheet("background-color : blue;")
    elif ans == "G":
        button_g.setStyleSheet("background-color : blue;")

    if reviewmode:
        if ansa == "A":
            button_a.setStyleSheet("background-color : green;")
        elif ansa == "B":
            button_b.setStyleSheet("background-color : green;")
        elif ansa == "C":
            button_c.setStyleSheet("background-color : green;")
        elif ansa == "D":
            button_d.setStyleSheet("background-color : green;")
        elif ansa == "E":
            button_e.setStyleSheet("background-color : green;")
        elif ansa == "F":
            button_f.setStyleSheet("background-color : green;")
        elif ansa == "G":
            button_g.setStyleSheet("background-color : green;")
        
def NewQuestion(*answerneed): # optional argument to handle answer button
    global answer
    global directories
    global pixmap
    global current_question_directory
    global showing_answer
    global random_paper_choice, button_answer
    if answerneed: # instead of making a new method to handle show answer button, its done here
        # shows or hides the answer of the current question
        if showing_answer == True:
            button_answer.setText("Show Answer")
            pixmap = QPixmap(r"assets\Questions\\" + random_paper_choice + "\\" + current_question_directory)
            label.setPixmap(pixmap)
            showing_answer = False
        elif showing_answer == False:
            print(current_question_directory)
            button_answer.setText("Question")
            pixmap = QPixmap(r"assets\Answers\\" + current_question_directory)
            label.setPixmap(pixmap)
            showing_answer = True
    else:
        # picks a new random question
        random_paper_choice = random.choice(directories)
        current_question_directory = random.choice(os.listdir(r"assets\Questions" + "\\" + random_paper_choice))
        pixmap = QPixmap(r"assets\Questions\\" + random_paper_choice + "\\" + current_question_directory)
        current_answer = current_question_directory.strip(".jpeg").split("_")[-1]
        answer = current_answer
        label.setPixmap(pixmap)
# makes question objects and puts them in a list for all questions in a test paper directory
def SetUpTest(directory):
    f = sorted(os.listdir('assets\Questions\\' + directory))

    for t in f:
        print(t)
        print('assets\Questions\\' + directory + '\\' + t)
        index = int(t.strip(".jpeg").split("_")[-2]) - 1
        Questions.pop(index)
        Questions.insert(index, Question('assets\Questions\\' + directory + '\\' + t, 'assets\Answers\\' + t, t.strip(".jpeg").split("_")[-1]))

    for q in Questions:
        print(q.directory)


pixmap = QPixmap(r"assets\Questions\tmua_2021_paper_1_1_F.jpeg")

label = QLabel()

label.setPixmap(pixmap)
label.setScaledContents(True)
label.setAlignment(QtCore.Qt.AlignCenter)
label.resize(500,800)

# ----------------------------- answer button code -----------------------

def ShowHideAnswer():
    global showing_answer
    if Test_mode == False:
        NewQuestion(True)
    else:
        if showing_answer == False:
            pixmap = QPixmap(Questions[TestQIndex].answerdirectory)
            label.setPixmap(pixmap)
            showing_answer = True
        else:
            pixmap = QPixmap(Questions[TestQIndex].directory)
            label.setPixmap(pixmap)
            showing_answer = False
            
def labelscore(num):
    global vbox
    scorelabel = QLabel(str(num))
    vbox.addWidget(scorelabel)

 # code for most of the buttons to take them to their functions
def button_click(sender):
    global Questions, TestQIndex, reviewmode

    if Test_mode == False:
        if sender.text() == answer:
            NewQuestion()
        elif sender.text() == "Skip":
            NewQuestion()
    else:
        if sender.text() == "=>" and TestQIndex < 19:
            TestQIndex += 1
            print(TestQIndex)
        elif sender.text() == "<=" and TestQIndex > 0:
            TestQIndex -= 1
        elif sender.text() in ["A", "B", "C", "D", "E", "F", "G"]:
            Questions[TestQIndex].user_answer = sender.text()
        elif sender.text() == "End":
            reviewmode = True
            score = 0
            grid_layout.addWidget(button_answer, 0, 10)
            for q in Questions:
                if q.user_answer == q.answer:
                    score += 1
            labelscore(score)
        UpdateTestView()
        
button_a = QPushButton("A")
button_b = QPushButton("B")
button_c = QPushButton("C")
button_d = QPushButton("D")
button_e = QPushButton("E")
button_f = QPushButton("F")
button_g = QPushButton("G")

button_skip = QPushButton("Skip")
button_answer = QPushButton("Show Answer")

button_prev = QPushButton("<=")
button_next = QPushButton("=>")
button_end = QPushButton("End")

button_a.clicked.connect(lambda: button_click(button_a))
button_b.clicked.connect(lambda: button_click(button_b))
button_c.clicked.connect(lambda: button_click(button_c))
button_d.clicked.connect(lambda: button_click(button_d))
button_e.clicked.connect(lambda: button_click(button_e))
button_f.clicked.connect(lambda: button_click(button_f))
button_g.clicked.connect(lambda: button_click(button_g))

button_skip.clicked.connect(lambda: button_click(button_skip))
button_answer.clicked.connect(ShowHideAnswer)

button_prev.clicked.connect(lambda: button_click(button_prev))
button_next.clicked.connect(lambda: button_click(button_next))
button_end.clicked.connect(lambda: button_click(button_end))

grid_layout = QGridLayout()

grid_layout.addWidget(button_a, 0, 0)
grid_layout.addWidget(button_b, 0, 1)
grid_layout.addWidget(button_c, 0, 2)
grid_layout.addWidget(button_d, 0, 3)
grid_layout.addWidget(button_e, 0, 4)
grid_layout.addWidget(button_f, 0, 5)
grid_layout.addWidget(button_g, 0, 6)




# ------------------------------------------------------------------------




container = QFrame()
vbox = QVBoxLayout()
container.setLayout(vbox)

vbox.addWidget(label)
vbox.addLayout(grid_layout)

window = QMainWindow()

def Start():
    
    if P1_2021.isChecked():
        directories.append("2021_P1")
    if P2_2021.isChecked():
        directories.append("2021_P2")

    window1.hide()

    window.setFixedSize(700, 900)
    window.show()
    window.setCentralWidget(container)
    print(Test_mode)
    if Test_mode == False:
        # buttons that are exclusive to the practice mode
        grid_layout.addWidget(button_answer, 0, 8)
        grid_layout.addWidget(button_skip, 0, 7)
        NewQuestion()
    else:
        SetUpTest(directories[0])
        grid_layout.addWidget(button_next, 0, 8)
        grid_layout.addWidget(button_prev, 0, 7)
        grid_layout.addWidget(button_end, 0, 9)
        UpdateTestView()
        
def DropdownActive(index):
    global Test_mode
    print(index)
    if index == 1:
        Test_mode = True
    else:
        Test_mode = False

# ------------------------------------- START OPTIONS --------------------------------------------------
Start_Layout = QVBoxLayout()

ComboBox = QComboBox()
ComboBox.addItem('Practice Mode')
ComboBox.addItem('Test Mode')
ComboBox.activated.connect(DropdownActive)

P1_2021 = QCheckBox("TMUA 2021 PAPER 1")
P2_2021 = QCheckBox("TMUA 2021 PAPER 2")

button_start = QPushButton("Start")
button_start.clicked.connect(Start)

Start_Layout.addWidget(ComboBox)
Start_Layout.addWidget(P1_2021)
Start_Layout.addWidget(P2_2021)
Start_Layout.addWidget(button_start)


window1 = QWidget()
window1.setLayout(Start_Layout)
window1.show()
window1.setFixedSize(600, 800)


sys.exit(app.exec_())
