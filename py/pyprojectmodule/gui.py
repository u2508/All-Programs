import os,sys
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
except ModuleNotFoundError:
    os.system("pip install pyqt5")
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
# create a Window class
class Window(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("tic tac toe")
        self.setStyleSheet("background-color: green;") 
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.showFullScreen()
  
    # method for components
    def UiComponents(self):
  
        # turn
        self.turn = 0
  
        # times
        self.times = 0
        self.welcome=QLabel("Welcome to \nTic Tac Toe",self)
        self.welcome.setGeometry(700, 60, 620, 200)
        self.welcome.setStyleSheet("QLabel"
                                 "{"
                                 "border : 6px solid black;"
                                 "background : yellow;"
                                 
                                 "}")
        
        self.welcome.setAlignment(Qt.AlignCenter)
  
        # setting font to the label
        self.welcome.setFont(QFont('Times', 56))
        # creating a push button list
        self.push_list = []
  
        # creating 2d list
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            # adding 3 push button in single row
            self.push_list.append(temp)
  
        # x and y co-ordinate
        x = 180
        y = 165
  
        # traversing through push button list
        for i in range(3):
            for j in range(3):
  
                # setting geometry to the button
                self.push_list[i][j].setGeometry(x*i + 85, 
                                                 y*j + 85,
                                                 180, 165)
  
                # setting font to the button
                self.push_list[i][j].setFont(QFont(QFont('Times',48 )))

                # setting colur to buttons
                self.push_list[i][j].setStyleSheet("background-color: red;"
                                                    "color : Blue;"
                                                    "border : 4px solid black;")
  
                # adding action
                self.push_list[i][j].clicked.connect(self.action_called)

        # creating label to tel the score
        self.label = QLabel(self)
  
        # setting geometry to the label
        self.label.setGeometry(115, 620, 500, 105)
  
        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 6px solid black;"
                                 "background : yellow;"
                                 "}")
  
        # setting label alignment
        self.label.setAlignment(Qt.AlignCenter)
  
        # setting font to the label
        self.label.setFont(QFont('Times', 32))
        self.label.setText("Player 1")
        # creating push button to restart the score
        reset_game = QPushButton("Reset-Game", self)
  
        # setting geometry
        reset_game.setGeometry(800, 320, 450, 150)

        # adding action action to the reset push button
        reset_game.clicked.connect(self.reset_game_action)
        reset_game.setFont(QFont('Times', 48))

        #set bg colour
        reset_game.setStyleSheet("background : orange;"
                                "border : 5px solid black;")


        exit=QPushButton("Exit-Game", self)

        # setting geometry
        exit.setGeometry(800, 520, 450, 150)

        # adding action action to the reset push button
        exit.clicked.connect(self.exit_game_action)
        
        #set bg colour
        exit.setStyleSheet("background : aqua;"
                        "border : 5px solid black;")
        exit.setFont(QFont('Times', 48))
    def action_called(self):
        pass
    def reset_game_action(self):
        pass
    def exit_game_action(self):
        pass
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
if __name__ == "__main__":
    App.exec()