from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QGridLayout , QPushButton , QTextEdit , QTabWidget
from PyQt5.QtCore import  QTimer , Qt , QTime
from PyQt5.QtGui import QFont , QFontDatabase , QIcon


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.clock_timer = QTimer(self)
        self.stopwatch_timer = QTimer(self)

        self.time_label = QLabel(self)
        self.name_label = QLabel("Clock: ")
        self.button = QPushButton("Event" , self)
        self.textbox = QTextEdit()
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()     
        self.tabs.addTab(self.tab1, "Digital Clock")
        self.tabs.addTab(self.tab2, "Stop Watch")
        self.tabs.addTab(self.tab3, "Alarm")
        self.tabs.addTab(self.tab4, "Reminder")
        self.name_labe2 = QLabel("StopWatch: ")
        self.time = QTime(0 , 0 , 0 , 0 )
        self.time_label2 = QLabel("00:00:00:00" , self)
        self.start_button = QPushButton("Start" , self)
        self.stop_button = QPushButton("Stop" , self)
        self.reset_button = QPushButton("Reset" , self)
        self.initUI()


    def initUI(self):
        tablayout = QGridLayout(self.tab1)
        tablayout2 = QGridLayout(self.tab2)
        tablayout3 = QGridLayout(self.tab3)
        tablayout4 = QGridLayout(self.tab4)
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("image.png"))
        self.setGeometry(0 , 0 ,1000 , 750)
        self.setFixedSize(1000 , 750)
        self.textbox.setText("Events will appear here")
        self.textbox.setReadOnly(True)
        grid = QGridLayout()
        grid.addWidget(self.tabs)

        tablayout.addWidget(self.name_label , 0 , 0 , 1 , 2)
        tablayout.addWidget(self.time_label,  1,  0,  1,  3)
        tablayout.addWidget(self.button ,     2 , 0 , 1 , 1 )
        tablayout.addWidget(self.textbox ,    3 , 0  , 3, 3)
        tablayout2.addWidget(self.name_labe2 , 0 , 0 ,1 , 2 )
        tablayout2.addWidget(self.time_label2 , 1 , 0 ,1 , 3 )
        tablayout2.addWidget(self.start_button , 2 , 0 ,1 , 1 )
        tablayout2.addWidget(self.stop_button , 2 , 1 ,1 , 1 )
        tablayout2.addWidget(self.reset_button , 2 , 2 ,1 , 1 )
        self.setLayout(grid)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.name_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.name_labe2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.time_label2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.setStyleSheet("""
            QTabBar::tab{
                    height : 30px;
                    width : 244px; 
                    font-family: Comic Sans MS;
                    font-size : 10 px       
                          
           }
                QTabWidget::pane {
                    background-color: hsl(229, 84%, 5%);
                    border: none;
            }
                QWidget {
                background-color: #020617;
            }

            QLabel {
                color: white;
            }

            QPushButton {
                background-color: #16a34a;
                color: white;
                border-radius: 22px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #15803d;
            }

            QPushButton:pressed {
                background-color: #166534;
            }

            QTextEdit {
                background-color: #0f172a;
                color: #e5e7eb;
                border-radius: 10px;
                padding: 15px;
            }
        """)
        self.clock_timer.timeout.connect(self.updatetime)
        self.clock_timer.start(1000)
        self.updatetime()

        self.time_label.setStyleSheet("font-size : 150px;"  )
        self.time_label2.setStyleSheet("font-size : 150px;"  )
        self.name_label.setFont(QFont("Comic Sans MS", 100))
        self.name_labe2.setFont(QFont("Comic Sans MS", 90))
        self.name_labe2.setStyleSheet("padding: 5px;")
        self.button.setFont(QFont("Arial", 60))
        self.start_button.setFont(QFont("Arial", 60))
        self.stop_button.setFont(QFont("Arial", 60))
        self.reset_button.setFont(QFont("Arial", 60))
        self.textbox.setFont(QFont("Courier New", 40))
  
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
        self.time_label2.setFont(my_font)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.stopwatch_timer.timeout.connect(self.update_display)



    def start(self):
        if not self.stopwatch_timer.isActive():
            self.stopwatch_timer.start(10)
        
    def stop(self):
            self.stopwatch_timer.stop()

    def reset(self):
            self.stopwatch_timer.stop()
            self.time = QTime(0 , 0 ,0 ,0)
            self.time_label2.setText(self.format_time(self.time))

    def format_time(self , time ):
            hours = time.hour()
            minutes = time.minute()
            seconds = time.second()
            milliseconds = time.msec() // 10
            return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        
    def update_display(self):
            self.time = self.time.addMSecs(10)
            self.time_label2.setText(self.format_time(self.time))


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
