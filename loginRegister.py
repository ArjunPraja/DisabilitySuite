import tkinter as tk
from tkinter import messagebox
def main():
    

    # Dummy user data for demonstration
    user_data = {'username': 'user123', 'password': 'password123'}

    def login():
        # Add your login logic here
        username = username_entry.get()
        password = password_entry.get()
        
        if username == user_data['username'] and password == user_data['password']:
            messagebox.showinfo("Login", "Login successful")
        else:
            messagebox.showerror("Login", "Login failed")

    def register():
        # Add your registration logic here

        
        # You should perform validation and save user data here

        messagebox.showinfo("Registration", "Registration successful")

    root = tk.Tk()
    root.title("Login Page using Python")
    root.geometry('750x550')
    root.configure(bg='plum1')

    frame = tk.Frame(root, bg='plum1')

    login_label = tk.Label(frame, text="Login", bg='plum1', fg="black", font=("Arial", 30))
    username_label = tk.Label(frame, text="Username", bg='plum1', fg="black", font=("Arial", 16, 'bold'))
    password_label = tk.Label(frame, text="Password", bg='plum1', fg="black", font=("Arial", 16, 'bold'))

    username_entry = tk.Entry(frame, font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
    login_button = tk.Button(frame, text="Submit", bg="black", fg="#FFFFFF", font=("Arial", 16), command=login)
    register_button = tk.Button(frame, text="Register", bg="black", fg="#FFFFFF", font=("Arial", 16), command=register)



    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=10)
    register_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Registration widgets (hidden by default)


    frame.pack()

    root.mainloop()
