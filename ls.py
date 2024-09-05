import mysql.connector
import hashlib
import os
from dotenv import load_dotenv
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image handling

# Load environment variables
load_dotenv()

config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Pratham@18'),  # Update with your password
}

# Connect to MySQL and create the database if it doesn't exist
def init_db():
    db = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password']
    )
    
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS users")
    db.commit()
    cursor.close()
    db.close()

# Connect to the database and create the login table if it doesn't exist
def init_table():
    db = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database='users'
    )
    
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user VARCHAR(100) NOT NULL,
            password VARCHAR(256) NOT NULL
        )
    """)
    db.commit()
    cursor.close()
    db.close()

# Register a new user
def register_user(username, password):
    db = mysql.connector.connect(**config, database='users')
    hashpw = hashlib.sha256(password.encode("utf-8")).hexdigest()  # Hashing password
    sql = "INSERT INTO login (user, password) VALUES (%s, %s)"
    values = (username, hashpw)
    cursor = db.cursor()

    try:
        cursor.execute(sql, values)
        db.commit()
        if cursor.rowcount == 1:
            messagebox.showinfo("Success", "You have registered successfully!")
        else:
            messagebox.showerror("Error", "User not added, please try again.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        db.close()

# Login user
def login_user(username, password):
    db = mysql.connector.connect(**config, database='users')
    hashpwd = hashlib.sha256(password.encode("utf-8")).hexdigest()
    cursor = db.cursor()
    sql = "SELECT * FROM login WHERE user=%s AND password=%s"
    user = (username, hashpwd)

    try:
        cursor.execute(sql, user)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showerror("Error", "Login unsuccessful")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        db.close()

# GUI Components for Registration
def register_gui():
    register_window = Toplevel(main_window)
    register_window.title("Register")
    register_window.geometry("500x350")  # Set window size
    register_window.config(bg='#f0f0f0')  # Background color

    # Set background image
    bg_image = Image.open("background_register.jpg")  # Replace with your image path
    bg_image = bg_image.resize((500, 350), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(register_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Add padding and style
    Label(register_window, text="Username:", font=("Helvetica", 12, 'bold'), bg='#f0f0f0').grid(row=0, column=0, padx=20, pady=10, sticky=E)
    Label(register_window, text="Password:", font=("Helvetica", 12, 'bold'), bg='#f0f0f0').grid(row=1, column=0, padx=20, pady=10, sticky=E)

    username_entry = Entry(register_window, font=("Helvetica", 12), width=30)
    password_entry = Entry(register_window, show="*", font=("Helvetica", 12), width=30)

    username_entry.grid(row=0, column=1, pady=10)
    password_entry.grid(row=1, column=1, pady=10)

    def handle_register():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            register_user(username, password)
            register_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    Button(register_window, text="Register", command=handle_register, font=("Helvetica", 12, 'bold'), bg='#4CAF50', fg='white').grid(row=2, columnspan=2, pady=20)

# GUI Components for Login
def login_gui():
    login_window = Toplevel(main_window)
    login_window.title("Login")
    login_window.geometry("500x350")  # Set window size
    login_window.config(bg='#f0f0f0')  # Background color

    # Set background image
    bg_image = Image.open("background_login.jpg")  # Replace with your image path
    bg_image = bg_image.resize((500, 350), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(login_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Add padding and style
    Label(login_window, text="Username:", font=("Helvetica", 12, 'bold'), bg='#f0f0f0').grid(row=0, column=0, padx=20, pady=10, sticky=E)
    Label(login_window, text="Password:", font=("Helvetica", 12, 'bold'), bg='#f0f0f0').grid(row=1, column=0, padx=20, pady=10, sticky=E)

    username_entry = Entry(login_window, font=("Helvetica", 12), width=30)
    password_entry = Entry(login_window, show="*", font=("Helvetica", 12), width=30)

    username_entry.grid(row=0, column=1, pady=10)
    password_entry.grid(row=1, column=1, pady=10)

    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            login_user(username, password)
            login_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    Button(login_window, text="Login", command=handle_login, font=("Helvetica", 12, 'bold'), bg='#4CAF50', fg='white').grid(row=2, columnspan=2, pady=20)

# Main Program Window
main_window = Tk()
main_window.title("Python and MySQL Login System")
main_window.geometry("500x400")  # Set initial window size
main_window.config(bg='#f0f0f0')  # Set background color

# Center the window
main_window.eval('tk::PlaceWindow . center')

# Set background image
bg_image = Image.open("background_main.jpg")  # Replace with your image path
bg_image = bg_image.resize((500, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(main_window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

Label(main_window, text="Welcome to the Login System", font=("Helvetica", 16, 'bold'), bg='#f0f0f0').pack(pady=20)

Button(main_window, text="Register", command=register_gui, font=("Helvetica", 14, 'bold'), bg='#2196F3', fg='white', width=20).pack(pady=10)
Button(main_window, text="Login", command=login_gui, font=("Helvetica", 14, 'bold'), bg='#2196F3', fg='white', width=20).pack(pady=10)

main_window.mainloop()

# Initialize the database and table on program start
if __name__ == "__main__":
    init_db()  # Create the database if it doesn't exist
    init_table()  # Create the login table if it doesn't exist
