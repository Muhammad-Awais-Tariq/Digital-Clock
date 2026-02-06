# Digital Clock
It’s a simple digital clock that shows 12-hour format time with a unique twist.

## Features
- Displays 12-hour format time with seconds
- Stopwatch with start, stop, and reset functionality
- Set alarms that play sound
- Set reminders with desktop toast notifications
- Shows a historical event based on the current hour when the "Event" button is pressed
- Graphical user interface (GUI) using PyQt5

## How the Clock Works
Open the program and use the tabs:

- **Digital Clock**: View current time. Press the **Event** button to display the historical event for the current hour in the text box.
- **Stop Watch**: Use Start, Stop, and Reset buttons to control the stopwatch.
- **Alarm**: Choose hour, minute, and AM/PM, then click **Set Alarm**. Alarm sound plays when time matches. Use **Stop Alarm** to silence it.
- **Reminder**: Type a message, select time, then click **Set Reminder**. A toast notification appears at the chosen time.

## How to Run the Program
1. Make sure **Python** is installed.
2. Install all required modules using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
3. Run the program
    ```bash
    python Clock.py
    ```
    
## File Structure
```bash
project/
│── Clock.py
│── README.md
│── requirements.txt
│── DS-DIGIT.TTF
│── image.png
│── Alarm-sound.wav
│── Reminder-image.ico
```

## Technologies Used
- Python
- PyQt5
- datetime
- win10toast
- pygame    

## Notes
- All historical events are approximate and mapped to hourly time slots.
- Alarm and reminder functionality depends on system time accuracy.
- This project is designed for Windows due to toast notifications.

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!