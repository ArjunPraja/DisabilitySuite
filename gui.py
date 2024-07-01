
import tkinter as tk
from robospeaker import ROBOGUI
from EyeTracker import start_eye_tracking
from loginRegister import main
def LoginRegister():
      main()
def on_click_OF_ROBOSPEAKER():
      ROBOGUI()
def EyeTracking():
      start_eye_tracking()
      
window = tk.Tk()

window.title("Disability Abuser")
window.geometry("700x500")
window.configure(bg="#BDE0FE")

text = tk.Label(window, text="WELCOME!", bg="#BDE0FE", font=('arial black', 20))
text.pack(pady=20)

text = tk.Label(window, text="Welcome To Disability Suite", bg="#BDE0FE", font=('century', 15))
text.pack(pady=5)

button1 = tk.Button(window, text="Eye Movement Cursor Controller", font=("century", 10), bg="#457B9D",command=EyeTracking)
button1.place(width=500, height=100)
button1.config(width=30, height=2)
button1.pack(pady=10)

button2 = tk.Button(window, text="Hand Signs", font=("century", 10), bg="#457B9D")
button2.place(width=500, height=100)
button2.config(width=30, height=2)
button2.pack(pady=10)

button3 = tk.Button(window, text="Robo Speaker", font=("century", 10), bg="#457B9D", command=on_click_OF_ROBOSPEAKER)
button3.place(width=500, height=100)
button3.config(width=30, height=2)
button3.pack(pady=10)
button4 = tk.Button(window, text="Login/Register", font=("century", 5), bg="#457B9D",command=LoginRegister)
button4.place(width=8009, height=100)
button4.config(width=10, height=2)
button4.pack(pady=10)



window.mainloop()
