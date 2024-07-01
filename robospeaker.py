import tkinter as tk
import pyttsx3

def Speak_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the speed (rate) of speech
    engine.setProperty('rate', 150)

    # Set the volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)

    # Speak the text
    engine.say(text)

    # Wait until speech is complete
    engine.runAndWait()

def on_button_click(text_entry):
    text = text_entry.get()
    Speak_text(text)

def ROBOGUI():
    # Create the main GUI window
    window = tk.Tk()
    window.title("Text Entry Box")

    # Create a label
    label = tk.Label(window, text="Enter your text:")
    label.pack(pady=10)

    # Create a text entry box
    text_entry = tk.Entry(window, width=30)
    text_entry.pack(pady=5)

    # Create a button
    button = tk.Button(window, text="Submit", command=lambda: on_button_click(text_entry))
    button.pack(pady=10)

    # Create a label to display the result
    result_label = tk.Label(window, text="", font=("Arial", 12))
    result_label.pack(pady=5)

    # Run the GUI main loop
    window.mainloop()

if __name__ == "__main__":
    ROBOGUI()
