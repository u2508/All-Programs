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
    # method called by reset button
    def reset_game_action(self):
  
        # resetting values
        self.turn = 0
        self.times = 0
  
        # making label text empty:
        self.label.setText("Player 1")
  
        # traversing push list
        for buttons in self.push_list:
            for button in buttons:
                # making all the button enabled
                button.setEnabled(True)
                # removing text of all the buttons
                button.setText("")
    
    # method called by reset button
    def exit_game_action(self):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Warning) 
    # setting message for Message Box 
        msg.setText("Do you want to exit") 
      # setting Message box window title 
        msg.setWindowTitle("Exit Window Confirmation") 
      # declaring buttons on Message Box        
        yes_button = msg.addButton(QMessageBox.Yes)
        
        no_button = msg.addButton(QMessageBox.No)
        yes_button.clicked.connect(self.onYesClicked)
        

        result = msg.exec_()

    def onYesClicked(self):
        exit()
        
  
    # action called by the push buttons
    def action_called(self):
  
        self.times += 1
  
        # getting button which called the action
        button = self.sender()
  
        # making button disabled
        button.setEnabled(False)
  
        # checking the turn
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
            text = "Player 2"
        else:
            button.setText("O")
            self.turn = 0
            text='Player 1'
        # call the winner checker method
        win = self.who_wins()
          
        # text
  
        # if winner is decided
        if win == True:
            # if current chance is 0
            if self.turn == 0:
                # O has won
                text = "O Won"
            # X has won
            else:
                text = "X Won"
  
            # disabling all the buttons
            for buttons in self.push_list:
                for push in buttons:
                    push.setEnabled(False)
  
        # if winner is not decided
        # and total times is 9
        elif self.times == 9:
            text = "Match is Draw"
  
        # setting text to the label
        self.label.setText(text)
  
  
    # method to check who wins
    def who_wins(self):
  
        # checking if any row crossed
        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                    and self.push_list[0][i].text() == self.push_list[2][i].text() \
                    and self.push_list[0][i].text() != "":
                return True
  
        # checking if any column crossed
        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                    and self.push_list[i][0].text() == self.push_list[i][2].text() \
                    and self.push_list[i][0].text() != "":
                return True
  
        # checking if diagonal crossed
        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            return True
  
        # if other diagonal is crossed
        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            return True
  
        #if nothing is crossed
        return False
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
if __name__ == "__main__":
    App.exec()
