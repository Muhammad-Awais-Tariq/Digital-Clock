from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QGridLayout , QPushButton , QTextEdit
from PyQt5.QtCore import QTime , QTimer , Qt
from PyQt5.QtGui import QFont , QFontDatabase


#add the grid layout and using row span in the first coloumn add the clock time function then in second coloumn add timer and then in the third one add the button and then the text area 
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.name_label = QLabel("Clock: ")
        self.button = QPushButton("Event" , self)
        self.textbox = QTextEdit()
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(0 , 0 ,1000 , 600)
        self.textbox.setText("Events will appear here")
        self.textbox.setReadOnly(True)
        grid = QGridLayout()
        grid.addWidget(self.name_label , 0 , 0 , 1 , 2)
        grid.addWidget(self.time_label,  1,  0,  1,  3)
        grid.addWidget(self.button ,     2 , 0 , 1 , 1 )
        grid.addWidget(self.textbox ,    3 , 0  , 3 , 3)
        self.setLayout(grid)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.name_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.time_label.setStyleSheet("font-size : 150px;"
                                      )
        self.name_label.setStyleSheet("font-size : 100px;"
                                      "font-family : Arial;"
                                      )   
        self.button.setStyleSheet("font-size : 100px;"
                                    "font-family : Arial;"
                                      ) 
        self.textbox.setStyleSheet("font-size : 50px;"
                                    "font-family : Arial;")   
        self.button.clicked.connect(self.event_finder)     
        grid.setRowStretch(0, 0)   
        grid.setRowStretch(1, 0)   
        grid.setRowStretch(2, 0) 
        grid.setRowStretch(3, 0)           
        grid.setRowStretch(4, 0)  
        grid.setRowStretch(5, 0)  
        grid.setRowStretch(6, 0)  
        grid.setRowStretch(7, 1)  
   
        
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_faimly = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_faimly , 150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.updatetime)
        self.timer.start(1000)
        self.updatetime()


    def updatetime(self):
        self.current = datetime.now().strftime("%I:%M:%S %p")
        self.time_label.setText(self.current)


    def event_finder(self):
        current_time = datetime.now().strftime("%I %p")

        Events = {
            "12 AM" : "Partition of India and Pakistan",
            "01 AM"  : "Vela Incident - suspected nuclear test near Prince Edward Islands",
            "02 AM"  : "First Usa nuclear test",
            "03 AM"  : "World War II Pacific operations intensify",
            "04 AM"  : "Japanese forces launch dawn surprise attack on Pearl Harbor",
            "05 AM"  : "Japanese surrender preparations on August 15 begin early morning before Emperor's broadcast.",
            "06 AM"  : "D-Day Allied invasion force crosses English Channel en route to Normandy beaches",
            "07 AM"  : "Warning sirens in Hiroshima before atomic bombing",
            "08 AM"  : "First atomic bomb dropped on Hiroshima",
            "09 AM"  : "United Airlines Flight 175 crashes into South Tower of World Trade Center.",
            "10 AM" : "United Flight 93 crashes in Pennsylvania during 9/11 after passenger revolt.",
            "11 AM" : "Atomic bomb dropped on Nagasaki",
            "12 PM" : "Emperor Hirohito's surrender broadcast",
            "01 PM"  : "Apollo 11 astronauts land on Moon and begin surface operations after lunar module touchdown",
            "02 PM"  : "Signing of the Treaty of Versailles formally ends World War I hostilities",
            "03 PM"  : "The Gunpowder Plot discovered in England after explosives found at Parliament",
            "04 PM"  : "Battle of Waterloo ends with Napoleon's defeat in early evening",
            "05 PM"  : "Fall of the Berlin Wall celebrations spread worldwide after barrier opened",
            "06 PM"  : "Black Death spreads through Europe; many cities become quarantined by dusk",
            "07 PM"  : "Industrial Revolution accelerates with steam power demonstrations",
            "08 PM"  : "Television broadcast of WWII events (Ve Day celebrations) reach global audiences in primetime",
            "09 PM"  : "United Nations founded after global meeting discussions",
            "10 PM" : "Moon landing missions commence night communications back to Earth via NASA's tracking stations.",
            "11 PM" : "Victory over Japan (V-J) radio news spreads globally late night after surrender acceptance"
        }
        
        if current_time in Events:
            self.textbox.setText("Event: " + Events[current_time])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
